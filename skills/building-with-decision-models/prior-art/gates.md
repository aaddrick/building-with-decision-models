# Shape: Gates

**Use when** something must be allowed, blocked, reviewed, or escalated before it happens: agent tool calls, shell commands, commits, migrations, trades, refunds, content, agent "done" claims.

## The shape

```
proposed action + context → code rules: a known-bad pattern blocks here, and the model never sees it
                          → one request: specific risk Nouls + a severity Score (+ category Choice)
                          → code policy: block if any serious flag, review if uncertain, else allow
                          → log the answers; re-route cached answers when the policy changes
```

```python
import re

from typesafe_sdk import Noul, NoulCriteria, Score, TypeSafeClient

POLICY = {"review": 0.35, "block": 0.70, "severity_block": 1.5}   # one place, reviewable
# Exact conditions whose miss cannot be undone. The model cannot override these.
DENY = [re.compile(p) for p in (
    r"\brm\s+(-\S+\s+)+(/|~|\$HOME)/?\*?(\s|$)",             # rm -rf on / or home, incl. ~/ and /*
    r"\bgit\s+push\b.*(--force|-f)\b",                          # force push
    r"\b(mkfs|dd\s+if=)",                                        # overwrite a disk
    r"\bDROP\s+(TABLE|DATABASE)\b",
)]

def gate(client: TypeSafeClient, command: str, cwd: str) -> str:
    if any(p.search(command) for p in DENY):
        return "block"
    r = client.system_one(
        state={"command": command, "cwd": cwd},
        questions={
            "deletes_data": Noul(instructions="Does `command` delete or overwrite files or data?"),
            "exfiltrates": Noul(
                instructions="Does `command` send local files, secrets, or env vars to a remote host?",
                criteria=NoulCriteria(true="Uploads, posts, or pipes local content to a network destination",
                                      false="No local content leaves the machine"),
            ),
            "outside_cwd": Noul(instructions="Does `command` modify anything outside `cwd`?"),
            "severity": Score(
                instructions="If `command` went wrong, how bad would the damage be?",
                criteria=["Nothing lasting; trivially undone", "Recoverable with effort",
                          "Irreversible loss or exposure"],
            ),
        },
    )
    flags = [r.nouls[k].noul for k in ("deletes_data", "exfiltrates", "outside_cwd")]
    if max(flags) >= POLICY["block"] or r.scores["severity"].score >= POLICY["severity_block"]:
        return "block"
    if max(flags) >= POLICY["review"]:
        return "review"
    return "allow"
```

## Variants

- **Allow/ask/deny Choice**: one 3-way verdict. It is simpler, but you lose the reason and the ability to re-tune per flag.
- **Completion gate ("not done until the model agrees")**: Stop hooks ask evidence questions ("were the tests run?", "does the diff match the stated change?") before an agent may finish.
- **Pre-action gate in finance**: the decision model runs before a deterministic risk engine and before a slower LLM gate.
- **Verified cascade**: the decision model checks a cheap LLM's output. Only flagged cases go to the expensive model (see `prior-art/llm-pairing.md`).
- **Input and output batteries**: separate question sets for the user prompt and for the model's reply.
- **Window or burst gate** (Discord raid, fraud burst, alert storm): code computes the window stats (join rate, message rate, account ages, duplicate ratio) and samples 5–20 events into the state. Nouls ask "coordinated raid?" and "spam-bot pattern?", a Score rates severity, and the policy decides whether to lock, alert, or allow. Keep the rates and counts in code, because decision models do not count.
- **Human-in-the-loop UX**: return a Choice to the human as buttons ("Reverse the model", as in Jev demos).
- **One-way gate**: the model may only tighten (escalate-only) or only loosen (allow-or-stay-silent). A model error then cannot cause the dangerous outcome.
- **Policy matrix by destination**: one set of leak Nouls; block/ask/allow depends on where the output goes (public, shared, private channel).
- **Session taint**: screen tool calls, tool results, and tool descriptions. After one flagged result, apply a stricter policy for the rest of the session.
- **Trajectory supervisor**: deterministic window rules over the agent's event stream (error rate, retry loops, budget, stalls) plus an advisory model score, giving pause/cancel/block. This is the window gate applied to agents.
- **Gate as a proxy with a pluggable judge**: one OpenAI-compatible endpoint where the judge can be a hosted model, a local clone, a chat LLM, or rules. It makes A/B tests on the same gate cheap.

