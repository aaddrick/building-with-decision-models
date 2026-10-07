# Shape: Pairing a Decision Model With an LLM

**Use when** part of the job needs generation, long reasoning, or perception, and part is a frequent, fast judgment. Split them.

## The shapes

| Pairing | Who does what | Use for |
|---|---|---|
| **Planner / actor** | An LLM sets a goal every N steps. The decision model picks actions every step. | Games, robots, long-horizon agents |
| **Verify-then-escalate cascade** | A cheap LLM produces. The decision model checks each field or claim. Flagged items go to a strong LLM. | Extraction, answers, citations, judging |
| **Front-door router** | The decision model classifies intent and complexity. It routes to code, a specialist LLM, or a human. | Support, assistants |
| **Model-tier router** | The decision model scores difficulty and risk per turn. Code maps the scores to a cheap, mid, or frontier LLM. | Coding agents, LLM proxies |
| **Proposer / selector** | An LLM or CV proposes candidates. The decision model selects. | Extraction, detection boxes, art |
| **Model decides, LLM writes** | The decision model picks the tool, arguments, and branch. A small LLM writes only the free-text field. | Tool calling, replies |
| **Rule writer / runner** | An LLM rewrites the rules or questions offline. The decision model runs them live. | Trading bots, prompt → rubric migration, harnesses |
| **Tutor → student** | Decisions or LLM-made labels train a small local model that takes over | High-volume narrow loops |
| **Trigger → investigator** | The decision model decides "is this serious?". An LLM digs into logs and writes a report. | Monitoring, SOC |

```python
from typesafe_sdk import Noul, TypeSafeClient

FIRE = 0.7
FLAWS = {
    "hallucinated": "Is `extracted_value` absent from `source_text`?",
    "off_target": "Does `extracted_value` answer a different field than `field_spec` asks for?",
    "format_violation": "Does `extracted_value` break the format in `field_spec`?",
}

def verify(client: TypeSafeClient, source: str, schema: dict, record: dict) -> bool:
    qs = {
        f"{field}::{flaw}": Noul(instructions={
            "field_spec": schema[field], "extracted_value": value, "question": text})
        for field, value in record.items() for flaw, text in FLAWS.items()
    }
    r = client.system_one(state={"source_text": source}, questions=qs)
    return max(a.noul for a in r.nouls.values()) > FIRE      # True → escalate to the strong LLM
```

## Variants

- **Measured router**: before routing, benchmark the decision model against the fallback LLM on your own labels or agreement logs. "Do not route" is a valid result.
- **Asymmetric tier router**: upgrade at a low bar and downgrade only at a high bar. Never downgrade on risk words or large contexts. Shadow-run it for a day before it switches models.
- **LLM-authored harness**: an LLM writes the features and questions offline, and reward traces (GEPA) refine them. At runtime the decision model runs alone.
- **Uncertainty-sampled labels**: spend the label budget only on the rows the model is least sure of. Then let an LLM rewrite the question definitions.
- **Contrastive synthetic training data**: a generator LLM writes near-identical pairs where one fact flips the label, and a verifier LLM checks them. A LoRA then trains a small decision model on them. Keep a human-reviewed holdout.
- **Output guard on all LLM traffic**: several Noul checks run on every LLM response, with replace, block, or annotate policies. This overlaps with `prior-art/gates.md`.

## Field lessons

- Escalate on the **maximum** flag, not the average.
- Hallucination checks read literally. A reformatted value ("03/14/2026" against the source's "March 14, 2026") scored 0.84 "absent" in a live test (Jev). Normalize values before the check, or ask "Is the value in `extracted_value` stated in `source_text`, in any format?".
- Put the decision model on the hot path (every tick, every item) and the LLM on the cold path (rare, hard).
- Thresholds do not transfer. Janus saw the best threshold move from 0.67 to 0.37 between datasets. Set the threshold before testing, then re-validate it per workload and per fallback model.
- Confidence is a routing signal, not a certificate. On judging work, expect to escalate 35–50% (about 46% at q < 0.9 in JEV-as-a-Judge).
- Every tier is paid. A cascade costs one check per item plus a second check on each escalated draft, so the savings depend on the escalation rate.
- Send "unanswerable from this context" to a human, not to the bigger LLM.
- Make routers asymmetric. NeuroLink upgrades at 0.3 and downgrades only at 0.6. Shadow-route for a day before switching models.
- Check the cheap tier alone before building a router. In tiershift's test, the fast model alone matched the flagship at 3% of the cost.
- "Define in an LLM → run in a decision model → train your own classifier on the collected labels" came up repeatedly. The decision model is a middle stage, not always the end state.
- An LLM can generate labels when you have none. Nimble generated contrastive pairs with one GPT-5.6 model and verified them with another. Strands Decider and decider-2b kept Qwen-written labels only when independent answers agreed. LLM-checked labels share the LLM's blind spots: decider-2b's LLM-labeled stage lost 2.2 points on human-labeled sets. Keep a human-reviewed holdout.
- A failed or deferred decision must not fall through to a business action. Treat "defer" as a valid answer and send it to the LLM or a human.
- Test the cheap and the expensive model of a family on your own data before picking by price. The smaller one can match or beat the larger.
- A model's own act/escalate output can be a worse escalation trigger than its option confidence. Measure both before you wire one to the cascade.
- **Jev:** overconfident in the top bucket: 99.4% stated against 90.2% actual on 8,801 examples (Anthus, reported). Calibrate before setting an escalate floor.
- Not on Jev? Model-specific pairing notes (escalation signals, zero-shot vs fine-tuned, training data): `models/clef.md`, `models/laya.md`, `models/kev.md`, `models/nimble.md`, `models/others.md` (Tev1). Index: `models/INDEX.md`.

## Prior art

- JEV-as-a-Judge (CMU). Jev judges, and anything under 0.9 escalates to GPT-6. Reported +0.9 points over GPT-6 at 41% of its fee on 1,610 pairs: [arXiv 2609.26550](https://arxiv.org/abs/2609.26550). Write-up: [flowtivity.ai](https://flowtivity.ai/blog/jev-as-a-judge/)
- tiershift: Jev scores 11 dimensions, and a YAML policy picks the fast, mid, or flagship tier in a median 180 ms. Reported flagship quality at 40% lower cost on 120 prompts: [iamvatsalpatel/tiershift](https://github.com/iamvatsalpatel/tiershift)
- JevHarness: an LLM writes the harness and its Jev questions, then GEPA refines them on rewards. Reported Pokémon win rate rose from 25% to 75% after 5 rounds: [TianyuCodings/JevHarness](https://github.com/TianyuCodings/JevHarness)

More projects (44 entries), grouped by sub-type (Verify-then-escalate cascades and judges, Routing (code, specialist LLM, model tier, or human), Planner / actor and proposer / selector, Rule writer / runner, Tutor → student and training recipes): `prior-art/projects/llm-pairing.md`.
