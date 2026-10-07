# Provider: Ollama (Nimble, Tev1) and Kev — local `/v1/systemone`

Snapshot 2026-10-06, sources: ollama.com blog and library pages, docs.ollama.com/api/systemone, llmconfigurator.com guides, the github.com/jaredpalmer/kev README, the github.com/bespokelabsai/nimble README. The live docs win.

## Ollama (0.35+)

```http
POST http://localhost:11434/v1/systemone
Content-Type: application/json
```

- No API key for local requests. The base URL has **no `/v1` suffix**, unlike Ollama's OpenAI-compatible base URL (pydantic.dev system-one page).
- The request uses the Jev shape (`model`, `state`, `questions`) and adds two optional fields: `images` (base64 only, no URLs or data URLs; needs Clef or Clef Flash with vision weights) and `keep_alive` (a duration string such as `5m`, or seconds) (docs.ollama.com).
- `instructions` takes "A nonempty string, or an object or array serialized as JSON text". Choice criteria are "Option keys mapped to descriptions, or null for a bare label" (docs.ollama.com).
- Response: `model`, `answers`, `usage.input_tokens`, `usage.output_tokens`. `model` **echoes the request name** (`"nimble"`), not a versioned ID like `jev-1.13.0` (blog example).

### Models

| Pull | Maker | Params / base | Download | Context | License | Source |
|---|---|---|---|---|---|---|
| `ollama pull nimble` (`nimble:9b`) | Bespoke Labs | 8.95B, Qwen3.5-9B, Q8_0 | 9.5 GB llama.cpp, 9.3 GB MLX | 8,192 | Apache-2.0 | ollama.com/library/nimble:9b |
| `ollama pull tev1` (`tev1:4b`) | Together AI (experimental) | 4B, Qwen3.5 | 4.4-4.5 GB | library page says 256K; llmconfigurator advises staying under ~2,000 tokens | MIT for code and data builders; the repo says weights "have their own terms" | ollama.com/library/tev1, github.com/togethercomputer/tev1 |
| `ollama pull tev1:0.8b` | Together AI (experimental) | 0.8B, Qwen3.5 | 797-812 MB, runs on CPU | as tev1 | as tev1 | same |
| `ollama pull iapp/openthai-systemone` (community) | iApp | 0.8B, Qwen3.5-0.8B-Base, Thai + English | 812 MB q8_0, 529 MB q4_K_M, 1.5 GB bf16 | not documented | Apache-2.0 | ollama.com/iapp/openthai-systemone:0.8b |
| `clef`, `clef-flash` | Cloudflare | 27B / 9B | 17.99 GB / 10.93 GB | not documented | not documented | llmconfigurator.com (needs Ollama 0.35.1+) |

Conflict: the Ollama blog lists three models (nimble, tev1, tev1:0.8b). llmconfigurator and docs.ollama.com also name `clef` and `clef-flash`, which need 0.35.1+ and are the only models that take images.

### Differences from Jev

| Item | Jev | Ollama | Source |
|---|---|---|---|
| Auth | Bearer key | none locally (the typesafe-sdk still needs a dummy `TYPESAFE_API_KEY=ollama`) | ollama.com blog |
| `confidence` formula | `(n·top − 1)/(n − 1)` (Choice), a distance-based formula (Score) | `1 − H(p)/ln(N)`, one minus the normalised entropy, for both Choice and Score | docs.ollama.com |
| Noul `confidence` | absent | not documented. The blog example has none. | blog |
| Rounding | 2 decimals | docs: "Example probabilities and confidence are rounded to four decimal places". The blog example shows 3 decimals (`0.985`, `0.922`). | docs.ollama.com, blog |
| Questions per request | not documented | 1-64 | docs.ollama.com |
| Choice options | max 255 | API docs: 2-255, and "The option limit depends on the model". Nimble's Ollama page: **2-26**. | ollama.com/library/nimble, see below |
| Score levels | 2-10 | 2-26, "depends on the model" | docs.ollama.com |
| Body size | not documented | 64 KiB, or 32 MiB with images | docs.ollama.com |
| `model` in response | versioned ID | echoes the request name | blog |
| Errors | 401/422/429/529 | 400 (bad request or unsupported model, including chat models, `:cloud` tags, and MLX models on Mac), 404 (model not pulled or Ollama < 0.35), 413 (too large), 500 (load or scoring failure, usually memory). Body: `{"error": "<string>"}`. | docs.ollama.com, llmconfigurator errors guide |

Score confidence is much lower under the entropy formula. The blog's `urgency` answer (probabilities 0.378/0.429/0.193) shows `confidence: 0.046`. Jev's formula would give about 0.14 for the same distribution. Do not reuse Jev confidence thresholds on Ollama. (The 0.046 and 0.922 values in the blog example check out against `1 − H/ln N`: 0.9223 and 0.0458.)

