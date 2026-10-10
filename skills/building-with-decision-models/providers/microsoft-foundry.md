# Provider: Microsoft Foundry (Microsoft-Decision-1)

Snapshot 2026-10-10, sources: the Microsoft Learn how-to [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision), the Foundry catalog card [[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1), the launch post on Command Line [[3]](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/), the Foundry blog announcement [[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742), OpenRouter's model page [[5]](https://openrouter.ai/microsoft/microsoft-decision-1), and live probes builders published [[6]](https://github.com/everruns/everruns/pull/4441)[[7]](https://github.com/ajbmachon/jev-navigator/blob/claude/model-guide/docs/models.md). Field notes (calibration, accuracy, failures): `models/microsoft-decision-1.md`.
The live docs win on any conflict: the Learn page [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision) (its Markdown source is in `MicrosoftDocs/azure-ai-docs` on GitHub, which you can read when learn.microsoft.com is blocked).

**Status: GA on the catalog card [[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1), "public preview" in the launch blog [[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742), and a preview that "Microsoft retires on 4 February 2027" in one builder's notes [[7]](https://github.com/ajbmachon/jev-navigator/blob/claude/model-guide/docs/models.md). Check the retirement date on your deployment before you build on it. The contract is Jev's `/v1/systemone` body under an Azure path and Azure auth.** Same `state`, the same `questions` map keyed by your IDs, the same `noul` / `choice` / `score` types and `criteria` shapes, and an `answers` map keyed by the same IDs [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision). What differs is the URL, the auth, the `model` value (your deployment name), and the limits below.

## HTTP

```http
POST <your-foundry-resource-endpoint>/providers/microsoft/v1/systemone
Authorization: Bearer $AZURE_ENTRA_TOKEN        # Entra ID, scope https://cognitiveservices.azure.com/.default
# or
api-key: $AZURE_API_KEY
Content-Type: application/json
```

```json
{
  "model": "<deployment-name>",
  "state": {"message": "Checkout is down again. This is my third request.", "customer_contact_count": 3},
  "questions": {
    "team":           {"type": "choice", "instructions": "Which team should handle this request?",
                       "criteria": {"billing": "Charges, invoices, and refunds",
                                    "engineering": "Bugs, errors, and outages",
                                    "support": "How-to and account questions"}},
    "severity":       {"type": "score", "instructions": "How severe is this issue?",
                       "criteria": ["Cosmetic", "Minor", "Major", "Critical"]},
    "repeat_contact": {"type": "noul", "instructions": "Has the customer contacted support before?"}
  }
}
```

(Official example [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision).)

- **`model` is your deployment name**, not `Microsoft-Decision-1`. A deployment named `pi-decision-1` sends `"model": "pi-decision-1"`. The response `model` names the underlying model (for example `microsoft-decision-1`), so it differs from what you sent [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision). Log the response value, and keep the deployment name in the constants module (rule 11).
- `state` accepts text or JSON [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision).
- Noul `criteria` (`true` / `false`) is optional [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision). Score `criteria` is an array, lowest level first. `score` is the probability-weighted mean of level indexes and can fall between levels [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision).
- Response: `answers.<id>` carries `type` plus the answer. The docs show only `choice` and say the response "also includes the deployed model name and token usage" [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision). Builders report Jev's answer fields: `noul`, `choice`, `score`, `probabilities`, `confidence`, `legend`, and `usage` [[6]](https://github.com/everruns/everruns/pull/4441)[[8]](https://github.com/agentjido/req_llm/pull/1092). One live call returned noul 0.9975, choice 0.995, and score 1.37 over three levels, so **values are not rounded to 0.01** as Jev's are [[6]](https://github.com/everruns/everruns/pull/4441). No source documents the `confidence` formula: do not assume Jev's.

### Auth and setup

```bash
export AZURE_ENDPOINT="<your-foundry-resource-endpoint>"
export DEPLOYMENT_NAME="<your-deployment-name>"
az login
export AZURE_ENTRA_TOKEN=$(az account get-access-token --resource https://cognitiveservices.azure.com --query accessToken --output tsv)
```

Entra ID is the recommended route; in Python, `azure.identity.DefaultAzureCredential().get_token("https://cognitiveservices.azure.com/.default")` [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision). Entra tokens last about an hour, so a long batch can fail midway with 401: refresh per request, or use the resource key for long runs [[7]](https://github.com/ajbmachon/jev-navigator/blob/claude/model-guide/docs/models.md). The blog's sample text names `FOUNDRY_BASE_URL`, `FOUNDRY_API_KEY`, `FOUNDRY_MODEL`, but its code reads `AZURE_ENDPOINT` and `DEPLOYMENT_NAME` [[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742). The Learn page uses the `AZURE_*` names.

Deploy (official [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)):

```bash
az cognitiveservices account deployment create \
  --name <ACCOUNT_NAME> --resource-group <RESOURCE_GROUP> \
  --deployment-name <DEPLOYMENT_NAME> \
  --model-name "Microsoft-Decision-1" --model-format Microsoft --model-version "1" \
  --sku-name GlobalStandard --sku-capacity 1
```

Use `--sku-name DataZoneStandard` to keep inference inside the nearest data zone (US or EU) [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)[[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742). Deploying needs the **Cognitive Services Contributor** role [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision).

### Errors [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)

| Status | Cause | Action |
|---|---|---|
| 400 | Invalid question type or shape | Check `state`, `questions`, `type`, `criteria` |
| 401 | Missing, invalid, or expired credential | Refresh the Entra token or check the `api-key` header |
| 403 | Identity has no access to the deployment | Check the role assignment |
| 404 | Wrong endpoint or path | Copy the endpoint from the deployment details page |
| 404 `DeploymentNotFound` | `model` names no deployment on this resource [[6]](https://github.com/everruns/everruns/pull/4441) | Send the deployment name, not the model name |
| 422 | Unsupported deployment name or question definition. Also returned **over the 32,768-token limit**, with the limit named in the body (Jev returns 400 there) [[7]](https://github.com/ajbmachon/jev-navigator/blob/claude/model-guide/docs/models.md) | Check `model` and each question; split or trim the state |
| 429 | Deployment rate limit | Exponential backoff, or request more quota |

There is no official SDK for the decision route. The Learn sample uses `urllib` and `azure-identity` [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision). Because the body is Jev's, a Jev client with its base URL set to `<endpoint>/providers/microsoft` should work with an Entra token as the bearer; that is inferred, not documented. With an API key you need a client that can send the `api-key` header instead of `Authorization`.

## Model facts (Microsoft-Decision-1, version 1)

| Item | Value |
|---|---|
| Base | Qwen3.5-9B, post-trained by Microsoft for single-pass scoring. Microsoft says later versions will rebase on MAI and OpenAI models [[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1)[[3]](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/). |
| Model version | `1`. OpenRouter's card says the weights "are updated continually, while the API shape stays the same" [[5]](https://openrouter.ai/microsoft/microsoft-decision-1). Re-check thresholds after any version change. |
| Price | $0.042 per million input tokens; output free [[3]](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)[[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742). Same in the US and EU Datazones [[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742). |
| Context | 32,768 tokens [[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1). OpenRouter lists 33K [[5]](https://openrouter.ai/microsoft/microsoft-decision-1). Half of Jev's 64k per-request total. |
| Limits (options, levels, questions per request) | Not documented [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)[[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1). Probes: Choice 2–255 options and Score 2–10 levels, as on Jev; 300 options or 11 levels return 400 [[6]](https://github.com/everruns/everruns/pull/4441). Questions per request: not reported. |
| Rate limits | Per-deployment quota; not published [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision). Builders on default quota hit 429 (with `Retry-After`) at 50–60 requests per minute and about 1 request in flight, where Jev took 32 in flight [[7]](https://github.com/ajbmachon/jev-navigator/blob/claude/model-guide/docs/models.md)[[9]](https://github.com/opper-ai/jevman-benchmark/pull/17). Request more quota before a batch job, or wall-clock time is the bottleneck. |
| Deployment types | `GlobalStandard` (any Azure region, latency can vary) and `DataZoneStandard` in selected regions (US, EU) [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)[[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742). Provisioned throughput (PTU) is offered for "Direct from Azure" models [[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1). |
| Input | Text or JSON only. No images, audio, or video [[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1). |
| Output | Probabilities only. No rationale [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)[[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1). |
| Latency | Vendor: 85 ms median, 125 ms p95, measured through Foundry in the same region, against other models' adjusted JevBench medians (Jev 240 ms) [[3]](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)[[10]](https://cellcog.ai/blog/microsoft-decision-1/)[[13]](https://www.pk-sharma.com/briefing/microsoft-decision-1-4-5-times-faster-runner-up-raw-timing-gives-1-4-times). Measured by others over the network: 0.21 s P50 on OpenRouter [[5]](https://openrouter.ai/microsoft/microsoft-decision-1), about 0.46–0.9 s per request on Foundry [[6]](https://github.com/everruns/everruns/pull/4441)[[11]](https://github.com/fstandhartinger/model-market-comparison/pull/290). Budget for the network, not the 85 ms. |
| Training data | Public datasets under Microsoft's Open Data process plus synthetic data [[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1). |
| Responsible use | Not the sole decision-maker for credit, employment, housing, insurance, education, healthcare, or legal rights; no surveillance or profiling [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)[[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1). |

## What Microsoft says about the model's limits [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)

- **Wording and order sensitivity:** scores change with the phrasing and order of questions and options, and badly framed questions still return scores. Microsoft suggests randomizing option order in testing. Its launch post reports 1.3% flips across eight perturbations, and none for paraphrased or shuffled options [[3]](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/): treat that as their benchmark, not your data.
- **Calibration is strongest on familiar task types.** Validate on your own labeled cases before you automate a threshold [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)[[4]](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742).
- **Score is for ordering and thresholds**, not as an absolute calibrated rating [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision).
- Add an abstention option such as `cannot tell` when a forced choice would be wrong [[1]](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)[[2]](https://ai.azure.com/catalog/models/Microsoft-Decision-1).

## Through OpenRouter

ID `microsoft/microsoft-decision-1` (versioned `microsoft/microsoft-decision-1-20261009` in responses [[12]](https://github.com/atlanai/decision-bench/pull/19)), one provider (Azure), $0.042/M input, free output, 33K context, released 2026-10-09 [[5]](https://openrouter.ai/microsoft/microsoft-decision-1). The card says it runs on OpenRouter's Decisions API, not the chat endpoint, and that chat-completions SDKs do not work with it [[5]](https://openrouter.ai/microsoft/microsoft-decision-1). OpenRouter's docs do not say whether `/api/v1/systemone` also routes it: test before you rely on the Jev path there. See `providers/gateways.md` for OpenRouter's two decision paths. Opper lists it as `azure:global/microsoft-decision-1` [[9]](https://github.com/opper-ai/jevman-benchmark/pull/17).

## Sources

1. [Microsoft Learn: Deploy and use Microsoft-Decision-1 in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision) (ms.date 10/07/2026). Markdown source: [MicrosoftDocs/azure-ai-docs](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision.md)
2. [Microsoft Foundry model catalog: Microsoft-Decision-1](https://ai.azure.com/catalog/models/Microsoft-Decision-1)
3. [Command Line: Introducing Microsoft-Decision-1 (Achint Srivastava, 2026-10-09)](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)
4. [Microsoft Foundry blog: Introducing Microsoft-Decision-1 in Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742)
5. [OpenRouter: microsoft/microsoft-decision-1](https://openrouter.ai/microsoft/microsoft-decision-1)
6. [everruns/everruns#4441 (live probes: limits, auth, 404, about 0.9 s)](https://github.com/everruns/everruns/pull/4441)
7. [jev-navigator docs/models.md (422 over context, quota, Entra token lifetime, retirement date)](https://github.com/ajbmachon/jev-navigator/blob/claude/model-guide/docs/models.md)
8. [agentjido/req_llm#1092](https://github.com/agentjido/req_llm/pull/1092)
9. [opper-ai/jevman-benchmark#17](https://github.com/opper-ai/jevman-benchmark/pull/17)
10. [cellcog: Microsoft-Decision-1 price, benchmarks, vs Jev (copies Microsoft's launch table)](https://cellcog.ai/blog/microsoft-decision-1/)
11. [fstandhartinger/model-market-comparison#290](https://github.com/fstandhartinger/model-market-comparison/pull/290)
12. [atlanai/decision-bench#19](https://github.com/atlanai/decision-bench/pull/19)
13. [pk-sharma: the vendor latency figures use different bases](https://www.pk-sharma.com/briefing/microsoft-decision-1-4-5-times-faster-runner-up-raw-timing-gives-1-4-times)
