# Projects: Incremental and Real-Time Decisions

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/incremental-realtime.md`.

### Voice agents and turn-taking

- Real-time dubbing on iPhone ("is this translated sentence complete enough to speak?"), about 0.35 s, about 2¢/hour: [HN](https://news.ycombinator.com/item?id=49814743), [HN](https://news.ycombinator.com/item?id=49814753)
- Voice browser, about 12 questions per spoken word including destructive and addressed-to-me: [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
- OpenAI's voice guide for Decisions. The Live API delegates to the client, so GPT-Live keeps talking while the app calls Decisions over the live transcript. Choices are the currently available actions plus `noop`. Skip the action if the request was cancelled or no longer fits the app state (gpt-6-luna): [developers.openai.com](https://developers.openai.com/api/docs/guides/decisions-voice)
- Voice-controlled Mac computer use: [X](https://x.com/instantricecook/status/2100814590300889426)
- SlidePilot, voice auto-advance for Slidev slides. 4 Nouls per utterance, with "still explaining" as a veto, a 1 s cancellable delay, and a 2 s cooldown: [harshil1712/slidepilot](https://github.com/harshil1712/slidepilot)
- audio-graph proposal (not yet built), semantic end-of-speech gate. VAD proposes a pause and a Noul batch confirms it. Reported 205→304 ms for 1→50 questions, about $0.006 per meeting-hour: [Codeseys-Labs/audio-graph#108](https://github.com/Codeseys-Labs/audio-graph/issues/108)
- Jev Voice (Mac), optional "smart end-of-speech" that asks whether a pause ends the command, with a hard silence cap and policy-driven confirm for delete and pay: [chris-wozniczek/jev-voice-control](https://github.com/chris-wozniczek/jev-voice-control)
- Jev Voice (Mac mini M4), local whisper.cpp plus one fan-out per command. Reported 550 ms end-of-speech, 170–420 ms decision, and "not sure" below 0.35: [kevinbadi/jev-voice](https://github.com/kevinbadi/jev-voice)
- jev-use, macOS voice control over the Accessibility tree, 1.5 s pause to submit, 0.3–1.5 s per step: [savka777/jev-use](https://github.com/savka777/jev-use)
- Windows voice control in Turkish and English, OpenAI Realtime speech plus Jev (via OpenRouter): [mstf-svndk/jev-windows-voice](https://github.com/mstf-svndk/jev-windows-voice)
- Rails engine for voice and typed commands defined in a Ruby DSL: [igorkasyanchuk/voice_control](https://github.com/igorkasyanchuk/voice_control)
- Speech-driven NPC addressee detection: [wondertwins/jev-benchmark](https://github.com/wondertwins/jev-benchmark)
- Home Assistant voice ("cold and dark in here" → lights and heat): [HN](https://news.ycombinator.com/item?id=49851245), [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev)

### Voice + gesture and webcam frames

- jev-canvas, "make a yellow circle here" while pointing. 9 questions per spoken word, about 350 ms, 200 ms debounce, at most 2 in flight. Ukrainian context in the questions raised recognition from about 12% to 87% (Jev via OpenRouter): [gaborishka/jev-canvas](https://github.com/gaborishka/jev-canvas)
- clef-demo webcam mode, one query in flight on the newest frame, live probability bars and an answer-change log, about 5 decisions/s on an RTX 3090 (Clef-flash, local): [tehtommeh/clef-demo](https://github.com/tehtommeh/clef-demo)
- clef-webcam, Mac webcam with custom MPS kernels, 250 ms per frame with 3 questions on an M5 Max vs 840 ms stock (Clef-flash, local): [huntharo/clef-webcam](https://github.com/huntharo/clef-webcam)
- ClefCam, a camera that captures when your rules match. Checks every ~1.5 s, slows down for unchanged scenes, and needs 2 consecutive matches ≥ 900 ms apart (Clef-flash, Workers AI): [tmchow/clefcam](https://github.com/tmchow/clefcam)

### Live speech analytics, captions, and audio

- semantic-live-caption, key-point, emotion, and intent badges on streaming captions. Partials use a 350 ms debounce and a 700 ms gap, and the final call overwrites them. Intent needs 0.55 plus a 0.12 margin: [limboinf/semantic-live-caption](https://github.com/limboinf/semantic-live-caption)
- RealtimeQA, a live call-centre QA scorecard over local streaming ASR. One request in flight, transcript updates coalesced (Nimble 9B via Ollama): [markramn/system-one-decision-models](https://github.com/markramn/system-one-decision-models)
- ReadAloud, word-by-word pronunciation feedback. Only misaligned words from streaming ASR go to the model: [wquguru/dasheng](https://github.com/wquguru/dasheng)
- jevmeter, a "BS meter" on video, every sentence scored. Reported 1,191 calls for $0.05, about 0.4 s median (offline, not live): [ChetasLua/jevmeter](https://github.com/ChetasLua/jevmeter)
- YouTube sponsor skip painting the probability on the seek bar: [valentynkit/jev-skip](https://github.com/valentynkit/jev-skip). Podcast ad removal: [ttlequals0/MinusPodJev](https://github.com/ttlequals0/MinusPodJev) ([flaviocopes.com](https://flaviocopes.com/jev/))
- Sponsor Skip, transcript, smart, or listen-only modes. It asks every few seconds over the last minute of audio and skips at 70–80%. Listening only near suspected reads costs ~$0.05/h vs $0.46/h for listen-only: [trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)
- Real-time audio beeper with ffmpeg: [santos-sanz/jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper)

### Typing and keystroke-driven UI

- Component Charades, Choice re-ranked every 350 ms while typing, commits at 0.85: [southleft/component-charades](https://github.com/southleft/component-charades)
- Shapeshift, one text box that morphs into an event card, checklist, or bill splitter, 14 questions per keystroke batch: [anishfn/shapeshift](https://github.com/anishfn/shapeshift)
- Steve Krouse's typewriter, 16 live Nouls as you type: [typesafe-demo.val.run](https://typesafe-demo.val.run/)
- Compose checker, 5 questions per typed word. `contains_secret` jumped from about 0.2 to 0.98 when a key was pasted, which blocked Send: [jiangyan/jev-demo PR #1](https://github.com/jiangyan/jev-demo/pull/1)
- jevcast, a macOS launcher that asks after each typing pause. Local results never wait for the model: [RyanErkal/jevcast](https://github.com/RyanErkal/jevcast)
- omarchy-mail, a terminal Gmail client that checks replies as you write: [petrzpav/omarchy-mail](https://github.com/petrzpav/omarchy-mail)
- CanvasDesk, planned local autocomplete for a diagram tool because LLM generation (1–3 s) broke typing rhythm, about 33 ms on GPU (Laya): [dev.to](https://dev.to/danku13/how-im-adding-local-ai-autocomplete-to-canvasdesk-laya-system-one-models-and-node-based-31jd)

### Other

- Home network monitoring in real time (the author's early experiment, mentioned in a RuntimeWire article on TypeSafe's valuation): [runtimewire.com](https://runtimewire.com/article/typesafe-investors-discuss-a-higher-valuation-after-jev-reaches-nearly-13-of-one)
- AI video editor, cutting >30 s tool latency (idea): [HN](https://news.ycombinator.com/item?id=49721095)
- For fixed-rate control loops, see `prior-art/projects/control-loops.md`
