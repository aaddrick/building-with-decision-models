# Provider: open-weight models — Laya, Strands Decider, CLM-8B, SemIf, NanoJev

Snapshot 2026-10-06, sources: the project READMEs on GitHub and secondary write-ups (pinggy.io, orcarouter.ai, llmconfigurator.com, news articles on CLM-8B). The READMEs and model cards win.

| Model | `/v1/systemone`? | Primitives | Size | License |
|---|---|---|---|---|
| Laya | yes, `laya-serve`, with extras and gaps | noul, choice, score | 421M / 322M encoder | Apache-2.0 |
| Strands Decider | yes, `strands-decider serve` | noul, choice, score | 1.9B | Apache-2.0 |
| CLM-8B | yes, `clm-serve` on port 8700 | noul, choice, score, plus free-form ranking | 8B (frozen Qwen3-8B + projection heads) | Apache-2.0 |
| SemIf | no, CLI only | typed options → logits | uses stock models (Qwen3.5-4B etc.) | MIT (code) |
| NanoJev | no, `POST /api/evaluate` | choice, boolean, score | 0.6B | MIT |

## Laya (ConvAI Innovations)

Laya is a non-autoregressive encoder on ModernBERT, not a decoder LLM. Repo: https://github.com/NandhaKishorM/laya. Weights: `convaiinnovations/laya` on Hugging Face.

```bash
pip install "laya[serve]"
LAYA_DEVICE=cuda LAYA_PRELOAD=1 laya-serve
```

| Checkpoint (`model`) | Params | Context |
|---|---|---|
| `english` (laya) | 421M (ModernBERT-large) | 512 |
| `multilingual` | 322M (mmBERT-base), 100+ languages | 1024-8192 |
| `typed-decisions` | 421M, fine-tuned | 1024 |

How it differs from Jev (README):

- Endpoints: `POST /v1/systemone`, `POST /v1/systemone/batch` (up to 64 states), `GET /health`.
- Extra request fields: `lang_guess`, `max_len`, `head_max_len`, and `min_confidence` (an abstention threshold).
- These fields are rejected with 422: `hooks`, `on_predict_start`, `on_predict_end`, `hooks_raise`, `hooks_timeout`.
- `model` takes a checkpoint name, not a Jev model ID.
- The response adds `answer_confidence` (a calibrated probability) beside `confidence`, which is "entropy-based". That is a different formula from Jev's.
- The HTTP server caps a question at **100 choice options**. Option labels share a 192-token (English) or 256-token (multilingual and typed-decisions) budget, and they "are trimmed to fit" when they overflow.
- Env vars: `LAYA_HOST`, `LAYA_PORT`, `LAYA_DEVICE` (cuda, mps, or cpu), `LAYA_PRELOAD`, `LAYA_API_KEY` (bearer token), `LAYA_DEFAULT_MODEL`, `LAYA_MAX_LOADED` (default 2).
- Rounding: not documented.

MCP server: `pip install "laya[mcp]"`, then `laya-mcp-server`. Its tools are `laya_predict`, `laya_route`, `laya_shortlist`, and `laya_predict_batch`. Other extras: `[langchain]`, `[onnx]`, `[fast]`.

Fine-tuning is effectively required:

- Typed-decisions benchmark (2,000 decisions): base 0.362, fine-tuned 0.766. Train with `laya-train --data tickets.csv --out ./ft`. The README links a Kaggle 2xT4 notebook and an MPS script.
- An independent run measured 0.583 macro accuracy (pinggy).
- The Decision Index scores it 6.0 (llmconfigurator).

Weak spots:

- **Large option sets.** It scores 0.425 on Banking77 (77 labels) against Jev's 0.870. Orcarouter says it fails past ~20 options. The README's advice is `predict_shortlist` or tournament mode.
- **Option order.** Reversing the options costs 13.75 points (orcarouter).
- **Non-Latin scripts.** "0.000 accuracy at 0.952 average confidence" (orcarouter).
- **Calibration.** The README says the shipped checkpoints are overconfident and should be temperature-calibrated on held-out data. Orcarouter measured ECE 0.466 by default and 0.081 after refitting.

Latency (README): T4 median 33 ms for one question and 72.3 ms for 10 batched. M1 Pro MPS about 30 ms per question. CPU (28 threads) 48 ms per question. Conflict: pinggy reports 66 ms median on an M3 Pro CPU and 39.5 ms per question on a T4. Orcarouter reports 32.8 ms p50 on a T4 and "under a gigabyte" resident for the MLX port.

## AWS Strands Decider (strands-labs)

Repo: https://github.com/strands-labs/strands-decider. Apache-2.0. Install with `pip install strands-decider`. On Apple Silicon, MLX comes from `pip install -e ".[mlx]"`.

