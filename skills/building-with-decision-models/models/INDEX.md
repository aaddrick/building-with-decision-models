# Model Notes Index

Field notes for each decision model other than Jev: limits people hit, calibration, where it does well, where it fails, and notes by shape. `providers/` holds the wire contract for each backend. This directory holds what the field learned running each model. Jev is the default: an unnamed result in `prior-art/` ran on Jev, and Jev notes stay in the shape files.

**On a model other than Jev, read its file here before you copy a design, threshold, or latency budget from `prior-art/`.**

| Model | File |
|---|---|
| Cloudflare Clef, Clef-flash | `models/clef.md` |
| Nimble (via Ollama) | `models/nimble.md` |
| Laya, VisionLaya | `models/laya.md` |
| Kev | `models/kev.md` |
| CLM-8B | `models/clm.md` |
| Perplexity pplx-decider | `models/pplx-decider.md` |
| OpenAI Decisions API (GPT-6 Luna) | `models/luna.md` |
| AWS Strands Decider | `models/strands-decider.md` |
| Tev1, decider-2b, Liquid d1, Databricks `ai_decide`, Mercury Decide, GLiNER2.5-Decide | `models/others.md` |

Cross-model comparisons (benchmarks, `confidence` definitions, conformance, re-fitting thresholds) are in `choosing-and-switching-models.md`.