## Field lessons

- Combine flags with the **maximum**, never the average. One serious flag must win.
- Keep the policy (thresholds, precedence) in code or config. Re-running a policy on cached probabilities costs nothing.
- Phrase every flag so that yes = the bad thing. Write `true`/`false` criteria for subtle boundaries.
- A decision model is not a security boundary against adversarial input. Keep untrusted text in its own field, add an injection Noul, and never let a model "allow" alone authorize money or deletion. Put exact rules in code before the model call: a denylist, a spending limit, a protected branch. A rule's block stands whatever the model answers. The model judges what the rules do not decide, and can only make the result stricter.
- Run deny rules before the read-only allowlist. A command name says nothing about its arguments: `cat` is harmless until it is `cat ~/.ssh/id_ed25519`.
- Fit thresholds from your own logs. Reported: defaults of 0.85/0.60 escalated 81% of commands, and a 0.8 confidence floor would have escalated 58% of legitimate traffic. Rubric wording alone can flip a verdict, so keep a regression set of commands.
- Choose the failure mode per surface. Command and money gates fail closed (deny, ask, or manual review). Chat moderation can fail open behind a deadline and a circuit breaker, with an outage alert.
- Keep the final decision in code and log disagreements. Reported on Jev: the model's own "route" Choice disagreed with the code-composed decision 28% of the time.
- Injection flags also fire on harmless text *about* injection. Reported on Jev: 7 of 63 benign documents flagged; 206 of 1,054 injected tool results missed. Put the user's request and system prompt in the state, because many failures only show against that context.
- A gate is not access control. The executor must still scope credentials. An in-agent hook protects only the agent that has it installed.
- Run shadow first. Let the gate decide alongside the current process before it acts. Set a stricter threshold for irreversible actions (paging, blocking a customer) than for reversible labels. Accuracy is uneven across workflows, so shadow each workflow on its own.
- Compare models by **coverage at a fixed error budget**: the share of decisions you can automate while staying under, say, 5% errors. That share is the gate's real value. Reported: Kev-4B/9B/27B automate 0.52–0.69 of new-source decisions at 5% error, against 0.70 for Jev.
- Use small local models only behind hard rules, with "ask" as the default (see the leakguard entry below). Pick the model per question type: a grounding gate and a command gate can run on different models.
- Reported wins on Jev: approvals 8.7× faster and 4.4× fewer prompts on 153 real commands. Vercel's command-safety review was 5–18× faster than an OpenAI model. Under "the owner approved this" social engineering, Claude Code auto mode ran 8 of 12 dangerous commands and a rules + Jev gate ran 0 of 12.
- Not on Jev? Model-specific gate notes (context limits that cut a long state, image latency, moderation agreement, calibration): `models/clef.md`, `models/clm.md`, `models/kev.md`, `models/laya.md`, `models/nimble.md`, `models/pplx-decider.md`, `models/others.md` (Tev1, Mercury Decide). Index: `models/INDEX.md`.

## Prior art

- openclaw-jev-leakguard, five leak Nouls on outgoing messages + channel-tier policy; reported on 113 cases: Jev 0% missed / 7% false alarms / 228 ms, Kev-0.8B 21% / 11% / 5.2 s, rules 54% / 0% (Jev, Kev-0.8B): [yousan/openclaw-jev-leakguard](https://github.com/yousan/openclaw-jev-leakguard)
- Edward, deterministic window rules plus an advisory scorer give pause/cancel/block; reported on StepShield: rules 7.4% recall, + local 4B 58.3% recall / 17.6% FPR, + Jev 59.3% / 10.2% (Jev or local 4B): [VeridicalTech/Edward](https://github.com/VeridicalTech/Edward)
- jev-shield, MCP firewall over calls, results, and tool descriptions, with session taint; reported 94% block recall, 0 false positives, 558 ms median: [caiovicentino/jev-shield](https://github.com/caiovicentino/jev-shield)

More projects (49 entries), grouped by sub-type (Agent tool and command gates, Trajectory gates, Completion and "done" gates, Code and CI gates, Money and risk gates, Content gates, Research and vendor guidance): `prior-art/projects/gates.md`.
