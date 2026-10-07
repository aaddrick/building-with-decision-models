# Projects: Control Loops

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/control-loops.md`.

**Games**
- Doom from text state, about 10 Hz, about $7/hour: TypeSafe launch post [typesafe.ai](https://typesafe.ai/blog/introducing-system-one-models-and-jev). Kevin Madura's ViZDoom version, with separate navigation (5 decisions/s) and combat (12 decisions/s) channels: [mattpaige68.substack.com](https://mattpaige68.substack.com/p/a-new-ai-model-just-launched-that)
- Wikiracing: link Choice, with a Score pre-rank when there are more than 255 links (same launch post).
- StarCraft 1998 shareware, mouse/keyboard harness, beat mission 1 in 421 decisions: [phyous/tsai-sc](https://github.com/phyous/tsai-sc)
- StarCraft II "JEV-Star": [HN](https://news.ycombinator.com/item?id=49834465)
- Civilization II in a browser harness: [phyous/tsai-civ2](https://github.com/phyous/tsai-civ2)
- Super Mario Bros, RAM to object JSON, a Choice over 7 NES inputs: [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario)
- Pokémon Red, goal Choice + A*, 4 badges for under $0.50: [milanboers/jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon), [HN](https://news.ycombinator.com/item?id=49845172)
- Minecraft, Mineflayer, objective ladder, 5–30 legal actions per tick: [Anahadd/jev-minecraft](https://github.com/Anahadd/jev-minecraft). It learned to flee zombies unprompted: [mindstudio.ai](https://www.mindstudio.ai/blog/jev-system-one-model-launch)
- Minecraft dragon kill with an LLM + Jev pair: [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent)
- Craftax, LLM planner + Jev macro-options, 5-agent comparison: [mansicer/jev-plays](https://github.com/mansicer/jev-plays)
- WoW TBC levelling, tutor → student distillation: [chalkychalk42/jev](https://github.com/chalkychalk42/jev)
- Clash Royale, card + placement: [vishxrad/clashroyale-jev](https://github.com/vishxrad/clashroyale-jev)
- Pong vs. LLMs: [runtimewire.com](https://runtimewire.com/article/diogo-almeida-typesafe-jev-40m-seed-pong)
- Snake and a fighting arena, Jev vs. the open Laya model: [PromptEngineer48/laya-vs-jev-arena](https://github.com/PromptEngineer48/laya-vs-jev-arena)
- Connect Four with nine query strategies over about 1,800 games. Engine-annotated state went 94-4-1: [hazlema/jev-connect4](https://github.com/hazlema/jev-connect4)
- Snake from 9 parallel hazard Nouls per tick, 29 foods in 461 ticks: [siroccomask/snake-jev](https://github.com/siroccomask/snake-jev). Snake where code blocks illegal moves: [sorrycc/typesafe-snake](https://github.com/sorrycc/typesafe-snake)
- 2048, a Choice over four directions with toggleable context layers and a Laya adapter: [ARCJ137442/jev-2048](https://github.com/ARCJ137442/jev-2048)
- Stealth game guards, 4 batched questions per guard. Stale revisions are rejected. 259.9 ms median, 0 fallbacks over 288 judgments: [AbdelStark/heist-one](https://github.com/AbdelStark/heist-one)
- Browser Doom with tactical macros and honest FALLBACK labels: [lukaske/jev-doom-agent](https://github.com/lukaske/jev-doom-agent)
- 1v1 browser shooter, configured ~9 Hz: [emrickgarrett/OneVOneJev](https://github.com/emrickgarrett/OneVOneJev)
- T-Rex runner race, Jev vs. a local MLX model: [virajbhartiya/laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev)
- Pac-Man race over a pruned route menu (Jev vs. Laya): [MaryNfs/pacman-ai-race](https://github.com/MaryNfs/pacman-ai-race)
- T-Rex, Super Mario and WikiRacing benchmarks: 16.5 ms vs. 149.8 ms on T-Rex, but 26/30 vs. 30/30 on WikiRacing (CLM-8B vs. Jev): [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM), [xenospectrum.com](https://xenospectrum.com/en/clm-8b-decision-cache-benchmark/)
- NES agent for Super Mario and Final Fantasy with GoalSelector menus. ~400 ms per decision, 0 off-menu answers in 900 (SemIf + Qwen3.5-4B): [ArturSkowronski/kNES](https://github.com/ArturSkowronski/kNES)
- Snake on a laptop at 75.40 moves/s over 2,400 moves, 0 deaths, 2 safety interventions (Laya via MLX): [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx)
- Ten browser games from raw pixels at 43 ms/move, 0.57 of the gap from random to the teacher policy (Qwen3.5-0.8B fine-tune): [OmniJev/PlayJev](https://github.com/OmniJev/PlayJev)
- Chess (failure case): [dperezcabrera/system-one-chess](https://github.com/dperezcabrera/system-one-chess), [HN](https://news.ycombinator.com/item?id=49746967)

**Robots, vehicles, simulations**
- Camera-only drone in MuJoCo, CV state → manoeuvre Choice + risk Score + "target lost" Noul at about 2.5 Hz: [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone)
- Franka arm from plain-English goals: [TarunTomar122/jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm)
- MuJoCo robot workbench, Jev vs. MiniCPM: [FBddcz/embodied-jev](https://github.com/FBddcz/embodied-jev)
- Three.js driving from path, traffic, and signal tables: [standardagents/jevpilot](https://github.com/standardagents/jevpilot). A 2D browser car sim that asks 4 questions every 200 ms: [vinilana/live-jev](https://github.com/vinilana/live-jev)
- Four-camera car with radar and blind-spot inputs: [kavehmz/typesafe-playground](https://github.com/kavehmz/typesafe-playground)
- Fixed-wing landing in JSBSim. Jev scored 56/100 vs. 69.9 for a baseline; GPT-6 controllers scored 0–49: [AlperKartkaya/FlightBench](https://github.com/AlperKartkaya/FlightBench)
- Browser driving game. Florence-2 captions frames locally. 151/156 expected calls, ~330 ms median: [reinhard-z/vision-jev](https://github.com/reinhard-z/vision-jev)
- Simulated PiPER arm choosing among 10 skills. 32.6 ms median, 10/10 seeds (decider-2b): [Hu-xiao-max/jev_robot](https://github.com/Hu-xiao-max/jev_robot)
- 1–15 drones with an advisory GLM planner, ~$0.0012 per decision: [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab)
- Franka in MuJoCo with an intent Choice, then axis and gripper Choices: [lykycy123/RoboJEV](https://github.com/lykycy123/RoboJEV). LIBERO manipulation tasks: [Dimweaker/jev-libero](https://github.com/Dimweaker/jev-libero)
- Real SO-101 arm workbench with bounded joint steps and a spend cap: [grmkris/robo-harness](https://github.com/grmkris/robo-harness). Real SO-101 ball-to-bowl at ~2 decisions/s: [hermes-ai.net](https://hermes-ai.net/es/jev/case/2100851116498186415/)
- Warehouse fleet triage, $24.57 per million decisions. Self-hosted ModernBERT was cheaper above ~977K/month: [robokrunch/jev-physical-ai](https://raw.githubusercontent.com/robokrunch/jev-physical-ai/main/README.md)
- Citywide traffic signal policy (Chicago): [skcache/jevtrafficsim](https://github.com/skcache/jevtrafficsim)
- Air traffic approach control: [HN](https://news.ycombinator.com/item?id=49829999)
- Rain nowcasting from radar vectors (App Store): [HN](https://news.ycombinator.com/item?id=49847565)

**Markets**
- On-chain market maker, one decision per Monad block, post-only orders: [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)
- Hyperliquid, five sleeves, long/short then open/close/hold: [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade)
- Six-judgment microstructure policy (regime, direction, toxic flow, liquidity stress, quote environment, inventory): [buberlo/jev-trader](https://github.com/buberlo/jev-trader)
- Self-rewriting Binance bot. Qwen rewrites the rules every 30 minutes, champion vs. challenger: [learnwithmeai.com](https://www.learnwithmeai.com/p/jev-trading-bot)
- Polymarket 5-minute BTC UP/DOWN/abstain: [VGabriel45/polymarket-btc5m-jev-trading](https://github.com/VGabriel45/polymarket-btc5m-jev-trading)
- O'Neil momentum backtest. Code owns stops and risk: [michaelpersonal/jev-trade-cc](https://github.com/michaelpersonal/jev-trade-cc)
- Three paper-by-default OKX bots behind a risk layer, $2/day model spend cap: [imikerussell/beebots](https://github.com/imikerussell/beebots)
- 24/7 market-making design with hard vetoes and a fallback ladder for a late answer: [youmind.com](https://youmind.com/landing/x-viral-articles/jev-hft-trading-system). Claude designs the strategy, Jev executes it: [youmind.com](https://youmind.com/landing/x-viral-articles/opus-jev-trading-bot)
- Survey of finance projects: [gist.github.com](https://gist.github.com/drillan/6916b16e8ea31a8ec36c8f59d6483150)

**Devices**
- Android over ADB, observe → decide → act → verify: [Friedjof/jev-mobile](https://github.com/Friedjof/jev-mobile). Real Android via the Mobilerun API, 9 Uber actions in ~21 s, verifies device state instead of trusting DONE: [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev). An a11y-tree Choice per step with a vision fallback after 3 stalled steps: [xinwang-nwpu/jev-mobile](https://github.com/xinwang-nwpu/jev-mobile). For computer and browser loops, see `prior-art/projects/select-from-candidates.md`.
