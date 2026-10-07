# Model notes: Perplexity pplx-decider

Field notes from people who built on pplx-decider (hosted or open weights), snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The wire contract (`POST /v1/decisions`, 262,144-token context, image tiles, rate limit, price) is in `providers/perplexity.md`.

## Limits

- **Latency grows with state length:** under 2 s on short prompts, up to 23 s near its context ceiling. Keep candidate tables short when latency matters.

## Calibration

- Reported ECE 0.018 on one shared index, the lowest of the three models measured there ([source](https://laurencemoroney.com/2026/10/02/decision-models-explained.html)).
- **Not fully deterministic:** identical requests can differ in the second decimal, so leave a margin around thresholds.

## Where it does well

- **Grounding checks** ("is this claim supported by the retrieved passage?"): the strongest reported model, RAGTruth 88.8% vs. Jev 77.3% (vendor panel) ([benchlm.ai](https://benchlm.ai/md/decision-models.md)).
- **Long states:** whole documents and long transcripts fit its context.

## Where it is weaker

- Jev is reported stronger on TruthfulQA (92.0% vs 85.4%). Pick the model per question type.

## By shape

- **As a gate:** use it for the "is this claim supported?" gate before publishing.
- **Ranking and retrieval:** use it for the support check on the retrieved passage.
- **Selecting from candidates:** keep candidate tables short; latency climbs with tokens.
- **Embedded in infrastructure:** do not mark a SQL function over it deterministic; leave a margin around thresholds.
