# Provider: Perplexity Decisions API (pplx-decider)

Snapshot 2026-10-06, sources: docs.perplexity.ai quickstart, API reference, pricing data, and changelog [1][2][3][4], Hugging Face model cards [5][6], OpenRouter catalog [7], third-party coverage [8].
The live docs win on any conflict: `https://docs.perplexity.ai/llms.txt`; append `.md` to any page path.

Launched October 2026 [4]. Weights are open (Apache 2.0) and fine-tuned from Qwen3.8-27B [5][6].

## HTTP

```http
POST https://api.perplexity.ai/v1/decisions
Authorization: Bearer $PERPLEXITY_API_KEY
Content-Type: application/json
```

- **Path is `/v1/decisions`, not `/v1/systemone`.** Any other path returns `404`, including a trailing slash [1].
- Any Perplexity API key works. An `x-api-key` header is ignored and returns `401` [1].
- Body: `model`, `state`, `questions`. Question and answer shapes are Jev's: `noul` / `choice` / `score`, `instructions`, `criteria` map or array; answers carry `noul`, `choice`, `probabilities`, `confidence`, `score`, `legend` [1][2]. **Unknown top-level fields return `400`** (`additionalProperties: false`) [1][2].

| Rule | Value [1][2] |
|---|---|
| Questions per request | 1–128, non-empty names |
| Choice options | 1–255. The v1.1 decision head is `[255, 5120]` [6]. |
| Score levels | 1–10. A single level always returns score 0, p=1. |
| Input tokens | Under 262,144 (state, images, and all questions) |
| Body | 32 MiB (`413` above) |
| Noul | Needs `instructions` or `criteria`. Neither returns `400` ("Noul question must have criteria or instructions"). |
| `state` | String, object, or array. `null` returns `400`. |
| `model` | Required on every request. A missing or unknown model returns `400`. |

### Images (differs from Clef / System1 / Strom)

There is no `images` field. Put images **inside `state`** as an array of OpenAI-style parts [1]:

```json
"state": ["Which color is the square?",
          {"type": "image_url", "image_url": {"url": "data:image/png;base64,iVBORw0KGgo..."}}]
```

- Accepts PNG, JPEG, or WebP data URLs. An `http(s)` URL returns `400`. An image can be the whole `state`.
- Max 2,048 tiles of 32×32 px per image (1440×1440 and 2048×1024 fit; 1600×1310 does not). **A larger image does not return `400`. The request hangs about a minute, then returns `504`.**
- Perplexity's tests found about 1,000 input tokens per megapixel.
- No per-request image count is documented.

## Response

```json
{"model": "pplx-decider-v1.1-27b",
 "answers": {"defect": {"type": "noul", "noul": 0.9424522889347015},
             "sentiment": {"type": "choice", "choice": "mixed", "confidence": 0.9255246944002182,
                           "probabilities": {"positive": 0.0206, "mixed": 0.9503, "negative": 0.0290}}},
 "usage": {"input_tokens": 367, "output_tokens": 3}}
```
(Values shortened from the official example [1].)

