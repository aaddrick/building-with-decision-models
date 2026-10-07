# Projects: Images and Multimodal Input

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/images-and-multimodal.md`.

Few community projects use image input yet. Most image work so far is launch-week tests and local demos. Numbers are author-reported.

**Screenshot and secret gates**
- Screenshot publish gate: readable secret, dark theme, network details, and screen type, with resize-before-send (Clef, Clef-flash): [flaviocopes.com](https://flaviocopes.com/clef.md)
- Local first-pass screenshot classifier that escalates uncertain answers to a larger model; not meant as a safety filter (Intern-Decision-0.8B via MLX): [dex0shubham/intern-decision-mlx](https://github.com/dex0shubham/intern-decision-mlx)

**Image classification and moderation**
- NSFW flagging with an open "VisionLaya" clone, too many false positives (VisionLaya): [HN](https://news.ycombinator.com/item?id=49779502)
- Coin classification, 41% vs 53% for Gemma 4 27B (Clef): [HN](https://news.ycombinator.com/item?id=49923692)
- Doodle and flower labels from image pixels with typed Choices (DiffusionGemma via SGLang): [Hangzhi/diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)
- Guess-what-I-drew: sketches as SVG text vs base64 PNG on a text-only model: [mikulskibartosz.name](https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew)

**Webcam, gesture, and video**
- clef-demo, clef-webcam, and ClefCam (Clef-flash, local and Workers AI); entries in `prior-art/projects/incremental-realtime.md`
- jev-canvas, voice plus a webcam-tracked finger; code tracks the hand, the model reads the transcript (Jev via OpenRouter): [gaborishka/jev-canvas](https://github.com/gaborishka/jev-canvas)
- Browser driving: Florence-2 captions each frame, a text model decides, ~330 ms median (Florence-2 + Jev): [reinhard-z/vision-jev](https://github.com/reinhard-z/vision-jev)
- Ten browser games from one 448 px frame at 43 ms/move (Qwen3.5-0.8B fine-tune): [OmniJev/PlayJev](https://github.com/OmniJev/PlayJev)
- Dual-camera images plus text pick preset skills for a MuJoCo arm, 13 decisions per episode (self-hosted multimodal model): [shapsider/OmniJev](https://github.com/shapsider/OmniJev)
- Camera-only drone, CV turns frames into state first; entry in `prior-art/projects/control-loops.md`
- JEVQA, video quality from encoding metadata; pixel-only failed: [arXiv:2609.24395](https://arxiv.org/abs/2609.24395)

**Screens and UI agents**
- GUI_JEV, recursive screenshot grounding: a grid of labelled tiles, a vision model describes them, a Choice picks the tile. 9/12 point hits on a smoke test (Jev + a vision model via Vercel AI Gateway, or OpenJev 0.8B locally): [ZihuaEvan/GUI_JEV](https://github.com/ZihuaEvan/GUI_JEV)
- Mac computer use with OCR and no screenshots, about $0.0002 per step: [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
- Android a11y-tree Choice with a vision fallback after 3 stalled steps: [xinwang-nwpu/jev-mobile](https://github.com/xinwang-nwpu/jev-mobile)
- FluidUse form filling over the Accessibility API (Laya, Kev-0.8B, Clef-vision): [FluidInference/FluidUse](https://github.com/FluidInference/FluidUse)
- Image-to-bounding-box grounding model (GroundingJev, Qwen3.5-0.8B): [xyzzzh/GroundingJev](https://github.com/xyzzzh/GroundingJev)

**Documents, receipts, and inspection photos**
- No image-based receipt or document project found yet. The official invoice eval workflow is text-side: [evals.typesafe.ai](https://evals.typesafe.ai/)
- Industrial inspection photos: 86.6 image AUROC zero-shot on 2,162 VisA photos, up to 4 images per request (RSI-Jev v4.0-VL): [Shanghua-Gao/RSI-Jev](https://github.com/Shanghua-Gao/RSI-Jev)

**Model notes and benchmarks**
- Clef launch post, image input in both models (Clef, Clef-flash): [blog.cloudflare.com](https://blog.cloudflare.com/clef-decision-models/)
- OpenAI Decisions guide, base64 `input_image` parts only (GPT-6 Luna): [developers.openai.com](https://developers.openai.com/api/docs/guides/decisions)
- pplx-decider with image input and a 262k context (pplx-decider): [huggingface.co](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b)
- Liquid d1, text plus up to 8 images; images only on Liquid's own console for now (Liquid d1): [liquid.ai](https://www.liquid.ai/blog/d1-decision-model)
- decider-2b-vision, images and game frames (decider-2b-vision): [huggingface.co](https://huggingface.co/Mapika/decider-2b-vision)
- Strands Decider `--vision` mode (Strands Decider 2B): [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider)
- Open vision decision models: Visual-JEV (Qwen3.5-4B) [jiangxiluning/Visual-Jev](https://github.com/jiangxiluning/Visual-Jev), Vev (Qwen3.5 LoRA) [Xiaooolong/vev](https://github.com/Xiaooolong/vev), Jev-Omni over text, images, audio, and video (Gemma-4-12B fine-tune) [huggingface.co](https://huggingface.co/akhilaaa3/Jev-Omni)
