# Provider: Gateways: OpenRouter, Vercel AI Gateway, LLM Gateway

Snapshot 2026-10-06, sources: OpenRouter docs and live catalog [1][2][3][4][5], Vercel AI Gateway docs and live model list [6][7][8], LLM Gateway docs and live model list [9][10][11].
The live docs win on any conflict: `https://openrouter.ai/docs/llms.txt`, `https://vercel.com/docs/llms.txt` (sitemap: `https://vercel.com/docs/sitemap.md`), `https://docs.llmgateway.io/llms.txt`.

## Which decision models each gateway routes (live catalogs, 2026-10-06)

| Model | OpenRouter | Vercel AI Gateway | LLM Gateway |
|---|---|---|---|
| TypeSafe Jev | `typesafe/jev-1.13`, alias `~typesafe/jev-latest`. Bare `jev-1.13` / `jev-latest` are also accepted on `/api/v1/systemone` [1][3]. $0.042/M, context 32,000 [4]. | `typesafe-ai/jev`, $0.042/M, context 32,000; description "64,000 tokens total per request; 32,000 for state plus the longest question" [8] | `jev-1.13.0`, aliases `jev`, `jev-latest`, `jev-preview`; optional `typesafe/` prefix. $0.042/M, context 64,000, text only [9][11] |
| Cloudflare Clef | `cloudflare/clef`, $0.24/M, 65,536, text+image [5] | not listed [8] | not listed [11] |
| Cloudflare Clef-flash | `cloudflare/clef-flash`, $0.09/M, 65,536, text+image [5] | not listed | not listed |
| Perplexity decider | `perplexity/pplx-decider-v1-27b` (endpoint `…-20261001`), **$0.04/M**, 262,144, text+image [5]. `pplx-decider-v1.1-27b` returns 404 on the endpoints API. | not listed | not listed |
| Laya (Convai) | not checked | `convaiinnovations/laya`, `convaiinnovations/laya-free`; free; 8,192 context [8] | not listed |
| Liquid d1 | not checked | `liquid/d1`, $0.04/M, 65,536 [8] | not listed |
| OpenAI `gpt-6-luna` | chat model only [5] | language model only [8] | not checked |
| System1 / Strom | `uprelic/strom-1.0.7` returns 404 [5]. System1 not found. | not listed | not listed |

- OpenRouter's Clef and decider entries come from the live endpoints API [5]. OpenRouter's docs talk only about Jev, so **whether `/api/v1/systemone` or `/api/alpha/decisions` routes Clef or the decider is not documented**. The request schema has no `images` field [2].
- The decider price conflicts: OpenRouter lists $0.04/M, while Perplexity's own docs now say $0.02/M (see perplexity.md).

---

## OpenRouter

| Item | Value |
|---|---|
| System One (TypeSafe-compatible) | `POST https://openrouter.ai/api/v1/systemone`. SDK base URL: `https://openrouter.ai/api` [1][3]. |
| Native Decisions (alpha) | `POST https://openrouter.ai/api/alpha/decisions`, with OpenRouter TS / Python / Go SDKs [1] |
| Auth | `Authorization: Bearer $OPENROUTER_API_KEY`. No TypeSafe account needed [1][3]. |
| Model ID mapping | `jev-1.13` → `typesafe/jev-1.13`. `jev-latest` → `~typesafe/jev-latest`. Prefixed IDs are used as-is [3]. |
| Response extras | `id` (`gen-dec-…`), `provider`, `usage.cost` (USD). `model` = the OpenRouter versioned ID, e.g. `typesafe/jev-1.13-20260917` [2][3]. |
| Request extras | `provider` (routing prefs), `session_id` (≤256 chars, never sent to the provider), `trace`, `user` [2] |
| Errors | `{"error": {"code": <int>, "message"}}`: 400, 401, 402 (insufficient credits), 403, 404, … [2] |
| `confidence` / rounding | Passed through from TypeSafe. The example shows 2 decimals [2]. |

typesafe-sdk works with a `base_url` override (official [3]):

```python
client = TypeSafeClient(api_key=os.environ["OPENROUTER_API_KEY"], base_url="https://openrouter.ai/api")
```

You can also set `TYPESAFE_BASE_URL=https://openrouter.ai/api` and `TYPESAFE_API_KEY=<OpenRouter key>` [3].

`client.models.list()` **fails**. It hits OpenRouter's `GET /api/v1/models`, which returns a different shape, and the SDK rejects it [3].

---

## Vercel AI Gateway

