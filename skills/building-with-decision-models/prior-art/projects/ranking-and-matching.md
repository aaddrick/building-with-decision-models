# Projects: Ranking, Matching, and Walking

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/ranking-and-matching.md`.

**Rerank and retrieval**
- Rerank cookbook, BM25 top-30 + Noul, top-10 38% → 62%: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md)
- RAG passage classifier, 4 Nouls per passage with first-match routing: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/classifying_rag_passages.md)
- LanceDB `TypeSafeReranker` ([`lancedb/rerankers/typesafe.py`](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py) in [lancedb/lancedb](https://github.com/lancedb/lancedb)), OpenViking [`jev_rerank.py`](https://github.com/volcengine/OpenViking/blob/main/openviking/models/rerank/jev_rerank.py) in [volcengine/OpenViking](https://github.com/volcengine/OpenViking), [hev/reranker](https://github.com/hev/reranker)
- Jev in production vs. a cross-encoder: [HN](https://news.ycombinator.com/item?id=49804788)
- Search planner (sources, time range, query terms, then rank): [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search)
- Federated retrieval routing gated at 0.6: [Bonzokoles/36_chambers](https://github.com/Bonzokoles/36_chambers)
- fastmcp [`jev_search` transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py) in [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)
- Hindsight agent-memory reranker, listwise Choice over the pool. Reported recall@1 0.950 vs. MiniLM 0.800 at 30 candidates, 0.783 vs. 0.583 at 240: [hindsight.vectorize.io](https://hindsight.vectorize.io/blog/2026/09/24/adding-jev-reranker-what-we-learned), [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
- Elastic ecommerce rerank on Amazon ESCI (250 queries), four policies. Reported nDCG@10 0.9351 → 0.9565 and Exact MRR 0.9201 → 0.9616: [elastic.co](https://www.elastic.co/search-labs/blog/ecommerce-search-reranking-llm-alternative-jev), [notebook](https://github.com/elastic/elastic-labs/tree/main/supporting-blog-content/ecommerce-search-reranking-llm-alternative-jev)
- ielab/llm-rankers, pointwise / pairwise / setwise / listwise on TREC DL19/20. Listwise reported 0.737 / 0.709 nDCG@10 (≈ RankZephyr-7B) at $0.0017 per query. One 100-passage request scored about the same: [ielab/llm-rankers](https://github.com/ielab/llm-rankers/tree/main/jev)
- llama-index-jev, a reranker (0–3 Score) and a router. Reported BEIR nfcorpus nDCG@5 0.340 → 0.396 at about $0.0003 per query: [WiktorB2004/llama-index-jev](https://github.com/WiktorB2004/llama-index-jev)
- Parallel.ai test: rerank NDCG@10 about 0.7, on par with their internal system. A large label set was a weakness: [parallel.ai](https://parallel.ai/blog/testing-jev)
- RAG rerank guide, BM25 21% → 54%, a batch dropping from about 40 s to 7.6 s with 64 concurrent requests: [mindstudio.ai](https://www.mindstudio.ai/blog/jev-reranker-rag/)
- Cribrix, a relevance Score plus "answers it" and "injection" Nouls per chunk, then a Noul per claim. Reported 82% → 100% correct on 62 questions: [david96182/cribrix](https://github.com/david96182/cribrix)
- Milvus "Search with Jev", nine notebooks (rerank, filter, stop searching, graph-relation rerank, cache validation). Examples, not benchmarks: [milvus-io/bootcamp](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev)
- Vector Graph RAG, optional rerank of graph relations in one pass. Reported average Recall@5 87.8% on multi-hop QA: [zilliztech/vector-graph-rag](https://github.com/zilliztech/vector-graph-rag)
- "Rerank is not a free win": over 33,047 catalog entries, a rerank alone did not beat vector retrieval (as described in [yibie/awesome-jev](https://github.com/yibie/awesome-jev)): [x.com/GoSailGlobal](https://x.com/GoSailGlobal/status/2100877682972258619)
- CLM-8B `POST /v1/rank`, candidates encoded separately and cached. Reported about 13× lower latency than Jev at about 1,000 cached candidates (CLM-8B): [Contrastive-LM/CLM](https://github.com/Contrastive-LM/CLM), [aicybr.com](https://aicybr.com/blog/clm-8b-contrastive-language-model-agent-decisions)
- clef-rag, filters at ingestion (boilerplate, planted instructions), asks 4 Nouls per passage (relevant, evidence, contradicts, instructions), ranks by evidence, and refuses below 0.35. Not yet benchmarked on Clef (Clef / Clef-flash): [MersivMedia/clef-rag](https://github.com/MersivMedia/clef-rag)
- RAGTruth (claims vs. retrieved evidence), reported 88.80% vs. Jev 77.27% (pplx-decider): [benchlm.ai](https://benchlm.ai/md/decision-models.md)

**Match and dedupe**
- Entity alignment cookbook (Score outcomes + companion Nouls): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/entity_alignment.md)
- OpenSanctions entity-resolution benchmark: [panios/jev-opensanctions-benchmark](https://github.com/panios/jev-opensanctions-benchmark)
- jlink, English match rules across datasets: [keltokhy/jlink](https://github.com/keltokhy/jlink)
- Genealogy matching discussion (block first, Splink): [HN](https://news.ycombinator.com/item?id=49723461)
- Resume vs. duplicate candidate records: [docs.typesafe.ai](https://docs.typesafe.ai/primitives/noul.md) (structured instructions section)
- Dedupe reported "underwhelming": [HN](https://news.ycombinator.com/item?id=49842510)
- jev-table-import-mapper, CSV column mapping: an exact pass, then one Noul per pair plus a guard Noul, threshold 0.75. 253 questions for about $0.0012 reported: [DuvInc/jev-table-import-mapper](https://github.com/DuvInc/jev-table-import-mapper)
- jevgraph, document to knowledge graph. Pairs are blocked by proximity and ontology type, then one relation Choice per pair. Reported FewRel 87.5% at p95 431 ms: [chenmingtang830/jevgraph](https://github.com/chenmingtang830/jevgraph)

**Walk graphs and taxonomies**
- Hierarchical classification with beam search: [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/hierarchical_classification.md)
- Coarse fallback (report the parent when confidence < 0.9): [docs.typesafe.ai](https://docs.typesafe.ai/cookbooks/classification_using_confidence.md)
- neo4jev, edges as a Choice + "goal reached?" Noul, beam over log-probs: [jexp/neo4jev](https://github.com/jexp/neo4jev)
- jev-tree, one Choice per level past the 255 cap: [reachjalil/jev-tree](https://github.com/reachjalil/jev-tree)
- Wikiracing via links: [typesafe.ai](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
- jev-folio-recursive-classifier, legal documents through the FOLIO ontology. Beam 3, depth 5, leaf threshold 0.9, more than 255 siblings put in temporary groups: [mttrbrts/jev-folio-recursive-classifier](https://github.com/mttrbrts/jev-folio-recursive-classifier)
- jev-bfs, Wikipedia paths. Ranks up to 128 links per request, beam of 5. It warns the beam can prune the shortest route: [komikat/jev-bfs](https://github.com/komikat/jev-bfs)
- Option tournament, groups of 16 then a final. BANKING77 0.430 → 0.610 reported (Laya): [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)

**Ranking people and things**
- Composite scoring (resume screening weights): [docs.typesafe.ai](https://docs.typesafe.ai/patterns/composite-scoring.md)
- 700 leads scored in 40 s: [x.com/romanbuildsaas](https://x.com/romanbuildsaas/status/2100891604735099103). 400 companies matched to one candidate: [x.com/sarvagya_kul](https://x.com/sarvagya_kul/status/2100980770206879849)
- Nifty 50 re-rank every 15 s: [arimanyus/warrenduffer](https://github.com/arimanyus/warrenduffer)
- "Poor man's ranking", top 5 of 1,000 articles (idea): [HN](https://news.ycombinator.com/item?id=49722440)
- jsort, ranks texts on a plain-English criterion with pairwise Nouls in a Swiss tournament and Bradley-Terry, about 5 comparisons per text: [keltokhy/jsort](https://github.com/keltokhy/jsort)
