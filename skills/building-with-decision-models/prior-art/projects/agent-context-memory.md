# Projects: Agent Context, Memory, and Effort

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/agent-context-memory.md`.

**Compaction and pruning**
- fast-jev-compaction: [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction). jev-pruner: [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner). winnow: [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow). save-token-jev: [IAmUnbounded/save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean). fast-jev-compaction was announced on X as "Instant compaction for Claude" (@tamarajtran). Reported: 1M tokens compacted for about $0.04 ([hermes-ai.net](https://hermes-ai.net/jev/case/2100913118528393596/), [alphasignal.ai](https://alphasignal.ai/news/tamara-tran-s-fast-jev-compaction-stops-claude-code-from-forgetting-critical))
- opencode-jev-compactor, which adds guidance to OpenCode's native compaction prompt and never writes the summary itself. It has a three-tier tool policy and an observe mode: [christian-taillon/opencode-jev-compactor](https://github.com/christian-taillon/opencode-jev-compactor)
- opencode-jev-compaction, which asks two Nouls per tool call (does the call matter, is the full output needed) and requires at least 25% shrinkage: [radqnico/opencode-jev-compaction](https://github.com/radqnico/opencode-jev-compaction)
- pi-fast-jev-compaction, a port to Pi that triggers at 60% context use and stores decisions as append-only session entries: [joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction)
- jev-compaction, which scores segments and never writes. Dropped output becomes a pointer that can be expanded back. Reported on SWE-bench Verified: 25% of tool output removed at admission with no loss in resolution, about 10% lower cost: [Waxmell114514/jev-compaction](https://github.com/Waxmell114514/jev-compaction)
- yoshi, a pruning proxy for Claude Code and Codex. It reported a 34% input cut on one trial, about 0% on another, a large slowdown, and judge failures, and its authors claim no validated saving: [compozy/yoshi](https://github.com/compozy/yoshi)
- LiteLLM TypeSafe guardrail that prunes tool results: `guardrail_hooks/typesafe/typesafe.py` in [BerriAI/litellm](https://github.com/BerriAI/litellm/blob/main/litellm/proxy/guardrails/guardrail_hooks/typesafe/typesafe.py)
- Context management "do all these tokens need to reach the agent?" (TypeSafe staffer idea): [HN](https://news.ycombinator.com/item?id=49719368)

**Judgment-kernel agents**
- mu, a coding agent with 38 decision points, including tool admission, forget, compact, memory capture/merge/applied, and completion. Reported: 40.2% context cut with zero required lines lost, about 0.3 s per question: [qybaihe/mu](https://github.com/qybaihe/mu)
- pi-quiet-ask, a decision layer for Pi with rule packs for clarifying, completion claims, and repeated failures. It runs in shadow mode by default and fails open: [HyunjunJeon/pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)

**Memory**
- Jevmem, save/skip into JEVMEM.md after each message: [HN](https://news.ycombinator.com/item?id=49846413)
- Proactive memory formation and retrieval (idea): [HN](https://news.ycombinator.com/item?id=49721409)
- invalidate, memory leases ended by new evidence: [chopratejas/invalidate](https://github.com/chopratejas/invalidate)
- Jev-Mem, a paper using Jev as the memory control plane (typing, relations, routing), 0.777 LoCoMo: [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem)
- hippo-memory, a local memory store for coding agents with an optional reranker. Reported: R@1 rose from 0.41 to 0.62, about $0.0004 per recall: [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory)

**Effort, model, and skill control**
- Vechen reasoning-effort governor, about 50% cost cut: [linas.substack.com](https://linas.substack.com/p/how-to-use-jev-ai)
- Jev-pilot (effort/model/skill per prompt): [HN](https://news.ycombinator.com/item?id=49837537). jev-effort: [HN](https://news.ycombinator.com/item?id=49824915). jev-effort benchmarks (55% at max, about 1.1% at high, adds about 601 ms): [everydev.ai](https://www.everydev.ai/tools/jev-effort)
- Astra-Ares, Codex effort control with a lease: the model also picks how many generations to hold its choice: [miuuyy/Astra-Ares](https://github.com/miuuyy/Astra-Ares)
- jev-opus, per-step effort for Opus. It raises effort on test failures and stores effort as replayed per-message statements: [WXK-AI/jev-opus](https://github.com/WXK-AI/jev-opus)
- spending-effort-with-jev, a Choice over low/medium/high/max/unclear that holds for one turn. Reported: 90% level accuracy: [Yaxin9Luo/spending-effort-with-jev](https://github.com/Yaxin9Luo/spending-effort-with-jev)
- jcm-router, a model and effort proxy whose cache failure is documented, plus the cost guard that fixed it: [adarshmishra07/jcm-router](https://github.com/adarshmishra07/jcm-router)
- jev-router (dirien), which never downgrades within a session. Bars: 85% for fast, 60% for balanced, 30% for frontier. Reported: 51% saved: [pulumi.com](https://www.pulumi.com/blog/route-every-claude-code-message-to-the-right-model-with-jev/), [dirien/jev-router](https://github.com/dirien/jev-router)
- jev-router (daviddl9), worker tier per step for OMP/Pi, with planning kept on a strong model: [daviddl9/jev-router](https://github.com/daviddl9/jev-router)
- Switchboard, which pins model and effort as separate axes for the whole conversation. Median 0.55 s (Jev; Laya as an experimental self-hosted option): [ruban-24/switchboard](https://github.com/ruban-24/switchboard)
- agent-router, a quota-aware choice of agent CLI plus model and effort: [nidhi-singh02/agent-router](https://github.com/nidhi-singh02/agent-router)
- Skill suggestion cookbook (progressive disclosure over 182 skills): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/skill_suggestion.md)
- skillranker, a Rust CLI and hooks with need and fit thresholds and a "none" option every candidate must beat: [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker)
- jev-rules, which delivers only the standing rules that apply, once per session. Reported: about 24% of the tokens of loading everything: [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules)
- jev-skillful, a per-prompt capability router. Reported holdout Recall@K is 0.60, and the outcome benchmark has not been run: [bestagentkits/jev-skillful](https://github.com/bestagentkits/jev-skillful)
- typesafe-skill-router, two-stage screening over 292 skills. Reported: wrong loads fell from 16.8% to 7.3%: [DECRUX9812/typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router)
- jev-agent-skill-router, which returns route / no_skill / review. Reported: 94.4% on 72 synthetic cases, with 25% sent to review: [GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)
- JevRouter, where models, subagents, skills, and tools form one candidate set. The model owns the probabilities and the router owns the permissions: [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter)
- codex-jev-router, evidence excerpt selection for Codex. The optional Laya reranker cost 8.8% more than the deterministic path (Laya): [suenot/codex-jev-router](https://github.com/suenot/codex-jev-router)
- Routers: see `prior-art/projects/select-from-candidates.md`

**Stop, continue, ask, wake**
- jev-belay, a Stop hook that blocks an unverified "done" with one four-question call over transcript evidence. Reported: AUROC 0.976, 346 ms: [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay)
- limpet, a Stop hook judged against plain-language rules, about 0.7 s per stop: [noplan-inc/limpet](https://github.com/noplan-inc/limpet)
- pi-warden, steering guardrails that catch a third retry of the same failing fix and send unverified "done" claims back: [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden)
- DeepSearcher stopping policy, a Noul that decides whether to stop or keep searching. Reported: same Recall@5 as an LLM policy at about 1/7 the cost: [zilliztech/deep-searcher](https://github.com/zilliztech/deep-searcher/blob/master/evaluation/jev_stopping/README.md)
- wakegate, a Choice (wake / not yet / unrelated) before a sleeping agent resumes. 21/21 on a smoke test: [shitianfang/wakegate](https://github.com/shitianfang/wakegate)
- Jev for Chrome, where independent "goal reached" and "stuck" Nouls veto a premature DONE or BLOCKED: [chy4pro/jev-for-chrome](https://github.com/chy4pro/jev-for-chrome)
- Strands tool-call intervention example, a `before_tool_call` hook with Nouls for grounded arguments and a premature call, returning Guide so the agent asks the user (Strands Decider 2B, local): [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider/tree/main/examples/strands), [strandsagents.com](https://strandsagents.com/blog/introducing-strands-decider/)
- pi-subagent-jev, which gates subagent dispatch on configurable rules and fails open: [G0-0000/pi-subagent-jev](https://github.com/G0-0000/pi-subagent-jev)

**Local and framework plumbing**
- ai-stack, a local decision service reached by Claude Code over MCP. About 0.7 s per call, 2050-token context (Tev1 4B via Ollama): [IgorChicherin/ai-stack](https://github.com/IgorChicherin/ai-stack)
- pydantic-ai `SystemOneModel`, which runs a deciding agent with `output_type` as the questions (CLM-8B (Stanford/Nvidia contrastive), Laya): [pydantic.dev](https://pydantic.dev/docs/ai/api/models/system_one/)
- Self-hosting guide that caches candidate action embeddings. "Cached vectors are not cached permissions or decisions." (CLM-8B (Stanford/Nvidia contrastive)): [wavect.io](https://wavect.io/blog/clm-8b-self-hosting-action-cache-verifier.md)

**Harness frameworks**
- Sokit, System One Harness, jevlike, DSPy fork: [HN](https://news.ycombinator.com/item?id=49744527), [HN](https://news.ycombinator.com/item?id=49778358), [HN](https://news.ycombinator.com/item?id=49719285)
- LangChain harness post (middleware for routing and auto mode): [langchain.com](https://www.langchain.com/blog/building-a-harness-with-jev)
- Jevify skill, converts an LLM "return JSON" call to Jev: [HN](https://news.ycombinator.com/item?id=49812519)
- Reverse Jev, the agent ends its turn with a Choice so the human replies with one button: [HN](https://news.ycombinator.com/item?id=49807602)
