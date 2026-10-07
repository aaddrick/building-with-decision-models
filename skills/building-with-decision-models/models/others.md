# Model notes: other models

Models with only a few field notes, snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. Each one's wire details are in the provider file named in its heading.

## Tev1 (Together AI, via Ollama; `providers/ollama.md`)

- **Options:** 2–24 per Choice ([model card](https://huggingface.co/togethercomputer/Tev1-4B-experimental)). It returns a letter, not probabilities. Large legal-action sets need a code pre-filter.
- **Context:** about 2k tokens through Ollama ([modelfit.io](https://modelfit.io/blog/ollama-decision-models-nimble-tev1-mac/)); Tev1 4B about 2,050 ([ai-stack](https://github.com/IgorChicherin/ai-stack)). That caps transcript windows.
- **Accuracy:** reported 0.901 vs 0.932 for Jev, the closest open model in that comparison ([respan.ai](https://www.respan.ai/articles/jev-alternatives)).
- **Precision:** Tev1 0.8B (`tev1-08b`) moved 0.0105 accuracy between fp32 and fp16. Report dtype and hardware in studies.
- **Training data:** benchmarked against Jev, not trained on its outputs.
- **Fails at:** shell-command auto-approval. Tev1 4B gave 3 false-safe approvals at a 0.9 threshold ([strument](https://github.com/dbohdan/strument/tree/c2320ca142f77495ecdcadd3cd7a4c9b9445369f/doc/experiments/2026-10-decision-models)).

## decider-2b (Mapika; `providers/open-weights.md`)

- **Options:** 2–255.
- **Latency:** 32.6 ms median on a laptop GPU.
- **Fails at positional keys:** accuracy fell from 0.70 to 0.51 when it picked records by position among 64 ([model card](https://huggingface.co/Mapika/decider-2b)). Give options descriptive keys.
- **Fails at learning from LLM labels alone:** its LLM-labeled training stage lost 2.2 points on human-labeled sets ([HF](https://huggingface.co/mapika/decider-2b)). Keep a human-reviewed holdout.

## Liquid d1 (Liquid AI; `providers/gateways.md`)

- **Hosted only:** API-only, so it cannot run locally. Not for regulated or on-prem data ([datanorth.ai](https://datanorth.ai/news/liquid-ai-releases-d1)).
- **Latency:** 200–300 ms per text decision ([liquid.ai](https://www.liquid.ai/blog/d1-decision-model)).
- **No published benchmarks.** Pilot it on one route before you trust it with a filter.

## Databricks `ai_decide` (`providers/databricks.md`)

- **The model is unnamed and may change.** For a study or a trend line, log the version in the returned `metadata`, or use open weights.
- **Answers can vary between calls** (per the docs). Snapshot results to a table, and do not mark a wrapper deterministic.
- **No published throughput, cost, or accuracy numbers.** Filter rows in SQL before asking many questions over a big table ([remio.ai](https://www.remio.ai/de/post/databricks-ai-decide-moves-governed-data-from-analysis-to-action-de)).
- Questions must be constant per query, which suits analytics columns.

## Mercury Decide

- **Fails at shell-command auto-approval:** 12 false-safe approvals at a 0.9 threshold ([strument](https://github.com/dbohdan/strument/tree/c2320ca142f77495ecdcadd3cd7a4c9b9445369f/doc/experiments/2026-10-decision-models)).

## GLiNER2.5-Decide

- **Fails as an agent "done?" or "wait" judge:** it gave the same answer almost every time ([aimultiple](https://aimultiple.com/decision-models)).
