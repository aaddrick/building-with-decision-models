# Provider: EU hosts: System1 Models and Uprelic Strom

Snapshot 2026-10-06, sources: system1models.ai llms.txt, llms-full.txt, OpenAPI, and models page [1][2][3][4]; platform.uprelic.com llms.txt, skill.md, blog, and OpenAPI [5][6][7][8]; Infrabase directory [9][10].
The live docs win on any conflict: `https://system1models.ai/llms.txt`, `https://platform.uprelic.com/llms.txt`.

Both services take a Jev-shaped body at `POST /v1/systemone` and add their own fields. Neither is affiliated with TypeSafe [1][6].

---

## System1 Models (Germany; inference in Finland)

### HTTP

```http
POST https://api.system1models.ai/v1/systemone
Authorization: Bearer $SYSTEM1_API_KEY
S1-Region: global | eu        (alias: p2p → global)
```

- `SYSTEM1_API_KEY` is the env var name in the official curl [2].
- `GET /v1/models` (alias `/models`) is the live model registry [1].
- Hosted MCP: `https://api.system1models.ai/mcp`, streamable HTTP, Bearer key. Tools: `decide`, `list_models`, `get_usage`, `get_balance` [1].
- The OpenAPI also lists `POST /v1/multimodal`. Its use is not documented in the llms files [2].

### Request differences from Jev

| Rule | Value |
|---|---|
| Questions per request | **Sources conflict.** llms.txt says s1-pro takes up to 3 text questions, and s1-fast / s1-vision take 1 [1][2]. The OpenAPI says "exactly one question per request by default", with "a per-model multi-question limit… only where the operator enabled it", and the `questions` description says s1-pro up to 3 [3]. `s1-llm-auto-router` takes its fixed routing questions, up to 7 [3]. Over the limit returns `400 request_limit_exceeded`. |
| Context | **4,096 input tokens** for s1-fast, s1-pro, and s1-vision. The count covers state, all questions, all options, and the image. Above that: `400 invalid_request`, never truncated, not billed. Tested 2026-10-06 (4,095 tokens accepted on s1-fast, 4,094 on s1-pro) [2][4]. `s1-llm-auto-router` reads 512 tokens and ignores the rest [2]. |
| State | At most 16 KiB of serialized JSON. Body at most 6 MiB [2][3]. |
| Choice options | `minProperties: 2`. **No maximum is documented**: "model option limits are enforced after model tokenization" [3]. |
| Score levels | `minItems: 2`. No maximum is documented [3]. |
| `instructions` | Optional (nullable) on all types. Choice and Score require `criteria` [3]. |
| Images | s1-vision only. `images` array with `maxItems: 1`: one PNG/JPEG/WebP as a base64 data URL **or a public HTTPS URL**. Max 4 MiB decoded and 2,000,000 pixels [1][3]. |
| Extra fields | Strict schema: `additionalProperties: false` on the request and on every question [3]. |

### Response differences

```json
{"id": "dec_example", "model": "s1-fast",
 "answers": {"urgency": {"type": "score", "score": 1.2, "confidence": 0.6,
             "legend": {"0": "Not urgent", "1": "Somewhat urgent", "2": "Urgent"},
             "probabilities": {"0": 0.1, "1": 0.6, "2": 0.3}}},
 "usage": {"input_tokens": 42, "output_tokens": 0, "decisions": 1},
 "tier": "eu"}
```
(Official OpenAPI example [3].)

- Adds `id`, `tier`, and `usage.decisions`. All are required in the schema [3].
- Headers: `S1-Request-Id`, `S1-Region`, `S1-Execution-Region`, `S1-Model`, `S1-Latency-Ms`, `S1-Charge-Nanos`, `S1-Currency` [3].
- `confidence`: present on Choice and Score. No formula is documented. The example (`0.6` with top probability `0.6`) fits top-probability, but it is one example [3].
- Rounding: not documented.

### Errors

Body: `{"error": {"code", "message", "request_id", "retryable"}}` [3].

| Status | Code / meaning [3] |
|---|---|
| 400 | `request_limit_exceeded`, `invalid_request` |
| 401 | `invalid_api_key` |
| 402 | Insufficient credit |
| 403 | `tier_not_allowed`, `dpa_acceptance_required` |
| 404 | Unknown model |
| 413 | Body, state, or image too large |
| 422 | Unsupported modality |
| 429 | `rate_limit_exceeded`. Honor `Retry-After`. The rate value itself is not documented. |
| 503 | Model unavailable or at capacity. Peer-to-Peer bundles "may return retryable 503" [2]. |
| 504 | Inference deadline expired |

### Models and pricing (launch, per 1M input tokens, output free) [1][2]

