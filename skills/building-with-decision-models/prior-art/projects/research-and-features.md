# Projects: Answers as Data

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/research-and-features.md`.

**Features and prediction**
- Autoresearch feature discovery (LLM proposes → Jev answers → CatBoost): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md)
- 67 numeric columns from Jev answers (suggested): [flaviocopes.com](https://flaviocopes.com/jev/)
- Demand forecasting and predictive features (idea): [docs.typesafe.ai](https://docs.typesafe.ai/concepts/use-case-map.md)
- One judge call vs. 12–14 dimension scores + logistic regression; bookkeeping 40.0% → 91.1%, guardrail false positives 1.5% → 37.2%, 20,139 rows for $1.43: [agentjournal.dev](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/)
- Jev vs. a trained 22M encoder + logistic head; "use Jev to extract structured evidence, then hand that evidence to a lightweight classifier": [mindstudio.ai](https://www.mindstudio.ai/blog/jev-vs-classic-classifiers-benchmark/)
- JEVQA, zero-shot video quality from encoding metadata and bitstream features (Pearson 0.737, on par with ITU-T P.1204.1 at 0.733; 0.824 combined; pixel-only failed): [arXiv:2609.24395](https://arxiv.org/abs/2609.24395)

**Research instruments**
- ENEM exam distractor psychometrics (option probabilities vs. real student choices): [Paulo83-dev/ARTIGO---PSICOMETRIA---JEV-CC-](https://github.com/Paulo83-dev/ARTIGO---PSICOMETRIA---JEV-CC-)
- RST discourse relation labelling (34 labels, 2 Choices per span pair): [mkrupo/som_rst_parsing](https://github.com/mkrupo/som_rst_parsing)
- Jev-Mem agent-memory paper (UT Dallas): [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem)
- Clinical variable extraction, Jev as a baseline: [JunMa11/MedJev](https://github.com/JunMa11/MedJev)
- Systematic-review extraction with verbatim quotes: [choxos/jev-reviewer](https://github.com/choxos/jev-reviewer)
- Engineering: CAD routing, FEM triage, DFM, BOM alignment: [Foadsf/jev-for-engineers](https://github.com/Foadsf/jev-for-engineers)
- Police crash narratives turned into probabilistic crash variables; 195,857 narratives coded, 27 questions, F1 0.908 against 2,416 blinded human judgments, 10,747 more injury/fatal crashes attributed per year: [arXiv:2609.24052](https://arxiv.org/abs/2609.24052)
- Text annotation for computational social science, pre-registered, 18 tasks vs. 19 LLMs; Jev trails the best LLM by a median 11.6 macro-F1 at 44× lower cost, and routing low-confidence items to an LLM matches the LLM at 25–50% of the cost (Jev, Laya, Kev, SemIf, Nimble, decider): [arXiv:2609.24574](https://arxiv.org/abs/2609.24574), [hazemibrahim97/decision-models-css](https://github.com/hazemibrahim97/decision-models-css)
- jlink, record linkage for economists with plain-English match rules; firms F1 0.73 vs. 0.69 for the best string baseline: [keltokhy/jlink](https://github.com/keltokhy/jlink)
- Semantic relation choices before deterministic scientific calculations; 7 wrong choices changed downstream counts but kept the final label: [arXiv:2609.24965](https://arxiv.org/abs/2609.24965)
- "Jev in the Wild", an ecosystem study of 2,170 GitHub projects: [arXiv:2609.30216](https://arxiv.org/abs/2609.30216)

**Analytics columns**
- Databricks ai_decide, a SQL function (beta) returning Noul/Choice/Score from governed tables; model unnamed and may change (ai_decide): [remio.ai](https://www.remio.ai/post/databricks-ai-decide-moves-governed-data-from-analysis-to-action)
- Databricks `ai_decide()` reference; returns a VARIANT with answers and version metadata, suggests aggregating probabilities in dashboards to track trends such as escalation rates (ai_decide): [docs.databricks.com](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_decide)
- jev-orderby-bench, on whether probabilities can drive `ORDER BY`; passes six pre-registered gates on newsgroups (ECE 0.045), fails four of six on product relevance: [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)

**Data curation**
- jev-curate, Rust streaming of Parquet/JSONL rubrics at >1,500 rows/s: [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate)
- "blask datos labelling", the top app on OpenRouter's Jev page (about 26.7B tokens): [openrouter.ai](https://openrouter.ai/typesafe/jev-1.13)

**Benchmarks of Jev**
- OpenSanctions entity resolution: [panios/jev-opensanctions-benchmark](https://github.com/panios/jev-opensanctions-benchmark)
- Chess vs. NPC-addressee detection (out-of-lane vs. in-lane): [wondertwins/jev-benchmark](https://github.com/wondertwins/jev-benchmark)
- Parallel vs. separate questions about one state (identical answers, 12× cheaper batched). This does not extend to many rows in one request, which degrades ranking (see jev-orderby-bench): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/parallel_questions.md)
- Self-consistency vs. LLMs: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook.md)
- Calibration critiques (fair die, "30% risk"): [HN](https://news.ycombinator.com/item?id=49830385), [HN](https://news.ycombinator.com/item?id=49816899)
- jevbench leaderboard (decider-4b slightly above Jev 1.13): [HN](https://news.ycombinator.com/item?id=49849014)
- Pre-registered test, about 9,750 calls vs. Haiku 4.5, Opus 5, and GPT-5.6; ECE Noul 0.012, Choice 0.086, Score 0.254: [primeline.cc](https://primeline.cc/blog/typesafe-jev-pre-registered-test)
- 16,000 calls vs. gpt-5.4-mini and gpt-5.6-luna; matches or beats both on 3 of 4 public sets, 5–56× cheaper: [amankumar.ai](https://amankumar.ai/blogs/jev-measured)
- Known physics distributions as binned Choices; mean total variation 0.518 vs. 0.546 for uniform: [maximumeffort.substack.com](https://maximumeffort.substack.com/p/jev-is-poorly-calibrated), [HN](https://news.ycombinator.com/item?id=49934399)
- jev-behavior-study, 11,621 controlled requests; 88% when the correct option comes first vs. 57% when last: [RINNECODER/jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)
- jev-report, an independent Chinese report (50 reproducible tests); ECE 0.070, measured 5–25× speedup: [HackSing/jev-report](https://github.com/HackSing/jev-report)
- jev-benchmarks with pinned revisions, SHA-256 artifacts, and bootstrapped CIs; Jev vs. GLiNER2.5 (91% AG News, 87% Banking77): [AbdelStark/jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks)

**Benchmarks across decision models**
- Model-vs-model benchmarks (S1MB, sysone-bench, hard-decisions, vendor panels, Red Hat, and more) are listed in `prior-art/projects/choosing-and-switching-models.md`, which links to the lessons from them.
- "Type-safe is not error-free": renaming options 0/1 → no/yes flips 70.4 more answers per 100 and moves AUC from 0.94 to 0.23 (typed decision models): [arXiv:2609.26758](https://arxiv.org/abs/2609.26758)
- Candidate-independent block-causal attention reduces option-order sensitivity (open decision-model architecture): [arXiv:2610.01601](https://arxiv.org/abs/2610.01601)
