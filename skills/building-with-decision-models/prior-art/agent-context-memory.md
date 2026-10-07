# Shape: Agent Context, Memory, and Effort

**Use when** you are building harness plumbing for an LLM agent: what stays in context, what gets remembered, when memories expire, how much reasoning effort to spend, which skill or tool to surface, and when the agent should stop, continue, or ask.

## The shape

Replace generative steps (summarize, rewrite) with **per-item decisions**. The kept content stays verbatim.

```
compaction : for each context block → Choice keep / truncate / drop, given the current task
memory     : after each turn → Noul "anything worth remembering?" → Choice category → append verbatim
lease      : for each stored memory → Noul "does the new evidence invalidate this?"
effort     : each step → Score "how stuck / how hard is this step?" → map to reasoning effort or model tier
stop       : on "done" → Nouls over transcript evidence ("claims done?", "verified?") → allow or send back
```

```python
from typesafe_sdk import Choice, TypeSafeClient

def compact(client: TypeSafeClient, task: str, blocks: list[str]) -> list[str]:
    qs = {
        f"b{i}": Choice(
            instructions={"question": "What should happen to `blocks[%d]` for the rest of `task`?" % i},
            criteria={"keep": "Still needed verbatim to finish the task",
                      "truncate": "Only the first lines or the result matter now",
                      "drop": "No longer relevant to the task"},
        )
        for i in range(len(blocks))
    }
    r = client.system_one(state={"task": task, "blocks": blocks}, questions=qs)
    out = []
    for i, b in enumerate(blocks):
        a = r.choices[f"b{i}"]
        if a.choice == "keep" or a.confidence < 0.5:           # unsure → keep
            out.append(b)
        elif a.choice == "truncate":
            out.append(b[:400] + "\n[truncated]")
    return out
```

Mind the model's context limit on state plus the longest question. Chunk the blocks across requests for long transcripts. See the window lesson below.

## Variants

- **Admission-time pruning.** Judge each tool output before it enters context, not only at compaction time.
- **Pointer plus expand.** A dropped block becomes a one-line pointer to a store. An `expand` tool returns the original byte for byte, so a wrong drop costs one tool call.
- **Effort lease.** The model returns both the effort level and how many steps to hold it (1, 2, 5, or 10).
- **Evidence-fed stop gate.** A Stop hook puts run facts from the transcript in the state and asks a few Nouls before allowing "done".
- **Ask before act.** A `before_tool_call` Noul asks "is it premature to call this tool before clarifying?" and returns guidance, so the agent asks the user instead of guessing.
- **Wake gate.** Ask a Choice (wake / not yet / unrelated) before resuming a sleeping agent's LLM.
- **Memory-applied tracking.** Retire lessons that get recalled but never followed.

## Field lessons

- A verbatim keep/drop is safer than a summary: nothing gets paraphrased wrong, and the decision is auditable.
- Changing the model mid-session rewrites the prompt cache and can erase the savings. Route subagents freely. Keep the main chat's tier fixed. One proxy reported a $19.53 loss over 309 requests before it added a cost guard ([HN](https://news.ycombinator.com/item?id=49831615), [jcm-router](https://github.com/adarshmishra07/jcm-router)).
- Change effort through a per-message statement, not the prefix. That kept the cache intact: 99.1% hit rate over 411 steps was reported on Jev ([jev-effort](https://www.everydev.ai/tools/jev-effort)).
- The bill moves less than the context. Reported: 16–17% smaller requests gave about 10% lower cost, and an effort proxy saved 55% at max effort but only 4–9% in a real session ([jev-compaction](https://github.com/Waxmell114514/jev-compaction), [jev-effort](https://www.everydev.ai/tools/jev-effort)). Measure dollars and wall-clock time, not tokens.
- Default to keep, or to "remember nothing", when confidence is low. False drops hurt more than extra tokens. Fail open to the harness's native path on errors.
- Decide in code which tool classes may lose content. Keep questions and skills in full, protect write/edit/shell calls, and let only reads (grep, find) be dropped. Require a minimum reduction (about 25%) before replacing the native compactor.
- Stop gates need evidence. Adding run facts lifted AUROC from 0.777 to 0.976 on Jev ([jev-belay](https://github.com/valentynkit/jev-belay)). Stop rules judged on wording alone caught only 5–12% of bad stops at a 5% false-positive rate ([limpet](https://github.com/noplan-inc/limpet)).
- Steer, don't block. Sending the agent back to prove "done" turned 76% of unverified claims into real test runs ([pi-warden](https://github.com/DevMortimer/pi-warden)).
- Skill selection needs an explicit "none" option, a `review` outcome, and suppression of skills already loaded. A lexical (BM25) prefilter capped recall at 0.60 because prompts describe tasks while skills describe capabilities ([skillranker](https://github.com/Dicklesworthstone/skillranker), [jev-skillful](https://github.com/bestagentkits/jev-skillful)).
- Use tiered confidence bars: require more confidence to downgrade to a cheaper tier, require a margin over the runner-up, and send ties to the middle tier ([dirien/jev-router](https://github.com/dirien/jev-router), [daviddl9/jev-router](https://github.com/daviddl9/jev-router)).
- Memory save/skip gates reported 98.5% accuracy at 0.3 s per decision. For memory, a reranker mostly shortens context: 2 memories ranked by Jev answered as well as 5 from a cross-encoder. Time decay made no measurable difference to recall ([hippo-memory](https://github.com/kitfunso/hippo-memory)).
- Pin the hosted model version in gates so thresholds do not drift under an alias.
- The context window decides which model can do compaction. Reported: Jev 32k tokens ([Cloudflare](https://blog.cloudflare.com/clef-decision-models/)). Several small local models read only 512 to 8,192 tokens, and one silently truncates past 2,048. Small local models fit per-block or per-memory decisions, not whole-transcript states.
- Not on Jev? Model-specific context and memory notes (context limits and how each model fails past them, such as CLM's silent truncation; dependent decisions and cache charges on Luna; check them before you send a transcript): `models/clef.md`, `models/clm.md`, `models/kev.md`, `models/laya.md`, `models/luna.md`, `models/nimble.md`, `models/others.md` (Tev1). Index: `models/INDEX.md`.

## Prior art

- jev-compaction, which scores segments and never writes. Dropped output becomes a pointer that can be expanded back. Reported on SWE-bench Verified: 25% of tool output removed at admission with no loss in resolution, about 10% lower cost: [Waxmell114514/jev-compaction](https://github.com/Waxmell114514/jev-compaction)
- jev-belay, a Stop hook that blocks an unverified "done" with one four-question call over transcript evidence. Reported: AUROC 0.976, 346 ms: [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay)
- jev-router (dirien), which never downgrades within a session. Bars: 85% for fast, 60% for balanced, 30% for frontier. Reported: 51% saved: [pulumi.com](https://www.pulumi.com/blog/route-every-claude-code-message-to-the-right-model-with-jev/), [dirien/jev-router](https://github.com/dirien/jev-router)

More projects (49 entries), grouped by sub-type (Compaction and pruning, Judgment-kernel agents, Memory, Effort, model, and skill control, Stop, continue, ask, wake, Local and framework plumbing, Harness frameworks): `prior-art/projects/agent-context-memory.md`.
