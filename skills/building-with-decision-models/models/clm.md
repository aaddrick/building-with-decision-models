# Model notes: CLM-8B (Contrastive-LM, Stanford + NVIDIA)

Field notes from people who built on CLM-v0.1-8B, a contrastive model that scores candidates by embedding similarity, snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The server, `confidence` formula, and errors are in `providers/open-weights.md`.

**Short version:** fast over a fixed candidate set, blind past 2,048 tokens, and it cannot tell you the right candidate is missing.

## Limits

- **It silently truncates any state past 2,048 tokens** by default, with no error ([CLM](https://github.com/Contrastive-LM/CLM)). Send short states, or raise `--max-model-len` and re-test.
- **It only ranks the candidates you give.** Its scores are relative within the set, and it never adds a missing candidate. Its free-form ranking mode scores only the candidates you pass, so it cannot tell you the right action is missing.
- **Latency:** 16.5 ms per decision vs 149.8 ms for Jev on a T-Rex game loop, but on a local GPU vs a hosted API ([cryptobriefing.com](https://cryptobriefing.com/stanford-nvidia-clm-8b-faster-than-jev/)). Caching a revisited state's vector took 28.6 ms down to 0.6 ms ([CLM](https://github.com/Contrastive-LM/CLM), [wavect.io](https://wavect.io/blog/clm-8b-self-hosting-action-cache-verifier.md)).
- **The cache helps only when the candidate set repeats** (embeddings cache on exact text). Its action-vector cache pays off only when the action set is stable ([pytorch.kr](https://discuss.pytorch.kr/t/clm-contrastive-lm-jev/12013)). Version the encoder, head, and catalog together.

## Calibration

- Score `confidence` ignores level distance, so it differs from Jev's Score formula. No ECE is published.
- Choice probabilities change when the number or content of candidates changes.

## Where it does well

- **Large, fixed rosters:** reported 95.2% on BFCL v4 vs 99.2% for Jev, but about 13× faster at around 1,000 cached candidates ([wavect.io](https://wavect.io/blog/clm-8b-self-hosting-action-cache-verifier/), [xenospectrum](https://xenospectrum.com/en/clm-8b-decision-cache-benchmark/)).
- **Per-step action or stop ranking over a fixed candidate set**, where the cache keeps each step under a millisecond.

## Where it fails

- **A long state:** truncated past 2,048 tokens, see above.
- **Tool-calling success:** reported weaker than Jev ([Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM)). WikiRacing 26/30 vs. Jev 30/30.
- **Agent "done?" or "wait" judges:** CLM-v0.1-8B gave the same answer almost every time, as did GLiNER2.5-Decide ([aimultiple](https://aimultiple.com/decision-models)).

## By shape

- **As a gate:** use it to pick the next action from a closed list, not to gate a long context.
- **In control loops:** it fits a Choice over known actions. Keep the action set stable so the cache works.
- **Selecting from candidates and ranking:** best on large, fixed rosters. Pair it with an absolute `fits` Noul or a code check, because it never reports a missing candidate.
- **Agent context and memory:** a cached vector is not a cached permission. Re-check permissions in code each step.
