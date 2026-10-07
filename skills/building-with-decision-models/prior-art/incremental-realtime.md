# Shape: Incremental and Real-Time Decisions

**Use when** the input arrives in pieces and you must decide before it is complete: speech transcripts, keystrokes, video captions, webcam frames, sensor feeds, live translation.

## The shape

```
on each increment (word, keystroke batch, caption segment, frame):
    one request over the input so far: "is it complete enough?", "what is it?", "is it risky?"
    commit when confidence crosses a bar, or when a max hold time expires; otherwise wait
```

```python
from typesafe_sdk import Choice, Noul, TypeSafeClient

COMMIT_AT = 0.85
MAX_HOLD_S = 17.0

def on_partial(client: TypeSafeClient, text_so_far: str, held_for_s: float, intents: dict) -> str | None:
    r = client.system_one(
        state={"utterance_so_far": text_so_far},
        questions={
            "complete": Noul(instructions="Is `utterance_so_far` a complete thought that can be acted on now?"),
            "addressed_to_me": Noul(instructions="Is `utterance_so_far` addressed to the assistant?"),
            "intent": Choice(instructions="What does the speaker want?", criteria=intents | {"unclear": None}),
            "destructive": Noul(instructions="Would acting on `utterance_so_far` be hard to undo?"),
        },
    )
    ready = r.nouls["complete"].noul > 0.8 and r.choices["intent"].confidence >= COMMIT_AT
    if (ready or held_for_s > MAX_HOLD_S) and r.nouls["addressed_to_me"].noul > 0.7:
        if r.nouls["destructive"].noul > 0.5:
            return "confirm:" + r.choices["intent"].choice
        return r.choices["intent"].choice
    return None
```

## Variants

- **Live, then final.** Debounced calls on partials drive the display. One authoritative call when the segment closes overwrites them.
- **VAD proposes, the model disposes.** Acoustic endpointing finds pause candidates. A Noul batch over the trailing transcript confirms end-of-turn. A hard silence cap is the fallback.
- **Cancellable commit.** After the bar is crossed, wait about 1 s and cancel if new input arrives. Then apply a cooldown.
- **Prefix consumption.** When a command commits, drop its transcript prefix so back-to-back commands in one breath work.
- **Persistence for frames.** Require N consecutive agreeing checks, and slow the check rate when the scene is unchanged.
- **Decide while the voice keeps talking.** A speech-to-speech model holds the conversation and hands the action to the app. The app asks the decision model to pick from the actions available now (plus `noop`), runs the action, and appends the result.

## Field lessons

- Keep one request in flight, always on the newest input. Drop or coalesce stale increments instead of queueing them.
- Debounce partials (200–350 ms reported), then re-decide on the final segment.
- Use append-only (stable-prefix) ASR. If the transcript can retract, labels flicker.
- Always add a max-hold timeout. A dubbing app capped the hold at 17 s where an LLM approach needed 40 s.
- Ask "addressed to me?", "still continuing?" and "destructive?" on every increment for voice. Partial speech misfires. Treat "still continuing" as a hard veto.
- Require persistence or a margin to commit: two matching checks ≥ 900 ms apart for frames, or a lead of about 0.12 over the runner-up for a Choice.
- Scale thresholds with consequence. Block a pasted credential. Warn on a minor issue.
- End-of-speech detection often costs more than the model call (550 ms vs 170–420 ms on Jev in one Mac app). Never make local, instant results wait for the model.
- Show the live probabilities in the UI (seek-bar painting, a morphing card, a top-3 bar). It makes the uncertainty legible.
- Before acting on a decision, re-check that the action still fits the current state. Speech or the screen may have moved on while the request was in flight.
- Latency, as reported. Vendor numbers are best-case, so measure your own loop. **Jev:** about 100–350 ms per decision, fast enough to re-ask on every word. Dubbing runs about 2¢ per hour of audio. Local small models can be faster, but some cap the context at 2k–8k tokens, which caps the transcript window.
- Not on Jev? Model-specific real-time notes (latency, context windows, local hardware; hosted Clef-flash and some local setups run several times slower than Jev): `models/clef.md`, `models/clm.md`, `models/kev.md`, `models/nimble.md`, `models/strands-decider.md`, `models/others.md` (Liquid d1). Index: `models/INDEX.md`.

## Prior art

- jev-canvas, "make a yellow circle here" while pointing. 9 questions per spoken word, about 350 ms, 200 ms debounce, at most 2 in flight. Ukrainian context in the questions raised recognition from about 12% to 87% (Jev via OpenRouter): [gaborishka/jev-canvas](https://github.com/gaborishka/jev-canvas)
- Jev Voice (Mac mini M4), local whisper.cpp plus one fan-out per command. Reported 550 ms end-of-speech, 170–420 ms decision, and "not sure" below 0.35: [kevinbadi/jev-voice](https://github.com/kevinbadi/jev-voice)
- semantic-live-caption, key-point, emotion, and intent badges on streaming captions. Partials use a 350 ms debounce and a 700 ms gap, and the final call overwrites them. Intent needs 0.55 plus a 0.12 margin: [limboinf/semantic-live-caption](https://github.com/limboinf/semantic-live-caption)

More projects (34 entries), grouped by sub-type (Voice agents and turn-taking, Voice + gesture and webcam frames, Live speech analytics, captions, and audio, Typing and keystroke-driven UI, Other): `prior-art/projects/incremental-realtime.md`.
