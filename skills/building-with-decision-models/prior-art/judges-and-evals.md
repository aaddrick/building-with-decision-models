# Shape: Judges and Evals

**Use when** you need to grade model outputs, agent traces, content, notes, or submissions against a rubric, online or offline. The same shape fits evaluating the decision model itself.

## The shape

```
artifact (+ reference, policy) → atomic rubric questions (one flaw or dimension each)
                               → code: max over failure flags, weighted sum over quality dimensions
                               → gold-label test set that measures agreement; diff what flips when questions change
```

```python
from typesafe_sdk import Choice, Noul, Score

TRACE_RUBRIC = {
    "needs_review": Noul(instructions="Should a human review the agent run in `trace`?"),
    "user_disagrees": Noul(instructions="Does the user reject or correct the assistant in `trace.messages`?"),
    "failure_mode": Choice(
        instructions="What is the main way the agent in `trace` fell short?",
        criteria={"wrong_tool": None, "hallucinated_fact": None, "ignored_instruction": None,
                  "gave_up": None, "none": "The run achieved the user's goal"},
    ),
    "severity": Score(
        instructions="If the run in `trace` went wrong, how much harm did it cause the user?",
        criteria=["No harm", "Wasted time, recoverable", "Wrong action taken or data lost"],
    ),
}
```

## Variants

- **Tuned-threshold judge**: tune the Noul cutoff on a labelled validation split, then confirm it on a held-out split. Never ship the 0.5 default.
- **Cascade, if errors are uncorrelated**: send low-confidence verdicts to an LLM judge. First measure how often the LLM repeats the model's confident errors on your gold set. If it repeats most of them, the cascade saves cost but does not add accuracy.
- **Shuffle-and-average Choice**: in offline evals, ask each Choice in several option orders and average the probabilities to cancel order bias.
- **Injection red team**: add natural-looking or adversarial text to the artifact and measure the verdict flip rate before you ship the judge.

## Field lessons

- Per-field or per-flaw judges beat one holistic judge ("is this good?" gave 0.56 where per-field checks gave 0.95 and 0.85).
- Treat the questions like code: YAML or constants, versioned, with a gold set and an agreement metric. Before shipping a wording change, diff which rows flip.
- Tune the threshold before you compare judges. Reported on RAGTruth: at 0.5, Jev trailed Opus 5 76% to 83% because 34% of grounded answers scored above 0.5. At 0.80, Jev matched Opus 5 at 87% ([Arize](https://arize.com/blog/jev-as-a-judge/)).
- Decision-model and LLM judges are often wrong on the same items. Reported: about 96% of LLM verdicts repeated Jev's confident errors, and a cascade gained at most 2.7 points ([arXiv 2609.29769](https://arxiv.org/abs/2609.29769)). Escalation cuts cost more than it raises accuracy.
- The judge reads untrusted text, so that text can steer the verdict. Reported: injected instructions flipped 12–22% of Jev verdicts ([Braintrust](https://www.braintrust.dev/evals/jev-vs-gpt-eval-judges)), and short natural-looking additions flipped 61–73% of correct decisions across four decision models ([arXiv 2609.30243](https://arxiv.org/abs/2609.30243)).
- Groundedness on short, atomic claims is the strong case. Reported for Jev: 92.3% on LFQA/RAGTruth but 53.3% on ExpertQA. Accuracy fell from 87% to 73.7% as claims got longer ([Braintrust](https://www.braintrust.dev/evals/jev-vs-gpt-eval-judges)).
- Calibrate per task and per question form. **Jev:** reported ECE 0.074 on the Decision Index. In one study, the middle of a 4-class Score was stated 0.75 but observed 0.61, and rewording the same question moved ECE by 0.071 ([runtimewire](https://runtimewire.com/article/jared-palmer-kev-qwen35-decision-models)).
- Stated confidence can fall apart on multi-step logic, even on a frontier vendor's model (Luna, `models/luna.md`). Do not let a confidence threshold route reasoning-heavy grading.
- Calibrated questions do not make a calibrated pipeline. Thresholds, weights, and branches break it. Validate the combined rubric score against outcomes ([Amplitude](https://amplitude.com/blog/jev-analysis)).
- Run-to-run stability is the strongest judge property. Reported: Jev's score variance on identical traces was 92–913× lower than LLM judges ([LangChain](https://langchain.com/blog/jev-agent-evals-langsmith)).
- Code review as the final verdict is weak. Use the model to triage and prioritize (P0/P1/P2).
- Offline evals: pin the model version, because aliases such as `jev-latest` move.
- Not on Jev? Model-specific judge notes (confidence on multi-step logic, grounding, degenerate "done" answers): `models/clm.md`, `models/luna.md`, `models/pplx-decider.md`, `models/others.md` (GLiNER2.5-Decide). Index: `models/INDEX.md`.

## Prior art

Comparing or benchmarking decision models against each other (indexes, head-to-heads, cross-model calibration, thresholds across models): see `choosing-and-switching-models.md`.

- Groundedness 80.2% across 11 datasets, best of 5 judges. JudgeBench answer correctness 78.1% vs Luna's 88.6%: [braintrust.dev](https://www.braintrust.dev/evals/jev-vs-gpt-eval-judges)
- RAGTruth and SummEval vs Opus 5. With a tuned threshold, hallucination accuracy matched at 87% for about 300× less cost. SummEval rank correlation 0.74 vs 0.70: [arize.com](https://arize.com/blog/jev-as-a-judge/)
- Rubric judges vs LLMs, 9 panels. LLM judges cost 16–325× more. A cascade gains at most 2.7 points because errors are correlated: [arXiv 2609.29769](https://arxiv.org/abs/2609.29769)

More projects (36 entries), grouped by sub-type (Platforms, Tools for managing judgments, Reported judge results, Hallucination and groundedness, Rubric scoring of content, Code review as triage): `prior-art/projects/judges-and-evals.md`.
