# Choosing and Switching Models

**Use when** you pick which decision model or provider to use, compare or benchmark models, move code from one provider or version to another, run behind a gateway or adapter so the backend can change, or re-fit thresholds after any of these.

This is the procedure behind "Pick the provider" and "Changing models" in `SKILL.md`. Each model's own limits and calibration are in `models/<name>.md` (index: `models/INDEX.md`); each backend's wire contract is in `providers/<name>.md`. Numbers stay here only when the comparison is the lesson.

## The shape

```
labeled cases from real traffic (include the hard ones near each threshold)
  → the same requests to the old and the new model (errors and 4xx count as wrong)
  → per question: accuracy, Brier or ECE, automation rate at a fixed error budget
  → re-fit every threshold on each model's own answers
  → shadow the new model on live traffic, log both model IDs
  → switch the constant (provider, model ID, thresholds) in one module
```

```python
from typesafe_sdk import Choice, Noul, TypeSafeAPIError, TypeSafeClient

# Only servers that speak Jev's /v1/systemone body and field names work here unchanged.
# Databricks ai_decide, OpenAI Decisions, Perplexity, and Clef REST need an adapter
# that maps their path, envelope, and field names to this shape first.
BACKENDS = {
    "jev": TypeSafeClient(model="jev-1.13.0"),               # pinned; reads TYPESAFE_API_KEY
    "nimble": TypeSafeClient(base_url="http://localhost:11434", api_key="ollama",
                             model="nimble", timeout=120),   # Ollama; 120 s covers a cold load
}
QUESTIONS = {
    "refund": Noul(instructions="Does `ticket.text` ask for money back?"),
    "team": Choice(instructions="Which team should handle `ticket.text`?",
                   criteria={"billing": None, "technical": None, "sales": None, "other": None}),
}
TARGET_PRECISION = 0.95   # the error budget you can live with when the code acts alone

def answers(client, cases):
    """cases: [{"state": {...}, "labels": {"refund": True, "team": "billing"}}] from real traffic."""
    out = []
    for c in cases:
        try:
            out.append((c["labels"], client.system_one(state=c["state"], questions=QUESTIONS)))
        except TypeSafeAPIError:
            out.append((c["labels"], None))                  # a rejection is a wrong answer
    return out

def score(rows, qid):
    """(bar value, correct?, Brier) per case. Noul uses max(p, 1-p); Choice uses confidence."""
    res = []
    for labels, r in rows:
        y = labels[qid]
        if r is None:
            res.append((0.0, False, 1.0))
        elif qid in r.nouls:
            p = r.nouls[qid].noul
            res.append((max(p, 1 - p), (p >= 0.5) == y, (p - y) ** 2))
        else:
            a = r.choices[qid]
            brier = sum((p - (opt == y)) ** 2 for opt, p in a.probabilities.items())
            res.append((a.confidence, a.choice == y, brier))
    return res

def fit_bar(res, target):
    """Lowest bar whose accepted answers meet the target precision, and the share automated."""
    for bar in sorted({b for b, _, _ in res}):
        kept = [ok for b, ok, _ in res if b >= bar]
        if kept and sum(kept) / len(kept) >= target:
            return bar, len(kept) / len(res)
    return None, 0.0

def compare(cases):
    for name, client in BACKENDS.items():
        rows = answers(client, cases)
        ids = {r.model for _, r in rows if r}                # log what actually answered
        for qid in QUESTIONS:
            res = score(rows, qid)
            acc = sum(ok for _, ok, _ in res) / len(res)
            brier = sum(b for _, _, b in res) / len(res)
            bar, auto = fit_bar(res, TARGET_PRECISION)
            print(f"{name} {ids} {qid}: acc {acc:.3f} brier {brier:.3f} bar {bar} automated {auto:.0%}")
```

Thresholds fitted here belong to that model ID on that server. Store them next to the model ID in the constants module (rule 11 in `SKILL.md`), never as one shared number.

## Variants

- **Conformance first.** Before you measure accuracy, run a conformance suite against the new server. Check option and level caps, question count, context length, and the `confidence` definition. A request it rejects or truncates silently fails before accuracy matters.
- **Shadow routing.** Send each live request to both models. Act on the old one, log both, and compare once enough labeled outcomes come back. Switch only after the new model has run on live traffic.
- **Adapter per vendor.** One file per provider maps its path, envelope, and field names to one internal answer type. The rest of the code never sees the vendor shape.
- **Gateway with fallback.** One endpoint routes to several backends and fails over on errors or low confidence. Each backend still needs its own thresholds, and a fallback answer must be judged on the fallback model's bar.
- **Automation rate at an error budget.** Compare models by the share of decisions you can automate at, say, 5% errors, not by accuracy alone. It folds accuracy and calibration into the number that decides cost.
- **Per-question-type calibration check.** Plot confidence against accuracy separately for Noul, Choice, and Score, and for small and large option lists. Pick the model per question type if they differ.
- **Drift monitor after an alias moves.** Watch the reported model ID, the answer distribution, and how many answers crowd each threshold. Alert on a change even before labels arrive.
- **Distill to a local model.** Log a hosted model's answers per decision site, train or fine-tune a small local model, shadow it, then serve locally with the hosted model as fallback.

## Field lessons

