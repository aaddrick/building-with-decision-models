<p align="center">
  <strong>Building with Decision Models</strong><br>
  <em>Typed decisions with calibrated confidence, for your coding agent.</em><br>
  <em>Jev, Clef, pplx-decider, ai_decide, Ollama, and more. 450+ linked projects, sorted by shape.</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/aaddrick/building-with-decision-models?style=flat" alt="License"></a>
  <a href=".github/workflows/checks.yml"><img src="https://img.shields.io/github/actions/workflow/status/aaddrick/building-with-decision-models/checks.yml?label=checks&style=flat" alt="Checks"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aaddrick/">Connect on LinkedIn!</a>
</p>

<p align="center">
  <strong>English</strong> ·
  <a href=".github/readme/README.zh-CN.md">简体中文</a> ·
  <a href=".github/readme/README.ja.md">日本語</a> ·
  <a href=".github/readme/README.ko.md">한국어</a> ·
  <a href=".github/readme/README.vi.md">Tiếng Việt</a> ·
  <a href=".github/readme/README.pt-BR.md">Português (BR)</a> ·
  <a href=".github/readme/README.it.md">Italiano</a>
</p>

> [!NOTE]
> This is an unofficial, community skill. It is not made, reviewed, or endorsed by TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, AWS, Ollama, or any other provider it covers. See [How this relates to the official TypeSafe skill](#how-this-relates-to-the-official-typesafe-skill).

Coding agents treat decision models like one more chat model. This skill teaches them to design for them: typed questions, calibrated confidence, the differences between providers, and links to 450+ community projects, sorted by how they work, with a code sketch for each pattern. It installs in Claude Code, Codex, Antigravity CLI, Muse, and Muse Code.

A decision model, also called a [System One](https://docs.typesafe.ai/concepts/system-one) model, does not write text. You send it content and a set of typed questions, and it answers each one with a value and a probability, usually in a few hundred milliseconds or less:

- **Choice** picks one option from a list. Example: route a ticket to billing, shipping, or support.
- **Score** places the content on a scale you describe. Example: grade a pull request from "ignores the spec" to "meets the spec".
- **Noul** gives the probability that a yes/no statement is true. Example: "this shell command deletes files outside the project."

TypeSafe's [Jev](https://docs.typesafe.ai/introduction) started the category on 2026-09-15. Within three weeks, others shipped models that use the same three question types:

| Kind | Models | How you call it |
|---|---|---|
| Hosted | TypeSafe Jev, Cloudflare Clef and Clef-flash, Perplexity pplx-decider, OpenAI Decisions API (`gpt-6-luna`), System1 Models, Strom | HTTP API, each with its own key |
| In your data warehouse | Databricks `ai_decide()` | SQL function or REST |
| On your machine | Nimble and Tev1 through Ollama, Kev, Laya, Strands Decider, CLM-8B | Local server, no key |
| Through one gateway | OpenRouter, Vercel AI Gateway, LLM Gateway, Pydantic AI | One key or one client for several models |

They share ideas, not always a wire format, and not their accuracy. The skill gives the agent the shared rules, a reference file per provider, and the field evidence on which model did well at what.

## Install

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add aaddrick/building-with-decision-models
```

```bash
claude plugin install building-with-decision-models@building-with-decision-models
```

The skill loads on its own when you work on decision-model code. To load it by hand, type:

```
/building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Claude Desktop, Cowork, and claude.ai</strong></summary>

**Step 1.** Open **Customize > Plugins**, select **Add**, then **Add marketplace**.

<img src=".github/assets/plugin-marketplace/step-1.png" alt="The Plugins page in Customize with the Add menu open. An amber box and arrow point at Add marketplace." width="100%">

**Step 2.** Choose **Add from a repository**.

<img src=".github/assets/plugin-marketplace/step-2.png" alt="The Add marketplace dialog. An amber box and arrow point at Add from a repository." width="100%">

**Step 3.** Enter `aaddrick/building-with-decision-models` or the full GitHub URL, then select **Sync**. If the dialog shows **Sync automatically**, leave it on so the plugin updates when this repository does.

<img src=".github/assets/plugin-marketplace/step-3.png" alt="The Add marketplace dialog with https://github.com/aaddrick/building-with-decision-models in the URL field. An amber box and arrow point at the URL field and the Sync button." width="100%">

**Step 4.** Select **Add** next to **Building with decision models**.

<img src=".github/assets/plugin-marketplace/step-4.png" alt="The Discover list showing Building with decision models. An amber box and arrow point at its Add button." width="100%">

**Step 5.** The button changes to **Added**, and the listing shows the version. The plugin also appears in the desktop app and Cowork on the same account.

<img src=".github/assets/plugin-marketplace/step-5.png" alt="The Discover list showing Building with decision models v0.1.0 with an Added button. An amber box and arrow point at Added." width="100%">

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add aaddrick/building-with-decision-models
```

```bash
codex plugin add building-with-decision-models@building-with-decision-models
```

Start a new thread. Codex loads the skill when the task matches. To load it by hand, type:

```
$building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Antigravity CLI</strong></summary>

```bash
agy plugin install https://github.com/aaddrick/building-with-decision-models
```

Check that it installed:

```bash
agy plugin list
```

Start a new session. Antigravity CLI loads the skill when the task matches. To load it by hand, type:

```
/building-with-decision-models:building-with-decision-models
```

Coming from Gemini CLI? If `agy plugin import gemini` brought this extension over, run the install command above anyway so the current copy replaces the imported one.

</details>

<details>
<summary><strong>Muse (muse.ai)</strong></summary>

Muse loads skills from `~/workspace/skills/` on its own computer. Paste this command into a Muse chat and ask Muse to run it:

```bash
curl -fsSL https://raw.githubusercontent.com/aaddrick/building-with-decision-models/main/scripts/install_muse.sh | bash
```

The script copies the skill folder there and rewrites the `SKILL.md` header into the shape Muse reads. Start a new chat. Muse loads the skill when the task matches. To update, run the command again.

</details>

<details>
<summary><strong>Muse Code</strong></summary>

Clone the repository:

```bash
git clone https://github.com/aaddrick/building-with-decision-models.git
```

Install the skill for every project:

```bash
muse skills install building-with-decision-models/skills/building-with-decision-models --scope user
```

Check that it installed:

```bash
muse skills list
```

Start a new session. Muse Code loads the skill when the task matches. To load it by hand, type:

```
/building-with-decision-models
```

</details>

<details>
<summary><strong>Any other agent that reads SKILL.md</strong></summary>

Copy the `skills/building-with-decision-models/` folder into your agent's skills folder. Keep the whole folder. `SKILL.md` links to the files beside it.

</details>


## Connect a model (optional, recommended)

The skill works without any model connected. With one, the agent can check its design against a real endpoint before the code reaches your project. That catches wrong field names, and questions the model reads differently than you meant.

<details>
<summary><strong>Local, free, no key</strong> (Ollama)</summary>

<br>

Install [Ollama](https://ollama.com/download) 0.35 or newer, then pull a decision model:

```bash
ollama pull nimble
```

Check that the agent can reach it:

```bash
curl -s http://localhost:11434/api/version
```

A local model checks the request shape for free. Its accuracy and calibration are not those of a hosted model, so the skill tells the agent not to copy thresholds between them.

</details>

<details>
<summary><strong>Hosted: which key goes in which variable</strong></summary>

<br>

| Provider | Variable | Get a key |
|---|---|---|
| TypeSafe Jev | `TYPESAFE_API_KEY` | [console.typesafe.ai](https://console.typesafe.ai/) (steps below) |
| Cloudflare Clef | `CLOUDFLARE_AUTH_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` | Cloudflare dashboard, Workers AI |
| Perplexity pplx-decider | `PERPLEXITY_API_KEY` | Perplexity API settings |
| OpenAI Decisions API | `OPENAI_API_KEY` | OpenAI platform |
| System1 Models | `SYSTEM1_API_KEY` | system1models.ai |
| Strom (Uprelic) | `UPRELIC_API_KEY` | platform.uprelic.com |
| OpenRouter | `OPENROUTER_API_KEY` | openrouter.ai |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | Vercel dashboard |
| LLM Gateway | `LLM_GATEWAY_API_KEY` | llmgateway.io |
| Databricks `ai_decide` | Your workspace credentials | Databricks workspace (a SQL warehouse needs no key in the agent's shell) |

Each provider file in `skills/building-with-decision-models/providers/` names its variable and how to call it. Store the keys the way the next section shows.

</details>

<details>
<summary><strong>Create, store, and troubleshoot a key</strong></summary>

<br>

<details>
<summary><strong>Example: create a TypeSafe key</strong> (four steps in the TypeSafe console)</summary>

**Step 1.** Sign in at [console.typesafe.ai](https://console.typesafe.ai/) and open **API Keys** in the sidebar.

<img src=".github/assets/api-key/step-1.png" alt="The TypeSafe console home page. An amber box and arrow point at API Keys in the left sidebar." width="100%">

**Step 2.** Click **Create key** at the top right.

<img src=".github/assets/api-key/step-2.png" alt="The API keys page. Existing keys are blurred. An amber box and arrow point at the Create key button at the top right." width="100%">

**Step 3.** Name the key after where it will live, such as the machine or the agent. Then click **Create key**.

<img src=".github/assets/api-key/step-3.png" alt="The Create API key dialog with the name my-coding-agent typed in. An amber box and arrow point at the name field and the Create key button." width="100%">

**Step 4.** Copy the key now. The console shows it once. If you lose it, create a new one and revoke the old one.

<img src=".github/assets/api-key/step-4.png" alt="The API key created dialog. The key value is masked. An amber box and arrow point at the Copy button." width="100%">

</details>

<details>
<summary><strong>Store the key</strong> (macOS, Linux, Windows)</summary>

Keep your keys in one file, readable only by you, with one `export` line per provider. The commands below use `TYPESAFE_API_KEY` as the example. For another provider, use its variable from the table above, and add a line to the same file instead of creating a new one. Agents often start shells without a terminal, so each section puts the keys where those shells can see them. Pick your system.

<details>
<summary><strong>macOS</strong> (zsh, the default shell)</summary>

Save the key to a private file:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Load it from `~/.zshenv`. Every zsh reads that file, including shells that agents start without a terminal. `~/.zshrc` is read only by interactive shells.

```bash
echo '[ -f ~/.config/decision-models/env ] && . ~/.config/decision-models/env' >> ~/.zshenv
```

Open a new terminal and check it. The command prints the length of the key, not the key:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux with bash</strong> (Ubuntu, Debian, Mint, Fedora, Arch)</summary>

Save the key to a private file:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Load it from the **top** of `~/.bashrc`. Ubuntu, Debian, Mint, and Arch start `~/.bashrc` with a line that stops early when no terminal is attached. A line below that guard never runs for agent shells. The top of the file is safe on every distribution:

```bash
sed -i '1i [ -f ~/.config/decision-models/env ] \&\& . ~/.config/decision-models/env' ~/.bashrc
```

Open a new terminal and check it:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux with zsh</strong></summary>

Follow the macOS steps. zsh reads `~/.zshenv` the same way on Linux.

</details>

<details>
<summary><strong>Linux with fish</strong></summary>

fish reads every file in `~/.config/fish/conf.d/`, with or without a terminal:

```fish
mkdir -p ~/.config/fish/conf.d; and echo 'set -gx TYPESAFE_API_KEY YOUR_KEY' >> ~/.config/fish/conf.d/decision-models.fish; and chmod 600 ~/.config/fish/conf.d/decision-models.fish
```

```fish
string length -- $TYPESAFE_API_KEY
```

</details>

<details>
<summary><strong>Windows</strong> (PowerShell)</summary>

Store the key as a user environment variable. New terminals and apps see it. Terminals that are already open do not:

```powershell
[Environment]::SetEnvironmentVariable('TYPESAFE_API_KEY', 'YOUR_KEY', 'User')
```

Open a new terminal and check it:

```powershell
$env:TYPESAFE_API_KEY.Length
```

**WSL:** Windows variables do not reach WSL by default. Inside WSL, follow the Linux with bash steps.

</details>

<details>
<summary><strong>Desktop apps and IDE extensions</strong></summary>

An app you start from the dock, the start menu, or a desktop launcher does not read your shell files.

- **Windows:** the user environment variable above already covers these apps.
- **Linux (systemd):** add the line `TYPESAFE_API_KEY=YOUR_KEY` to `~/.config/environment.d/decision-models.conf`, then log out and back in.
- **macOS:** start the app from a terminal, or set the variable in the app's own settings. macOS has no simple per-user file that desktop apps read.

</details>

</details>

<details>
<summary><strong>If the agent cannot see the key</strong></summary>

Ask the agent to run `echo ${#TYPESAFE_API_KEY}` (or `$env:TYPESAFE_API_KEY.Length` on Windows), with your provider's variable in place of `TYPESAFE_API_KEY`. If it prints `0` or nothing, check these in order:

- **You started the agent before you stored the key.** Agent shells copy the environment of the program that started them. Quit the agent and start it from a new terminal.
- **You started the agent from the dock, the start menu, or an IDE.** Those apps do not read your shell files. See "Desktop apps and IDE extensions" above.
- **Codex filters the environment.** If `~/.codex/config.toml` sets `include_only` under `[shell_environment_policy]`, add your variable to it. If it sets `ignore_default_excludes = false`, Codex drops every variable with `KEY` or `TOKEN` in its name. Remove that line.
- **WSL.** Windows variables do not reach WSL. Store the key inside WSL with the Linux steps.

</details>

</details>

## What is inside

The skill loads in layers, so the agent reads only what the task needs.

| File | What it holds | When the agent reads it |
|---|---|---|
| `SKILL.md` | Which provider and primitive to pick, 11 design rules, how to use probabilities and confidence, how to change models safely, common mistakes | Every decision-model task |
| `providers/jev.md` | The reference `/v1/systemone` contract: HTTP API, Python and JavaScript SDKs, limits, errors, environment variables | When it writes the code |
| `providers/*.md` | 10 provider files (Clef, Perplexity, OpenAI, Databricks, Ollama and Kev, EU hosts, gateways, Pydantic AI, open-weight models): how each differs from Jev, with sources | When it targets that provider |
| `models/*.md` | 9 model files (Clef, Nimble, Laya, Kev, CLM-8B, pplx-decider, GPT-6 Luna, Strands Decider, and the rest) plus an index: the limits people hit, calibration, where each model does well and fails, and notes per shape | When it runs on a model other than Jev |
| `patterns.md` | The 4 official patterns and techniques from 18 cookbooks, with their thresholds | When it designs a workflow |
| `choosing-and-switching-models.md` | How to compare models, re-fit thresholds, shadow, and switch, with the lessons from people who switched and the benchmarks that exist | When it picks, compares, or changes a model |
| `prior-art/INDEX.md` | A map from "what I want to build" to a shape, plus one-line headlines of ideas that failed on any model | Before it designs something new |
| `prior-art/bad-fits.md` | Every idea that failed on any model, with the evidence and links. Failures on one model are in its `models/` file | When a design looks like a known bad fit |
| `prior-art/*.md` | 12 shape files: a code sketch, field lessons that hold for any model, and two or three flagship projects, each tagged with its model | One or two per design |
| `prior-art/projects/*.md` | The full linked project list for each shape, grouped by sub-type, each tagged with its model | When it needs more examples |
| `prior-art/more-indexes.md` | Bigger outside catalogs of decision-model projects and benchmarks | When the library has no match |

## The prior-art library

Most catalogs sort projects by industry. This library sorts them by implementation shape. A game bot, a drone, and a trading bot share one shape: a control loop. Sorted that way, the three share one code sketch and one set of field lessons. Every entry names the model it ran on, so a lesson learned on Laya is not mistaken for one learned on Jev. The 12 shapes:

- **[Control loops](skills/building-with-decision-models/prior-art/control-loops.md)**: games, drones, robots, markets.
- **[Select from candidates](skills/building-with-decision-models/prior-art/select-from-candidates.md)**: browser and phone agents, tool calling without an LLM, extraction, routers.
- **[Gates](skills/building-with-decision-models/prior-art/gates.md)**: tool-call approval, "done" checks, CI, money, content.
- **[Stream filters](skills/building-with-decision-models/prior-art/stream-filters.md)**: slop filters, moderation, email, logs, bulk labels.
- **[Ranking and matching](skills/building-with-decision-models/prior-art/ranking-and-matching.md)**: rerankers, entity matching, graph and taxonomy walks.
- **[Judges and evals](skills/building-with-decision-models/prior-art/judges-and-evals.md)**: rubric judges, trace grading, code review as triage, benchmarks of the models themselves.
- **[Incremental and real-time](skills/building-with-decision-models/prior-art/incremental-realtime.md)**: dubbing, voice, webcam, keystroke-driven interfaces.
- **[Agent context and memory](skills/building-with-decision-models/prior-art/agent-context-memory.md)**: compaction, memory gates, stop and ask decisions, effort control.
- **[Pairing with an LLM](skills/building-with-decision-models/prior-art/llm-pairing.md)**: planner and actor, verify-then-escalate, model-tier routing, distillation.
- **[Answers as data](skills/building-with-decision-models/prior-art/research-and-features.md)**: features for classical models, research instruments, analytics columns, benchmarks.
- **[Embedding in infrastructure](skills/building-with-decision-models/prior-art/embedding-in-infrastructure.md)**: SQL functions, gateways, MCP servers, CI hooks, Home Assistant.
- **[Images and other non-text input](skills/building-with-decision-models/prior-art/images-and-multimodal.md)**: screenshot gates, image moderation, webcam loops, documents.

Two guides sit beside the library: [patterns](skills/building-with-decision-models/patterns.md) for the official patterns and cookbook thresholds, and [choosing and switching models](skills/building-with-decision-models/choosing-and-switching-models.md) for benchmarks, compatibility, head-to-head results, and moving to a new provider without breaking thresholds.

The index also lists, one line each, the ideas that failed in the field on decision models in general: chess, final judgment on math or code, many labels when you already have training data, and calibration taken on trust. Failures on one model, such as zero-shot Laya or hosted Clef-flash in tight loops, are in that model's file in `models/`. A failed attempt saves the next builder from repeating it.

## How this relates to the official TypeSafe skill

TypeSafe publishes its own skill at [typesafe-ai/skills](https://github.com/typesafe-ai/skills). It is one file of design guidance for Jev. For API details, it sends the agent to the live docs on every task. The two skills have different names and do not conflict, so you can install both.

This skill covers every decision model, not only Jev. It holds more inside the skill itself: exact API shapes and the differences between providers, cookbook thresholds, community failure modes, and the prior-art library. The agent can design without a network round trip and see what others built first.

Decision models change fast, and new ones arrive every week. The skill is a snapshot of the providers' docs and the community on 2026-10-06, and it tells the agent a provider's live docs win on any conflict. If a fact is wrong, please open an issue with a link to the source.

## Credits

The facts about each API come from that provider's public documentation: TypeSafe AI's docs and cookbooks, Cloudflare, Perplexity, OpenAI, Databricks, Ollama, System1 Models, Uprelic, OpenRouter, Vercel, LLM Gateway, Pydantic, and the open-model READMEs. The prior art comes from the builders who published their projects, from the Hacker News community, and from these indexes: [awesome-jev](https://github.com/yibie/awesome-jev), [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe), [JevDirectory](https://www.jevdirectory.org/resources), [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases), [awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev), [amplifying.ai](https://amplifying.ai/decision-models), and [BenchLM](https://benchlm.ai/decision-models). Each shape file links to the original projects.

TypeSafe, Jev, and System One are names of TypeSafe AI. Clef and Workers AI belong to Cloudflare, pplx-decider to Perplexity, and every other model name to its maker. This project uses them only to say what the skill is for.

## License

MIT. See [LICENSE](./LICENSE).
