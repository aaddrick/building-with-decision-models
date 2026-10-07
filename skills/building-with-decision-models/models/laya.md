# Model notes: Laya (ConvAI Innovations)

Field notes from people who built on Laya, a ModernBERT encoder, snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The server, checkpoints, extra fields, and the 100-option HTTP cap are in `providers/open-weights.md`.

**Short version:** fast and tiny, but a base to fine-tune, not a zero-shot model. Fine-tune it, calibrate it, and keep option lists short.

## Limits

- **Context:** the English checkpoint reads only 512 tokens. The multilingual checkpoint reads 1,024, expandable to 8,192 ([laya](https://github.com/NandhaKishorM/laya)). Pass excerpts, not whole documents.
- **Options:** about 20 options with descriptions fit, the rest are trimmed, and the server caps a question at 100 options.
- **Latency:** 33 ms on a T4, and it runs on CPU ([orcarouter.ai](https://www.orcarouter.ai/blog/laya-vs-nimble)). 13.42 ms p50 on an M3 Max with MLX.

## Calibration

- The multilingual checkpoint ships uncalibrated. Fit temperatures on your own labels before you set thresholds.
- **Long option lists:** calibration error rose from 0.032 to 0.573 as the list grew ([decision-models-under-pressure](https://github.com/gazelle93/decision-models-under-pressure)).
- **Escalation signal:** gate escalation on option confidence (AUROC 0.77), not on the act/escalate head (AUROC 0.30) ([HF](https://huggingface.co/convaiinnovations/laya)).

## Where it does well

- After fine-tuning: 0.362 zero-shot rose to 0.766 fine-tuned on the typed-decisions benchmark.
- Speed and size: it fits CPU and edge deployments where nothing larger runs.

## Where it fails

- **Zero-shot:** 0.362, below a majority-class baseline of 0.461 ([besthub.dev](https://www.besthub.dev/articles/open-source-decision-model-laya-vs-jev-speed-wins-zero-shot-fails-befced0a2228)). Near random zero-shot in another test ([orcarouter.ai](https://www.orcarouter.ai/blog/laya-vs-nimble)). Fine-tune it first.
- **Many labels:** it falls from 0.950 at 4 labels to 0.425 at 77 ([creativeainews](https://www.creativeainews.com/articles/open-jev-clones-benchmark-disagreement-2026/)), and to 38.2% against Jev's 76.4% in another test ([stuntd](https://github.com/bladedevoff/stuntd)). Zero-shot BANKING77 0.43 vs. Jev 0.87; `predict_tournament()` lifted it to 0.61 ([laya](https://github.com/NandhaKishorM/laya)). Weak past about 20 options.
- **Tool calling:** BFCL 38.13, press-reported ([pasqualepillitteri.it](https://pasqualepillitteri.it/es/news/19915/cloudflare-clef-desafia-jev)).
- **Its act/escalate output as the escalation trigger:** AUROC 0.30 ([HF](https://huggingface.co/convaiinnovations/laya)).
- **Reranker over small evidence sets:** cost 8.8% more than a deterministic selector, with no gain ([codex-jev-router](https://github.com/suenot/codex-jev-router)).
- **Long option lists:** calibration collapses as the list grows (see Calibration).
- **NSFW image flagging via an open "VisionLaya" clone:** too many false positives ([HN](https://news.ycombinator.com/item?id=49779502)). Put a dedicated classifier or a human in front.

## By shape

- **As a gate:** 512 tokens (English) cannot hold a long context. Calibrate before you set thresholds, and gate escalation on option confidence.
- **In control loops:** fast, but fine-tune before using it in a loop.
- **In stream filters:** fine-tune and calibrate first. Keep label sets under about 20.
- **Ranking and walking:** use the option tournament (groups of about 16, then a final over the winners) for anything over about 20 options.
- **LLM pairing:** a base to fine-tune, not a zero-shot first pass in a cascade.
- **Agent context and memory:** per-block decisions only, on excerpts.
