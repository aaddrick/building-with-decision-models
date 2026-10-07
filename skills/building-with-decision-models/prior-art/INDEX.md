# Prior Art Index

Community projects built on decision models, grouped by **implementation shape**. Snapshot 2026-10-06, three weeks after Jev launched and one week after the first rival models. Most are weekend projects. Treat them as design references, not proven production systems. Numbers are author-reported unless a line says otherwise.

**Which model?** An entry with no model in parentheses ran on TypeSafe Jev. Every other entry names its model: `(Clef)`, `(Clef-flash)`, `(Nimble via Ollama)`, `(Kev)`, `(Laya)`, `(pplx-decider)`, `(ai_decide)`, `(CLM-8B)`, and so on. A result on one model is evidence about that model only. Before you copy a threshold or a "this works", check which model produced it (see "Changing models" in `SKILL.md`). Shape files keep lessons that hold for any model, plus Jev notes. On another model, read `models/<name>.md` too (index: `models/INDEX.md`): it holds that model's limits, calibration, failures, and per-shape notes.

## How to use

1. Find your intent in the table. Open only that shape file.
2. Or grep: `grep -ril "<keyword>" ~/.claude/skills/building-with-decision-models/prior-art/`. Try a domain word (trading, drone, email, SQL, dubbing), a mechanism word (beam, cascade, lease, tick), or a model name (Clef, Nimble, Laya).
3. Each shape file holds the core: the shape → a code sketch → variants → field lessons → two or three flagship projects. The full project list for each shape, grouped by sub-type, is in `prior-art/projects/<shape>.md` (for example `prior-art/projects/gates.md`). Open it when you need more examples than the flagships. The grep in step 2 is recursive, so it searches those lists too. Fetch a linked repo only when you need its details.
4. Check the bad-fit headlines below before you design. `prior-art/bad-fits.md` has the evidence. Model-specific failures are in `models/`.

Every file path in this skill is relative to the skill root, wherever it appears.

The code sketches use `typesafe-sdk`. Other providers that accept the same body work through its `base_url`, or through plain HTTP. Each provider file in `providers/` says which.

## Find the shape

| I want to… | Shape file | Core move |
|---|---|---|
| Act every tick in a game, sim, robot, market, or UI | `prior-art/control-loops.md` | State → Choice over legal actions. Code executes. |
| Pick the right thing from a list (UI element, tool, function args, extracted value) | `prior-art/select-from-candidates.md` | Candidates become Choice keys. The model never generates. |
| Allow, block, or require approval before something happens | `prior-art/gates.md` | Risk Nouls + policy in code + escalation |
| Filter or label every item in a big or endless stream (posts, logs, rows, emails) | `prior-art/stream-filters.md` | One cheap request per item. Threshold in code. |
| Sort, rerank, dedupe, match, or walk a taxonomy, including **more than about 255 options** | `prior-art/ranking-and-matching.md` | Noul per pair, or Choice per level + beam search |
| Grade outputs, traces, or content against a rubric | `prior-art/judges-and-evals.md` | Atomic rubric questions, combined in code |
| Choose, compare, benchmark, or switch decision models | `choosing-and-switching-models.md` | Same labeled requests to both. Re-fit thresholds, shadow, switch. |
| Decide on partial input as it arrives (speech, typing, video, webcam) | `prior-art/incremental-realtime.md` | Re-ask per increment. Commit at a confidence bar. |
| Manage an agent's context, memory, effort, or stopping; decide whether it may stop, continue, ask, or wake | `prior-art/agent-context-memory.md` | Keep/drop/lease/stop Nouls at the hook, not summaries |
| Pair a decision model with an LLM (planner/actor, cascade, distillation, LLM tier routing) | `prior-art/llm-pairing.md` | Decision model takes the frequent part, the LLM the rare, hard part |
| Use answers as data (ML features, research measurement, analytics columns) | `prior-art/research-and-features.md` | Probabilities become columns |
| Put a decision model inside infrastructure (SQL, vector DB, CI, middleware), or swap/proxy the endpoint itself | `prior-art/embedding-in-infrastructure.md` | Wrap one call as a native primitive of the host |
| Decide on an image, screenshot, video frame, or scan | `prior-art/images-and-multimodal.md` | Perception in code first. Few small images, off the hot path. |
| Detect a pattern across a **window or burst of events** (raid, fraud, alert storm), then act | `prior-art/gates.md` (+ `prior-art/stream-filters.md`) | Code computes window stats. The model judges. Gate policy acts. |

**Many designs combine two shapes.** Open the one that owns the final decision first (usually a gate or a control loop), then the one that feeds it.

## Known bad fits (headlines)

Any decision model:

- Chess and puzzle-like search: keep search in code.
- Coding, chat, summarization, complex reasoning.
- Final judge on math, code, or logic: triage and risk scoring only.
- Code review as the only reviewer.
- Expert-domain groundedness.
- Exact counting: count in code.
- Recovering known probability distributions.
- Empathy-style constructs as research variables.
- Many labels when you already have training data: try an embedding + logistic regression baseline first; it beat every decision model on one benchmark.
- Sorting by probability on hard relevance tasks.
- A rerank in place of good retrieval.
- "None of these" inside a ranking Choice: use a separate `fits` Noul.
- Planning a tool-call sequence in one request.
- Detecting failures across a whole agent run with small judges.
- Element-table browser agents on shadow DOM, iframes, canvas, or uploads.
- Semantic HTTP routing for authentication or authorization.
- Model routing without measuring first.
- Probabilities wired straight to irreversible trades.
- Continuous flight control from a hosted model.
- Perception: do it with CV first.
- General context-pruning proxies and working-memory pruning.
- Out-of-box calibration claims: fit Platt scaling on your own labels.
- Speed marketing: batched LLM calls can match it offline.
- Record dedupe and a personal prompt router.
- Sound-alike profanity in usernames.

Model-specific bad fits (Laya, Nimble, Kev, CLM, Luna, Clef, …): "Where it fails" in each model's file, `models/INDEX.md`.

Evidence and links for every item: `prior-art/bad-fits.md`. Bigger indexes: `prior-art/more-indexes.md`.
