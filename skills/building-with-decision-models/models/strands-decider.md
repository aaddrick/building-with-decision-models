# Model notes: AWS Strands Decider 2B

Field notes from people who built on Strands Decider 2B, snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The server, model IDs, vision extra, and README benchmarks are in `providers/open-weights.md`.

## Limits

- **Latency grows roughly linearly with tokens** ([strandsagents.com](https://strandsagents.com/blog/introducing-strands-decider/)). About 115 ms median locally (RTX 3090) and about 153 ms on an M3 MacBook for short inputs. 106 ms median / 296 ms p95 on an RTX 3090 in another report ([aiweekly.co](https://aiweekly.co/alerts/amazon-ships-strands-decider-2b-an-open-source-jev-rival)). 2.5–3.8 s for 2,500–5,000-token inputs on an M3 Pro ([xenospectrum](https://xenospectrum.com/aws-strands-decider-local-decision-model/)). Keep passages and candidate tables short.
- **Request shape:** it returned HTTP 422 on null `criteria` values that other Jev-style servers accept ([classmethod.jp](https://dev.classmethod.jp/articles/strands-decider-2b-m4-mac-kiro-crew/)). Test your exact request shape before swapping backends.

## Calibration

- Answers at ≥0.9 confidence were reported correct about 95% of the time ([aiweekly.co](https://aiweekly.co/alerts/amazon-ships-strands-decider-2b-an-open-source-jev-rival)).

## Where it fails

- **Negated questions:** it sometimes gives the same answer when a question is negated ("which applies" vs. "which doesn't apply"). Phrase criteria positively ([xenospectrum](https://xenospectrum.com/aws-strands-decider-local-decision-model/)).
- **Multi-step reasoning or long documents:** its own model card says it struggles with both ([HF](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19)).

## By shape

- **In stream filters and real-time UIs:** fast on short items; the 0.9 band is usable as an act threshold after you check it on your labels.
- **Ranking and selecting:** keep passages short and criteria positive.
