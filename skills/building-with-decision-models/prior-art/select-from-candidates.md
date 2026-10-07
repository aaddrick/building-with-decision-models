# Shape: Select From Candidates

**Use when** the answer already exists somewhere: a UI element, a tool, a function argument value, a span of text, a model tier, a handler. The model picks it and code copies it. The model never generates.

## The shape

```
enumerate  → code lists candidates (DOM/a11y refs, OCR boxes, regex hits, tool registry, Literal values)
select     → Choice with the candidates as keys (+ "none"), plus an absolute Noul ("does any fit?")
execute    → code uses the exact selected string or object
```

```python
from typesafe_sdk import Choice, Noul, TypeSafeClient

def pick(client: TypeSafeClient, goal: str, elements: list[dict]) -> dict | None:
    table = {f"e{i}": el for i, el in enumerate(elements)}       # opaque keys, details in state
    r = client.system_one(
        state={"goal": goal, "elements": table},
        questions={
            "target": Choice(
                instructions="Which element in `elements` should be used next to achieve `goal`?",
                criteria={k: None for k in table} | {"none": "No element helps with the goal"},
            ),
            "destructive": Noul(instructions="Would acting on the most relevant element delete, "
                                             "pay, send, or otherwise be hard to undo?"),
        },
    )
    t = r.choices["target"]
    if t.choice == "none" or t.confidence < 0.5 or r.nouls["destructive"].noul > 0.5:
        return None                                              # ask a human or escalate
    return table[t.choice]
```

## Variants

- **Operation + target in one Choice**: keys like `click:e12`, `type:e4`, `scroll:down`. One call per step.
- **Function calling with no LLM**: a `__tool__` Choice picks the function. Each `Literal` argument becomes a Choice keyed by the exact accepted strings, each `list[Literal]` one Noul per member, each `bool` a Noul. A `stated` Noul per argument ("did the user say anything about this?") keeps defaults. Code builds any text reply. Put all questions in one request (54 in the cookbook).
- **Three-way tool gateway**: one Choice over the tools plus `none`, then three outcomes. High confidence and every argument closed: code answers alone. High confidence and some argument open: force that tool and let an LLM write only the open arguments. Low confidence: pass the request to the LLM untouched (jev-gateway).
- **Value extraction**: an over-eager regex finds candidates. The candidate strings are the Choice keys, plus `none`. No transposed digits, no invented values.
- **Candidate spans for free text**: code cuts candidate spans (a search query, a URL) out of the input and a Choice picks one. No LLM is needed (jev-voice-browser).
- **Routers**: the candidates are models, effort levels, skills, MCP tools, or HTTP handlers.
- **Large rosters**: up to 255 options per Choice on most models. Above that, pre-rank with a Score or Noul, or use two stages (short descriptions → top 3 with full text). For a large roster that rarely changes, a contrastive model (CLM-8B) can cache the candidate embeddings once.

## Field lessons

- Give opaque keys (`e0`, `c3`) and put the details in state or in the option values. Where the exact string is the payload (extraction, `Literal` args), use the string itself as the key.
- A Choice always has a winner. Pair it with an absolute Noul (`exists`, `fits`, `stated`), or add a `none` key. Its probabilities are relative: they change when the number or content of candidates changes (measured on CLM-8B).
- Numbered element tables beat screenshots. Reported on Jev: $0.0002–$0.004 per step and 7 s flight bookings, against minutes and dollars for vision agents.
- When a free-text value is needed (a search query, a message body), call a small LLM for that one field only. If a chosen tool has a free `str` argument, either send that whole step to an LLM (pydantic-ai `UnfillableRoute`) or force the tool and let the LLM fill only that argument.
- Drop ineligible candidates (quota, context fit, permissions) in code before asking. Gate risk and confirmation in code after. If the top pick fails a filter, take the next one and log the original pick.
- Never trust a `DONE` choice. Check in code after every action that the change really happened.
- Ask one step per request. Planning whole tool sequences scored 38–44% position-wise on Jev (JevRouter). Leave planning to an LLM.
- Fit thresholds on your own labels, and re-fit them when the workload changes. On Jev, the best escalation threshold moved from 0.67 to 0.37 between two 500-example sets (Janus).
- A distilled 706k-parameter specialist beat hosted Jev on form filling (99.7% vs. 83.6%, 7–9 ms). At high volume on one narrow task, consider distilling.
- Tool-calling scores and deciding *whether* to call a tool are different skills. A model can lead on BFCL and still trail Jev on When2Call (Clef, `models/clef.md`). Validate the `none` question on any new model.
- **Screenshots as state:** Clef, pplx-decider, the OpenAI Decisions API, Liquid d1 and decider-2b-vision accept images. Jev is text-only. d1 takes images only on Liquid's own console for now; on Vercel AI Gateway and OpenRouter it is text-only.
- **Limits differ** by model: option caps, whether probabilities come back at all, and whether dependent questions need a separate request. Check the model file before you size a roster.
- Latency grows with state length, on every model measured (from about 0.1 s to several seconds over a few thousand tokens). Keep candidate tables short.
- Not on Jev? Model-specific selection notes (tool calling, roster limits, latency): `models/clef.md`, `models/clm.md`, `models/luna.md`, `models/nimble.md`, `models/pplx-decider.md`, `models/strands-decider.md`, `models/others.md` (Tev1, decider-2b). Index: `models/INDEX.md`.

## Prior art

- jev-browser MCP server, one Choice over up to 240 elements plus `goal reached` and `stuck` Nouls. Wikipedia Coffee→Espresso in about 4 s for $0.0016: [jkudish/jev-browser](https://github.com/jkudish/jev-browser)
- Janus, which measures the escalation threshold to an LLM fallback. Reported on Banking77: 80.2%, 53% cheaper, 11.6% escalated: [FirasSX914/Janus](https://github.com/FirasSX914/Janus)
- jev-gateway, a local gateway in front of coding agents. The model picks the tool or passes the request through. Reported −57% output tokens and −39% time on bug fixes, mixed on feature work: [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway)

More projects (53 entries), grouped by sub-type (Browser, computer, phone, Tool and function calling without an LLM, Extraction by selection, Routers, Benchmarks and model notes): `prior-art/projects/select-from-candidates.md`.