Choice option limits: docs.ollama.com lists 2-255 but says the limit depends on the model. Ollama's own Nimble page settles it for Nimble: "Choice and score questions take 2 to 26 options" (checked 2026-10-06). Three secondary sources agree on 26: llmconfigurator ("2–26 options per choice question"), pydantic-ai (`decision_max_choice_options` 26 for Ollama), and the openthai model page ("Maximum 26 options per question"). Treat 26 as the limit for nimble and tev1 through Ollama. Nimble's own README allows "1 to 255 string choices in the latest release" (2026-09-24), but that applies to Bespoke Labs' own runtime (MLX, CUDA) and hosted API, not Ollama.

`confidence` is not correctness. llmconfigurator quotes the Ollama API docs: it is "not calibrated correctness", and "a higher value does not guarantee the answer is correct".

### Example (Ollama blog, verbatim)

```bash
curl http://localhost:11434/v1/systemone -d '{
  "model": "nimble",
  "state": {"ticket": "I was charged twice. Please refund the extra payment."},
  "questions": {
    "team": {"type": "choice", "instructions": "Which team should handle this ticket?",
             "criteria": {"billing": "Payments and refunds", "technical": "Bugs and integrations", "other": "None of the above"}},
    "refund": {"type": "noul", "instructions": "Does the customer explicitly ask for a refund?"},
    "urgency": {"type": "score", "instructions": "How urgent is this ticket?", "criteria": ["Routine", "Soon", "Urgent"]}
  }
}'
```

```json
{"model": "nimble",
 "answers": {
   "team": {"type": "choice", "choice": "billing",
            "probabilities": {"billing": 0.985, "technical": 0.012, "other": 0.003}, "confidence": 0.922},
   "refund": {"type": "noul", "noul": 0.997},
   "urgency": {"type": "score", "score": 0.815, "legend": {"0": "Routine", "1": "Soon", "2": "Urgent"},
               "probabilities": {"0": 0.378, "1": 0.429, "2": 0.193}, "confidence": 0.046}},
 "usage": {"input_tokens": 841, "output_tokens": 4}}
```

The typesafe-sdk works unchanged with `TYPESAFE_BASE_URL=http://localhost:11434`, `TYPESAFE_API_KEY=ollama`, `TYPESAFE_DEFAULT_MODEL=nimble`. The blog uses `TypeSafeClient(timeout=120)`, which covers the cold model load.

### Accuracy and latency

| Model | Accuracy | Source |
|---|---|---|
| nimble | 75.7% on 13 public datasets (3,880 decisions), against Jev's 76.0%. Broken down: choice 81.6%, yes/no 80.2%, score 54.6%. | ollama.com/library/nimble:9b, llmconfigurator |
| nimble | 90.12% agreement on 324 held-out examples, against Jev 1.13.0 93.21% and base Qwen3.5-9B 66.36% | github.com/bespokelabsai/nimble |
| tev1 | 73.3% (same 13-dataset benchmark). Together's own figures: 880/1,000 main and 300/300 policy-transfer, on reused dev benchmarks. | ollama.com/library/tev1, github.com/togethercomputer/tev1 |
| tev1:0.8b | 63.5% | ollama.com/library/tev1 |
| openthai-systemone 0.8b | 74.3% macro on public benchmarks, 82.5% on Thai (nimble scores 78.3% on Thai) | ollama.com/iapp/openthai-systemone:0.8b |
| Decision Index 0.2.1 | tev1:0.8b 12.85, tev1 29.24, nimble 39.57, Jev 1.13 57.91 | llmconfigurator.com/en/guides/decision-models |

Calibration: Tev1's repo says "Logprobs are model preferences, not calibrated confidence". Nimble's first release used temperature T=2.179. The latest checkpoint uses T=1.0 "without separate fitting" (nimble README). Ollama publishes no ECE for these models.

Latency: the blog reports "Nimble 9B averaged 91ms per decision" on an M5 Max. Nimble's README gives a median of 444 ms on an M5 Pro 64 GB and 106 ms on an H100. These conflict with the 91 ms figure and were likely measured differently. The README recommends 64 GB RAM on a Mac, or 18 GB+ BF16 VRAM on Linux for the native server. OpenThai takes about 23 ms for one question and 136 ms for three on an H100. Ollama's blog lists "Faster performance on Apple Silicon powered by MLX" as upcoming. Conflict: the nimble library page already lists an MLX variant, while the errors guide says MLX models on Mac return 400.

## Kev (Jared Palmer)

- What it is: rank-16 LoRA adapters plus a pointer head on frozen Qwen3.5 bases. Trained in a "decision-v7" run (two epochs over ~10,000 examples from ten public datasets, plus 896 generated policy examples and 1,680 rule-based examples) for "roughly $95 in H100 time on Modal" (orcarouter.ai laya-vs-kev, runtimewire).
- License: Apache-2.0, and the Qwen bases are Apache-2.0 too. Training datasets keep their own licenses (README).
- Contract: it "mirrors TypeSafe's public /v1/systemone contract", and the typesafe-sdk works by changing the base URL. Default alias `kev-latest`.

