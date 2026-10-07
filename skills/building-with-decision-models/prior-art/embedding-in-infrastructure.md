# Shape: Embedding a Decision Model in Existing Infrastructure

**Use when** you want a decision model to feel native inside a host system: SQL, a vector DB, a web framework, CI, an agent framework, a home-automation hub, a browser.

## The shape

Wrap one `system_one` call as the host's own primitive:

| Host | Native primitive | Example |
|---|---|---|
| SQL database | predicate / scalar function | `WHERE jev(row, 'the name is European')` |
| Vector DB / search | reranker class | `TypeSafeReranker` |
| Web framework | router / middleware | the model picks the handler |
| API gateway / proxy | pass-through route | log, cost-track, drift-check, or learn every decision |
| Agent framework | middleware / guardrail hook / block | tool-call gate, model router |
| CI / git | hook / plugin / lint rule | commit, migration, and semantic lint checks |
| Home automation | sensor / automation action / conversation agent | answers as entities |
| Browser | extension content script | per-element or per-post labels |
| Test runner | plugin | test-claim checks |
| Data platform | built-in SQL function | Databricks `ai_decide(state, questions)` |

```python
# Sketch: a SQLite scalar function (per-row call; cache aggressively, filter in SQL first)
import functools, json, sqlite3
from typesafe_sdk import Noul, TypeSafeClient

client = TypeSafeClient()

@functools.lru_cache(maxsize=100_000)
def _jev(row_json: str, predicate: str) -> float:
    r = client.system_one(state={"row": json.loads(row_json)},
                          questions={"p": Noul(instructions=f"Is this true of `row`: {predicate}")})
    return r.nouls["p"].noul

db = sqlite3.connect("app.db")
db.create_function("jev", 2, _jev, deterministic=True)
# SELECT * FROM people WHERE country = 'DE' AND jev(json_object('name', name), 'the name is European') > 0.7
```

## Variants

- **Vendor SQL function.** The platform ships the primitive (Databricks `ai_decide`). No extension to maintain. You lose control of batching and model pinning.
- **Local compatible server.** Point the same client at a local `/v1/systemone` (llama.cpp, Ollama, laya-server, decidealot). The same host code then runs offline. Re-fit thresholds first.
- **Edge binding.** Call the model through the platform binding instead of REST (Cloudflare `env.AI.run` for Clef). No token to manage. The response shape differs from REST.
- **Wrap the endpoint itself.** A proxy in front of `/v1/systemone` adds logging, cost tracking, drift alerts, failover, or a locally trained head with cloud fallback.
- **Pinned router.** Middleware that picks the LLM tier once per conversation, then keeps it to preserve the prompt cache.

## Field lessons

- A per-row call is one HTTP request per row. Filter with ordinary SQL first, cache results, and batch where the host allows it. Batching requests is the big win (pg_typesafe reported 27×: 1,000 rows in 23 s vs 0.86 s).
- Batch questions over one item, not many items into one state, when you will sort by the result. On Jev, packing 40 rows into one state dropped rank correlation from 0.950 to 0.506 ([jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench)).
- Probabilities come back with two decimals, so `ORDER BY p LIMIT k` hits big ties (Jev: 45 distinct values over 360 rows). Add a secondary key: `ORDER BY p DESC, id`.
- Mark the function deterministic only with a pinned model version. The alias moves. Some hosted models answer identical requests differently, so snapshot results to a table and leave a margin around thresholds.
- Store raw probabilities, not verdicts. A threshold change then replays over stored answers with no new inference. Store "not evaluated" explicitly.
- A "compatible" `/v1/systemone` server is not a drop-in swap. For conformance checks (jevcompat), `confidence` and limit differences, and re-fitting thresholds per backend, see `choosing-and-switching-models.md`.
- Vendor endpoints do not share one wire format. **OpenAI Decisions (`gpt-6-luna`):** `POST /v1/decisions` with `input` and a `questions` array, and `predicate` in place of Noul. **pplx-decider:** `POST /v1/decisions` with `state`/`questions`, Bearer auth only, 10 requests/s per org, base64 images only. **Liquid d1:** `/v1/systemone` that the TypeSafe SDK calls unchanged. Keep each vendor behind a thin adapter in one file.
- Edge and local backends rarely hit their advertised latency inside a real host. Cache answers in the host's store and require a margin before acting.
- In any client-side host (browser, mobile), the API key is exposed. Proxy through a server. The JS SDK needs `dangerouslyAllowBrowser` for a reason.
- A router middleware should decide once per conversation and pin the choice. Switching models mid-conversation loses prompt-cache reuse. An explicit user request beats the router.
- In CI, do not send text off-machine on fork PRs, and step aside on checker failure unless strict mode is set (Sniff Test).
- Home automation users push back on cloud round-trips. Offer a local fallback. Suggest through the host's review UI (Home Assistant Repairs) rather than acting.
- The strongest adoption signal is a decision model inside established OSS behind a feature flag or optional provider, not decision-model-first products.
- Not on Jev? Model-specific hosting notes (Workers AI envelope and error 5006, per-question state cost on Ollama, nondeterministic answers, unnamed vendor models): `models/clef.md`, `models/nimble.md`, `models/pplx-decider.md`, `models/others.md` (`ai_decide`). Index: `models/INDEX.md`.

## Prior art

- duckdb-jev: [colliber/duckdb-jev](https://github.com/colliber/duckdb-jev). JevQL: [kylemclaren/jevql](https://github.com/kylemclaren/jevql), [flaviocopes.com](https://flaviocopes.com/jev/). vgi-typesafe: [Query-farm/vgi-typesafe](https://github.com/Query-farm/vgi-typesafe)
- ry, a Workers 404 router: rules and typo fixes first, then Clef picks the target. Redirects at ≥0.7, or ≥0.5 with a 3× lead over the runner-up. Reported 76% fixed without the model, 97% including suggestions, on a 662-page site (Clef): [ygwyg/ry](https://github.com/ygwyg/ry)
- Local `/v1/systemone` servers: llama.cpp llama-server, reported 3–43 ms for 144M–27B models (Laya, Kev, Clef, OpenJev): [HF blog](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp). Ollama 0.35+, 1–64 questions, Score 2–26 levels (Nimble via Ollama): [docs.ollama.com](https://docs.ollama.com/api/systemone). decidealot, one Docker HTTP + MCP service (Laya, Von, CLM, Jev proxy): [psyb0t/decidealot](https://hub.docker.com/r/psyb0t/decidealot). laya-server (Laya): [1Panel-dev/laya-server](https://github.com/1Panel-dev/laya-server)

More projects (53 entries), grouped by sub-type (Databases and search, Frameworks and agent stacks, Vendor decision endpoints, Gateways, proxies, and edge, Products embedding Jev, CI and dev loop, Home and desktop, Ecosystem ports): `prior-art/projects/embedding-in-infrastructure.md`.
