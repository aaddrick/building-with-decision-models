# Model notes: Cloudflare Clef / Clef-flash

Field notes from people who built on Clef (27B) and Clef-flash (9B), snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The wire contract (REST `result` envelope, `images` field, errors, price, context) is in `providers/clef.md`. Local serving through Ollama is in `providers/ollama.md`.

## Limits

- **Hosted latency is far above the vendor figure.** Cloudflare reports 38.8 ms median and 122.4 ms p95 for Clef-flash on one H200 ([model card](https://huggingface.co/Cloudflare/clef-flash)). Users of the hosted API measured Clef-flash at a median of 661–850 ms against 110–237 ms for Jev ([HN](https://news.ycombinator.com/item?id=49923692)), and 661 ms against 230 ms in another test ([HN](https://news.ycombinator.com/item?id=49925250)). On a review-gate task, Clef measured about 850 ms p50 against about 110 ms for Jev ([HN](https://news.ycombinator.com/item?id=49928781)). One Workers app measured 0.5–5 s for uncached text calls, not the advertised ~40 ms ([ry](https://github.com/ygwyg/ry)).
- **Image requests are slow.** Every image request took 13–30 s on launch day (2026-10-01), on both models ([flaviocopes.com](https://flaviocopes.com/clef/), [flaviocopes.com](https://flaviocopes.com/clef.md)). Use a 60 s timeout and decide what happens on a timeout.
- **Image size.** Image tokens were estimated as base64 length / 4. A 1.3 MB and a 575 KB PNG overflowed the 65,536-token context, and requests failed above about 190 KB. Resized to 1024 px JPEG at quality 80, they became 140 KB and 48 KB (1,048 and 1,272 billed tokens). Keep each image under about 190 KB. Cloudflare does not document this.
- **Context window.** 64k tokens, against 32k for Jev in the same post ([Cloudflare](https://blog.cloudflare.com/clef-decision-models/)).
- **Cost.** Reported: 100,000 tickets of about 400 tokens cost $1.68 on Jev, $3.60 on Clef-flash, and $9.60 on Clef. Measured medians from Italy were 191–205 ms (Clef-flash) and 524–726 ms (Clef) ([flaviocopes.com](https://flaviocopes.com/clef/)).
- **Local hardware.** The 27B needs one 48–80 GB GPU ([mindstudio.ai](https://www.mindstudio.ai/blog/clef-27b-decision-model-local/)). Clef-flash runs about 5 decisions/s on an RTX 3090 ([clef-demo](https://github.com/tehtommeh/clef-demo)), and 250 ms per frame with 3 questions on an M5 Max with custom MPS kernels, 840 ms stock ([clef-webcam](https://github.com/huntharo/clef-webcam)).
- **Local via Ollama.** Ollama counts the shared state again for each question scored separately (see `models/nimble.md`). ClefMCP reported 0.5 s for 1 question and 18.6 s for 64 on an M4 Pro ([ClefMCP](https://github.com/HighlyLoadedEgo/ClefMCP)).

## Calibration and agreement

- **Clef and Clef-flash can disagree sharply on the same input.** On one dashboard screenshot, "shows network details" was 0.67 on Clef and 0.21 on Clef-flash. Both correctly scored "readable secret" at 0.07–0.08. Label your own set before trusting either.
- Hosted `confidence` values fit neither Jev's formula nor top probability. Never reuse a Jev confidence bar. Other servers' definitions are compared in `choosing-and-switching-models.md`.
- Thresholds tuned on Jev do not carry over: clef-rag ships Jev-tuned thresholds and says to re-tune them for Clef.

## Where it does well

- **Tool calling (vendor-reported).** BFCL 98.5 (Clef) and 98.8 (Clef-flash) against 95.8 for Jev, and a 209 ms / 38.8 ms median against 524 ms for Jev in the same launch run. Hosted users measured far slower (see Limits).
- **Function selection.** One guide reported 98.76% accuracy for Clef-flash against 98.47% for Clef. Test both on your own data before picking by price.
- **Quality on review routing.** In one user's test, Clef matched Jev on quality (recall 0.98 vs 1.00).
- **Images.** It accepts images, which Jev does not. See `prior-art/images-and-multimodal.md` for the request.

## Where it fails

- **Hosted Clef-flash in sub-second interactive loops**: the hosted medians above, and Clef-flash over-escalated in a review-gate test ([HN](https://news.ycombinator.com/item?id=49923692), [HN](https://news.ycombinator.com/item?id=49925250), [HN](https://news.ycombinator.com/item?id=49928781)). Run it on your own GPU or pick a faster model.
- **Images on a synchronous or latency-bound path**: 13–30 s per image request at launch, and failures above about 190 KB ([flaviocopes.com](https://flaviocopes.com/clef/)).
- **Fine-grained image classification**: one user got 41% on coins against Gemma 4 27B's 53%, and Gemma was about 4× faster ([HN](https://news.ycombinator.com/item?id=49923692)). Do not use a decision model as a fine-grained image classifier.
- **Deciding whether to call a tool, or to escalate.** Jev is better at deciding *whether* to call a tool (When2Call 81 vs 72). Validate the `none` question on Clef before relying on it. In one test Jev also did better at deciding when to escalate to a human ([mindstudio.ai](https://www.mindstudio.ai/blog/clef-27b-decision-model-local/)).
- **Uneven accuracy across workflows.** Clef was reported at 64.7% on invoices but 62.9% on security incidents.

## By shape

- **As a gate:** start on Clef-flash and move a question to Clef only when your labels show Clef-flash failing. Resize images first and keep image gates off the hot path. Clef-flash over-escalated in a review-gate test.
- **In control loops and real-time UIs:** hosted, both are slower than Jev (numbers above). Locally, Clef-flash is fast enough for webcam loops. A concrete "none" option and larger frames for small objects help.
- **In stream filters:** use Clef-flash for latency-bound filters and Jev for cost-bound ones. For moderation, check the review band: Jev escalated to a human better in one test.
- **Selecting from candidates:** strong on tool calling, weaker on "should I call a tool at all?". Validate the `none` key.
- **Embedded in infrastructure (Workers AI):** REST wraps answers in Cloudflare's `result` envelope, while `env.AI.run` returns them directly. `model` must be `clef` or `clef-flash`; `jev-latest` fails with error 5006. Cache answers in KV and require a margin before acting ([ry](https://github.com/ygwyg/ry)).
- **On images:** see the limits above. Validate size before you send.
