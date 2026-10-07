# Projects: Stream Filters and Bulk Labelling

Community projects that use this shape, grouped by sub-type. Numbers are author-reported. An entry with no model in parentheses ran on TypeSafe Jev; every other entry names its model. The shape, code sketch, variants, and field lessons are in `prior-art/stream-filters.md`.

**Consumer filters (extensions)**
- sift, labels posts on X/LinkedIn/Reddit/YouTube for about $0.00003 per post: [bohutang/sift](https://github.com/bohutang/sift)
- slop-filter, weights fit to your labels: [adamnroman/slop-filter](https://github.com/adamnroman/slop-filter)
- Slop Mop (LinkedIn), flags badly written posts rather than AI-written ones: [HN](https://news.ycombinator.com/item?id=49819820), [tomfrazier/slopmop](https://github.com/tomfrazier/slopmop). Sniffslop: [HN](https://news.ycombinator.com/item?id=49813985)
- jev-slop-guard, blurs and stamps X/LinkedIn posts above a slider threshold (default 70%), scores each post once: [davertor/jev-slop-guard](https://github.com/davertor/jev-slop-guard)
- x-scanner, one request per X post with 6 questions, reported $0.000038 per post, pinned model version: [oso95/x-scanner](https://github.com/oso95/x-scanner)
- Jevx, categorizes X posts and classifies replies in context: [aadhil-kh/jevx](https://github.com/aadhil-kh/jevx). no-slop, reversible slop/clickbait/content-farm hiding: [juztripper/no-slop](https://github.com/juztripper/no-slop)
- sift for Google, re-ranks results and hides or dims SEO filler (flag at 0.85, hide only above 0.6 confidence, 7-day cache): [tylergibbs1/sift](https://github.com/tylergibbs1/sift)
- Twitch chat filter, reported about $0.15/hour at 2 msg/s with a $0.50/hour spend cap: [ethanplusai/jev-chat-for-twitch](https://github.com/ethanplusai/jev-chat-for-twitch)
- Ad blocker by meaning: [realZachi/typesafe-adblock](https://github.com/realZachi/typesafe-adblock)
- Scroll-time slop detector [x.com/RBilgil](https://x.com/RBilgil/status/2100976648552169805), YouTube sponsor skipper [x.com/tdinh_me](https://x.com/tdinh_me/status/2100793777103466615), plain-language X post hiding [x.com/marcelpociot](https://x.com/marcelpociot/status/2100520134481735729), Doomscroll Filter [x.com/robj3d3](https://x.com/robj3d3/status/2101074194260000982), reply-guy filter [x.com/iannuttall](https://x.com/iannuttall/status/2100888635943883244)
- Ground Truth article-framing overlay: [x.com](https://x.com/jagenaujagenau/status/2100622352333574460). Privacy Facts policy labels: [thenewpotato/privacy-facts](https://github.com/thenewpotato/privacy-facts)

**Moderation and anti-spam**
- Telegram bot that deletes only high-confidence spam: [backmeupplz/jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot)
- Discord moderation bot "Soter": [HN](https://news.ycombinator.com/item?id=49825787). mastra-jev-moderation: [CodeAlive-AI/mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation)
- Jev-Moderation-Bot (Discord), 5 scores, escalating timeouts, local memory of pardoned messages, fails open after 3 API errors: [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot)
- Discord/Twitch chat moderator, deletes at ≥0.8 and sends 0.5–0.8 to review, reported under 2¢ per 1,000 messages: [composio.dev](https://composio.dev/content/how-to-build-a-real-time-ai-chat-moderator-with-jev), [shricodev/jev-youtube-discord-moderator](https://github.com/shricodev/jev-youtube-discord-moderator)
- Profanity checker on a Cloudflare Worker, with a username mode for disguised profanity: [4rays/profanity-checker](https://github.com/4rays/profanity-checker)
- Scam Shield, SMS scam filter where code extracts URL/sender signals and 11 questions feed a weighted policy: [ShupingR/scam-shield](https://github.com/ShupingR/scam-shield)
- Cloudflare's internal Trust and Safety report review and support triage pilots, no accuracy published (Clef): [blog.cloudflare.com](https://blog.cloudflare.com/clef-decision-models/)
- Local ticket triage and content moderation, about 91 ms per decision on an M5 Max (Nimble via Ollama): [ollama.com](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models)
- Phishing and spam bands (≥0.9 block, 0.6–0.9 review), reported 99.3% on Enron spam after fine-tuning (Laya): [horadecodar.com.br](https://horadecodar.com.br/?p=46018)
- Trust and safety ideas (severity × confidence → allow/warn/review/block): [docs.typesafe.ai](https://docs.typesafe.ai/concepts/use-case-map.md)

**Email, support, CRM**
- Chatwoot conversation priority/labels: [`captain/conversation_classifier_service.rb`](https://github.com/chatwoot/chatwoot/blob/develop/app/services/captain/conversation_classifier_service.rb) in [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot)
- inbox-zero decision model: [`utils/decision-model/typesafe.ts`](https://github.com/elie222/inbox-zero/blob/main/apps/web/utils/decision-model/typesafe.ts) in [elie222/inbox-zero](https://github.com/elie222/inbox-zero)
- Bryo AI email triage (Gemini slightly more accurate, 10–20× the cost): [marktechpost.com](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/)
- Jevmail 5-tray Gmail sorter: [fazlerocks/jevmail](https://github.com/fazlerocks/jevmail)
- jev-mail (Chrome), category/priority/spam %/reply % per email, reported 9¢ per 1,000 emails, 20k inbox in about 40 min: [muhammedilyasy/jev-mail](https://github.com/muhammedilyasy/jev-mail). Ryan Vogel's run, 1,700 emails for 18¢: [ai.joaoqueiros.com](https://www.ai.joaoqueiros.com/blog/jev-email-triage-lead-scoring-fast-routing-ryan-vogel)
- jevMail (Apps Script), headers and snippet first, full body only when unsure, separate archive threshold: [ilyamk/jev-gmail-ai-spam-filter-and-labeling](https://github.com/ilyamk/jev-gmail-ai-spam-filter-and-labeling)
- Jev-Mail (Apps Script, 24/7), act ≥0.55, skip ≤0.2, "Review" label in between, label-only by default: [vynnlee/jev-mail](https://github.com/vynnlee/jev-mail)
- n8n Gmail triage every minute, low confidence → needs-review label (Jev via OpenRouter): [n8n.io](https://n8n.io/workflows/19908-triage-gmail-messages-with-jev-via-openrouter-google-sheets-and-telegram/)
- Local Gmail labeller, Decider found 6/6 personal emails in a 10-email sample, Laya 1/6 (Decider, Laya via Ollaya): [withone.ai](https://www.withone.ai/blog/ollaya-local-jev-decisions-one-cli/md)
- Support cost study: [HN](https://news.ycombinator.com/item?id=49794787). CraftCX write-up: [HN](https://news.ycombinator.com/item?id=49846104)

**Issues and tickets**
- hush, GitHub Action that labels issues only when confident, reported 78% precision on 800 issues at about $0.00002 per issue: [emreozyoruk/hush](https://github.com/emreozyoruk/hush)

**Logs, code, security**
- Grev/jgrep "thinking grep", 1M log lines for about $10: [HN](https://news.ycombinator.com/item?id=49837132), [kyu1204/jgrep](https://github.com/kyu1204/jgrep)
- jev-semgrep with AND/OR/NOT and JA/EN: [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep). askgrep: [fajarhide/askgrep](https://github.com/fajarhide/askgrep)
- SOC alert triage and grouping: [HN](https://news.ycombinator.com/item?id=49850990), [evals.typesafe.ai](https://evals.typesafe.ai/)
- jevlogs, scores OpenTelemetry logs before LLM analysis, reported 0.84% retained and 87% lower modelled LLM spend (Jev via Vercel AI Gateway): [reachjalil/jevlogs](https://github.com/reachjalil/jevlogs)
- jev-logtriage, routes log batches to suppress/watch/review/page, never auto-fixes security: [jyatesdotdev/jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage)
- triagedy, JSONL-in UNIX filter for SOC alerts, reported 63:1 noise suppression on 64 alerts: [m0rphtail/triagedy](https://github.com/m0rphtail/triagedy)
- jev-triage, test failures to RETRY/FIX_CODE/FIX_ENV, rules settle 44% at zero cost: [ccai40359-wq/jev-triage](https://github.com/ccai40359-wq/jev-triage)

**Bulk business labelling**
- Ad teardown, 724 ads for 9¢ (Matthew Berman via [linas.substack.com](https://linas.substack.com/p/how-to-use-jev-ai))
- Resume vs. 6,245 YC companies for $0.37: [flaviocopes.com](https://flaviocopes.com/jev/)
- IRS forms across 261 classes: kyotofin ([gist.github.com](https://gist.github.com/drillan/6916b16e8ea31a8ec36c8f59d6483150))
- Forum DB curation for backlinks: [HN](https://news.ycombinator.com/item?id=49804096). Site SEO audit with 52 rules: [AgriciDaniel/jev-seo](https://github.com/AgriciDaniel/jev-seo)
- PDF classification and packet splitting: [jerryjliu/docjev](https://github.com/jerryjliu/docjev)
- CV screening with an editable policy: [gtaras7/typesafe-jev](https://github.com/gtaras7/typesafe-jev)
- Litigation discovery, 3 checks per page: [langchain.com](https://www.langchain.com/blog/building-prod-with-jev-and-langgraph)
- jev-curate, Rust filter for Parquet/JSONL training data, reported 24 rows/s on one node (1,500+ rows/s is a distributed target): [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate)
- jev-sift, screens up to 50 items per request so an agent reads only relevant ones: [kbhuw/jev-sift](https://github.com/kbhuw/jev-sift)
- Tag every review row with its issue and return intent in one SQL query (ai_decide): [databricks.com](https://databricks.com/blog/introducing-aidecide-make-fast-decisions-your-governed-data), [docs](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_decide)

**Feeds**
- worldmonitor headline threat level: [`shared/jev-classify.js`](https://github.com/koala73/worldmonitor/blob/main/shared/jev-classify.js) in [koala73/worldmonitor](https://github.com/koala73/worldmonitor)
- "Should AI Kill Us All?", headlines every 10 minutes: shouldaikillusall.com ([hellogumbo/should-ai-kill-us-all](https://github.com/hellogumbo/should-ai-kill-us-all))
- Paper Radar, every new arXiv paper each morning for a reported $0.06/day, thresholds fit to your feedback: [Eliot5566/JEV-Paper-Radar](https://github.com/Eliot5566/JEV-Paper-Radar)