- **Values are not rounded.** They come back at full float precision [1].
- `model` echoes the name you sent. It is not a versioned build ID [1].
- `output_tokens` is non-zero (3 in the example) but free [1].
- Identical requests "occasionally differ in the second decimal place" [1].
- `confidence` (Choice and Score): "the model's own certainty estimate… It is not the top probability… It drops when the runner-up is close" [1]. The single official example fits Jev's Choice formula `(n·top − 1)/(n − 1)` = 0.9255. Its Score answer fits `1 − Σ pᵢ·|i − top|` = 0.7839, **without** Jev's `U` normalization (Jev's formula would give 0.676). This is inferred from one example and is not documented.

### Errors

The body is `{"error": {"message", "type", "code"}}`. Branch on `error.type`, not `error.code`, which can be a string, a number, or null. `404` and `405` have empty bodies. `504` may return HTML [1].

| Status | Why [1] |
|---|---|
| 400 | Bad JSON, missing or unknown model, unknown field, a limit exceeded, bad image URL |
| 401 | Bad or missing key, or key sent in `x-api-key` |
| 404 / 405 | Wrong path or method (`Allow: POST`) |
| 413 | Body over 32 MiB |
| 429 | Rate or token limit. Honor `Retry-After` (seconds). |
| 5xx | `504` after about a minute when the model did not answer in time. Otherwise a service failure. |

Responses carry an `x-request-id` header, except on 401, 404, and 504 [1].

## Model facts

| Item | Value |
|---|---|
| Model IDs | `pplx-decider-v1.1-27b` (docs default), `pplx-decider-v1-27b` [1][3]. No aliases. |
| Price | **Conflict.** The current quickstart, API reference, and pricing data say **$0.02 / 1M input**, output free, no per-request fee [1][2][3]. The October 2026 changelog launch entry and OpenRouter (`perplexity/pplx-decider-v1-27b`, `0.00000004`) say **$0.04 / 1M** [4][7]. Most likely the price was cut after launch, but no page says so. |
| Rate limit | 10 requests/s per organization on every plan, plus a token limit for large bursts. Headers: `x-ratelimit-limit`, `-remaining`, `-used`, `-reset` (Unix seconds) [1]. |
| Latency (Perplexity's tests, 2026-09-30) | A few hundred tokens: under 2 s. About 90K tokens: 5 s. About 190K: 14 s. Near the limit: 23 s. Use a 30 s client timeout for any input; 10 s is enough for small inputs [1]. |
| Context | 262,144 tokens [1] |
| Input | Text, JSON, images [1] |
| Data / residency | Not documented on the Decisions pages. "Usage is billed to the organization that owns the API key" [1]. |
| Open weights | `perplexity-ai/pplx-decider-v1-27b` and `perplexity-ai/pplx-decider-v1.1-27b` on HF. Python 3.12+ and about 49 GiB of GPU memory [5][6]. v1.1 needs its bundled noncausal-attention inference code and a separate 255-row readout head, not an `lm_head` [6]. |
| Benchmarks (vendor) | v1: 85.71% vs Jev 84.51% on Perplexity's own 11-benchmark panel [5]. v1.1: Decision Index 61.56 vs Jev 57.9 [6]. |

## SDK compatibility

- Perplexity documents no SDK for Decisions. Use plain HTTP (`httpx`, `fetch`) [1].
- `typesafe-sdk` with only a `base_url` override: **does not work as documented.** The SDK appends `/v1/systemone`, and Perplexity returns `404` for any path other than `/v1/decisions` [1]. The SDK also sends `model` only when one is set, but Perplexity requires it. A custom `fetch` or transport that rewrites the path could work. Nobody has tested that.

## Minimal request (official [1])

```bash
curl -X POST https://api.perplexity.ai/v1/decisions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "pplx-decider-v1.1-27b",
       "state": {"title": "Battery died after two weeks",
                 "review": "The headphones sound great, but the battery stopped charging after two weeks."},
       "questions": {"defect": {"type": "noul", "instructions": "Does the review report a product defect?"}}}'
```

## Sources

1. https://docs.perplexity.ai/docs/decisions/quickstart.md
2. https://docs.perplexity.ai/api-reference/decisions-post.md (OpenAPI 3.0.3, server `https://api.perplexity.ai/v1`)
3. https://docs.perplexity.ai/docs/getting-started/models.md (embedded pricing data: `decisions.input: 0.02`)
4. https://docs.perplexity.ai/docs/resources/changelog.md (October 2026 entry: `pplx-decider-v1-27b`, $0.04)
5. https://huggingface.co/perplexity-ai/pplx-decider-v1-27b
6. https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b
7. https://openrouter.ai/api/v1/models/perplexity/pplx-decider-v1-27b/endpoints
8. https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel (third party; repeats $0.04, 262,144, under 2 s to 23 s)
