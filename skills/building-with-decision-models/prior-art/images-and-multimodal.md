# Shape: Images and Multimodal Input

**Use when** the decision depends on an image, screenshot, video frame, webcam, scanned document, or other non-text input: screenshot secret/PII gates, image moderation, picking a UI element from a screenshot, webcam/gesture loops, document/receipt checks, product photo QA.

## The shape

```
raw pixels → code does perception first: OCR, CV, object detection, element tables, crop/resize/compress
           → code rules on what it extracted (a regex hit on OCR text blocks here; the model never sees it)
           → one request: a few downsized images (if the model takes images) + the extracted text as state
             (a text-only model gets a caption or OCR text from code instead)
           → code policy on the probabilities; video: commit only after 2 agreeing checks
           → image calls run off the hot path, with a long timeout and a fallback
```

Code owns the pixels: what to crop, how small to make it, and what can be read exactly (text, boxes, counts). The model judges only what code cannot: "is this a readable secret?", "is this the checkout button?", "is the product damaged?".

This conflicts with `prior-art/select-from-candidates.md`, where numbered element tables beat screenshots. When code can list the candidates (DOM, a11y tree, OCR boxes), use the table. Send pixels only when nothing can be listed: canvas, games, camera frames, scans, photos.

Sketch: a screenshot gate on **Cloudflare Clef-flash over REST**. It is the provider with a fully documented image request (`providers/clef.md`). Other providers put the image in a different field (see the table below).

```python
import base64, io, os, re

import httpx
from PIL import Image

URL = (f"https://api.cloudflare.com/client/v4/accounts/{os.environ['CLOUDFLARE_ACCOUNT_ID']}"
       "/ai/run/@cf/cloudflare/clef-flash")
HEADERS = {"Authorization": f"Bearer {os.environ['CLOUDFLARE_AUTH_TOKEN']}"}
MAX_BYTES = 190_000            # observed overflow above ~190 KB per image on Workers AI
SECRET = re.compile(r"(AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|ghp_[A-Za-z0-9]{36})")

def to_data_url(path: str, max_side: int = 1024) -> str:
    img = Image.open(path).convert("RGB")
    while max_side >= 256:
        img.thumbnail((max_side, max_side))          # keeps aspect ratio, only shrinks
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=80)
        if buf.tell() <= MAX_BYTES:
            return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
        max_side //= 2
    raise ValueError("image still too large after downscaling")

def screenshot_gate(path: str, ocr_text: str) -> str:
    if SECRET.search(ocr_text):                       # exact pattern from OCR: block, no model call
        return "block"
    body = {
        "model": "clef-flash",
        "images": [to_data_url(path)],                # max 4; base64 data URLs only, no remote URLs
        "state": {"ocr_text": ocr_text[:4000], "destination": "public blog post"},
        "questions": {
            "secret": {"type": "noul", "instructions":
                       "Does the screenshot show an API key, password, or access token in readable form?"},
            "network": {"type": "noul", "instructions":
                        "Does the screenshot show IP addresses or internal hostnames?"},
            "pii": {"type": "noul", "instructions":
                    "Does the screenshot show a person's email, phone number, or home address?"},
        },
    }
    try:
        r = httpx.post(URL, headers=HEADERS, json=body, timeout=60)   # image calls took 13–30 s at launch
        r.raise_for_status()
    except httpx.HTTPError:
        return "review"                               # fail closed to a human, not to "allow"
    answers = r.json()["result"]["answers"]           # REST wraps answers in a `result` envelope
    p = max(answers[k]["noul"] for k in ("secret", "network", "pii"))
    return "block" if p >= 0.7 else "review" if p >= 0.3 else "allow"
```

The thresholds are placeholders. Fit them on your own labelled screenshots, per model.

**Where the image goes, by provider** (from the provider files; check them before porting):

| Provider | Field | Limits |
|---|---|---|
| Clef / Clef-flash, Workers AI (`providers/clef.md`) | `images`: data URL strings or `{content_type, base64}` | Max 4. PNG/JPEG/WebP. 4 MiB and 16 MP each, 8 MiB total, 13 MiB body. Remote URLs rejected. Keep each under about 190 KB in practice. |
| Clef via Ollama (`providers/ollama.md`) | `images`: plain base64, no data URLs | Only `clef` and `clef-flash` take images. Body up to 32 MiB with images. |
| OpenAI Decisions (`providers/openai-decisions.md`) | `input` parts: `{"type": "input_image", "image_url": "data:image/png;base64,..."}` | Base64 data URLs only. Hosted URLs and `file_id` rejected. Image limits not documented. |
| pplx-decider (`providers/perplexity.md`) | Inside `state` as `{"type": "image_url", "image_url": {"url": "data:..."}}` parts | Data URLs only. Max 2,048 tiles of 32×32 px; a larger image hangs about a minute, then returns `504`. |
| Strom (`providers/eu-hosts.md`) | `media`: `{"type": "image", "url": ...}` | Up to 8. Data URL or public URL (10 MB, 10 s). Scaled to 1 MP. |
| System1 s1-vision (`providers/eu-hosts.md`) | `images` | 1 image, 4 MiB, 2 MP. 4,096-token context covers the image too. |
| Strands Decider (`providers/open-weights.md`) | `--vision`, base64 images | Needs the `[vision]` extra. |
| Jev, Nimble, Tev1, OpenRouter's schema | none | Text only. Send a caption or OCR text. |