- Model ID: `StrandsAgents/strands-decider-2B-hobson-v21` (v19 is also available).
- 1.9B parameters: a Qwen3.5-2B-Base torso, a rank-16 LoRA adapter, and a ~1M-parameter pointer head that replaces the language-model head.
- One masked softmax produces all three primitives.

```bash
strands-decider serve StrandsAgents/strands-decider-2B-hobson-v21 --port 8000
strands-decider ask StrandsAgents/strands-decider-2B-hobson-v21 \
  --state "Help! My payouts have been failing for 3 days!" \
  --choice "Which team should handle this?=billing,sales,retail"
```

- Serves `/v1/systemone` with the Jev request shape (`state`, `questions`).
- The response adds `latency_ms` beside `model`, `answers`, and `usage`.
- No option cap: "Nothing caps how many options a question may carry".
- `--vision` accepts base64 images and needs `pip install "strands-decider[vision]"`.
- Strands Agents integration: `examples/strands/` gates a tool call through a `before_tool_call` hook.
- Rounding and error codes: not documented.
- Accuracy (v21): JevBench 0.762 (176/231), ECE 0.064. "answers at confidence 0.9+ are right ~95% of the time on unseen tasks".
- Latency: RTX 3090 median 115 ms, p95 299 ms. M3 Pro warm (<300 tokens) 153 ms.
- Training needs NVIDIA GPUs on Linux or WSL2.

Not to be confused with **Decider by Mapika** (github.com/Mapika/decider). That is a separate Qwen3.5 family at 0.8B, 2B, 4B, and 35B-A3B, also Apache-2.0. It is served by `decider.serve` with a `DECIDER_MODEL` env var, works with the typesafe-sdk unchanged, takes 2-255 options, and accepts `abstain_below=t`. Decision Index scores: 2B 29.0, 4B 40.7, 35B-A3B 47.1. Source: llmconfigurator open-models page.

## CLM-8B (Contrastive-LM: Stanford + NVIDIA)

Repo: https://github.com/Contrastive-LM/CLM (Apache-2.0). Weights: `Contrastive-LM/CLM-v0.1-8B` on Hugging Face, Apache-2.0. Paper: "Contrastive Language Models" (2026), published as a Notion blog at https://contrastive-lm.notion.site. Authors per the README: Jacky Kwok, Hangoo Kang, Tarun Suresh, Jon Saad-Falcon, Marco Pavone, Christopher Ré, Azalia Mirhoseini. The README does not state their affiliations. The news coverage says Stanford and NVIDIA.

- Architecture: two projection heads (state and action) on a frozen Qwen3-8B encoder, trained with bidirectional InfoNCE. It scores candidates by embedding similarity and generates no text (model card). News reports put each head at about 20M parameters (pasqualepillitteri.it).
- **Primitives: Noul, Choice, and Score over `/v1/systemone`**, plus `Engine.rank()` for ranking free-form candidates (model card, README). VentureBeat: "choosing between options, returning a yes/no probability, scoring against an ordered scale and ranking arbitrary candidates." The earlier "ranking only" reading from the news articles was wrong.

```bash
pip install contrastive-lm
vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b --runner pooling --max-model-len 2048 --port 8090 &
clm-serve
```

```python
from clm import CLMClient, Choice, Noul, Score

client = CLMClient()
r = client.system_one(
    state="Customer: my invoice was charged twice",
    questions={
        "urgency": Noul(instructions="Is this urgent?"),
        "department": Choice(instructions="Which team?",
                             criteria={"billing": "...", "technical": "..."})
    }
)
```

How it differs from Jev (README unless noted):

- The server runs on `http://localhost:8700` and serves a web playground there. It needs a vLLM Qwen3-8B pooling server, port 8090 in the docs' example.
- Models: `clm-latest` (the default reference head), `clm-raw` (an ablation using raw cosine similarity in encoder space), and custom heads via `--model NAME=PATH`. Pydantic AI's `system-one:clm-latest` matches.
- Answer fields: Noul `noul`, Choice `choice`/`confidence`/`probabilities`, Score `score`/`confidence`/`legend`/`probabilities`. These match Jev's names.
- `confidence` = "top probability minus the mean of the others", for both Choice and Score. For Choice this equals Jev's `(n·top − 1)/(n − 1)`. For Score it ignores level distance, so it differs from Jev's Score formula. Noul has no `confidence`.
- **States longer than 2048 tokens are truncated**, with no error. Change it with `--max-model-len`. Jev's limit is 64k.
- Limits: Score needs at least 2 levels, with no maximum stated. The max options and max questions are not documented. Rounding is not documented.
- Auth: set `CLM_API_KEY` to require a bearer token.
- Errors: 401 (bad key), 422 (malformed request), 502 (embedder unreachable).
- TypeSafe requests replay unchanged: "a request written for TypeSafe replays as `client.system_one(state, questions)`".
- `usage.input_tokens` counts only cache misses. Cached state and action vectors cost no tokens.
- Latency (README): RTX 4090 about 28 ms with a new state and 0.6-0.7 ms with a cached state. 4.1-5.7x faster than Jev as a code verifier on an H100. About 13x faster with ~1k action candidates through caching (model card). Conflict: news reports give 16.5 ms against Jev's 149.8 ms on T-Rex ("up to 9x"). The setups differ.
- Accuracy: DeepSWE 81.6% and Terminal-Bench 2.1 87.6%, but only with fine-tuned verifier heads. "SOTA results require fine-tuned heads" (model card). It matched Jev zero-shot on computer use, gaming, and WikiRacing. No ECE or calibration figures are published.
- Not for open-ended reasoning, math, long-form generation, or planning (VentureBeat, quoting the authors).
- **CLM-35B:** not released as of 2026-10-06. The model card and VentureBeat call it a multimodal CLM-35B-A3B planned for "early October". The README gives no date.
- Conflict: hermes-ai.net calls it an "MIT-licensed open-source project by Nous Research" and links github.com/NousResearch/hermes-agent. The official repo and model card say Apache-2.0 and Contrastive-LM, so hermes-ai.net is wrong.

