# Model notes: Microsoft-Decision-1 (Microsoft Foundry)

Field notes from people who built on Microsoft-Decision-1 (Qwen3.5-9B post-trained by Microsoft, released 2026-10-09), snapshot 2026-10-10. Numbers are author-reported unless a line says otherwise. The wire contract (Jev's body at `<endpoint>/providers/microsoft/v1/systemone`, deployment name as `model`, Azure auth, errors, quota) is in `providers/microsoft-foundry.md`.

The model is one day old at this snapshot. Every number below comes from a launch table or a few dozen early PRs. Re-check before you lean on any of it.

## Limits

- **Context:** 32,768 tokens including the decision token; over it, HTTP 422 naming the limit ([jev-navigator](https://raw.githubusercontent.com/ajbmachon/jev-navigator/claude/model-guide/docs/models.md)). Half of Jev's per-request total. 21–22 JevBench items failed on context alone ([model-market-comparison#290](https://github.com/fstandhartinger/model-market-comparison/pull/290)).
- **Options and levels:** Choice 2–255, Score 2–10, as on Jev ([everruns#4441](https://github.com/everruns/everruns/pull/4441)).
- **Throughput on default quota:** about 1 request in flight at 50–60 RPM before 429s ([jev-navigator](https://raw.githubusercontent.com/ajbmachon/jev-navigator/claude/model-guide/docs/models.md), [jevman-benchmark#17](https://github.com/opper-ai/jevman-benchmark/pull/17)). A relevance search took 7.4 s at 4 items per request against Jev's 1.8 s at 16.
- **Text only.** No images ([catalog](https://ai.azure.com/catalog/models/Microsoft-Decision-1)). Batch inference is disabled ([orcarouter](https://www.orcarouter.ai/blog/microsoft-decision-1-explained)).
- **Lifecycle:** one builder records a preview retiring on 2027-02-04. Weights "are updated continually" behind the same API ([OpenRouter](https://openrouter.ai/microsoft/microsoft-decision-1)), so log the model the response reports.

## Calibration

- **Vendor table (100 = perfect):** Decision-1 92.2, behind Jev 1.13.0 at 93.7 and Quyet-1.0-Large at 93.1; GPT-6 Luna Decisions 89.9 ([cellcog](https://cellcog.ai/blog/microsoft-decision-1/), copying Microsoft's launch chart). No ECE, Brier, or reliability curve is published.
- **Independent JevBench v1.7.31, native Foundry:** calibration 84.40, against 90.6 for Jev 1.13.0 on the same board ([model-market-comparison#290](https://github.com/fstandhartinger/model-market-comparison/pull/290)).
- **Its probabilities sit lower than Jev's on the same pairs.** "Absolute probabilities do not transfer between models": refit every threshold, band, and weight ([jev-navigator](https://raw.githubusercontent.com/ajbmachon/jev-navigator/claude/model-guide/docs/models.md)). jarvis flags its Jev-tuned 0.9 / 0.5 bars for the same reason ([jarvis#681](https://github.com/DanAakesen/jarvis/issues/681)).
- **Not rounded to 0.01** as Jev is (a live Noul came back 0.9975), so ties are rarer, but keep the tiebreaker.

## Accuracy

- **Vendor, 36 benchmarks, 147,137 questions kept blind from training:** Decision-1 83.5%, Jev 82.3%, Quyet 81.9%, Surogate Rune 79.7%, GPT-6 Luna Decisions 79.4%, deck-31B 77.8%, H2O-Lightning-4B 77.2%; Strands-Decider 2B 54.8% on 23 of the 36 ([cellcog](https://cellcog.ai/blog/microsoft-decision-1/)). The Jev rows were added after launch. The 1.2-point lead over Jev has no confidence interval.
- **Independent:** JevBench capability 70.78 against Jev's 77.1 ([#290](https://github.com/fstandhartinger/model-market-comparison/pull/290)). decision-bench text-only rows 90.73% (CI 88.71–92.41), behind pplx-decider 93.89% and ahead of GPT-6 Luna Decisions 89.46% ([atlanai/decision-bench#19](https://github.com/atlanai/decision-bench/pull/19)).
- **opendecider paired bootstrap** ([#49](https://github.com/manjunathshiva/opendecider/pull/49)): ahead of Jev on 200 general decisions (0.795 vs 0.730) and 2,000 typed decisions (0.783 vs 0.754); behind on Laya's 10-task battery (0.751 vs 0.774); **0.530 on toxicity** against 0.77–0.81 for the other models.
- **Robustness (vendor):** decisions flip on 1.3% of eight perturbation types, and never on paraphrased or shuffled options ([launch post](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)). Microsoft's own docs still warn that wording and option order change scores ([Learn](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)).

## Latency and cost

- **Vendor:** 85 ms median, 125 ms p95. A reviewer found the other models' figures were adjusted JevBench medians (2× raw + 150 ms) while Decision-1's was measured through Foundry in-region; on raw timings the lead over Quyet shrinks from 4.5× to about 1.4×, and H2O's raw 29 ms is faster ([pk-sharma](https://www.pk-sharma.com/briefing/microsoft-decision-1-4-5-times-faster-runner-up-raw-timing-gives-1-4-times)).
- **Measured over the network:** 459 ms median on JevBench, 607 ms median and 846 ms p95 at concurrency 3 on decision-bench, about 0.9 s on a single call, 301 ms via Opper against about 1,040 ms via one Foundry deployment.
- **Cost:** $0.042/M input, output free, the same list price as Jev. Measured $0.019–0.030 per 1,000 decisions.

## Where it does well

- **General and typed single-question decisions,** where it led Jev by 3–6.5 points in opendecider and matched GPT-6 Luna Decisions on decision-bench.
- **Microsoft's internal uses** (vendor): Xbox feedback themes over 10,000+ items, quality competitive with GPT-6 Sol at 14× the speed and 1/200 the cost; Copilot quality control; incident knowledge retrieval; adaptive replanning in Microsoft Discovery.
- **Azure shops** that need EU or US data-zone processing and Entra auth on the decision call.

## Where it fails

- **Many items in one request.** As a relevance judge it separated relevant from irrelevant at AUC 0.53 with 16 items per request and 0.58 with 4; Spearman agreement with Jev fell from 0.77 at 1 item to 0.47 at 16 ([jev-navigator](https://raw.githubusercontent.com/ajbmachon/jev-navigator/claude/model-guide/docs/models.md)). Keep each request to a few items, then mind the quota.
- **More false alarms on yes/no:** 6 against Jev's 3 on 106 questions; a Jev + Decision-1 jury scored worse than Jev alone ([abita_s2s#148](https://github.com/chasef07/abita_s2s/pull/148)).
- **Toxicity screening** (0.530 in opendecider). Do not use it alone as a content-safety filter; Microsoft's docs also warn it can miss subtle harm.
- **Route variance:** the same Pac-Man agent scored 2,390 via Opper and 1,298 via one Foundry deployment, with 12.6% fallback moves against 2.1% ([jevman-benchmark#17](https://github.com/opper-ai/jevman-benchmark/pull/17)). The cause (latency budget, quota, region) is not established. Measure on the deployment you will serve.

## By shape

- **Gates:** put the code rule first, and fit the threshold on its own probabilities. Its yes/no false-alarm rate ran higher than Jev's.
- **Rerank and relevance judges:** a few items per request, not 16. Budget for the per-deployment quota.
- **Control loops:** the measured round trip (0.3–1 s) and the 429s, not the 85 ms, set the tick budget. Keep a fallback move.
- **Choosing and switching:** run it in shadow next to the incumbent, and refit every threshold; jarvis and pasta both keep it behind a provider switch or as a comparison column ([jarvis#681](https://github.com/DanAakesen/jarvis/issues/681), [pasta#179](https://github.com/crmitchelmore/pasta/pull/179)).