## Variants

- **Screenshot secrets gate before upload**: OCR + regex block exact secrets first. The model looks for what regex misses (a half-visible token, a URL bar, a terminal history).
- **Image moderation with a text-first prefilter**: judge the caption, filename, alt text, and uploader history as text first. Send the image only for the uncertain middle band. Keep a dedicated image classifier in front for NSFW.
- **Screenshot UI selection vs element table**: use the a11y tree or DOM table when you have one. Without one, cut the screenshot into a labelled grid and ask a Choice over tiles, recursing into the winner (GUI_JEV). Snap the final box to a real element before clicking.
- **Vision fallback after stalls**: run the text/a11y loop by default and attach a screenshot only after N stalled steps.
- **Webcam/gesture loop with a 2-check commit**: one request in flight on the newest frame. Code tracks the hand or object. Act only after 2 agreeing checks ≥ 900 ms apart, and slow the check rate when the scene is unchanged. See `prior-art/incremental-realtime.md`.
- **Document/receipt field checks**: OCR extracts candidate fields in code. A Choice picks among the candidate strings (plus `none`) and Nouls check "is this a receipt?", "is the total legible?". Send the page image only to confirm a doubtful field.
- **Product photo QA**: code crops to the product with object detection. Ask defect Nouls and a severity Score on the crop, not the whole frame.
- **Text-only fallback**: a local captioner or OCR turns the image into text. Any text decision model (Jev included) decides on that text.

## Field lessons

- **Perception first.** Most decision models are text-only, and perception is the reported bottleneck. On Jev, numbered element tables cost $0.0002–$0.004 per step against minutes and dollars for vision agents. Pixel-only input failed in JEVQA, where encoding metadata worked.
- **Text-only models cannot read pixels.** **Jev:** 9% (chance) on sketches sent as base64 PNG, 35% on the same sketches as SVG stroke text, against 91% for Claude on the images, with a strong "airplane" bias ([mikulskibartosz.name](https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew)). Give a text model a caption, not bytes.
- **Image calls are slow and size-limited even where images are supported.** On the hosted model with the most complete image API, every image request took 13–30 s at launch and images over about 190 KB overflowed the context (Clef, `models/clef.md`). Keep image gates off the hot path, set a long timeout, decide what happens on a timeout, and resize before you send.
- **Validate size before you send.** Limits differ and fail differently: Clef takes 4 images and rejects remote URLs, OpenAI takes base64 data URLs only (no hosted URLs or `file_id`), System1 s1-vision takes 1. An oversized **pplx-decider** image does not return `400`; it hangs about a minute, then `504`.
- **Two sizes of one model can disagree sharply on the same image.** Label your own set before trusting either.
- **Do not use a decision model as a fine-grained image classifier or an NSFW filter.** A general vision LLM beat one on fine-grained classification, and an open clone flagged too many false positives. Put a dedicated classifier or a human in front.
- **Downscaling is the biggest latency lever locally.** **Intern-Decision-0.8B (MLX, M2 Air):** a 1080p screenshot took about 3.6 s at full size, 0.9 s at 1024 px, 0.6 s at 768 px, against 204 ms text-only ([intern-decision-mlx](https://github.com/dex0shubham/intern-decision-mlx)). Make small objects bigger by cropping, not by sending a larger frame.
- **Frames need persistence.** ClefCam checks every ~1.5 s and needs 2 consecutive matches ≥ 900 ms apart ([clefcam](https://github.com/tmchow/clefcam)). Keep one request in flight on the newest frame and drop stale ones. A concrete "none" option helps.
- **Images cost more per request.** **System1 s1-vision:** all input tokens bill at $0.217/M with an image vs $0.038/M text-only (vendor). **Strom:** one token per 32×32 px, 64–1,024 per image (vendor). **pplx-decider:** about 1,000 input tokens per megapixel (vendor-reported). Downscale before you pay for it.
- Not on Jev? Model-specific image notes (Clef and Clef-flash latency, size, disagreement and local speed; VisionLaya): `models/clef.md`, `models/laya.md`. Index: `models/INDEX.md`.

## Prior art

- Screenshot publish gate: readable secret, dark theme, network details, and screen type, with resize-before-send (Clef, Clef-flash): [flaviocopes.com](https://flaviocopes.com/clef.md)
- Local first-pass screenshot classifier that escalates uncertain answers to a larger model; not meant as a safety filter (Intern-Decision-0.8B via MLX): [dex0shubham/intern-decision-mlx](https://github.com/dex0shubham/intern-decision-mlx)
- Browser driving: Florence-2 captions each frame, a text model decides, ~330 ms median (Florence-2 + Jev): [reinhard-z/vision-jev](https://github.com/reinhard-z/vision-jev)

More projects (27 entries), grouped by sub-type (Screenshot and secret gates, Image classification and moderation, Webcam, gesture, and video, Screens and UI agents, Documents, receipts, and inspection photos, Model notes and benchmarks): `prior-art/projects/images-and-multimodal.md`.