- **Thresholds do not transfer**, even on one model. On Jev, Janus saw the best escalation threshold move from 0.67 to 0.37 between two datasets. Across models it is worse: clef-rag ships Jev-tuned thresholds and says to re-tune them for Clef, and Kev's scores bunch near 0.9, so a small shift flips many verdicts (`models/clef.md`, `models/kev.md`).
- **`confidence` means different things on different servers.** jevcompat found top probability on some, the top-two margin on another, and one minus normalized entropy on a third. Ollama uses the entropy form, so its values read much lower. Clef, CLM's Score, and Pydantic AI each use yet another definition (`providers/ollama.md`, `models/clef.md`, `models/clm.md`, `providers/pydantic-ai.md`). Never reuse a `confidence` bar across servers.
- **Same weights, different serving stack, different calibration.** Nimble calibrates far worse on raw Ollama than behind a fitted temperature, Kev's served probabilities drift from its fp32 eval path, and Tev1 0.8B changed accuracy between fp32 and fp16 (`models/nimble.md`, `models/kev.md`, `models/others.md`). Measure on the stack you will serve.
- **Calibration differs by question type and option count.** **Jev:** reported ECE Noul 0.012, Choice 0.086, Score 0.254. Laya and Kev-9B lose calibration as option lists grow, and Nimble is far weaker on Score (`models/laya.md`, `models/kev.md`, `models/nimble.md`). Check each question type and list size on its own.
- **Public benchmarks disagree, and every vendor ranks itself first somewhere.** Jev's Banking77 score ranges from 76.3% to 87.0% across four evals. Clef's launch post (vendor-reported) has Banking77 at 94.2 vs Jev 79.7. Perplexity's panel (vendor-reported) has its model ahead, with no prompts or item IDs published. Vendor panels report no calibration.
- **Familiar data overstates generalization.** bekko-400m scored 76 on S1MB and 54 on novel tasks. Kev reports familiar and new sources separately. Ask which one a number is.
- **Rerun hosted models before trusting a number.** GLiDE scored 82.9% on Oct 2 and 76.4% on an Oct 3 rerun of the same benchmark. Aliases move. Ollama echoes the request name, not a version (`providers/ollama.md`), and Databricks `ai_decide` does not name its model and says it may change (`models/others.md`). Log the version from `metadata`.
- **Limits differ more than the request shape.** jevcompat found 4 of 8 servers capped Choice at 26–128 options instead of 255, and Pydantic AI's Ollama profile allows 26. Context runs from 512 to 262,144 tokens, and some servers truncate a long state silently. Strands Decider returned 422 on null `criteria` that others accept. Run a conformance check (Variants), then read the new model's Limits in `models/<name>.md` and its provider file.
- **Field names and envelopes differ.** Clef REST wraps answers in `result`. Databricks names the Noul answer `probability` and returns `error_message` instead of raising. OpenAI Decisions uses `POST /v1/decisions` with `input` and `predicate`. Perplexity uses `/v1/decisions`, requires `model`, and rejects unknown fields with 400. Vercel's native API uses `boolean` and `inputTokens`. The details are in each `providers/<name>.md`. Keep each one in its adapter.
- **A language-model fallback is not a decision model.** On Vercel decision fallbacks, a language model answering a Choice returns `confidence: 0` and `probabilities: {}`, which mean "unavailable", not "zero". Branch on that before a threshold reads it (`providers/gateways.md`).
- **Close accuracy can hide a calibration gap.** Opper reported Jev 96.5% vs Kev 4B 95.7%, but Kev's calibration drifted more on Stack Exchange and GitHub tasks. At a 5% error budget, Kev-4B/9B/27B were reported to automate 0.52–0.69 of new-source decisions against 0.70 for Jev. (Details: `models/kev.md`.)
- **The best model depends on the question.** pplx-decider (vendor panel) leads on RAGTruth grounding, 88.8% vs Jev 77.3%. Jev leads on TruthfulQA, 92.0% vs 85.4%. Kev-9B leads on support routing (0.952 vs 0.897) but trails on MMLU-Pro (0.515 vs 0.840). Choosing a model per question in the constants module is fine. (Details: `models/pplx-decider.md`, `models/kev.md`.)
- **Count errors, rejections, and degenerate answers as wrong.** Several small models gave the same "done" or "wait" answer almost every time in AIM's tests. A model that returns 400 on your request has failed that case.
- **Cost and latency differ on the same request.** Jev adds about 257 hidden input tokens per request (Opper). Ollama counts the shared state again for each question. Compare `usage.input_tokens` and latency on your real requests, not the price page.

## Benchmarks and prior art

The benchmarks that exist (Jev Decision Index, BenchLM, JevBench, AIM, S1MB, sysone-bench, amplifying.ai) and their numbers are the first group in `prior-art/projects/choosing-and-switching-models.md`. Three that show the method:

- hard-decisions, 3,600 ProofWriter problems by proof depth, all requests kept verbatim: Jev 83.8%, GLiDE 82.9% (76.4% on rerun), GPT-6 Luna 64.1%, Kev-9B 58.6%, Laya 42.4% (GPT-6 Luna, GLiDE, Kev, Laya): [hard-decisions.anth.us](https://hard-decisions.anth.us/)
- Anthus OpenAI Decisions preview test: at ≥99% stated confidence Luna was right 68% of the time vs 98.9% for Jev; 78% of Luna's errors were stated at ≥95%, and AUROC fell to 0.51 at five chained steps (OpenAI Decisions API): [anth.us](https://anth.us/blog/openai-decisions-api-preview/)
- Kev README: familiar vs novel sources, automation share at a 5% error budget per checkpoint, fitted temperatures. A temperature fit cuts Kev-9B confident errors from 8.2% to 2.4% (Jev 3.7%) (Kev): [jaredpalmer/kev](https://github.com/jaredpalmer/kev)

More projects (43 entries), grouped by sub-type (Benchmarks and indexes, Vendor-reported launch numbers, Head-to-head comparisons, Conformance and compatibility, Gateways, adapters, and routers that switch backends, Migration and porting write-ups): `prior-art/projects/choosing-and-switching-models.md`.
