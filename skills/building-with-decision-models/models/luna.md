# Model notes: OpenAI Decisions API (GPT-6 Luna)

Field notes from people who built on the OpenAI Decisions API with `gpt-6-luna` (public beta), snapshot 2026-10-06. Numbers are author-reported unless a line says otherwise. The wire contract (`POST /v1/decisions`, `input`, `predicate`, price, data terms) is in `providers/openai-decisions.md`.

## Limits

- **Dependent questions need separate requests.** A question that depends on another answer needs its own request; put independent ones together ([docs](https://developers.openai.com/api/docs/guides/decisions)).
- **No published option cap.** It returns probabilities, but no limit on options is documented. Test your largest option list.
- **No cache charges** are listed, so the prompt-cache cost that drives effort routing on chat models does not apply to the decision call itself ([OpenAI docs](https://developers.openai.com/api/docs/guides/decisions)).

## Calibration

- **Stated confidence fell apart on multi-step logic** (reasoning off). At ≥99% stated confidence it was right 68% of the time, and AUROC fell from 0.88 to 0.51 at five chained steps ([anth.us](https://anth.us/blog/openai-decisions-api-preview/)). Its confidence is not a usable measurement on hard items.

## Where it does well

- Final judgment on answer correctness: JudgeBench 88.6% against Jev's 78.1% (see `prior-art/bad-fits.md`).

## Where it fails

- **Confidence on multi-step reasoning:** right only 68% of the time at 99%+ stated confidence ([anth.us](https://anth.us/blog/openai-decisions-api-preview/)).
- **A fixed answer list can leave out the right outcome.** Include a review or "other" answer ([vercel.com](https://vercel.com/i/what-is-openai-decisions-api)).

## By shape

- **Judges and research measurement:** do not let a confidence threshold route reasoning-heavy grading, and do not treat its confidence as a measurement on hard items.
- **In stream filters:** always include a review or "other" answer.
- **In control loops and agent harnesses:** a step that depends on an earlier answer needs a separate request, so plan the extra round trip.
