# Shape: Control Loops

**Use when** something must act repeatedly on changing state: games, simulations, robots, drones, vehicles, trading, device automation.

## The shape

```
loop every tick:
    observe  → code turns raw state into compact text/JSON (RAM, CV, order book, a11y tree)
    decide   → one request: a Choice over the LEGAL actions, plus speculative side questions
    act      → code executes: pathing, flight control, order placement, input injection
    verify   → code checks the effect; failures feed the next observation
```

Code owns physics, pathing, math, risk limits, and the action set. The model only answers "what does this situation call for?".

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()  # one client for the whole loop

def decide(obs: dict, legal: list[str]) -> str | None:
    r = client.system_one(
        state={"observation": obs},
        questions={
            "action": Choice(
                instructions="Given `observation`, which action best advances the goal?",
                criteria={a: None for a in legal},     # only legal actions; rebuild every tick
            ),
            "danger": Score(
                instructions="How much immediate danger is the agent in?",
                criteria=["No threat nearby", "Threat present but not engaging",
                          "Taking damage or about to"],
            ),
            "target_lost": Noul(instructions="Is the tracked target no longer visible in `observation`?"),
        },
    )
    if r.choices["action"].confidence < 0.4:
        return None                                    # hold, or escalate to a planner
    return r.choices["action"].choice
```

## Variants

- **Hierarchical**: the model picks a goal ("go to Pewter City"), code pathfinds (A*). The model only takes the branch points. This is cheaper and more robust than per-button control.
- **Planner + actor**: an LLM sets a goal every N ticks, and the decision model picks macro-actions each tick. See `prior-art/llm-pairing.md`.
- **Objective ladder**: code keeps a fixed curriculum (wood → stone → iron → diamond). The model picks among the actions for the current rung.
- **Tutor → student**: log the model's decisions from successful episodes and train a small local policy that gradually takes over. The loop gets cheaper the longer it runs.
- **Multi-channel**: separate questions per subsystem (navigation vs. combat, direction vs. regime vs. inventory) in the same request.
- **Engine-annotated state**: code computes every tactical fact (threats, wins, blocks). The model makes only the strategic pick.
- **Intent → parameters**: one Choice picks an intent, a second picks discrete axis or gripper commands.
- **Pruned route menu**: code precomputes routes and drops fatal ones, the model picks, and code never overrides the pick.
- **Advisory System 2**: an LLM is consulted asynchronously when confidence drops. It never blocks the tick.

## Field lessons

- Put **objects**, not pixels or raw bytes, in the state: object-centric JSON from RAM, numbered UI elements, a range-sector table from CV. Most decision models are text-only and weak on raw numbers.
- Representation matters more than the model. On Connect Four, the same model went from 22.2% to 74.7% wins when code precomputed the lines. The best setup let the engine compute all the tactics, at 1/25th the bytes. Compressed symbols hurt accuracy. Reported on Jev ([jev-connect4](https://github.com/hazlema/jev-connect4)).
- Keep what code observed apart from what the model inferred. An inferred label is not a fact. Before acting on an answer, check that the state it came from still holds. A decision about a stale observation is a decision about a different situation. A model's DONE is not proof: verify the effect.
- Rebuild the Choice options every tick from what is actually legal. An illegal option wastes probability mass and invites bad actions. Pin each answer to a state revision and reject stale ones.
- Give options descriptive keys, not positions. On one small model, accuracy fell from 0.70 to 0.51 when it picked records by position among 64 (decider-2b, `models/others.md`).
- Per-move hazard questions give reflexes, not plans. A Snake agent built on 9 Nouls per tick died on self-collision ([snake-jev](https://github.com/siroccomask/snake-jev)). Keep route planning in code. Search-heavy games (chess) fail. Reflex and situational games (Doom, Mario, Pong, Minecraft survival) work.
- Tick rates people hit on hosted Jev: about 2.5 Hz (drone), about 5 Hz (4 questions every 200 ms, driving), about 10 Hz (Doom), about 300 ms per block (on-chain trading). Per-decision latency is about 80–300 ms. Local small models can run at 13–33 ms per decision, and hosted Clef was measured several times slower than Jev. Check the model file before you set a tick rate.
- Continuous control is a poor fit. In a landing sim, Jev at 2.4 Hz scored 56 vs. 69.9 for a simple baseline controller. LLMs at 2.5–4.5 s per decision mostly crashed ([FlightBench](https://github.com/AlperKartkaya/FlightBench)). Let the model pick discrete, labelled modes and keep the control law in code.
- Check a model's limits before porting a loop to it. Jev allows 255 options per Choice; some local models cap a Choice at 24 or 26 and a context at 2k–8k tokens. Large legal-action sets need a code pre-filter.
- For money, the model proposes and a deterministic risk gate disposes. Nobody lets it place orders unguarded. Use dry-run defaults, spend caps, and a fallback for a late or missing answer.
- Cost reference: Doom about $7/hour at 10 Hz. Minecraft about 1¢ per 2 minutes. Pokémon Red took 4 badges for under $0.50.
- Not on Jev? Model-specific loop notes (option caps, context, latency, dependent questions): `models/clef.md`, `models/clm.md`, `models/laya.md`, `models/luna.md`, `models/nimble.md`, `models/others.md` (Tev1, decider-2b). Index: `models/INDEX.md`.

## Prior art

- Connect Four with nine query strategies over about 1,800 games. Engine-annotated state went 94-4-1: [hazlema/jev-connect4](https://github.com/hazlema/jev-connect4)
- Fixed-wing landing in JSBSim. Jev scored 56/100 vs. 69.9 for a baseline; GPT-6 controllers scored 0–49: [AlperKartkaya/FlightBench](https://github.com/AlperKartkaya/FlightBench)
- Stealth game guards, 4 batched questions per guard. Stale revisions are rejected. 259.9 ms median, 0 fallbacks over 288 judgments: [AbdelStark/heist-one](https://github.com/AbdelStark/heist-one)

More projects (52 entries), grouped by sub-type (Games, Robots, vehicles, simulations, Markets, Devices): `prior-art/projects/control-loops.md`.
