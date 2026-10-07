# Provider: Pydantic AI decision models (`DecisionModel`, `SystemOneModel`)

Snapshot 2026-10-06, sources: pydantic.dev/docs/ai/models/decision/, /docs/ai/models/system-one/, /docs/ai/api/models/decision/. The live docs win. /docs/ai/api/models/system-one/ returned 404, so the `SystemOneModel` constructor signature was not captured.

## Backends and model strings

| String | Class | Backend |
|---|---|---|
| `typesafe:jev-latest` | `TypeSafeModel` | TypeSafe Jev |
| `system-one:<model>` | `SystemOneModel` | any server that speaks `POST /v1/systemone` |
| `system-one:nimble`, `system-one:tev1` | `SystemOneModel` | Ollama 0.35.0+ |
| `system-one:clm-latest` | `SystemOneModel` | Contrastive Language Models (self-hosted `clm-serve`, default `http://localhost:8700`, per github.com/Contrastive-LM/CLM) |

The docs also name Laya as reachable over the same API. They give no model string or base URL for it.

`SystemOneModel` needs only `pydantic-ai-slim`. It is configured by `SYSTEM_ONE_BASE_URL` and `SYSTEM_ONE_API_KEY` (optional), or by `SystemOneProvider(base_url=..., api_key=..., http_client=...)`.

Ollama (docs, verbatim):

```bash
ollama pull nimble
export SYSTEM_ONE_BASE_URL='http://localhost:11434'   # no /v1 suffix
```

```python
from typing import Literal
from pydantic_ai import Agent

agent = Agent(
    'system-one:nimble',
    output_type=Literal['billing', 'bug', 'account'],
    instructions='Which label fits this support ticket?',
)
result = agent.run_sync('Our checkout has returned 500 errors since 9am.')
print(result.output)
#> bug
```

## Type → question mapping (decision guide)

| Field type | Question | `output` value |
|---|---|---|
| `bool` | Noul | `True` if P(yes) ≥ `decision_boolean_threshold` |
| `float` bounded 0-1 | Noul | the unrounded probability |
| `Literal` / `Enum` of strings | Choice | the chosen option |
| `IntEnum` (whole numbers ≥ 0) with descriptions | Score | the nearest level. "The ordering is the numbers' own, so the order the levels are declared in does not matter." |
| `list` (or `dict`) of options | one Noul per option | the options answered yes |
| nested model | its fields | |

- `Annotated[bool, BoolCriteria(true=..., false=...)]` sets Noul `criteria`.
- Field descriptions become `instructions`: use `Field(description=...)` or `use_attribute_docstrings=True`. The output type's docstring states the goal.
- `str`, unbounded numbers, and `datetime` cannot be decided. A run with them hands off to a language model through `FallbackModel`, for example `FallbackModel('typesafe:jev-latest', 'anthropic:claude-opus-5-5')`.
- Several output types or tools become a "route" choice. The run's prompt becomes the `text` state, message history becomes `history`, and tool calls and results since the latest prompt become `done`.
- Exceptions: `DecisionHandOff` (base), `UnfillableRoute` (the route has fields a decision model cannot fill), `UnsureRoute` (P(route) fell below `decision_route_threshold`).
- Limits: no text output, no images, audio, video, or documents, no files, and no revised answers on `ModelRetry`.

## Settings

| Setting | Default | Meaning (API docstring) |
|---|---|---|
| `decision_boolean_threshold` | 0.5 | "How likely a yes has to be before a `bool` field is `True`, from 0 to 1." |
| `decision_route_threshold` | unset | "How likely the picked route has to be before it is taken, from 0 to 1. Default: unset, so the pick always is." |

`SystemOneModelSettings` adds `temperature`, `timeout`, `extra_headers`, and `extra_body`. On temperature, the docs say only that where a backend supports it, "it moves every probability a threshold reads".

## Capability limits

- `DecisionModel.max_choice_options`: "The most options the backend accepts in one pick-one question, or `None` for no limit." Default `None`.
- `DecisionModel.max_score_levels`: the same for rubric levels. Default `None`.
- The system-one page names the profile fields `decision_max_choice_options` and `decision_max_score_levels` (on `DecisionModelProfile`). The API page names the model attributes `max_choice_options` and `max_score_levels`. These are probably the profile and model views of the same limit, but no source confirms it.
- Ollama profile: at most **26** options and levels, 64 questions, and 64 KiB requests (system-one page). This conflicts with docs.ollama.com, which lists choice as 2-255 but says the limit "depends on the model".

## Confidence

`result.response.provider_details` holds `confidence` (per field), `probabilities` (Choice distributions), and `scores` (unrounded rubric positions).

```python
print(result.response.provider_details['confidence'])
#> {'area': 1.0, 'urgent': 0.86}
```

This `confidence` is **Pydantic AI's own statistic, not the backend's.** For a yes/no it is "how far the probability of yes sits from the threshold that decided it, scaled to run from 0 at the threshold to 1 at certainty". So it exists for `bool` fields, unlike Jev, which has no Noul `confidence`. A `float` field has no entry: "The probability _is_ its answer".

The docs advise: "Measure accuracy, the hand-off rate and any threshold on labelled examples of your own before relying on them."

## Sources

- https://pydantic.dev/docs/ai/models/system-one/
- https://pydantic.dev/docs/ai/models/decision/
- https://pydantic.dev/docs/ai/api/models/decision/
- https://docs.ollama.com/api/systemone
- https://github.com/Contrastive-LM/CLM