| Model | Engine | Peer-to-Peer (`global`) | EU |
|---|---|---|---|
| `s1-fast` | Plumb-4B, text | $0.032 / €0.028 | $0.034 / €0.030 |
| `s1-pro` | Surogate Rune 26B-A4B v3 (EU); falls back to Winnow-12B Q8 | $0.038 / €0.033 | $0.040 / €0.035 |
| `s1-vision` (text only) | Rune; image fallback Gemma 4 12B | $0.038 / €0.033 | $0.040 / €0.035 |
| `s1-vision` with an image | all input tokens at the image rate | $0.217 / €0.190 | $0.228 / €0.200 |
| `s1-llm-auto-router` | CPU routing classifier | $0.001 / €0.001 | $0.001 / €0.001 |

Infrabase lists s1-pro as Winnow-12B and s1-vision as Gemma 4 12B [9]. That is out of date: the official llms.txt now names Rune as the main EU engine, with those models as fallbacks [1].

### Data and residency [1][2]

- API gateway and database: Hetzner, Helsinki. EU inference: Verda, Finland. EU-tier inference always stays in the EU.
- Peer-to-Peer uses spare EU capacity first. When busy, it may rent GPUs through Lium (lium.io) outside the EU/EEA, **but only for keys with "Allow worldwide processing" enabled**. Without that opt-in, requests queue or are rejected. `S1-Region: global` alone never enables worldwide processing.
- No content is stored on any node. Prompts and outputs are never used for training. A DPA is accepted at signup, and inference fails closed (`403`) until it is.

### Latency (vendor, measured from Nuremberg, 2026-10-02; one question, medium text, warm HTTP/2) [4]

| | median | p95 |
|---|---|---|
| s1-pro EU | 199.6 ms | 749.4 ms |
| s1-fast EU | 155.1 ms | 286.7 ms |
| Jev 1.13.0 (same run) | 233.6 ms | 340.2 ms |

### SDK

No System1 SDK is documented. `typesafe-sdk` with `base_url="https://api.system1models.ai"` should reach `/v1/systemone`, since the path matches. **This is not documented or tested.** Risks: the SDK must forward an `S1-Region` header (`extra_headers` / `headers`), the response carries extra fields (`id`, `tier`, `usage.decisions`), and the strict request schema rejects unknown fields.

### Minimal request (official [2])

```bash
curl https://api.system1models.ai/v1/systemone \
  -H "Authorization: Bearer $SYSTEM1_API_KEY" \
  -H "Content-Type: application/json" \
  -H "S1-Region: global" \
  -d '{"model":"s1-fast","state":"Mia owns a red bicycle.","questions":{"color":{"type":"choice","instructions":"Which color is the bicycle?","criteria":{"red":null,"blue":null}}}}'
```

---

## Uprelic Strom (Berlin company; inference in Paris)

**Status: beta. Sources conflict on how to get access.** Infrabase says "In beta, access granted manually" [10]. Uprelic's own skill.md says to sign up at platform.uprelic.com, create a key, and verify a card for 5 units of free credit [6]. Uprelic's own pages do not use the word "beta" [5][6]. Infrabase lists the HQ as Germany [10]; Uprelic says Berlin [6]. Servers are in Paris on Scaleway [6][10].

### HTTP

```http
POST https://api.uprelic.com/v1/systemone
Authorization: Bearer $UPRELIC_API_KEY
```

- `GET https://api.uprelic.com/v1/models` needs no key. Today it returns one model, `strom-1.0.7` (release_date 2026-09-15; "Probabilities calibrated since 2026-10-01") [6][8].
- OpenAPI: `https://api.uprelic.com/v1/openapi.json`. Rendered docs: `https://api.uprelic.com/v1/docs` [6].
- "Switching means pointing the client at `https://api.uprelic.com` with an Uprelic key" [6].

### Request differences from Jev

| Rule | Value [6][8] |
|---|---|
| Questions | 1–256 per request (`maxProperties: 256`) |
| Choice options | 1–256 per skill.md. The OpenAPI sets no bound. |
| Score levels | `minItems: 1`. **No maximum is documented.** |
| Context | 32,768 tokens for state, images, and questions together. This number is from skill.md's "doesn't fit" list; there is no limits table. |
| Images | **The field is `media`, not `images`.** Up to 8 items: `{"type": "image", "url": ...}`, where `url` is a `data:image/...` URL or a public http(s) URL (max 10 MB, 10 s, no redirects). Images are scaled to at most 1 megapixel. Cost is one token per 32×32 px, between 64 and 1,024. |
| `instructions` / criteria | Strings or JSON objects |

### Response differences

