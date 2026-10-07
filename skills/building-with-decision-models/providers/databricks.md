# Provider: Databricks `ai_decide`

Snapshot 2026-10-06, sources: docs.databricks.com (the SQL function reference, the AI Functions overview, and the REST API reference). The live docs win. The launch blog post ("Introducing ai_decide", 2026-10-01) has no technical specs beyond the docs. It promises decisions "in a fraction of a second" but gives no latency, throughput, or accuracy numbers.

Status: **Beta**. A workspace admin enables it on the Previews page.

## SQL

```sql
ai_decide(state, questions [, options])
```

| Arg | Type | Notes |
|---|---|---|
| `state` | `VARIANT` or `STRING` | plain text, or a JSON-encoded object or array |
| `questions` | **constant** `STRING` | "A constant `STRING` expression containing a nonempty JSON object". Each entry has question ID → `type`, `instructions`, and `criteria` where it applies. The Jev question shape. |
| `options` | `MAP<STRING, STRING>`, optional | only `version`, `'1.0'` (the default) |

Example (docs, verbatim):

```sql
SELECT ai_decide(
  '{"name": "TrailShell jacket", "description": "Lightweight waterproof hiking jacket made from recycled polyester. Packs into its own pocket."}',
  '{
    "category": {
      "type": "choice",
      "instructions": "Which product category best fits this item?",
      "criteria": {
        "outerwear": "Jackets, coats, and other protective outer layers",
        "footwear": "Shoes, boots, and sandals",
        "accessories": "Bags, hats, and other accessories"
      }
    }
  }',
  map('version', '1.0')) AS decision;
```

## Return `VARIANT`

```json
{"response": {"answers": {"<id>": {...}}}, "metadata": {"version": "1.0"}, "error_message": null}
```

On failure, `response` is `null` and `error_message` describes the failure. The function does not raise. Filter on `error_message`.

Answer shapes (docs):

| Type | Fields |
|---|---|
| noul | `{"type": "noul", "probability": 0.1}`. **The field is `probability`, not `noul` as in Jev.** Confirmed in both the SQL and REST references. |
| choice | `type`, `choice`, `probabilities`, `confidence` (0-1) |
| score | `type`, `score` (probability-weighted index, "It can be fractional"), `legend`, `probabilities` (keys `"0"`, `"1"`, ...), `confidence` |

The docs' field paths are `response.answers.<id>.probability`, `.choice`, and `.score`.

- Choice criteria: "maps 1 to 255 nonempty labels". Each description can be "a string, JSON object, JSON array, or `null`".
- Score criteria: "2 to 10 descriptions, ordered from lowest to highest". Same as Jev.
- Noul criteria: optional.
- `confidence` formula: not documented. The docs' example numbers (choice probabilities 0.8/0.1/0.1 with `confidence: 0.9`) fit neither Jev's formula (0.70) nor the entropy formula (0.42), so treat them as illustrative.
- Rounding: not documented.
- No `usage` or `model` field is documented in the response.

## REST (real-time)

```http
POST https://<workspace-host>/api/2.0/ai-functions/ai-decide
```

- OAuth scope `ai-functions`. Beta.
- Body: `{"state": ..., "questions": {...}, "options": {"version": "1.0"}}`.
- Response: `{"response": {"answers": {...}}, "metadata": {"version": "..."}}`, with the same answer shapes. Noul uses `probability`.
- Error and status codes: not enumerated in the reference.
- Rate limit: none documented for ai-decide. The same reference lists ai-classify at 1,200 req/min and ai-extract at 120 req/min.

## Platform facts

| Item | Value |
|---|---|
| Runtime | DBR 15.4 LTS minimum, 18.2+ recommended |
| Not available on | Databricks SQL Classic |
| Regions (AWS) | `ap-northeast-1`, `ap-south-1`, `ap-southeast-2`, `ca-central-1`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `sa-east-1`, `us-east-1`, `us-east-2`, `us-west-2` (feature-region-support, AI functions table). No cross-geography or Asia-geo footnote applies to ai_decide. Workspaces with the Enhanced Security and Compliance add-on have separate regional support. Azure and GCP region lists were not captured. |
| Model | not named. The docs say only that the models are licensed under Apache 2.0. The launch blog (2026-10-01) says only that it is "powered by a decision model", cites TypeSafe's Jev as an example of the category, and gives no maker or size. |
| Pricing | not published. The SQL docs link the Databricks SQL pricing page, which has no ai_decide price. The AI Functions pricing page lists only AI Parse Document, AI Extract, and AI Classify (for example AI Classify at 3-60 DBUs per 1,000 documents). The blog claims "lower latency and cost than an LLM on similar tasks" without numbers. |
| State size / context | not documented |
| Data | processed "within the Databricks security perimeter", and the parameters passed are not stored |

## Sources

- https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_decide
- https://docs.databricks.com/aws/en/large-language-models/ai-functions
- https://docs.databricks.com/api/ai-functions/v1/ai-decide
- https://www.databricks.com/product/pricing/databricks-sql
- https://www.databricks.com/product/pricing/ai-functions
- https://docs.databricks.com/aws/en/resources/feature-region-support
- https://www.databricks.com/blog/introducing-aidecide-make-fast-decisions-your-governed-data
