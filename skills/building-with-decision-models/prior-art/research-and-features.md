# Shape: Answers as Data

**Use when** the output is not an action but a measurement: features for a classical model, labels for a dataset, variables for a study, or a benchmark of the decision model itself.

## The shape

```
rows → one request per row with N questions → a numeric table
     Noul  → 1 column (P(yes))
     Score → 2 columns (mean level, spread) or one column per level probability
     Choice→ one column per option probability
→ train (CatBoost/logistic), correlate with outcomes, or compare with human data
```

```python
def to_features(r) -> dict[str, float]:
    row = {}
    for qid, a in r.nouls.items():
        row[qid] = a.noul
    for qid, a in r.scores.items():
        mean = a.score
        row[f"{qid}_mean"] = mean
        row[f"{qid}_sd"] = sum(p * (lvl - mean) ** 2 for lvl, p in a.probabilities.items()) ** 0.5
    for qid, a in r.choices.items():
        row.update({f"{qid}={opt}": p for opt, p in a.probabilities.items()})
    return row
```

## Variants

- **Dimensions + fitted weights.** Ask 10–15 narrow questions per row, cache the answers, fit a logistic regression. Stack with a cheap n-gram baseline.
- **Confidence-routed annotation.** The decision model codes everything. Items below a confidence bar go to an LLM or a human.
- **Label-free invariant checks.** Before trusting a measurement, check P(q) ≈ 1 − P(not q), stability under paraphrase, and mirrored output on a reversed scale.
- **Probabilistic record linkage.** Block candidate pairs in code, ask a Noul per pair with a plain-English match rule, resolve by threshold.

## Field lessons

- Many narrow features + a trained model beat asking the model for the target directly (RMSE 1.77 vs. 2.15). Decompose only where the direct call is weak: one study gained 7–51 points there, but got 25× more false positives on a security guardrail.
- With labels, a trained classifier on the same features still wins (Banking77 93.2% vs. 80.1% for Jev). Use the decision model as a feature extractor or a zero-shot start.
- An LLM can propose the candidate questions. Keep the ones that improve held-out error (an autoresearch loop).
- Research designs that use the calibrated probabilities themselves are a novel angle. Example: do option probabilities match how human test-takers distribute their answers?
- Calibration varies by construct, not just by model. Check it against labels for each variable before you treat a probability as a frequency. Recalibrate on your own labels (crash coding: 3.3× lower error after recalibration).
- **Jev:** calibration error differs by question type: Noul 0.012, Choice 0.086, Score 0.254 in one pre-registered test. Treat Score means as the least trustworthy column.
- **Jev:** mid-range probabilities (0.3–0.7) carry little signal, and full Choice distributions run too peaky. Do not read a distribution as frequencies without checking.
- Option names and positions bias answers. Renaming 0/1 to no/yes flipped 70 answers per 100. Moving the correct option from first to last dropped Jev from 88% to 57%. Randomize option order and report the label wording.
- One state per request when rows must be comparable. Packing 40 rows into one Jev request raised ranking inversion from 0.036 to 0.171.
- **Jev:** probabilities have two decimals, so ties are common (53 of 360 rows at 0.99). Add a tie-breaker before `ORDER BY … LIMIT`.
- **Open weights:** a temperature fitted on few options breaks on many. Refit for your label space.
- For studies, pin the model ID and report it, plus dtype and hardware for open weights (one 0.8B model moved 0.0105 accuracy between fp32 and fp16). Measure run-to-run stability (std ≈ 0.01 reported) before you trust small effects.
- A vendor function that does not name its model cannot anchor a trend line. Log the version it returns, or use open weights.
- Not on Jev? Model-specific measurement notes (calibration by option count, unnamed models, confidence on hard items): `models/kev.md`, `models/luna.md`, `models/nimble.md`, `models/others.md` (Tev1, `ai_decide`). Index: `models/INDEX.md`.

## Prior art

- One judge call vs. 12–14 dimension scores + logistic regression; bookkeeping 40.0% → 91.1%, guardrail false positives 1.5% → 37.2%, 20,139 rows for $1.43: [agentjournal.dev](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/)
- Text annotation for computational social science, pre-registered, 18 tasks vs. 19 LLMs; Jev trails the best LLM by a median 11.6 macro-F1 at 44× lower cost, and routing low-confidence items to an LLM matches the LLM at 25–50% of the cost (Jev, Laya, Kev, SemIf, Nimble, decider): [arXiv:2609.24574](https://arxiv.org/abs/2609.24574), [hazemibrahim97/decision-models-css](https://github.com/hazemibrahim97/decision-models-css)
- jev-behavior-study, 11,621 controlled requests; 88% when the correct option comes first vs. 57% when last: [RINNECODER/jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study)

More projects (37 entries), grouped by sub-type (Features and prediction, Research instruments, Analytics columns, Data curation, Benchmarks of Jev, Benchmarks across decision models): `prior-art/projects/research-and-features.md`.