## SemIf (TheoLeeCJ)

Repo: https://github.com/TheoLeeCJ/SemIf-OpenJev, MIT for the code. "Semantic ifs from open models, on a 3090 at home."

- No fine-tuning. It reads native option logits from stock models: Qwen3-0.6B, MiniCPM5-2B, Qwen3.5-4B, Qwen3-Reranker-4B, and a Qwen3.8-27B EXL3 bridge.
- Input: JSONL with `state`, `question`, and `options: [{id, description}]`. That is **not** the Jev `questions` map.
- No REST endpoint is documented.

```bash
CUDA_VISIBLE_DEVICES=0 semif-score --mode direct --model Qwen/Qwen3.5-4B \
  --input examples/decisions.jsonl --output results.jsonl
```

- `--backend llamacpp --gguf <path>` runs on CPU. MLX and MPS are also supported.
- Accuracy: Qwen3.5-4B 0.813 balanced accuracy on authored decisions and 0.637 on WANLI, against published Jev 0.883 (102-row subset). Pinggy reports "0.845 modal agreement" with TypeSafe's published results and 0.958 for a quantized 27B.
- Latency: 1.023 s for 21 criteria on an RTX 3090, against 5.332 s for autoregressive JSON. Prefix reuse reaches 20.03 decisions per second.

## NanoJev (TianyuCodings)

Repo: https://github.com/TianyuCodings/NanoJev, MIT. "A nano replica of Jev".

- 0.6B: a Qwen3-0.6B backbone with decision heads. HF: `C-Tianyu/NanoJev` and `C-Tianyu/NanoJev-Data`. Release `unified-games-v1`.
- Primitives: Choice (2-255 candidates, softmax), Boolean (sigmoid), Score (2-10 levels).
- API: `POST http://127.0.0.1:8765/api/evaluate`, started by `python scripts/serve_decisions.py --checkpoint-dir checkpoints/NanoJev-unified --web-root web`. **Not `/v1/systemone`.**
- It is trained for game control loops (18,760 questions from four games), not general text. Test results: ViZDoom Basic 128/128 (Jev 56/128), Predict Position 27/128, Maze 4/10, Snake 8/8.
- Needs CUDA. No Apple Silicon support.

## Sources

- https://github.com/NandhaKishorM/laya
- https://huggingface.co/convaiinnovations/laya
- https://www.orcarouter.ai/blog/laya-vs-kev
- https://pinggy.io/blog/best_open_source_jev_alternatives_self_hosted_decision_models/
- https://llmconfigurator.com/en/guides/decision-models
- https://llmconfigurator.com/en/guides/decision-models/open-models-beyond-ollama
- https://github.com/strands-labs
- https://github.com/strands-labs/strands-decider
- https://github.com/Contrastive-LM/CLM
- https://huggingface.co/Contrastive-LM/CLM-v0.1-8B
- https://contrastive-lm.notion.site
- https://venturebeat.com/technology/stanford-and-nvidias-open-clm-8b-caches-reusable-agent-actions-and-runs-up-to-9x-faster-than-jev-in-tests
- https://cryptobriefing.com/stanford-nvidia-clm-8b-faster-than-jev/
- https://pro.edgex.exchange/en-US/news/article/stanford-nvidia-clm-8b-9x-faster-ai-agents
- https://pasqualepillitteri.it/en/news/19074/clm-8b-nvidia-stanford-jev-en (search snippet only, the fetch failed)
- https://hermes-ai.net/news/stanford-s-clm-turns-agent-decisions-into-vector-search-9x-faster/
- https://pydantic.dev/docs/ai/models/system-one/
- https://github.com/TheoLeeCJ/SemIf-OpenJev
- https://github.com/TianyuCodings/NanoJev