| Item | Value |
|---|---|
| TypeSafe-compatible | Base `https://ai-gateway.vercel.sh/typesafe`. Endpoints: `POST /typesafe/v1/systemone`, `GET /typesafe/v1/models` [6]. |
| Native HTTP | `POST https://ai-gateway.vercel.sh/v1/evaluate` [7] |
| AI SDK | `experimental_decide` from `ai`. Needs `ai` 7.0.128+, or `experimental_evaluate` on earlier AI SDK 7. `gateway.decisionModel('typesafe-ai/jev')`. The old `evaluationModel()` still works [7]. |
| Not supported | Decisions are not available through the OpenAI-, Anthropic-, or Cohere-compatible endpoints [7] |
| Auth | `Authorization: Bearer $AI_GATEWAY_API_KEY`, or a Vercel OIDC token. BYOK: add a TypeSafe key to bill the provider directly [6]. |
| Model ID | `typesafe-ai/jev`. No versioned ID is shown [6][8]. |

**Native `/v1/evaluate` uses different field names** from Jev [7]:

| Jev / TypeSafe-compat | Vercel `/v1/evaluate` and AI SDK |
|---|---|
| `type: "noul"` | `type: "boolean"` |
| answer `noul` | answer `probability` |
| `usage.input_tokens` | `usage.inputTokens` |
| (n/a) | `providerMetadata.gateway.{routing, cost, marketCost, surchargeCost, gatewayCost, generationId}` |

The `/typesafe` path keeps TypeSafe names (`noul`) and adds `provider_metadata.gateway` (snake case) [6].

**Decision fallbacks** are a Vercel extension. Use `providerOptions.gateway.models: [{model, when: {question, confidenceBelow}}]` to rerun an uncertain answer on another model. Both stages are billed and run one after the other [6][7]. If a language model answers Choice or Score, the response returns `confidence: 0` and `probabilities: {}`, which mean "unavailable" and not "zero" [6]. `providerOptions.gateway.zeroDataRetention: true` and `only: [...]` restrict providers [7].

The typesafe-sdk JS client works with a `baseURL` override (official [6]):

```ts
new TypeSafeClient({ apiKey: process.env.AI_GATEWAY_API_KEY, baseURL: 'https://ai-gateway.vercel.sh/typesafe' });
```

The SDK's request type has no `providerOptions` field. Pass it through an intermediate object [6]. Vercel's page shows only JS for the SDK; its Python example uses `requests` [6].

---

## LLM Gateway (llmgateway.io)

| Item | Value |
|---|---|
| Endpoint | `POST https://api.llmgateway.io/v1/systemone` [9] |
| Auth | `Authorization: Bearer $LLM_GATEWAY_API_KEY` [9] |
| Models | Only Jev today: `jev-1.13.0` (aliases `jev`, `jev-latest`, `jev-preview`) [11]. Models page: `https://llmgateway.io/models?filters=1` [9]. |
| Aliases | Moving aliases resolve to the pinned version. Response `model` is provider-prefixed, e.g. `typesafe/jev-1.13.0` [9]. |
| Input | **Text only** [9] |
| Restrictions | Decision models work only on `/v1/systemone`. Using one on `/v1/chat/completions` returns a 400 that points to the right endpoint. They are not available in the playground [9]. |
| Response | TypeSafe shape. The example shows 2 decimals and `confidence` [9]. |
| Self-host | AGPLv3 core, runs in Docker [10] |
| SDK | No typesafe-sdk guide. `base_url="https://api.llmgateway.io"` should resolve to `/v1/systemone`, but this is **not documented or tested**. |

## Sources

1. https://openrouter.ai/docs/guides/community/jev.md
2. https://openrouter.ai/docs/api/api-reference/systemone/submit-a-system-one-request.md
3. https://openrouter.ai/docs/guides/community/typesafe-sdk.md
4. https://openrouter.ai/api/v1/models/typesafe/jev-1.13/endpoints
5. https://openrouter.ai/api/v1/models/{cloudflare/clef, cloudflare/clef-flash, perplexity/pplx-decider-v1-27b, openai/gpt-6-luna}/endpoints (live, 2026-10-06; 404 for perplexity/pplx-decider-v1.1-27b and uprelic/strom-1.0.7)
6. https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe.md
7. https://vercel.com/docs/ai-gateway/modalities/decision.md
8. https://ai-gateway.vercel.sh/v1/models (live, 2026-10-06; filter `type == "evaluation"`)
9. https://docs.llmgateway.io/features/system-one (text taken from https://docs.llmgateway.io/llms-full.txt)
10. https://docs.llmgateway.io/llms.txt
11. https://api.llmgateway.io/v1/models (live, 2026-10-06)
