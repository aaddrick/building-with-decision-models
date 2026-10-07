# Projects: Select From Candidates

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/select-from-candidates.md`.

**Browser, computer, phone**
- Browser Use "jev-ultrafast": a numbered element table, one Choice = operation + target. Zürich→London flight search in 7.1 s for $0.0039 (via [dev.to](https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e))
- Independent jev-ultrafast review, median 9.45 s → 7.09 s, 1,092 → 101 CDP calls. No shadow roots, iframes, canvas, or uploads: [andrew.ooo](https://andrew.ooo/posts/jev-ultrafast-review-browser-use-typesafe-jev-browser-agent/)
- Browserbase Stagehand `act()` rebuilt on Jev, median 1.97 s → 0.46 s: [langchain.com](https://www.langchain.com/blog/building-prod-with-jev-and-langgraph)
- jev-browser MCP server, one Choice over up to 240 elements plus `goal reached` and `stuck` Nouls. Wikipedia Coffee→Espresso in about 4 s for $0.0016: [jkudish/jev-browser](https://github.com/jkudish/jev-browser)
- jev-browser, the LLM plans and the decision model picks element, action, value and done/blocked/irreversible. 40/42 tasks, 5-step checkout in about 14 s, about 8k vs 557k page tokens for the LLM: [Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser)
- jev-voice-browser, 9–11 questions per partial transcript, with text and URL spans picked from candidates. About 330 ms and $0.0002 per call: [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)
- jev-ego, an element-table agent for the ego lite browser, 0.17–0.27 s per local action: [romaluev/jev-ego](https://github.com/romaluev/jev-ego)
- Mac computer use with OCR, no screenshots, about $0.0002 per step, an LLM only for free text: [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)
- Accessibility-tree browser agent, 10–40 refs per step, 21–23 decisions all correct for about $0.001: [HN](https://news.ycombinator.com/item?id=49758669)
- macOS Accessibility tree, with voice control: [savka777/jev-use](https://github.com/savka777/jev-use). CUA's separate Jev example: [trycua/cua](https://github.com/trycua/cua) `libs/cua-driver/examples/jev-use`
- Windows/Chrome GUI delegate. Code matches first and the model is called only when matching is unsure. About 90% fewer main-model tokens: [YUTA-fywoo/jev-gui-delegate](https://github.com/YUTA-fywoo/jev-gui-delegate)
- Droidrun mobile-jev, 9 Uber actions on a real phone in 21 s: [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev). iOS/Android jev-phone: [HN](https://news.ycombinator.com/item?id=49831841)
- jev-mobile, an Android loop of observe → normalize → decide → mutate → verify. Candidates come in pages of 10, `ESCALATE` is always an option, and each change is checked independently: [friedjof/jev-mobile](https://github.com/friedjof/jev-mobile)
- FluidUse, on-device macOS form filling over the Accessibility API. Each field becomes a typed question with its options. Reported: Laya 3.6 ms median per question, a 706K-parameter form specialist 0.9 ms per decision. It doesn't reason about dropdowns or write free text (Laya, Kev-0.8B, Clef-vision): [FluidInference/FluidUse](https://github.com/FluidInference/FluidUse)
- Rental search across Craigslist, FB Marketplace, Redfin, Zillow: Hearth, [Nancy-Chauhan/hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)
- Distilled form-filler that beats Jev: [HN](https://news.ycombinator.com/item?id=49767564)

**Tool and function calling without an LLM**
- Function-calling cookbook: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/function_calling.md)
- pydantic-ai `DecisionModel`, where tools become a route Choice, `Literal` args Choices and `bool` args Nouls. A `str` arg escalates to a `FallbackModel` (Jev, CLM, Laya, Ollama): [pydantic.dev](https://pydantic.dev/docs/ai/models/decision/)
- jev-gateway, a local gateway in front of coding agents. The model picks the tool or passes the request through. Reported −57% output tokens and −39% time on bug fixes, mixed on feature work: [vinilana/jev-gateway](https://github.com/vinilana/jev-gateway)
- Chat where the model picks the tool and arguments and code builds the reply: [w3cj/jev-chat](https://github.com/w3cj/jev-chat)
- pi-mcp-adapter MCP tool search over 95 tools, expected tool first in 10 of 11 cases vs 5 for text search: [newreleases.io](https://newreleases.io/project/github/nicobailon/pi-mcp-adapter/release/v2.35.0)
- JevRouter, one router over models, subagents, skills, MCP tools and CLIs. Code owns permissions, risk and fallback: [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter)
- OpenClaw decision-model plugin API, about 15 community PRs for tool filtering and model selection (Jev, Kev): [openclaw.ai](https://openclaw.ai/blog/decision-models-in-openclaw)
- WebMCP browser extension: [sdras/jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension)
- jevexpress: Express with no routes, the model picks the handler: [carllippert/jev-router](https://github.com/carllippert/jev-router)
- hono-jev-router, plain-language HTTP routes, one Noul each. First match at ≥0.5 wins, else `notFound()`. Not for auth: [yusukebe/hono-jev-router](https://github.com/yusukebe/hono-jev-router)
- Smart-home demo, speculative fan-out over category/room/device/action: [docs.typesafe.ai](https://docs.typesafe.ai/demos/smart-home.md)

**Extraction by selection**
- Pre-parsed value extraction cookbook: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook.md)
- Date extraction as 7 enumerated Choices: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook.md)
- Line-by-line search, a Choice over line IDs + an `exists` Noul: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/semantic_find.md)

**Routers**
- OpenRouter official "Jev Router" (model + reasoning effort): [openrouter.ai](https://openrouter.ai/typesafe)
- LangChain model-routing middleware: [langchain.com](https://www.langchain.com/blog/building-a-harness-with-jev)
- [jev-router](https://github.com/gargpratyush/jev-router), [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router), [pi-jev-model-router](https://github.com/da-vinci-noob/pi-jev-model-router), [tiershift](https://github.com/iamvatsalpatel/tiershift)
- Jevonian, a local OpenAI/Anthropic-compatible proxy. Config filters first, then one call returns route plus thinking depth: [xinyao27/jevonian](https://github.com/xinyao27/jevonian)
- agent-router, which picks Cursor, Claude Code, Codex or OpenCode plus effort. Quota rules run first: [nidhi-singh02/agent-router](https://github.com/nidhi-singh02/agent-router)
- Janus, which measures the escalation threshold to an LLM fallback. Reported on Banking77: 80.2%, 53% cheaper, 11.6% escalated: [FirasSX914/Janus](https://github.com/FirasSX914/Janus)
- Flash-first cascade arithmetic: escalating 20% saves about 42.5% of input cost, break-even at about 62.5% (Clef-flash, Clef): [rohitai.com](https://rohitai.com/blog/cloudflare-clef-decision-models-agent-routing-workers-ai)
- Skill routers: skill_suggestion cookbook [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/skill_suggestion.md), [jev-skill-suggester](https://github.com/win4r/jev-skill-suggester), [typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router), [skillranker](https://github.com/Dicklesworthstone/skillranker), [tink-route](https://github.com/jon-devlapaz/tink-route)
- jev-agent-skill-router, which returns `route` / `no_skill` / `review` from need, ambiguity and fit Nouls. Reported 68/72 with zero wrong routes and 25% sent to review: [GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)
- Jev-pilot, Claude Code effort/model/skill per prompt: [HN](https://news.ycombinator.com/item?id=49837537)
- OpenCode agent router for subagents: [HN](https://news.ycombinator.com/item?id=49822796)

**Benchmarks and model notes**
- Clef launch post: BFCL 98.47 vs Jev 95.75, When2Call 72.37 vs 80.97, image input, Jev-API compatible (Clef): [blog.cloudflare.com](https://blog.cloudflare.com/clef-decision-models/). Clef-flash at 38.8 ms (Clef-flash): [ai-tldr.dev](https://ai-tldr.dev/models/clef/). Laya at BFCL 38.13, press-reported (Laya): [pasqualepillitteri.it](https://pasqualepillitteri.it/es/news/19915/cloudflare-clef-desafia-jev)
- CLM-8B: tool calling 95.2% vs 99.2% for Jev, WikiRacing 26/30 vs 30/30. Caching cut median latency from 2.0 ms to 0.7 ms on fixed candidates (CLM-8B): [xenospectrum.com](https://xenospectrum.com/en/clm-8b-decision-cache-benchmark/), [cryptobriefing.com](https://cryptobriefing.com/stanford-nvidia-clm-8b-faster-than-jev/)
- Clef vs Jev user test on review routing: recall 0.98 vs 1.00, hosted p50 about 850 ms vs about 110 ms, Clef-flash over-escalates (Clef, Clef-flash): [HN](https://news.ycombinator.com/item?id=49928781)
- Strands Decider 2B, a pointer head that scores the supplied options. Stated uses are tool routing and action review, about 72% on JevBench v19 at 106 ms (Strands Decider 2B): [fourweekmba.com](https://fourweekmba.com/ai-strands-decider-2b-amazon-removes-lm-head/), [aiweekly.co](https://aiweekly.co/fr/alerts/aws-strands-labs-ouvre-strands-decider-2b-72-sur-jevbench-en-106-ms-de-latence). Per its model card, it struggles with multi-step reasoning and long documents (Strands Decider 2B): [huggingface.co](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19). Reported 3.8 s on long inputs. The model "does not make the final business decision"; code does: [xenospectrum.com](https://xenospectrum.com/en/aws-strands-decider-local-decision-model/)
- pplx-decider-v1-27b, open weights with an `/v1/decisions` API. Accepts images (`images=["screenshot.png"]`) and has a 262k context. Reported 85.71% vs Jev 84.51% on an 11-test panel. Needs about 49 GiB of GPU memory locally (pplx-decider): [explainx.ai](https://explainx.ai/blog/perplexity-pplx-decider-decisions-api-2026), [huggingface.co](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b)
- decider-2b, `/v1/systemone`-compatible, 2–255 options, 3.2 ms per request. Reported 90.3% sampled success on live browser tasks, but only 22 text click tasks and still overconfident on hard items (decider-2b): [huggingface.co](https://huggingface.co/Mapika/decider-2b). A vision variant takes images and game frames (decider-2b-vision): [huggingface.co](https://huggingface.co/Mapika/decider-2b-vision)
- Liquid d1, text plus up to 8 images at `/decisions/v1/systemone`, 200–300 ms on text. Web automation and agent decisions are among its stated uses (Liquid d1): [liquid.ai](https://www.liquid.ai/blog/d1-decision-model), [docs.liquid.ai](https://docs.liquid.ai/lfm/models/decision-models)
- Tev1-4B: 2–24 options, returns a single letter, 88% on its dev set (Tev1): [featherless.ai](https://featherless.ai/models/togethercomputer/Tev1-4B-experimental)
- Ollama `/v1/systemone`: Nimble at 91 ms on an M5 Max, 74.8% macro vs Jev 76.0% (Nimble via Ollama): [runtimewire.com](https://runtimewire.com/article/ollama-local-decision-models-systemone)
- OpenAI Decisions API preview: one answer from a fixed set, text or image context, "choose the next action an AI agent should take" (GPT-6 Luna): [alphasignal.ai](https://alphasignal.ai/news/openai-s-decisions-api-gives-developers-a-constrained-gpt-6-luna-router). The public beta docs show probability maps for choices and levels, and one probability for a predicate. Images go in as base64 data URLs only. OpenAI says to use function calling, not this API, when tool arguments are needed (GPT-6 Luna): [developers.openai.com](https://developers.openai.com/api/docs/guides/decisions)
- Databricks `ai_decide()`: Choice takes 1–255 labels and returns the full probability map (ai_decide): [docs.databricks.com](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_decide)
- "Jev in the Wild", a study of 2,170 GitHub projects. Routing and interface agents are 19.6% of projects but hold 63% of stars: [arxiv.org](https://arxiv.org/pdf/2609.30216)
