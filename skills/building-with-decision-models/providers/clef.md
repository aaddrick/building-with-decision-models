# Provider: Cloudflare Clef / Clef-flash (Workers AI)

Snapshot 2026-10-06, sources: developers.cloudflare.com model pages and raw JSON schemas [1][2][3][4], Workers AI pricing/errors/limits pages [5][6][7], Cloudflare blog [8], Hugging Face model cards and reference code [9][10][11], flaviocopes.com hands-on test [12]. Third-party claims are marked.
The live docs win on any conflict: `https://developers.cloudflare.com/llms.txt`; append "index.md" to any docs page path.

Released 2026-10-01 [8]. Clef = 27B, post-trained from Qwen3.8-27B. Clef-flash = 9B, from Qwen3.5-9B. Both have a vision encoder. Apache 2.0 weights on Hugging Face [8][9][10].

## HTTP

```http
POST https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/cloudflare/clef
Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN
```

- Swap `clef` for `clef-flash` in the path for the 9B model [1][2].
- The env var names `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_AUTH_TOKEN` come from the official curl and Python examples [1].
- The token needs Workers AI permissions. flaviocopes names them as `Workers AI - Read` and `Workers AI - Edit` [12]. Cloudflare's model page does not list them.
- **Path is not `/v1/systemone`.** The official route is `/ai/run/@cf/cloudflare/<model>` [1][2]. A third-party blog says Clef is "served at the same POST /v1/systemone path" [13]. No Cloudflare page shows that path for Workers AI. The `/v1/systemone` wording appears only in the HF reference code, where a `systemone()` Python function takes a Jev-shaped body [11].

Body: Jev-shaped (`model`, `state`, `questions`) plus an optional `images` field [3].

| Field | Rule (from the input schema [3]) |
|---|---|
| `model` | **Required.** Pattern `^\s*(clef\|clef-flash)\s*$`. It is sent in the body and named in the URL too. |
| `state` | Required. String, object, or array. "Long text state is truncated to fit the model's token limit." |
| `questions` | Required. 1–64 questions. IDs: letters, digits, `_`, `.`, `-`, max 100 chars. |
| `instructions` | Required on noul, choice, and score in the hosted schema. The HF card says `instructions` is optional and the question ID is used when it is missing [9]. That is the self-hosted code only. |
| Noul `criteria` | Optional `{true, false}`. |
| Choice `criteria` | Map of option → description or `null`. **2 to 255 options** (text of the schema description; there is no `maxProperties` keyword). |
| Score `criteria` | Ordered array. `minItems: 2`, `maxItems: 10`. |
| `images` | "Clef extension to the System One API." Max 4. Each is a base64 data URL string, or `{content_type, base64}`. PNG/JPEG/WebP. Each image max 4 MiB and 16 megapixels, 8 MiB total decoded. Whole body max 13 MiB. Remote URLs are rejected. Images are "placed before the state". |

### Choice option limit: resolved

- **255** (2–255 options). This is the official Workers AI input schema for both models [3][4]. flaviocopes says the same [12].
- **26** comes from one third-party blog (OrcaRouter, 2026-10-02), which says "choice (2 to 26 named options), score (2 to 26 ordered levels)" [13]. No Cloudflare page or HF card says this. The score part also contradicts the official `maxItems: 10`. Treat 26 as wrong.
- Self-hosting: the HF reference code enforces no option count [11]. Its `encode_record` has a default token limit of `max_length=16384` [9].

## Response

The output schema is the same for both models [4]. Field names match Jev: `model`, `answers{}`, `usage{input_tokens, output_tokens}`. Choice: `choice`, `probabilities`, `confidence`. Score: `score`, `legend` (string keys), `probabilities`, `confidence`. Noul: `noul`.

**REST wraps the answer** in Cloudflare's standard envelope. This is observed by flaviocopes [12]; the output schema [4] does not show it:

