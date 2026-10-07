# Projects: Pairing a Decision Model With an LLM

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/llm-pairing.md`.

### Verify-then-escalate cascades and judges

- SDE cascade cookbook (gpt-5.4-mini extracts → Jev checks per field → gpt-5.5 escalates): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/sde_cascade.md)
- OpenRouter "Cut LLM Cost with a Jev-Verified Cascade": [openrouter.ai](https://openrouter.ai/typesafe). Cookbook version: gpt-luna drafts, Jev checks support at 0.8, failures go to gpt-astra, declined questions go to a human. Reported 0 wrong answers for $0.012 on 50 questions, against 2 wrong for $0.175 frontier-only: [openrouter.ai docs](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade)
- JEV-as-a-Judge (CMU). Jev judges, and anything under 0.9 escalates to GPT-6. Reported +0.9 points over GPT-6 at 41% of its fee on 1,610 pairs: [arXiv 2609.26550](https://arxiv.org/abs/2609.26550). Write-up: [flowtivity.ai](https://flowtivity.ai/blog/jev-as-a-judge/)
- Cheap-confirm-escalate (regex/small model → Jev → big model): [HN](https://news.ycombinator.com/item?id=49763623). Lev: [HN](https://news.ycombinator.com/item?id=49844757)
- LangGraph Jev + LLM fallback: [langchain.com](https://www.langchain.com/blog/building-prod-with-jev-and-langgraph)
- tripwire runs seven Jev checks (PII, injection, tone, on-topic, hallucination risk, ...) on every LLM response in about 100 ms, then replaces, blocks, or annotates it: [noelzappy/tripwire](https://github.com/noelzappy/tripwire)
- Pentest decision layer: the model adjudicates findings and severity for an LLM pentest agent. One case study, not statistically significant (Jev, Laya): [arXiv 2609.28940](https://arxiv.org/abs/2609.28940)
- Amplitude anomaly first pass before review. Reported 100% recall but 55.8% precision on 64 charts: [amplitude.com](https://amplitude.com/blog/jev-analysis)

### Routing (code, specialist LLM, model tier, or human)

- Intent routing pattern (code / specialist LLM / human): [docs.typesafe.ai](https://docs.typesafe.ai/patterns/intent-routing.md)
- Smart home: Jev fan-out, a compound-request Noul → an LLM splits the request, chat falls back to an LLM: [docs.typesafe.ai](https://docs.typesafe.ai/demos/smart-home.md)
- tiershift: Jev scores 11 dimensions, and a YAML policy picks the fast, mid, or flagship tier in a median 180 ms. Reported flagship quality at 40% lower cost on 120 prompts: [iamvatsalpatel/tiershift](https://github.com/iamvatsalpatel/tiershift)
- Janus measures on your data whether Jev beats the fallback before routing. Reported 80.2% on Banking77 at half the cost. On another dataset its verdict was "DO NOT ROUTE": [FirasSX914/Janus](https://github.com/FirasSX914/Janus)
- Jevonian, a local proxy for coding agents. Code narrows the routes, then Jev picks the route and thinking level: [xinyao27/jevonian](https://github.com/xinyao27/jevonian)
- hermes-jev-skills: per-turn model choice in about 0.4 s. It never routes down on risk words, and a shadow mode logs decisions before switching: [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)
- NeuroLink SDK: one Jev request picks the model (upgrade at 0.3, downgrade at 0.6) and prunes context: [juspay/neurolink](https://github.com/juspay/neurolink)
- "LLM writes, Jev decides, code acts" guide: a Claude Code command guard, a Haiku/Sonnet/Opus router with a 0.75 floor, and a log-triage cron that escalates unknown templates to Claude Code: [aibuilderclub.com](https://www.aibuilderclub.com/blog/jev-engineering-guide)
- LangChain harness: Jev routes between models and blocks risky tool calls: [youmind.com](https://youmind.com/landing/x-viral-articles/jev-langchain-harness)
- Decisions API with the GPT-6 Luna prompt path kept warm as the fallback during preview (OpenAI Decisions): [orcarouter.ai](https://www.orcarouter.ai/blog/openai-decisions-api-gpt-6-luna). The official guide says to escalate low-confidence answers to GPT-6 Structured Outputs or function calling, using thresholds set on your labeled examples (OpenAI Decisions): [developers.openai.com](https://developers.openai.com/api/docs/guides/decisions)
- ai_decide scores prompt difficulty and the reasoning level needed, then routes to the matching model. It also judges AI answers against policy before they are released (Databricks ai_decide): [databricks.com](https://databricks.com/blog/introducing-aidecide-make-fast-decisions-your-governed-data)
- Clef routing guide: validate each response, treat deferral as a valid outcome, set thresholds on labeled tickets, and never let a failed request default to an action (Clef, Clef-flash): [rohitai.com](https://rohitai.com/blog/cloudflare-clef-decision-models-agent-routing-workers-ai)
- Decider as a gating layer before expensive generation, behind one decision schema with per-vendor adapters that fail over on confidence (pplx-decider): [explainx.ai](https://explainx.ai/blog/perplexity-pplx-decider-decisions-api-2026)

### Planner / actor and proposer / selector

- Craftax planner/actor with a 5-agent comparison: [mansicer/jev-plays](https://github.com/mansicer/jev-plays)
- Minecraft dragon kill (LLM + Jev): [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent)
- Pokémon: Jev in the overworld, escalate hard battles to Sonnet/Opus (idea): [HN](https://news.ycombinator.com/item?id=49849494)
- Pixel art (LLM sketches shapes → Jev picks style → code renders): [joce-unity/pixeljev](https://github.com/joce-unity/pixeljev)
- YOLO-World proposes boxes, Jev keeps or drops each: [huggingface.co](https://huggingface.co/spaces/iluvblender/yolo-jev-scene-filter)
- Fraud detection with Jev + Kimi K3: [x.com/nutlope](https://x.com/nutlope/status/2100614659690713543)
- Monitoring trigger → LLM report: [tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making)
- Clef on an agent's hot path, with a Workers AI LLM taking the action (Clef): [blog.cloudflare.com](https://blog.cloudflare.com/clef-decision-models/)
- Hybrid agents: the LLM makes the hard calls and the decider makes the rote ones (routing, tool choice, argument checks, guardrails). A worked example gates a weather tool on two Nouls, so the agent asks which city instead of guessing. Reported 115 ms median on an RTX 3090 (Strands Decider 2B): [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider)

### Rule writer / runner

- Self-rewriting Binance bot (Qwen rewrites the rules every 30 minutes): [learnwithmeai.com](https://www.learnwithmeai.com/p/jev-trading-bot)
- JevHarness: an LLM writes the harness and its Jev questions, then GEPA refines them on rewards. Reported Pokémon win rate rose from 25% to 75% after 5 rounds: [TianyuCodings/JevHarness](https://github.com/TianyuCodings/JevHarness)
- jev-align: humans label the rows Jev is least sure of, then GEPA rewrites the function definition: [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)
- Define in Claude, run in Jev: [HN](https://news.ycombinator.com/item?id=49719902). Prompt → rubric → own classifier: [HN](https://news.ycombinator.com/item?id=49849617)
- Intent-Router, an agent skill that compiles vague requests into typed contracts (probe, ask, route, halt) before a decision model runs (Jev, Laya): [angel291592/Intent-Router](https://github.com/angel291592/Intent-Router)
- Jevper, Jev's interface on any OpenAI-compatible model: [HN](https://news.ycombinator.com/item?id=49815066). TypeSafe [`system-one-adapter-python`](https://github.com/typesafe-ai/system-one-adapter-python)

### Tutor → student and training recipes

- WoW tutor → student distillation: [chalkychalk42/jev](https://github.com/chalkychalk42/jev)
- Nimble: one GPT-5.6 model generates 2,676 contrastive pairs and another verifies them, then a LoRA trains Qwen3.5-9B. Reported 90.12% against Jev's 93.21%. Not trained on Jev outputs (Nimble): [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble)
- Kev: a LoRA plus pointer head on Qwen3.5, trained on public, generated, and rule-based examples. Reported Kev-9B 0.837 against Jev's 0.857, and about $95 of H100 time. Jev was the reference only (Kev): [jaredpalmer/kev](https://github.com/jaredpalmer/kev)
- Tev1: a LoRA SFT on Qwen3.5-4B, 37,840 examples for about $17. Labels come from public datasets and executable rules, with no Jev or LLM answers (Tev1): [togethercomputer/tev1](https://github.com/togethercomputer/tev1/blob/main/DATA_SOURCES.md)
- Laya fine-tuning notebook on free Kaggle 2×T4: build the data, train, fit calibration temperatures (Laya): [notebook](https://github.com/NandhaKishorM/laya/blob/main/notebooks/laya_finetune_typed_decisions_2xT4_kaggle.ipynb), [model card](https://huggingface.co/convaiinnovations/laya)
- Strands Decider training data: public datasets plus labels written by Qwen3.6-27B and kept when Qwen3.5-397B agreed. No Jev data (Strands Decider 2B): [data/sources.md](https://github.com/strands-labs/strands-decider/blob/main/data/sources.md)
- decider-2b: 11,356 questions written by Qwen3.6-27B, kept only when two further answers agreed, plus replay toward its own previous version's distributions. Reported 2.2 points lost on human-labeled sets (decider-2b): [huggingface.co/mapika/decider-2b](https://huggingface.co/mapika/decider-2b)
- Clef RL fine-tuning service. It starts as a hands-on service with Cloudflare's forward-deployed engineers, with self-serve planned (Clef): [blog.cloudflare.com](https://blog.cloudflare.com/clef-decision-models/)
