# Projects: Judges and Evals

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/judges-and-evals.md`.

Comparing or benchmarking decision models against each other (indexes, head-to-heads, cross-model calibration, thresholds across models): see `prior-art/projects/choosing-and-switching-models.md`.

**Platforms**
- Langfuse built-in Jev-as-a-judge evaluators on production traces: [langfuse.com](https://langfuse.com/changelog/2026-09-22-jev-as-a-judge), [langfuse.com](https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals)
- TypeSafe official eval workflows (agent trace QA, support, invoice, SOC): [evals.typesafe.ai](https://evals.typesafe.ai/)
- deepeval Jev metric: [deepeval.com](https://deepeval.com/integrations/models/typesafe-ai). harbor rewardkit judges: [harbor-framework/harbor](https://github.com/harbor-framework/harbor). vercel/ai evaluate: [vercel/ai](https://github.com/vercel/ai). Arize tracing: [arize.com](https://arize.com/docs/ax/integrations/python-agent-frameworks/typesafe/typesafe-tracing). Opik tracing: [comet.com](https://www.comet.com/docs/opik/integrations/typesafe)
- "sel-jev-rubric-judge", about 9.2B tokens on OpenRouter: [openrouter.ai](https://openrouter.ai/typesafe/jev-1.13)
- Jev as a judge in LangSmith. Reported: 500/500 binary verdicts matched the oracle, and score variance was 92–913× lower than LLM judges: [langchain.com](https://langchain.com/blog/jev-agent-evals-langsmith)
- Ollaya, a local runtime that applies each model's fitted temperature at load (Nimble, Laya): [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya)
- `ai_decide()` in SQL. Score takes 2–10 ordered levels and returns a weighted score (for example 1.8). The docs suggest it for rubric-based prioritization but give no calibration guidance, and the backing model is not named (Databricks ai_decide): [docs.databricks.com](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_decide)

**Tools for managing judgments**
- hunch, "dbt for judgments": YAML specs, cached runs, gold-label tests, and a diff of rows that would flip: [oneryalcin/hunch](https://github.com/oneryalcin/hunch)
- jev-align, active labelling + GEPA optimization: [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)
- JevEval "Jev-as-a-judge": [HN](https://news.ycombinator.com/item?id=49807852)
- Kiln auto-optimization of questions with the model fixed. Reported: half the errors at 1/7 the cost: [kiln.tech](https://kiln.tech/blog/auto_optimizing_jev_with_autoresearch)

**Reported judge results**
- Tessl verifiers, 2,725 tests, 85.9% agreement: [HN](https://news.ycombinator.com/item?id=49821631)
- AITA benchmark, 2nd of 7: [HN](https://news.ycombinator.com/item?id=49821894)
- Every's editorial vibe check: [every.to](https://every.to/vibe-check/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds)
- Second-opinion verification of other models' outputs (Good Start Labs): [HN](https://news.ycombinator.com/item?id=49718890)
- Rubric judges vs LLMs, 9 panels. LLM judges cost 16–325× more. A cascade gains at most 2.7 points because errors are correlated: [arXiv 2609.29769](https://arxiv.org/abs/2609.29769)
- Accept when confident, escalate when unsure. Within 3 points of GPT-6 at 36% of the cost, and the cascade gains 0.9 points at 41% of the cost: [arXiv 2609.26550](https://arxiv.org/abs/2609.26550)
- Zero-shot detection of 10 alignment-failure types across 44 benchmarks. Median AUROC 0.886, 63× cheaper than LLM judges: [arXiv 2609.29429](https://arxiv.org/abs/2609.29429)
- Text annotation in social science: trails the best LLM on 14 of 15 tasks at 44× lower cost. Routing low-confidence items to an LLM matches the LLM at ¼–½ the cost: [arXiv 2609.24574](https://arxiv.org/abs/2609.24574)
- Analytics anomaly escalation: 100% recall, 55.8% precision: [amplitude.com](https://amplitude.com/blog/jev-analysis). Prose evaluation: ECE 0.121, Brier 0.090: [infinisynapse.com](https://infinisynapse.com/en/blog/jev-benchmark)
- Natural context flips decisions: 61.4% of correct Jev decisions were redirected, and three other decision models flipped 64.9–73.2%: [arXiv 2609.30243](https://arxiv.org/abs/2609.30243)

**Hallucination and groundedness**
- RAGTruth and SummEval vs Opus 5. With a tuned threshold, hallucination accuracy matched at 87% for about 300× less cost. SummEval rank correlation 0.74 vs 0.70: [arize.com](https://arize.com/blog/jev-as-a-judge/)
- Groundedness 80.2% across 11 datasets, best of 5 judges. JudgeBench answer correctness 78.1% vs Luna's 88.6%: [braintrust.dev](https://www.braintrust.dev/evals/jev-vs-gpt-eval-judges)
- Cribrix filters RAG chunks and withholds answers that fail claim verification: [david96182/cribrix](https://github.com/david96182/cribrix). citation-verifier checks whether cited papers support the claim: [MarissaFamularo/citation-verifier](https://github.com/MarissaFamularo/citation-verifier)

**Rubric scoring of content**
- Study notes (Knowledge Signal): [HN](https://news.ycombinator.com/item?id=49840561)
- Sentence-by-sentence debate scoring for about $0.05 per video: jevmeter [ChetasLua/jevmeter](https://github.com/ChetasLua/jevmeter)
- Startup idea KILL/FIX/SHIP: killmyidea [monteduro/killmyidea](https://github.com/monteduro/killmyidea)
- Persona testing, posts judged by 100–10,000 simulated personas: Crowdcheck [crowdcheck-ai.vercel.app](https://crowdcheck-ai.vercel.app/)
- Self-consistency cookbooks (measuring judge stability): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook.md)
- Prose linters with boolean dimensions: Sniff Test, 10 per paragraph, measured against Haiku: [DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest). slop-grader: [lukstei/slop-grader](https://github.com/lukstei/slop-grader)
- Editorial QA on whether an edit preserves the original, calibrated on Wikipedia diffs: jev-fidelity [klauswg/jev-suite](https://github.com/klauswg/jev-suite/tree/master/jev-fidelity)
- Content rules, reported precision 1.00 on 119 trial pages (Kev): Qualm [RoderickQiu/qualm](https://github.com/RoderickQiu/qualm)

**Code review as triage**
- diffjury: [raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury). jev-review (staged Noul risk matrix): [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review)
- Calibrating Jev as a reviewer: [HN](https://news.ycombinator.com/item?id=49803758). Pushback: [HN](https://news.ycombinator.com/item?id=49842208)
- Semantic linting against AGENTS.md: Perch [HN](https://news.ycombinator.com/item?id=49840204), adhere [HN](https://news.ycombinator.com/item?id=49843708), slop-linter [almcc/slop-linter](https://github.com/almcc/slop-linter), taste-lint [mblode/taste-lint](https://github.com/mblode/taste-lint)
- Clean Code Judge, 31 boolean smells per PR file: [frostney/clean-code-review](https://github.com/frostney/clean-code-review). semcheck, Go linter with published precision: [arturobermejo/semcheck](https://github.com/arturobermejo/semcheck). Blink, post-change verification: [blink.review](https://blink.review)
