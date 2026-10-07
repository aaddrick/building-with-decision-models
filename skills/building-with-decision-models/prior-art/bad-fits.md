# Known Bad Fits

Uses of decision models that the field tried and reported as failures. Each entry names the model it was measured on, in parentheses or in the text. A bad fit on one model may work on another, so check the model before you rule a design out. Numbers are author-reported unless a line says otherwise.

The general items (any decision model) also appear as one-line headlines in `prior-art/INDEX.md`. This file holds their evidence and links. Model-specific failures live in `models/`.

### Any decision model

- **Chess, and puzzle-like search**: it blunders on every move (Jev, [HN](https://news.ycombinator.com/item?id=49746967)). Keep search in code.
- **Coding, chat, summarization, complex reasoning**: out of scope by design, and latency grows with state size (Strands Decider's own guidance, [Strands blog](https://strandsagents.com/blog/introducing-strands-decider/)).
- **Final judge on math, code, or logic correctness**: Jev trails GPT-6 by about 14.5 points ([arXiv 2609.26550](https://arxiv.org/abs/2609.26550)), and scored 78.1% on JudgeBench against Luna's 88.6% ([Braintrust](https://www.braintrust.dev/evals/jev-vs-gpt-eval-judges)). Triage and risk scoring work. Final judgment does not.
- **Code review as the only reviewer**: too weak at reasoning (Jev, [HN](https://news.ycombinator.com/item?id=49842208)).
- **Expert-domain groundedness**: 53.3% on ExpertQA (Jev, [Braintrust](https://www.braintrust.dev/evals/jev-vs-gpt-eval-judges)).
- **Exact counting**: letter counting was right 117 times out of 216 (Jev, [jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)). Count in code.
- **Recovering known probability distributions**: binned physics distributions came out barely better than uniform, 0.518 vs. 0.546 total variation (Jev, [substack](https://maximumeffort.substack.com/p/jev-is-poorly-calibrated)).
- **Empathy-style constructs as research variables**: high confidence came with near-chance accuracy (Jev, [arXiv:2609.24574](https://arxiv.org/abs/2609.24574)).
- **Many labels when you already have training data**: bge-small plus logistic regression beat every decision model on Banking77 at 93.3% ([jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval)). Flat classification over a large label set is a reported weakness even on Jev ([parallel.ai](https://parallel.ai/blog/testing-jev)).
- **Sorting by probability on hard relevance tasks**: Jev 1.13.0 failed 4 of 6 gates on Amazon product-relevance data (inversion 0.255, ECE 0.279), and rewording a question moved answers by 0.164 ([jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)).
- **A rerank in place of good retrieval**: over 33,047 catalog entries, a Jev rerank alone did not beat vector retrieval ([X](https://x.com/GoSailGlobal/status/2100877682972258619)).
- **"None of these" inside a ranking Choice**: on Jev it returned empty results for 35 of 200 queries ([Hindsight](https://hindsight.vectorize.io/blog/2026/09/24/adding-jev-reranker-what-we-learned)). Use a separate `fits` Noul.
- **Planning a sequence of tool calls in one request**: 38–44% position-wise on Jev ([JevRouter](https://github.com/BillionsBobby/JevRouter)).
- **Detecting failures across a whole agent run with small judges**: about 59% recall for Jev and a local 4B, against 95% for GPT-4.1-mini on StepShield ([Edward](https://github.com/VeridicalTech/Edward)).
- **Element-table browser agents on shadow DOM, iframes, canvas, or uploads**: none of them support these ([andrew.ooo](https://andrew.ooo/posts/jev-ultrafast-review-browser-use-typesafe-jev-browser-agent/), [jev-ego](https://github.com/romaluev/jev-ego)).
- **Semantic HTTP routing for authentication or authorization**: the project's own README warns against it ([hono-jev-router](https://github.com/yusukebe/hono-jev-router)).
- **Model routing without measuring first**: Janus found routing cost more and gained nothing on one dataset ([Janus](https://github.com/FirasSX914/Janus)).
- **Probabilities wired straight to irreversible trades**: one case study reports a $31,680 loss ([besthub.dev](https://www.besthub.dev/articles/jev-the-ai-model-that-decides-doesn-t-generate-text-3ddd3e29c005)).
- **Continuous flight control from a hosted model**: Jev at 2.4 Hz scored 56 when landing, against 69.9 for a simple baseline controller ([FlightBench](https://github.com/AlperKartkaya/FlightBench)).
- **Perception**: most decision models are text-only. Self-driving pushback: perception is the bottleneck ([HN](https://news.ycombinator.com/item?id=49722214)). Do perception with CV first, even where a model accepts images (see `models/clef.md`).
- **General context-pruning proxies and working-memory pruning**: about 0% savings on one trial, with a large slowdown ([yoshi](https://github.com/compozy/yoshi)). One guardrail harness shelved pruning because the benefit did not cover the cost ([pi-warden](https://github.com/DevMortimer/pi-warden)).
- **Out-of-box calibration claims**: on Jev, a fair die gave face 1 about 83% of the time ([HN](https://news.ycombinator.com/item?id=49830385), [HN](https://news.ycombinator.com/item?id=49839995)). Fit Platt scaling on your own labels, whatever the model.
- **Speed marketing**: measured gains for Jev were about 5–7× over small LLMs, not 40–200× ([HN](https://news.ycombinator.com/item?id=49845146)). Batched LLM calls can match it offline.
- **Record dedupe and a personal prompt router**: one user found these "underwhelming / OK at best" on Jev ([HN](https://news.ycombinator.com/item?id=49842510)).
- **Sound-alike profanity in usernames**: puns like `mike_hunt` score about 0.16, under the threshold. Look-alike spellings are caught (Jev, [profanity-checker](https://github.com/4rays/profanity-checker)).

### Specific models

Failures measured on one model live in that model's file, under "Where it fails", so an agent on that model reads them next to the model's limits and calibration. Index: `models/INDEX.md`.

- Laya (zero-shot, many labels, tool calling, act/escalate head, small-set rerank, long option lists, VisionLaya NSFW): `models/laya.md`
- Nimble (as the only moderation gate): `models/nimble.md`
- Kev and other small local models (as the only leak or destructive-action gate): `models/kev.md`
- CLM-8B (long state, tool calling, "done"/"wait" judges): `models/clm.md`
- GPT-6 Luna (confidence on multi-step reasoning): `models/luna.md`
- Clef and Clef-flash (sub-second hosted loops, images on a synchronous path, fine-grained image classification): `models/clef.md`
- Strands Decider 2B (multi-step reasoning, long documents): `models/strands-decider.md`
- Tev1, Mercury Decide, Liquid d1, decider-2b, GLiNER2.5-Decide: `models/others.md`