```json
{"model": "strom-1.0.7",
 "answers": {"team": {"type": "choice", "choice": "engineering", "confidence": 0.83,
                      "probabilities": {"engineering": 0.89, "billing": 0.07, "account": 0.04}},
             "urgent": {"type": "noul", "noul": 0.96}},
 "usage": {"input_tokens": 283, "output_tokens": 2, "cached_input_tokens": 256,
           "cost": 0.000011886, "currency": "usd"},
 "metadata": {"server_processing_time_ms": 85}}
```
(Official example, "values are illustrative" [6].)

- Adds `usage.cached_input_tokens`, `usage.cost`, `usage.currency` (usd, eur, gbp, or chf), and `metadata.server_processing_time_ms`, also sent as a `Server-Timing` header [6][8].
- `output_tokens` is one per question and free [8].
- `model` "may differ from the alias supplied in the request" [8].
- `confidence` on Choice and Score: "how concentrated the probabilities are" [6]. No formula is given. The example (0.83 with top 0.89, n=3) fits Jev's Choice formula: `(3·0.89 − 1)/2 = 0.835`. That is one illustrative example.
- Rounding: the examples show 2 decimals. Not documented.
- Calibration: ECE 0.033 on public JevBench tasks, per the vendor [7].

### Errors

The error body uses a `detail` field (FastAPI style) [6].

| Status | Meaning [6] |
|---|---|
| 400 | Bad image |
| 401 | Missing or wrong key |
| 402 | Empty prepaid balance |
| 422 | Invalid request, with the field path |
| 429 | Over the limit. Honor `Retry-After`. |
| 5xx | Server error |

### Facts

| Item | Value |
|---|---|
| Price | $0.042 / 1M input tokens. Output free. Only `200` responses are charged, from a prepaid balance [6][10]. |
| Rate limits | 1,200 requests/min and 16 concurrent per account. More through support@uprelic.com [6]. |
| Latency (model time, median, vendor) | 1 question: 91 ms at 550 tokens, 181 ms at 2,000, 228 ms at 8,000, 673 ms at 24,000. 2,000-token text: 281 ms with 8 questions, 438 ms with 16. A 512 px image: 66 ms with 1 question. Add network time; about 100 ms from Germany [6][7]. |
| Data | GPUs in the EU (Paris). No third-party AI provider. **Request contents are deleted after 90 days** (not zero retention) and never used for training [6]. Strom Enterprise offers dedicated deployment in France, Germany, or another EU region, a fixed model version, contract retention, and an SLA [5]. |
| Accounts | Balances in USD, EUR, GBP, or CHF [6] |

### SDK

- Official Python SDK: `pip install uprelic` (Python 3.10+). It reads `UPRELIC_API_KEY`. `Uprelic` / `AsyncUprelic` expose `client.system_one(model=, state=, questions=)`, with helpers `Noul`, `Choice`, `Score` and typed views `.nouls`, `.choices`, `.scores`, like typesafe-sdk [6].
- SDK exceptions: `APIError` → `AuthenticationError` 401, `InsufficientBalanceError` 402, `InvalidRequestError` 400/422, `RateLimitError` 429, `ServerError` 5xx. It retries 429, 502–504, and connection failures twice (`max_retries=`) [6].
- There is no JS SDK. Use `fetch` [6].
- `typesafe-sdk` with `base_url="https://api.uprelic.com"`: Uprelic says switching is a URL and key change [6], but it does not name typesafe-sdk. **Not tested.** Images need `media` through `extra_body`.

### Minimal request (official [6])

```sh
curl https://api.uprelic.com/v1/systemone \
  -H "Authorization: Bearer $UPRELIC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "strom-1.0.7",
       "state": "Our whole team is blocked. The app has been down since this morning.",
       "questions": {"urgent": {"type": "noul", "instructions": "This message needs urgent attention."}}}'
```

## Sources

1. https://system1models.ai/llms.txt
2. https://system1models.ai/llms-full.txt
3. https://api.system1models.ai/openapi.json ("authoritative"; snapshot at https://system1models.ai/openapi.json)
4. https://system1models.ai/models (input limits, benchmarks, latency chart); evidence file https://system1models.ai/evidence/input-limits-2026-10-06.json
5. https://platform.uprelic.com/llms.txt
6. https://platform.uprelic.com/skill.md
7. https://platform.uprelic.com/blog/strom-eu-alternative-decision-model-to-jev.md
8. https://api.uprelic.com/v1/openapi.json ; https://api.uprelic.com/v1/models
9. https://infrabase.ai/inference-apis/system1-models (third party)
10. https://infrabase.ai/inference-apis/strom (third party; "beta, access granted manually", Paris/Scaleway, $0.042)
