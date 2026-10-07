# Shape: Ranking, Matching, and Walking

**Use when** you must order candidates, decide whether two records are the same, or navigate a graph or taxonomy.

## The shapes

**Rerank**: retrieve a shortlist in code (BM25, vectors), then ask a Noul per (query, candidate) and sort by `.noul`. The same value also prunes: drop anything below a threshold.

**Match / dedupe**: put both records in one state, then ask a Score with outcome levels (different / maybe / same) plus field-level Nouls. Route to the nearest level.

**Walk**: at each node, a Choice over the children or outgoing edges, plus a "goal reached?" Noul. Beam search keeps the top K paths.

```python
import math
from typesafe_sdk import Choice, Noul, TypeSafeClient

def walk(client: TypeSafeClient, doc: str, tree: dict, k: int = 3) -> list[tuple[list[str], float]]:
    beams = [([], 0.0)]                                    # (path, sum of log p)
    while any(_children(tree, p) for p, _ in beams):
        nxt = []
        for path, lp in beams:
            kids = _children(tree, path)
            if not kids:
                nxt.append((path, lp)); continue
            keys = {f"c{i}": name for i, name in enumerate(kids)}
            r = client.system_one(
                state={"document": doc},
                questions={"next": Choice(
                    instructions="Which direct child category best matches `document`?",
                    criteria={key: {"category": name, "subtree": kids[name]}  # the key hides the name
                              for key, name in keys.items()},
                )},
            )
            for key, p in r.choices["next"].probabilities.items():
                if p > 0:
                    nxt.append((path + [keys[key]], lp + math.log(p)))
        beams = sorted(nxt, key=lambda b: b[1] / max(len(b[0]), 1), reverse=True)[:k]
    return beams
```

`_children(tree, path)` returns a dict of `{child_name: subtree_or_description}`. The beam ranks paths by the geometric mean of their probabilities.

## Variants

- **Relationship rerank**: a Choice over exact / substitute / complement / irrelevant, then `sum(p * utility)` in code. Reported best on Elastic's ecommerce test.
- **Pairwise tournament**: a Noul "A ranks higher than B", asked in both orders, in a Swiss tournament. Fit Bradley-Terry to get one scale.
- **Mapping matrix**: a free exact-match pass, then one Noul per remaining pair plus a "has no match" guard Noul. Assign in code.
- **Option tournament**: split a large option set into groups of about 16, Choice per group, then a final Choice over the winners. Use it for models with small option budgets (Laya) or as a pre-rank past a 255 cap.
- **Cached-candidate rank**: when the candidate catalog is fixed (tools, SKUs, taxonomy leaves) and the state changes, a contrastive model (CLM-8B) caches candidate embeddings. Version the encoder, head, and catalog together.

## Field lessons

- Rerank on a shortlist, never on the whole corpus. BM25 top-30 + a Noul per pair lifted top-10 hits from 38% to 62% for $0.0645 per 1,200 pairs.
- Ask several questions per pair in the same call (relevant, contains evidence, contradicts, injection).
- For entity resolution, block first (cheap keys), then pair-score. Keep numeric comparisons (ABV, dates, amounts) in code.
- Score levels named as outcomes remove the need for a threshold: `OUTCOME[round(score)]`.
- Beam (K=3) beat greedy 4/4 vs. 2/4 on the taxonomy walk. Showing subtrees in the option descriptions lets the model see what lives under a branch.
- Choice probabilities are relative and normalized within one pool, so do not compare them across queries. For "is anything relevant at all?" or "no match is fine", add absolute Nouls.
- Keep the cutoff out of the ranking Choice. A "none of these" option returned empty results on 35 of 200 queries on Jev. Filter with a separate Score or Noul, and expect it to drop some gold evidence (19% reported) ([Hindsight](https://hindsight.vectorize.io/blog/2026/09/24/adding-jev-reranker-what-we-learned)).
- Listwise vs. one call per candidate: reports conflict. Hindsight and ielab found listwise as good or better on Jev. llama-index-jev sends one passage per call to avoid context degradation. Measure on your data. A graded Score rubric beat a yes/no Noul for pointwise rerank (DL19 nDCG@10 0.728 vs. 0.693, reported on Jev).
- For pairwise comparisons, ask a Noul, not a 2-option Choice. On Jev both were 95.6% correct, but the Choice pushed 93% of answers outside 0.1–0.9 and left nothing to fit a scale on. Ask each pair in both orders to cancel position bias ([jsort](https://github.com/keltokhy/jsort)).
- Relevance alone passes near misses. Add an "answers the question" Noul, and check numbers literally in code ([cribrix](https://github.com/david96182/cribrix)).
- A cross-encoder is still the cheaper default for static relevance. A decision model pays off when the relevance definition is written in instructions and changes.
- Thresholds do not transfer between models. Re-tune cutoffs on your own labels when you swap models (clef-rag ships Jev-tuned thresholds and says so).
- Small models break on large option sets first, and a contrastive model never adds a candidate you did not pass. Use the option tournament or a pre-rank, and keep an absolute `fits` Noul.
- Not on Jev? Model-specific ranking notes (option caps, short context, caching, negation, grounding strength): `models/clm.md`, `models/laya.md`, `models/pplx-decider.md`, `models/strands-decider.md`. Index: `models/INDEX.md`.

## Prior art

- Hindsight agent-memory reranker, listwise Choice over the pool. Reported recall@1 0.950 vs. MiniLM 0.800 at 30 candidates, 0.783 vs. 0.583 at 240: [hindsight.vectorize.io](https://hindsight.vectorize.io/blog/2026/09/24/adding-jev-reranker-what-we-learned), [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
- Cribrix, a relevance Score plus "answers it" and "injection" Nouls per chunk, then a Noul per claim. Reported 82% → 100% correct on 62 questions: [david96182/cribrix](https://github.com/david96182/cribrix)
- jsort, ranks texts on a plain-English criterion with pairwise Nouls in a Swiss tournament and Bradley-Terry, about 5 comparisons per text: [keltokhy/jsort](https://github.com/keltokhy/jsort)

More projects (41 entries), grouped by sub-type (Rerank and retrieval, Match and dedupe, Walk graphs and taxonomies, Ranking people and things): `prior-art/projects/ranking-and-matching.md`.
