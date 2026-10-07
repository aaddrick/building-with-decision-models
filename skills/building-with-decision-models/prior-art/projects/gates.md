# Projects: Gates

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/gates.md`.

**Agent tool and command gates**
- LangChain AutoModeMiddleware, a Noul blocks risky tool calls: [langchain.com](https://www.langchain.com/blog/building-a-harness-with-jev)
- hermes-jev-approvals, 8.7× faster, 4.4× fewer prompts: [anpicasso/hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals)
- jev-guard, three questions before every call (deny/ask/allow): [blacksinisterx/jev-guard](https://github.com/blacksinisterx/jev-guard)
- actionreflex: [eyenpi/actionreflex](https://github.com/eyenpi/actionreflex). pi-warden: [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden)
- Agent Chaperone, tool calls + results + injection: [HN](https://news.ycombinator.com/item?id=49789538)
- Vercel command-safety classifier (Pranit Sharma): [techcrunch.com](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)
- OpenRouter cookbooks "Gate Agent Tool Calls" and "Auto-Approve Coding Agent Permission Prompts": [openrouter.ai](https://openrouter.ai/typesafe)
- Pydantic AI harmful-request example: [pydantic.dev](https://pydantic.dev/docs/ai/models/typesafe/)
- claude-code-templates jev-auto-mode security judge: [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)
- jev-shield, MCP firewall over calls, results, and tool descriptions, with session taint; reported 94% block recall, 0 false positives, 558 ms median: [caiovicentino/jev-shield](https://github.com/caiovicentino/jev-shield)
- jevwire, escalate-only plugin (notes, overridable tripwires, stop checks); reported p50 2.8 ms prefiltered, 210 ms judged: [Brainwires/jevwire](https://github.com/Brainwires/jevwire)
- jev-auto-approve, allow-or-stay-silent hook at P ≥ 0.95 behind a hard-no list; reported 0/8 state-changing commands approved: [BasmaAbouzied0/jev-auto-approve](https://github.com/BasmaAbouzied0/jev-auto-approve)
- jev-engineering, hard rules → read-only fast path → one model call → thresholds from logs; reported 0/12 dangerous commands run vs 8/12 for Claude Code auto mode: [eugeniughelbur/jev-engineering](https://github.com/eugeniughelbur/jev-engineering)
- Reflex, five risk Nouls per state-changing call with cautious/balanced/bold presets; reported ~380 ms: [kaustav1996/reflex](https://github.com/kaustav1996/reflex)
- pi-verdict, allow/ask/deny Choice for gray-zone Pi calls, fail-closed; reported ~350 ms and 1,265 audited verdicts (Jev via TypeSafe, OpenRouter, Workers AI, or Vercel AI Gateway): [jesset/pi-verdict](https://github.com/jesset/pi-verdict)
- approval-judge-bridge, OpenAI-compatible proxy gating shell commands; only "approve" auto-runs; reported 0.18 s median (Jev, yajev, any chat LLM, or rules): [oppih/approval-judge-bridge](https://github.com/oppih/approval-judge-bridge)
- jev-style, Claude Code guard with four Nouls + a 0–4 risk Score; reported 77.6% label agreement with rules, 61.2% model alone, no deny-labelled call allowed, 443 ms (jev-style 0.8B, local Qwen3.5 fine-tune): [lawrence3699/jev-style](https://github.com/lawrence3699/jev-style)
- r2r-jev, two Nouls per call treated as evidence, admitted only with source reliability and corroboration: [Thneoly/r2r-jev](https://github.com/Thneoly/r2r-jev)
- Vercel KB, clear/caution Choice before a tool call runs; `auto()` applies no threshold: [vercel.com](https://vercel.com/kb/guide/auto-approve-tool-calls-eve-jev)
- Also: pi-heed (call vs. what the user asked) [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed), pi-jev-sentinel [harshwasan/pi-jev-sentinel](https://github.com/harshwasan/pi-jev-sentinel), jev-guard (injection + dangerous actions) [leepokai/jev-guard](https://github.com/leepokai/jev-guard), dsh-jev-interceptor (risk Choice + irreversibility Noul) [AskTheWay/dsh-jev-interceptor](https://github.com/AskTheWay/dsh-jev-interceptor)

**Trajectory gates**
- Edward, deterministic window rules plus an advisory scorer give pause/cancel/block; reported on StepShield: rules 7.4% recall, + local 4B 58.3% recall / 17.6% FPR, + Jev 59.3% / 10.2% (Jev or local 4B): [VeridicalTech/Edward](https://github.com/VeridicalTech/Edward)

**Completion and "done" gates**
- ralph-jev, the loop won't stop until the Jev judge agrees: [flaviomartil/ralph-jev](https://github.com/flaviomartil/ralph-jev)
- jev-belay (4 evidence questions): [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay), limpet: [noplan-inc/limpet](https://github.com/noplan-inc/limpet)
- Overseer rubric for CLI agents (idea): [HN](https://news.ycombinator.com/item?id=49723571)
- Canny, no "done" claim without evidence: [qkal/Canny](https://github.com/qkal/Canny). wakegate, wake / not yet / unrelated Choice before resuming a sleeping agent: [shitianfang/wakegate](https://github.com/shitianfang/wakegate)

**Code and CI gates**
- Destructive migration blocker: [opaielsheikh/typesafe-migration-guard](https://github.com/opaielsheikh/typesafe-migration-guard)
- Commit message vs. diff + secrets: [valentynkit/jev-commit](https://github.com/valentynkit/jev-commit). Test claims: [allebee/pytest-jev](https://github.com/allebee/pytest-jev)
- JevPR, LOW/NORMAL/SPECIALIST Choice per pull request, mapped to actions in YAML: [HexyeDEV/JevPR](https://github.com/HexyeDEV/JevPR). Staged-diff secrets gate: [AkashPriyadarshii/jev-git](https://github.com/AkashPriyadarshii/jev-git)
- Math-To-Manim stage approval: [`astra/jev.py`](https://github.com/HarleyCoops/Math-To-Manim/blob/main/astra/jev.py) in [HarleyCoops/Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim)

**Money and risk gates**
- Rust MT4 service behind a deterministic risk gate: [iamngoni/veyra](https://github.com/iamngoni/veyra)
- QuantDinger pre-trade gate: [gist.github.com](https://gist.github.com/drillan/6916b16e8ea31a8ec36c8f59d6483150)
- Refund branching at >85% confidence: [tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making)
- Voice banking, confidence rising with the stakes: [docs.typesafe.ai](https://docs.typesafe.ai/patterns/confidence-routing.md)
- jev-guard (crypto), 24h window features in code, hard-rule veto, four questions, asymmetric routing for irreversible withdrawals; reported p50 272 ms, zero missed freezes on 100 synthetic samples: [klauswg/jev-guard](https://github.com/klauswg/jev-guard)

**Content gates**
- LLM guardrails cookbook (strict/permissive policies): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/llm_guardrails.md)
- deer-flow guardrails: [`backend/packages/harness/deerflow/guardrails/typesafe.py`](https://github.com/bytedance/deer-flow/blob/main/backend/packages/harness/deerflow/guardrails/typesafe.py) in [bytedance/deer-flow](https://github.com/bytedance/deer-flow), LiteLLM TypeSafe guardrail hook: [`litellm/proxy/guardrails/guardrail_hooks/typesafe/typesafe.py`](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/guardrails/guardrail_hooks/typesafe/typesafe.py) in [BerriAI/litellm](https://github.com/BerriAI/litellm)
- mastra-jev-moderation, input gate at P ≥ 0.7, fails open behind a 5 s deadline and circuit breaker; reported 9/9 hostile blocked, 0/49 legit blocked, 0.39–0.44 s vs 1.97 s for GPT-OSS-120B: [CodeAlive-AI/mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation)
- tripwire, seven checks on every LLM response (PII, injection compliance, tone, category, on-topic, follows-system Score, hallucination Score); v0.1, no accuracy numbers yet: [noelzappy/tripwire](https://github.com/noelzappy/tripwire)
- Jev Moderation Bot, Discord warn → timeout ladder; pardoned false positives become "safe precedents" in the state: [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)
- openclaw-jev-leakguard, five leak Nouls on outgoing messages + channel-tier policy; reported on 113 cases: Jev 0% missed / 7% false alarms / 228 ms, Kev-0.8B 21% / 11% / 5.2 s, rules 54% / 0% (Jev, Kev-0.8B): [yousan/openclaw-jev-leakguard](https://github.com/yousan/openclaw-jev-leakguard)
- Clef support-inbox gate: toxic Noul + queue Choice + priority Score; page on-call only if toxic > 0.85 and queue confidence ≥ 0.55 (Clef, Clef-flash): [qwe.edu.pl](https://www.qwe.edu.pl/tutorial/clef-open-weight-decision-models-rl-tutorial/)
- Screenshot publish gate (exposed secrets, network details) and support router escalating below 0.5 confidence (Clef, Clef-flash): [flaviocopes.com](https://flaviocopes.com/clef.md)
- Clef review thresholds: a stricter bar for paging or blocking than for a reversible label, and shadow routing before the gate acts (Clef): [nxcode.io](https://www.nxcode.io/resources/news/cloudflare-clef-decision-models-agent-routing-2026)
- Laya CLI with ready-made `moderation` and `guard` presets (Laya): [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)
- `ai_decide()` in SQL, which checks whether an AI support answer follows the refund policy and scores how completely it answers the request (Databricks ai_decide, beta): [databricks.com](https://databricks.com/blog/introducing-aidecide-make-fast-decisions-your-governed-data)

**Research and vendor guidance**
- "Just Ask Jev", zero-shot detection of jailbreak, injection, deception, reward hacking and more across 44 benchmarks; reported median AUROC 0.886 at 63× lower cost than LLM judges: [arxiv.org](https://arxiv.org/abs/2609.29429)
- Strands Decider lists grounding checks, safety and policy classification, and tool-argument checks before execution as target uses; reported ECE 0.064, 115 ms median on an RTX 3090. No community gate found yet (Strands Decider 2B): [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider)
- Perplexity decision panel, with grounding (RAGTruth) as the gate-relevant task (pplx-decider-v1-27b): [explainx.ai](https://explainx.ai/blog/perplexity-pplx-decider-decisions-api-2026)
- Kev README, which reports what share of decisions can be automated at a 5% error budget, per checkpoint (Kev): [jaredpalmer/kev](https://github.com/jaredpalmer/kev)
