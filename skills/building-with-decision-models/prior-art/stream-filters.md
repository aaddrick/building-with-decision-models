# Shape: Stream Filters and Bulk Labelling

**Use when** you must label, filter, or route every item in a large or endless flow: social posts, emails, logs, rows, comments, DOM elements, headlines, applications.

## The shape

```
for each item (bounded concurrency, about 8 workers):
    one request: several speculative questions about this item
    code: threshold / label / drop / route; store the raw probabilities
```

```python
from concurrent.futures import ThreadPoolExecutor
from typesafe_sdk import Choice, Noul, TypeSafeClient

client = TypeSafeClient()
QUESTIONS = {
    "ai_written": Noul(instructions="Does `post` read as AI-generated filler rather than a person's own words?"),
    "promotional": Noul(instructions="Is `post` primarily promoting a product, service, or the author?"),
    "topic": Choice(instructions="What is `post` mainly about?",
                    criteria={"work": None, "tech": None, "politics": None, "personal": None, "other": None}),
}

def label(post: str) -> dict:
    r = client.system_one(state={"post": post}, questions=QUESTIONS)
    return {"ai": r.nouls["ai_written"].noul, "promo": r.nouls["promotional"].noul,
            "topic": r.choices["topic"].choice, "model": r.model}

with ThreadPoolExecutor(max_workers=8) as pool:
    labels = list(pool.map(label, posts))
hidden = [p for p, l in zip(posts, labels) if max(l["ai"], l["promo"]) > 0.8]
```

## Variants

- **User-tuned weights**: store the raw probabilities and let the user's own labels fit the weights or thresholds (slop-filter).
- **Per-DOM-element**: "is this element an ad?" in a browser extension. Batch many elements per request, one Noul per element, where one page is the state.
- **Log and code grep by meaning**: pre-filter with a regex or line window, then ask per line or chunk.
- **Bulk offline jobs**: resumes, papers, reviews, applications. Cache on (state, questions, model).
- **Periodic feeds**: poll headlines every N minutes and score them.
- **Rules first, model for the rest**: deterministic rules settle the obvious items. Only the ambiguous remainder goes to the model, batched (jev-triage, triagedy).
- **Cheap state first**: ask on metadata or a snippet. Fetch the full item only when confidence is low (jevMail).
- **Gate before an LLM**: drop only the confidently useless records before an expensive LLM step. Errors and uncertain items always pass (jevlogs, jev-sift).
- **SQL-native bulk labelling**: `ai_decide()` per row inside the warehouse, filtered in SQL.
- **Local or offline**: Ollama `/v1/systemone` (Nimble, Tev1) or Ollaya (Decider, Laya) behind the same API shape for private inboxes. Re-fit thresholds per model.

## Field lessons

- About 8 concurrent workers is the practical ceiling on a shared key before 429s. Jev's reported limit is about 1,200 requests/minute (jev-mail).
- Reported Jev costs: about $0.00003 per social post; 500 emails for 3.5¢; about 9¢ per 1,000 emails; about $0.00002 per GitHub issue; 1M log lines for about $10; all of arXiv for $0.06 a day; Twitch chat for about $0.15/hour at 2 msg/s.
- Put many questions in each request. The state (the item) dominates tokens, so extra questions are almost free. Split compound judgments into narrow ones and combine them in code (jev-mail).
- Use two thresholds and a review band. Act only on the confident tails and label the middle "Review" (hush, Jev-Mail, jevMail).
- Destructive actions (archive, delete, hide) need a higher bar than labelling. Fail open on API errors: pause moderation rather than mass-delete (Jev-Moderation-Bot).
- Pin the model version in a filter whose thresholds you tuned (x-scanner). Hosted SQL functions may swap the model under you.
- Rewording the question or its criteria usually beats moving the threshold. Low precision often means a bad label definition, not a bad model (hush).
- Annotating alone saves nothing. The downstream step must actually skip the low-value items (jevlogs).
- Take a hard look at "is this AI-written?" questions. They are vibes-level judgments. Calibrate on your own labels before hiding content.
- For offline bulk work, batched LLM prompts (20 records per call) can match Jev on cost ([HN](https://news.ycombinator.com/item?id=49821799)). Jev wins on latency and per-item isolation.
- Price and latency can rank models differently. Pick per filter: a latency-bound filter and a cost-bound one may want different models.
- A local model removes the per-call cost but usually trails Jev on agreement with human labels. Validate it on your own labels before it hides or deletes anything.
- Test your exact request shape before you swap backends. "Compatible" servers reject fields that others accept.
- Not on Jev? Model-specific filter notes (cost, latency, moderation agreement, zero-shot accuracy, request-shape errors): `models/clef.md`, `models/laya.md`, `models/luna.md`, `models/nimble.md`, `models/strands-decider.md`, `models/others.md` (Tev1, Liquid d1, `ai_decide`). Index: `models/INDEX.md`.

## Prior art

- jevlogs, scores OpenTelemetry logs before LLM analysis, reported 0.84% retained and 87% lower modelled LLM spend (Jev via Vercel AI Gateway): [reachjalil/jevlogs](https://github.com/reachjalil/jevlogs)
- jev-slop-guard, blurs and stamps X/LinkedIn posts above a slider threshold (default 70%), scores each post once: [davertor/jev-slop-guard](https://github.com/davertor/jev-slop-guard)
- Twitch chat filter, reported about $0.15/hour at 2 msg/s with a $0.50/hour spend cap: [ethanplusai/jev-chat-for-twitch](https://github.com/ethanplusai/jev-chat-for-twitch)

More projects (52 entries), grouped by sub-type (Consumer filters (extensions), Moderation and anti-spam, Email, support, CRM, Issues and tickets, Logs, code, security, Bulk business labelling, Feeds): `prior-art/projects/stream-filters.md`.
