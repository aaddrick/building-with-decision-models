# Provider: OpenAI Decisions API (gpt-6-luna)

Snapshot 2026-10-06, sources: developers.openai.com Decisions guide [1], voice guide [2], GPT-6 Luna model page [3], third-party coverage [4][5].
The live docs win on any conflict: `https://developers.openai.com/llms.txt`; append `.md` to any page path.

**Status: beta. The contract is NOT Jev-compatible.** The official guide says "The Decisions API is in public beta, and we expect to GA in the coming weeks" [1]. Third-party coverage of DevDay (2026-09-29) calls it a "limited preview" and says there was "no price per call published yet" [4]. The official guide now publishes a price. **The official docs win.** No API reference page for `/v1/decisions` exists: it is not in `https://developers.openai.com/api/llms.txt`, and the guessed reference URLs return 404. Everything below comes from the guide and its examples.

## HTTP

```http
POST https://api.openai.com/v1/decisions
Authorization: Bearer $OPENAI_API_KEY
Content-Type: application/json
```

There is a Playground at `https://platform.openai.com/decisions` [1].

## Request: different field names from Jev

| Jev | OpenAI Decisions [1] |
|---|---|
| `state` | `input`: a string, or user messages with `input_text` / `input_image` parts |
| `questions` (map keyed by ID) | `questions`: an **array**. Each item carries a unique `name`. |
| `type: "noul"` | `type: "predicate"` |
| Choice `criteria: {id: desc}` | `choices: [{"value", "description"}]` |
| Score `criteria: [desc, ...]` | `levels: [{"label", "description"}]`, lowest first, indices from 0 |
| `instructions` | `instructions` (same) |
| `model: "jev-latest"` | `model: "gpt-6-luna"`, the only model supported today |

Images: inline base64 data URLs only, as `{"type": "input_image", "image_url": "data:image/png;base64,..."}`. Hosted http(s) URLs and `file_id` are rejected [1].

## Response

`answers` is an **array**. Each answer carries `name` [1].

```json
{"answers": [
  {"type": "predicate", "name": "visible_damage", "probability": 0.92},
  {"type": "choice", "name": "department", "choice": "billing",
   "probabilities": [{"value": "billing", "probability": 0.95}, {"value": "technical", "probability": 0.02},
                     {"value": "shipping", "probability": 0.01}, {"value": "other", "probability": 0.02}],
   "confidence": 0.93},
  {"type": "score", "name": "severity", "score": 1.1,
   "probabilities": [{"value": 0, "label": "Cosmetic", "probability": 0.1},
                     {"value": 1, "label": "Workaround available", "probability": 0.7},
                     {"value": 2, "label": "Fully blocked", "probability": 0.2}],
   "confidence": 0.55}]}
```

The guide labels all of these as "illustrative response excerpt[s]" [1]. Full response fields (`model`, `usage`, `id`) are **not documented**.

- Predicate → `probability` (Jev: `noul`). There is no `confidence`.
- Choice and Score `probabilities` are arrays of objects, not maps. Score has no `legend`; each probability entry carries `label`.
- `confidence` exists on Choice and Score: "a separate `confidence` field" [1]. No formula is given. Both illustrative values match Jev's formulas: Choice `(4·0.95 − 1)/3 = 0.933`, and Score `1 − 0.3/(2/3) = 0.55`. This is inferred from illustrative numbers only.
- Rounding: the examples show 2 decimals. Real behavior is not documented.

## Facts

| Item | Value |
|---|---|
| Price | $0.10 / 1M input tokens with `gpt-6-luna` on `/v1/decisions`. No cache-read, cache-write, or output charges. Regional-processing premiums and long-context multipliers apply [1]. The model page gives these as +10% regional and 2× input above 272K [3]. |
| Latency | "about 10x faster than the Responses API" [1]. About 150 ms per third-party coverage [4]. OpenAI states no ms figure. |
| Limits (questions, choices, levels, images, context) | **Not documented** for `/v1/decisions`. GPT-6 Luna's general context is 1,050,000 tokens with max input 922,000 [3], but nothing says this applies to Decisions. |
| Rate limits | Not documented for Decisions. Luna's general limits are 5,000 RPM / 2M TPM on the Build tier [3]. |
| Data | ZDR and HIPAA for eligible customers. Data residency and regional processing in the US and Europe (EEA + Switzerland) [1]. |
| Customization | Not documented. Luna fine-tuning shows "Not supported" [3]. |
| Multi-step | Send dependent questions as separate requests [1]. |
| SDK | No `client.decisions` is documented. The guide uses curl only. **`typesafe-sdk` cannot be used**: the path, field names, and response shapes all differ. |

## Minimal request (official [1])

```bash
curl https://api.openai.com/v1/decisions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-6-luna", "input": "I was charged twice for my order.",
       "questions": [{"type": "choice", "name": "department",
                      "instructions": "Which department should handle this complaint?",
                      "choices": [{"value": "billing", "description": "Payments, invoices, and refunds."},
                                  {"value": "technical", "description": "Problems using the product."},
                                  {"value": "other", "description": "Requests outside these categories."}]}]}'
```

## Gateways

OpenRouter and Vercel list `openai/gpt-6-luna` only as a **chat/language** model [6][7]. Neither routes OpenAI's `/v1/decisions`. Vercel's decision fallbacks can name a language model, which then answers through structured output and returns `confidence: 0`, `probabilities: {}` [7]. See gateways.md.

## Sources

1. https://developers.openai.com/api/docs/guides/decisions.md (platform.openai.com/docs/guides/decisions redirects here)
2. https://developers.openai.com/api/docs/guides/decisions-voice.md
3. https://developers.openai.com/api/docs/models/gpt-6-luna.md
4. https://cryptobriefing.com/openai-decisions-api-gpt-6-luna/ (third party; "limited preview", ~150 ms, no price at announcement)
5. https://www.orcarouter.ai/blog/openai-decisions-api-gpt-6-luna (third party)
6. https://openrouter.ai/api/v1/models/openai/gpt-6-luna/endpoints
7. https://ai-gateway.vercel.sh/v1/models ; https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe.md
