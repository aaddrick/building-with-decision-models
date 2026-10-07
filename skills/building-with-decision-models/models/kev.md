# Model notes: Kev (Jared Palmer)

Field notes from people who built on Kev (0.8B, 4B, 9B, 27B), snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The server, checkpoints, fitted temperatures, and README benchmarks are in `providers/ollama.md` (Kev section).

## Limits

- **Context:** 0.8B–9B validated to 8,192 tokens, Kev-27B to 65,536 ([kev](https://github.com/jaredpalmer/kev)). Small checkpoints fit per-block decisions, not whole-transcript states.
- **Latency:** 39 ms (1.7B), 69 ms (4B), and 117 ms (8B) for 8 questions over 512 tokens. A 32-question, 2k-token request takes 116 ms on the 1.7B ([iluvatarlabs.com](https://iluvatarlabs.com/blog/2026/09/kev-fast-jev-style-decision-model/)). Fast enough for per-keystroke local use.

## Calibration

- **A temperature fitted on few options breaks on many:** Kev-9B ECE 0.051 at 5 options, 0.377 at 150. Refit for your label space.
- **Scores bunch near 0.9**, so a small shift flips many verdicts.
- **Served vs eval path:** served probabilities differ from the fp32 eval path by up to about 0.03–0.05, and the top answer flips on about 1 question in 300.
- **Close accuracy can hide a calibration gap.** Opper reported Jev 96.5% vs Kev 4B 95.7%, but Kev's calibration drifted more on Stack Exchange and GitHub tasks.

## Where it does well

- **Automation at an error budget:** Kev-4B/9B/27B automate 0.52–0.69 of new-source decisions at 5% error, against 0.70 for Jev.
- **Narrow routing:** Kev-9B leads Jev on support routing (0.952 vs 0.897) but trails on MMLU-Pro (0.515 vs 0.840).
- **Training data:** benchmarked against Jev, not trained on its outputs. Its data came from public datasets, executable rules, or other LLMs.

## Where it fails

- **A small checkpoint as the only gate for leaks or destructive actions:** on 113 leak cases Kev-0.8B missed 21% of leaks at 5.2 s; Jev missed 0% at 228 ms, and rules alone missed 54% ([openclaw-jev-leakguard](https://github.com/yousan/openclaw-jev-leakguard)). Another open 0.8B model agreed with labels only 61.2% of the time without hard rules ([jev-style](https://github.com/lawrence3699/jev-style)).

## By shape

- **As a gate:** use small local checkpoints only behind hard rules, with "ask" as the default. Compare against Jev by coverage at your error budget.
- **Real-time and keystroke UIs:** the small checkpoints are fast enough to re-ask on every keystroke.
- **Answers as data:** refit the temperature for your option count before reading probabilities as frequencies.
- **Agent context and memory:** 8,192 tokens for 0.8B–9B; use 27B for long states.