```bash
git clone https://github.com/jaredpalmer/kev.git && cd kev
uv sync --extra serve
uv run --extra serve python -m kev.serve --run jaredpalmer/kev-4b --port 8009
```

The server binds 127.0.0.1 with no auth by default (orcarouter). Set `KEV_API_KEY` to require a bearer token.

| HF ID | Base | Context | Accuracy, new / trained sources (README) |
|---|---|---|---|
| `jaredpalmer/kev-0.8b` | Qwen3.5-0.8B | 8,192 | 0.648 / 0.827 |
| `jaredpalmer/kev-4b` (recommended) | Qwen3.5-4B | 8,192 | 0.817 / 0.873 |
| `jaredpalmer/kev-9b` | Qwen3.5-9B | 8,192 | 0.820 / 0.874 |
| `jaredpalmer/kev-27b` | Qwen3.8-27B | 65,536 | 0.851 / 0.865 (80 GB GPU) |

| Item | Value | Source |
|---|---|---|
| Options / levels | 1-255 per question. Orcarouter says score 2-255. | README, orcarouter |
| Questions per request | no stated limit | README |
| Long state | 422 with the token count and limit. `KEV_TRUNCATE_STATES=1` reads the first 65,536 tokens instead. | README |
| Errors | 422 for invalid requests | README |
| `confidence` | the same formulas as Jev's adapter. Choice: `(p_max − 1/K)/(1 − 1/K)`. Score: `max(0, 1 − E|level − mode|/D)`. | README |
| Calibration | a fitted temperature per checkpoint by default (0.8B 2.35, 4B 2.41, 9B 2.19, 27B 1.32). `KEV_TEMPERATURE=1.0` gives raw probabilities. | README |
| Rounding | not documented. Served probabilities differ from the fp32 eval path by up to ~0.03 on GPU and ~0.05 on Mac, and the top answer flips "on about one question in 300". `KEV_DTYPE=fp32` serves the exact eval path. | README |
| Other env vars | `KEV_DATE_FACTS=1` appends day counts between dates | README |
| Latency | H100: 4B 18.1 ms for 6 short questions (101 req/s), 9B 24.0 ms, 27B 75.0 ms of model time. M5 32 GB with MLX: 4B ~721 ms cold, 136 ms with cached text. | README |
| Weak spots | knowledge questions (MMLU ~0.70-0.74 against Jev's 0.90), date arithmetic (60% against Jev's 93%). An older default was overconfident: `KEV_TEMPERATURE=2.0` cut confident errors from 8.7% to 4.4%. Kev beats Jev on narrow routing (0.952 against 0.897). | orcarouter, pinggy.io |

Conflicts:
- **MLX.** The README says MLX installs and runs automatically on Apple Silicon. Runtimewire and orcarouter say MLX was not ready yet ("DeltaNet kernels do not exist for MLX yet"), and CUDA needs `flash-linear-attention`. The README is newer, so it wins.
- **Accuracy.** Runtimewire reports 0.837 / 0.832 / 0.668 (9B / 4B / 0.8B) on a locked test set. The README's "new source" column reports 0.820 / 0.817 / 0.648. Pinggy reports Kev-9B 0.822 against Jev 0.857.
- **Confident errors.** The README gives Kev-9B 2.4% against Jev 3.7%. Pinggy gives 4.0%.
- **Latency.** Pinggy reports 47 ms repeated and 77 ms fresh on an M3 Pro with MLX. The README reports 136 ms cached and 721 ms cold on an M5. The setups differ, so measure on your own hardware.
- **OpenRouter.** `openrouter.ai/jaredpalmer/kev-4b` appeared in search results but returned 404 when fetched. Treat it as unverified.

## Sources

- https://ollama.com/blog/ollama-now-supports-jev-style-decision-models
- https://docs.ollama.com/api/systemone
- https://ollama.com/library/nimble:9b
- https://ollama.com/library/tev1
- https://ollama.com/iapp/openthai-systemone:0.8b
- https://github.com/bespokelabsai/nimble
- https://github.com/togethercomputer/tev1
- https://llmconfigurator.com/en/guides/decision-models
- https://llmconfigurator.com/en/guides/decision-models/ollama-setup
- https://llmconfigurator.com/en/guides/decision-models/confidence-and-thresholds
- https://llmconfigurator.com/en/guides/troubleshooting/ollama-systemone-errors
- https://pydantic.dev/docs/ai/models/system-one/
- https://github.com/jaredpalmer/kev
- https://runtimewire.com/article/jared-palmer-kev-qwen35-decision-models
- https://www.orcarouter.ai/blog/laya-vs-kev
- https://pinggy.io/blog/best_open_source_jev_alternatives_self_hosted_decision_models/
