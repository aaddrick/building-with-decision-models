# Model notes: Nimble (Bespoke Labs, via Ollama)

Field notes from people who built on Nimble 9B, snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The Ollama wire contract (no `/v1` suffix, entropy `confidence`, rounding, errors, model table) is in `providers/ollama.md`.

## Limits

- **Context:** 8,192 tokens ([ollama.com](https://ollama.com/library/nimble), [nimble](https://github.com/bespokelabsai/nimble)), about 8k in practice ([modelfit.io](https://modelfit.io/blog/ollama-decision-models-nimble-tev1-mac/)). That caps transcript windows: fit per-block or per-memory decisions, not whole-transcript states.
- **Options per Choice or Score:** 2–26 through Ollama, per Ollama's own Nimble page ([ollama.com](https://ollama.com/library/nimble)). Bespoke Labs' own runtime (MLX, CUDA) and hosted API allow 1–255 choices per Choice in the latest release, 2026-09-24 ([nimble](https://github.com/bespokelabsai/nimble)). Jev allows 255. Large legal-action sets need a code pre-filter.
- **Text only.** No images.
- **Latency:** about 91 ms per decision on an M5 Max, with no per-call cost ([runtimewire.com](https://runtimewire.com/article/ollama-local-decision-models-systemone)). The "under 100 ms" claim has no published method. The only documented Apple Silicon figure is a 444 ms median on an M5 Pro ([modelfit.io](https://modelfit.io/blog/ollama-decision-models-nimble-tev1-mac/)).
- **Cost of many questions on Ollama:** shared state is counted again for each question scored separately, so many questions per state cost more than on Jev ([docs](https://docs.ollama.com/api/systemone)).

## Calibration

- **The serving stack sets the calibration.** Reported ECE 0.024 on one shared index ([source](https://laurencemoroney.com/2026/10/02/decision-models-explained.html)). The same weights scored 0.022 behind Ollaya's fitted temperature and 0.122 on raw Ollama ([source](https://pyshine.com/Ollaya-Run-Open-Decision-Models-Locally/)). Fit a temperature or Platt scaling on your own labels before you set thresholds on raw Ollama.
- **By question type:** reported 81.6% on Choice but 54.6% on Score. Treat Score answers as the weakest.

## Training data

- Benchmarked against Jev, not trained on its outputs. Nimble generated contrastive pairs with one GPT-5.6 model and verified them with another.

## Where it fails

- **As the only moderation gate:** 70.3% agreement with human moderation labels on Civil Comments, against 81.0% for Jev ([runtimewire](https://runtimewire.com/article/ollama-local-decision-models-systemone)). Validate on your own labels before using it as a moderation gate, and keep a human review band.

## By shape

- **As a gate or moderation filter:** see the agreement gap above. Put hard rules in front and default to "ask".
- **In stream filters:** good for private inboxes and offline jobs (no per-call cost). Re-fit thresholds against Jev's.
- **In control loops and real-time UIs:** check the 26-option cap and the 8k context before porting a loop. Measure latency on your own hardware.
- **Agent context and memory:** 8,192 tokens fits per-block keep/drop decisions, not whole transcripts.