```json
{"result": {"model": "clef-flash", "answers": {...}, "usage": {"input_tokens": 395, "output_tokens": 0}},
 "success": true, "errors": [], "messages": []}
```

- **Workers binding** (`env.AI.run`) returns the Jev-shaped object directly, with no envelope [12]. The official example returns `Response.json(response)` and reads `response.answers.*` [1].
- `model` comes back as `clef` / `clef-flash`, with no version number [12]. No versioned ID or alias is documented.
- `output_tokens` was 0 in every response flaviocopes saw [12]. Output is not billed [5].

### Rounding and `confidence` (differs from Jev)

- **Rounding: 4 decimals**, not 2. The flaviocopes response shows `0.9664`, `0.9126`, `1.1069` [12]. The HF reference code calls `round(x, 4)` [11]. The hosted docs say nothing on rounding.
- **`confidence` is not Jev's formula.** The sources conflict:
  - HF reference `systemone_answer()`: `confidence` = top probability, for both Choice and Score [11].
  - Hosted (flaviocopes' two live answers [12]): the top-probability rule does not fit (top 0.9664 → confidence 0.9126). Jev's formulas do not fit either. Both answers fit `(n·Σpᵢ² − 1)/(n − 1)` (Choice n=4: 0.9125 vs 0.9126; Score n=3: 0.4298 vs 0.4298). **This is inferred from two data points and is not documented.** Under that formula Score confidence ignores how far probability sits from the top level.
  - Official schema text: "How certain the model is, derived from the probabilities" [4].
  - Do not reuse thresholds tuned on Jev's `confidence`.

### Errors

| Code | Meaning | Source |
|---|---|---|
| `5006` | `model` field does not match the `clef\|clef-flash` pattern (for example `jev-latest` left in) | flaviocopes only [12]. **Not in** Cloudflare's errors table [6]. |
| `5007` / 400 | No such model | [6] |
| `3006` / 413 | Request too large | [6] |
| `3036` / 429 | Daily free allocation of 10,000 neurons used up | [6] |
| `3040` / 429 | Out of capacity, try again | [6] |
| `3007` / 408 | Timeout | [6] |
| (message) | `exceeded this model context window limit (65536)` | Seen by flaviocopes with large images [12] |

Images: Workers AI estimated image tokens as base64 length / 4. A 575 KB PNG was rejected for exceeding the 65,536-token context. Keep each image under about 190 KB. This was observed 2026-10-01 [12]. Cloudflare does not document it.

## Model facts

| Item | Clef | Clef-flash |
|---|---|---|
| Model ID | `@cf/cloudflare/clef` | `@cf/cloudflare/clef-flash` |
| `model` body value | `clef` | `clef-flash` |
| Price | $0.24 / 1M input (21,818 neurons/M) | $0.09 / 1M input (8,182 neurons/M) [5] |
| Free tier | 10,000 neurons/day on Free and Paid plans, then $0.011 / 1,000 neurons [5]. flaviocopes estimates this as about 458K Clef or 1.2M Clef-flash tokens/day [12]. | same |
| Context | 65,536 tokens [1][2] | 65,536 tokens |
| Median / p95 latency (Cloudflare's own run) | 209.3 / 238.6 ms | 38.8 / 122.4 ms [8] |
| Latency, REST from Italy (flaviocopes) | median 524–726 ms | median 191–205 ms [12] |
| Input | text, JSON, images. The model page also says video [1]. The hosted schema has only `images` [3]; the HF code accepts `videos` [9]. | same |
| Rate limit | Not documented per model. The model page lists Clef under "Text Generation" [1], and the Workers AI default for that task is 300 req/min [7]. This is inferred, not stated for Clef. | same |
| Data | "we don't read, store, or train on your requests or responses" (except for opt-in fine-tuning) [8] | same |
| Customization | RL fine-tuning service. Today it is hands-on through Cloudflare's FDE team. A self-serve platform comes later. Pipeline: AI Gateway (dataset capture) → Workers AI (rollouts) → Containers (RL sandbox) → new Trainer → BYO-model redeploy. Cloudflare takes expressions of interest only [8]. | same |

## Workers binding (official example [1])

```jsonc
// wrangler.jsonc (from flaviocopes [12]; the binding name is your choice)
{ "ai": { "binding": "AI" } }
```

```ts
const response = await env.AI.run("@cf/cloudflare/clef", {
  model: "clef",
  state: "Checkout has been failing for every customer for the last hour.",
  questions: {
    urgent: { type: "noul", instructions: "Is this support request urgent?" },
    team: { type: "choice", instructions: "Which team should handle this request?",
            criteria: { billing: "Payments, invoices, and refunds",
                        technical: "Outages, errors, and configuration",
                        sales: "Plans and upgrades" } },
    severity: { type: "score", instructions: "How severe is the customer impact?",
                criteria: ["No impact", "Minor", "Major", "Critical"] },
  },
});
```

As of 2026-10-01, the types from `wrangler types` do not cover Clef, so `answers` is `unknown`. Declare your own type [12].

## REST (official curl [1])

```sh
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/cloudflare/clef \
  -X POST \
  -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
  -d '{"model": "clef", "state": "Checkout has been failing for every customer for the last hour.",
       "questions": {"urgent": {"type": "noul", "instructions": "Is this support request urgent?"}}}'
```

Read `.result.answers`.

## SDK compatibility

- `typesafe-sdk` / `@typesafe-ai/sdk` with only a `base_url` override: **does not work** as documented. The SDK posts to `<base>/v1/systemone`, and Cloudflare's route is `/ai/run/@cf/cloudflare/<model>` with a `result` envelope. Cloudflare documents no `/v1/systemone` route.
- JS workaround (flaviocopes [12], not official): pass a custom `fetch` to `TypeSafeClient`. It rewrites the URL to `/ai/run/@cf/cloudflare/${model}` and returns `result`. Set `defaultModel: 'clef-flash'` and `apiKey: CLOUDFLARE_AUTH_TOKEN`. Only `systemOne()` works. `client.models.list()` does not.
- Python: no documented adapter. The SDK's `transport=` / `http_client=` arguments may allow one, but nobody has tested that.

## Gateways

OpenRouter lists `cloudflare/clef` and `cloudflare/clef-flash` (modality `text+image->decisions`, 65,536 context, $0.24 / $0.09) [14]. See gateways.md.

## Sources

1. https://developers.cloudflare.com/workers-ai/models/clef/index.md
2. https://developers.cloudflare.com/workers-ai/models/clef-flash/index.md
3. https://developers.cloudflare.com/workers-ai/models/clef/schema-input.json (identical to `clef-flash/schema-input.json`)
4. https://developers.cloudflare.com/workers-ai/models/clef/schema-output.json (identical to `clef-flash/schema-output.json`)
5. https://developers.cloudflare.com/workers-ai/platform/pricing/index.md
6. https://developers.cloudflare.com/workers-ai/platform/errors/index.md
7. https://developers.cloudflare.com/workers-ai/platform/limits/index.md
8. https://blog.cloudflare.com/clef-decision-models/ (2026-10-01)
9. https://huggingface.co/Cloudflare/clef (README)
10. https://huggingface.co/Cloudflare/clef-flash (README)
11. https://huggingface.co/Cloudflare/clef/raw/main/joint_schema_model.py (`systemone_answer`, `systemone`)
12. https://flaviocopes.com/clef.md (third party, hands-on, 2026-10-01)
13. https://www.orcarouter.ai/blog/clef-decision-models-release (third party, 2026-10-02; source of the "26 options" and "/v1/systemone path" claims)
14. https://openrouter.ai/api/v1/models/cloudflare/clef/endpoints, https://openrouter.ai/api/v1/models/cloudflare/clef-flash/endpoints
