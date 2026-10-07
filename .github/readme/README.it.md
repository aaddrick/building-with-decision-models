<p align="center">
  <strong>Building with Decision Models</strong><br>
  <em>Decisioni tipizzate con confidenza calibrata, per il tuo agente di coding.</em><br>
  <em>Jev, Clef, pplx-decider, ai_decide, Ollama e altri. Oltre 450 progetti collegati, ordinati per forma.</em>
</p>

<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/aaddrick/building-with-decision-models?style=flat" alt="License"></a>
  <a href="../workflows/checks.yml"><img src="https://img.shields.io/github/actions/workflow/status/aaddrick/building-with-decision-models/checks.yml?label=checks&style=flat" alt="Checks"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aaddrick/">Seguimi su LinkedIn!</a>
</p>

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.vi.md">Tiếng Việt</a> ·
  <a href="README.pt-BR.md">Português (BR)</a> ·
  <strong>Italiano</strong>
</p>

> [!NOTE]
> Questa è una skill non ufficiale, della community. Non è creata, verificata o approvata da TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, AWS, Ollama o da nessun altro fornitore di cui parla. Vedi [Come si rapporta alla skill ufficiale di TypeSafe](#come-si-rapporta-alla-skill-ufficiale-di-typesafe).

Gli agenti di coding trattano i modelli decisionali come l'ennesimo modello di chat. Questa skill insegna loro a progettare per questi modelli: domande tipizzate, confidenza calibrata, le differenze tra i fornitori e link a oltre 450 progetti della community, ordinati per come funzionano, con uno schema di codice per ogni pattern. Si installa in Claude Code, Codex, Antigravity CLI, Muse e Muse Code.

Un modello decisionale, detto anche modello [System One](https://docs.typesafe.ai/concepts/system-one), non scrive testo. Gli invii un contenuto e un insieme di domande tipizzate, e lui risponde a ogni domanda con un valore e una probabilità, di solito in poche centinaia di millisecondi o meno:

- **Choice** sceglie un'opzione da un elenco. Esempio: instradare un ticket a fatturazione, spedizioni o assistenza.
- **Score** colloca il contenuto su una scala che descrivi tu. Esempio: valutare una pull request da "ignora la specifica" a "rispetta la specifica".
- **Noul** dà la probabilità che un'affermazione sì/no sia vera. Esempio: "questo comando di shell elimina file fuori dal progetto."

[Jev](https://docs.typesafe.ai/introduction) di TypeSafe ha aperto la categoria il 2026-09-15. In meno di tre settimane, altri hanno rilasciato modelli che usano gli stessi tre tipi di domanda:

| Tipo | Modelli | Come lo chiami |
|---|---|---|
| In hosting | TypeSafe Jev, Cloudflare Clef e Clef-flash, Perplexity pplx-decider, OpenAI Decisions API (`gpt-6-luna`), System1 Models, Strom | API HTTP, ognuna con la propria chiave |
| Nel tuo data warehouse | Databricks `ai_decide()` | Funzione SQL o REST |
| Sul tuo computer | Nimble e Tev1 tramite Ollama, Kev, Laya, Strands Decider, CLM-8B | Server locale, nessuna chiave |
| Tramite un unico gateway | OpenRouter, Vercel AI Gateway, LLM Gateway, Pydantic AI | Una chiave o un client per più modelli |

Condividono le idee, non sempre il formato dei messaggi, e non la precisione. La skill dà all'agente le regole comuni, un file di riferimento per ogni fornitore e le prove dal campo su quale modello è andato bene in cosa.

## Installazione

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add aaddrick/building-with-decision-models
```

```bash
claude plugin install building-with-decision-models@building-with-decision-models
```

La skill si carica da sola quando lavori su codice per modelli decisionali. Per caricarla a mano, digita:

```
/building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Claude Desktop, Cowork e claude.ai</strong></summary>

**Passo 1.** Apri **Customize > Plugins**, seleziona **Add** e poi **Add marketplace**.

<img src="../assets/plugin-marketplace/step-1.png" alt="La pagina Plugins in Customize con il menu Add aperto. Un riquadro e una freccia color ambra indicano Add marketplace." width="100%">

**Passo 2.** Scegli **Add from a repository**.

<img src="../assets/plugin-marketplace/step-2.png" alt="La finestra di dialogo Add marketplace. Un riquadro e una freccia color ambra indicano Add from a repository." width="100%">

**Passo 3.** Inserisci `aaddrick/building-with-decision-models` o l'URL GitHub completo, poi seleziona **Sync**. Se la finestra mostra **Sync automatically**, lascialo attivo così il plugin si aggiorna insieme a questo repository.

<img src="../assets/plugin-marketplace/step-3.png" alt="La finestra di dialogo Add marketplace con https://github.com/aaddrick/building-with-decision-models nel campo URL. Un riquadro e una freccia color ambra indicano il campo URL e il pulsante Sync." width="100%">

**Passo 4.** Seleziona **Add** accanto a **Building with decision models**.

<img src="../assets/plugin-marketplace/step-4.png" alt="L'elenco Discover con Building with decision models. Un riquadro e una freccia color ambra indicano il suo pulsante Add." width="100%">

**Passo 5.** Il pulsante diventa **Added** e l'elenco mostra la versione. Il plugin compare anche nell'app desktop e in Cowork con lo stesso account.

<img src="../assets/plugin-marketplace/step-5.png" alt="L'elenco Discover con Building with decision models v0.1.0 e un pulsante Added. Un riquadro e una freccia color ambra indicano Added." width="100%">

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add aaddrick/building-with-decision-models
```

```bash
codex plugin add building-with-decision-models@building-with-decision-models
```

Apri un nuovo thread. Codex carica la skill quando il task corrisponde. Per caricarla a mano, digita:

```
$building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Antigravity CLI</strong></summary>

```bash
agy plugin install https://github.com/aaddrick/building-with-decision-models
```

Verifica che sia stata installata:

```bash
agy plugin list
```

Avvia una nuova sessione. Antigravity CLI carica la skill quando il task corrisponde. Per caricarla a mano, digita:

```
/building-with-decision-models:building-with-decision-models
```

Arrivi da Gemini CLI? Se `agy plugin import gemini` ha importato questa estensione, esegui comunque il comando di installazione qui sopra, così la copia attuale sostituisce quella importata.

</details>

<details>
<summary><strong>Muse (muse.ai)</strong></summary>

Muse carica le skill da `~/workspace/skills/` sul proprio computer. Incolla questo comando in una chat di Muse e chiedi a Muse di eseguirlo:

```bash
curl -fsSL https://raw.githubusercontent.com/aaddrick/building-with-decision-models/main/scripts/install_muse.sh | bash
```

Lo script copia lì la cartella della skill e riscrive l'intestazione di `SKILL.md` nella forma che Muse legge. Apri una nuova chat. Muse carica la skill quando il task corrisponde. Per aggiornarla, esegui di nuovo il comando.

</details>

<details>
<summary><strong>Muse Code</strong></summary>

Clona il repository:

```bash
git clone https://github.com/aaddrick/building-with-decision-models.git
```

Installa la skill per tutti i progetti:

```bash
muse skills install building-with-decision-models/skills/building-with-decision-models --scope user
```

Verifica che sia installata:

```bash
muse skills list
```

Avvia una nuova sessione. Muse Code carica la skill quando il task corrisponde. Per caricarla a mano, digita:

```
/building-with-decision-models
```

</details>

<details>
<summary><strong>Qualsiasi altro agente che legge SKILL.md</strong></summary>

Copia la cartella `skills/building-with-decision-models/` nella cartella delle skill del tuo agente. Copia la cartella intera. `SKILL.md` rimanda ai file che le stanno accanto.

</details>


## Collega un modello (facoltativo, consigliato)

La skill funziona anche senza alcun modello collegato. Con un modello collegato, l'agente può verificare il suo design con un endpoint reale prima che il codice arrivi nel tuo progetto. Così trova i nomi di campo sbagliati e le domande che il modello legge in modo diverso da come le intendevi.

<details>
<summary><strong>Locale, gratis, senza chiave</strong> (Ollama)</summary>

<br>

Installa [Ollama](https://ollama.com/download) 0.35 o successivo, poi scarica un modello decisionale:

```bash
ollama pull nimble
```

Verifica che l'agente riesca a raggiungerlo:

```bash
curl -s http://localhost:11434/api/version
```

Un modello locale verifica gratis la forma della richiesta. La sua precisione e la sua calibrazione non sono quelle di un modello in hosting, quindi la skill dice all'agente di non copiare le soglie da uno all'altro.

</details>

<details>
<summary><strong>In hosting: quale chiave va in quale variabile</strong></summary>

<br>

| Fornitore | Variabile | Dove trovare una chiave |
|---|---|---|
| TypeSafe Jev | `TYPESAFE_API_KEY` | [console.typesafe.ai](https://console.typesafe.ai/) (passi qui sotto) |
| Cloudflare Clef | `CLOUDFLARE_AUTH_TOKEN` e `CLOUDFLARE_ACCOUNT_ID` | Dashboard di Cloudflare, Workers AI |
| Perplexity pplx-decider | `PERPLEXITY_API_KEY` | Impostazioni API di Perplexity |
| OpenAI Decisions API | `OPENAI_API_KEY` | Piattaforma OpenAI |
| System1 Models | `SYSTEM1_API_KEY` | system1models.ai |
| Strom (Uprelic) | `UPRELIC_API_KEY` | platform.uprelic.com |
| OpenRouter | `OPENROUTER_API_KEY` | openrouter.ai |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | Dashboard di Vercel |
| LLM Gateway | `LLM_GATEWAY_API_KEY` | llmgateway.io |
| Databricks `ai_decide` | Le credenziali del tuo workspace | Workspace Databricks (un SQL warehouse non richiede chiavi nella shell dell'agente) |

Ogni file di fornitore in `skills/building-with-decision-models/providers/` indica la sua variabile e come chiamarlo. Salva le chiavi come mostra la sezione successiva.

</details>

<details>
<summary><strong>Crea, salva e risolvi i problemi di una chiave</strong></summary>

<br>

<details>
<summary><strong>Esempio: crea una chiave TypeSafe</strong> (quattro passi nella console TypeSafe)</summary>

**Passo 1.** Accedi a [console.typesafe.ai](https://console.typesafe.ai/) e apri **API Keys** nella barra laterale.

<img src="../assets/api-key/step-1.png" alt="La home page della console TypeSafe. Un riquadro e una freccia color ambra indicano API Keys nella barra laterale sinistra." width="100%">

**Passo 2.** Fai clic su **Create key** in alto a destra.

<img src="../assets/api-key/step-2.png" alt="La pagina delle chiavi API. Le chiavi esistenti sono sfocate. Un riquadro e una freccia color ambra indicano il pulsante Create key in alto a destra." width="100%">

**Passo 3.** Dai alla chiave il nome del posto in cui verrà usata, per esempio il computer o l'agente. Poi fai clic su **Create key**.

<img src="../assets/api-key/step-3.png" alt="La finestra Create API key con il nome my-coding-agent inserito. Un riquadro e una freccia color ambra indicano il campo del nome e il pulsante Create key." width="100%">

**Passo 4.** Copia subito la chiave. La console la mostra una sola volta. Se la perdi, creane una nuova e revoca quella vecchia.

<img src="../assets/api-key/step-4.png" alt="La finestra API key created. Il valore della chiave è nascosto. Un riquadro e una freccia color ambra indicano il pulsante Copy." width="100%">

</details>

<details>
<summary><strong>Salva la chiave</strong> (macOS, Linux, Windows)</summary>

Tieni le chiavi in un unico file, leggibile solo da te, con una riga `export` per fornitore. I comandi qui sotto usano `TYPESAFE_API_KEY` come esempio. Per un altro fornitore, usa la sua variabile dalla tabella sopra e aggiungi una riga allo stesso file invece di crearne uno nuovo. Gli agenti spesso avviano shell senza terminale, quindi ogni sezione mette le chiavi dove quelle shell possono vederle. Scegli il tuo sistema.

<details>
<summary><strong>macOS</strong> (zsh, la shell predefinita)</summary>

Salva la chiave in un file privato:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Caricala da `~/.zshenv`. Ogni zsh legge quel file, comprese le shell che gli agenti avviano senza terminale. `~/.zshrc` viene letto solo dalle shell interattive.

```bash
echo '[ -f ~/.config/decision-models/env ] && . ~/.config/decision-models/env' >> ~/.zshenv
```

Apri un nuovo terminale e controlla. Il comando stampa la lunghezza della chiave, non la chiave:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux con bash</strong> (Ubuntu, Debian, Mint, Fedora, Arch)</summary>

Salva la chiave in un file privato:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Caricala dall'**inizio** di `~/.bashrc`. Ubuntu, Debian, Mint e Arch iniziano `~/.bashrc` con una riga che si ferma subito quando non c'è un terminale collegato. Una riga sotto quel controllo non viene mai eseguita per le shell degli agenti. L'inizio del file è sicuro su ogni distribuzione:

```bash
sed -i '1i [ -f ~/.config/decision-models/env ] \&\& . ~/.config/decision-models/env' ~/.bashrc
```

Apri un nuovo terminale e controlla:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux con zsh</strong></summary>

Segui i passaggi per macOS. zsh legge `~/.zshenv` allo stesso modo su Linux.

</details>

<details>
<summary><strong>Linux con fish</strong></summary>

fish legge ogni file in `~/.config/fish/conf.d/`, con o senza terminale:

```fish
mkdir -p ~/.config/fish/conf.d; and echo 'set -gx TYPESAFE_API_KEY YOUR_KEY' >> ~/.config/fish/conf.d/decision-models.fish; and chmod 600 ~/.config/fish/conf.d/decision-models.fish
```

```fish
string length -- $TYPESAFE_API_KEY
```

</details>

<details>
<summary><strong>Windows</strong> (PowerShell)</summary>

Salva la chiave come variabile d'ambiente utente. I nuovi terminali e le nuove app la vedono. I terminali già aperti no:

```powershell
[Environment]::SetEnvironmentVariable('TYPESAFE_API_KEY', 'YOUR_KEY', 'User')
```

Apri un nuovo terminale e controlla:

```powershell
$env:TYPESAFE_API_KEY.Length
```

**WSL:** per impostazione predefinita le variabili di Windows non arrivano a WSL. Dentro WSL, segui i passaggi per Linux con bash.

</details>

<details>
<summary><strong>App desktop ed estensioni per IDE</strong></summary>

Un'app avviata dal dock, dal menu Start o da un launcher del desktop non legge i file della tua shell.

- **Windows:** la variabile d'ambiente utente vista sopra copre già queste app.
- **Linux (systemd):** aggiungi la riga `TYPESAFE_API_KEY=YOUR_KEY` a `~/.config/environment.d/decision-models.conf`, poi esci e rientra nella sessione.
- **macOS:** avvia l'app da un terminale, oppure imposta la variabile nelle impostazioni dell'app stessa. macOS non ha un semplice file per utente che le app desktop leggono.

</details>

</details>

<details>
<summary><strong>Se l'agente non vede la chiave</strong></summary>

Chiedi all'agente di eseguire `echo ${#TYPESAFE_API_KEY}` (oppure `$env:TYPESAFE_API_KEY.Length` su Windows), con la variabile del tuo fornitore al posto di `TYPESAFE_API_KEY`. Se stampa `0` o niente, controlla questi punti in ordine:

- **Hai avviato l'agente prima di salvare la chiave.** Le shell degli agenti copiano l'ambiente del programma che le ha avviate. Chiudi l'agente e avvialo da un nuovo terminale.
- **Hai avviato l'agente dal dock, dal menu Start o da un IDE.** Quelle app non leggono i file della tua shell. Vedi "App desktop ed estensioni per IDE" sopra.
- **Codex filtra l'ambiente.** Se `~/.codex/config.toml` imposta `include_only` sotto `[shell_environment_policy]`, aggiungi lì la tua variabile. Se imposta `ignore_default_excludes = false`, Codex scarta ogni variabile che ha `KEY` o `TOKEN` nel nome. Rimuovi quella riga.
- **WSL.** Le variabili di Windows non arrivano a WSL. Salva la chiave dentro WSL con i passaggi per Linux.

</details>

</details>

## Cosa contiene

La skill si carica a livelli, così l'agente legge solo quello che serve al task.

| File | Cosa contiene | Quando l'agente lo legge |
|---|---|---|
| `SKILL.md` | Quale fornitore e quale primitiva scegliere, 11 regole di design, come usare probabilità e confidenza, come cambiare modello in sicurezza, errori comuni | In ogni task con un modello decisionale |
| `providers/jev.md` | Il contratto di riferimento `/v1/systemone`: API HTTP, SDK Python e JavaScript, limiti, errori, variabili d'ambiente | Quando scrive il codice |
| `providers/*.md` | 10 file di fornitore (Clef, Perplexity, OpenAI, Databricks, Ollama e Kev, host UE, gateway, Pydantic AI, modelli open-weight): in cosa ciascuno differisce da Jev, con le fonti | Quando lavora con quel fornitore |
| `models/*.md` | 9 file di modello (Clef, Nimble, Laya, Kev, CLM-8B, pplx-decider, GPT-6 Luna, Strands Decider e gli altri) più un indice: i limiti incontrati sul campo, la calibrazione, dove ciascun modello funziona bene e dove fallisce, e note per forma | Quando usa un modello diverso da Jev |
| `patterns.md` | I 4 pattern ufficiali e le tecniche da 18 cookbook, con le relative soglie | Quando progetta un workflow |
| `choosing-and-switching-models.md` | Come confrontare i modelli, ricalibrare le soglie, provare il nuovo modello in ombra e cambiare, con le lezioni di chi ha cambiato modello e i benchmark esistenti | Quando sceglie, confronta o cambia un modello |
| `prior-art/INDEX.md` | Una mappa da "cosa voglio costruire" a una forma, più i titoli in una riga delle idee che non hanno funzionato su nessun modello | Prima di progettare qualcosa di nuovo |
| `prior-art/bad-fits.md` | Tutte le idee che non hanno funzionato su qualsiasi modello, con prove e link. I fallimenti di un singolo modello sono nel suo file in `models/` | Quando un progetto somiglia a un caso noto di scarsa idoneità |
| `prior-art/*.md` | 12 file di forma: uno sketch di codice, lezioni dal campo valide per qualsiasi modello e due o tre progetti di riferimento, ognuno etichettato con il suo modello | Uno o due per design |
| `prior-art/projects/*.md` | L'elenco completo dei progetti collegati per ogni forma, raggruppati per sottotipo, ognuno etichettato con il suo modello | Quando servono più esempi |
| `prior-art/more-indexes.md` | Cataloghi esterni più ampi di progetti e benchmark sui modelli decisionali | Quando la libreria non ha corrispondenze |

## La libreria di esempi

La maggior parte dei cataloghi ordina i progetti per settore. Questa libreria li ordina per forma di implementazione. Un bot per videogiochi, un drone e un bot di trading hanno la stessa forma: un ciclo di controllo. Ordinati così, i tre condividono uno sketch di codice e un insieme di lezioni dal campo. Ogni voce indica il modello su cui è stata eseguita, così una lezione imparata su Laya non viene scambiata per una imparata su Jev. Le 12 forme:

- **[Cicli di controllo](../../skills/building-with-decision-models/prior-art/control-loops.md)**: giochi, droni, robot, mercati.
- **[Scelta tra candidati](../../skills/building-with-decision-models/prior-art/select-from-candidates.md)**: agenti per browser e telefono, tool calling senza LLM, estrazione, router.
- **[Gate](../../skills/building-with-decision-models/prior-art/gates.md)**: approvazione delle chiamate ai tool, controlli di "fatto", CI, denaro, contenuti.
- **[Filtri di stream](../../skills/building-with-decision-models/prior-art/stream-filters.md)**: filtri anti-slop, moderazione, email, log, etichettatura in blocco.
- **[Ranking e matching](../../skills/building-with-decision-models/prior-art/ranking-and-matching.md)**: reranker, entity matching, navigazione di grafi e tassonomie.
- **[Giudici e valutazioni](../../skills/building-with-decision-models/prior-art/judges-and-evals.md)**: giudici con rubrica, valutazione delle tracce, code review come triage, benchmark dei modelli stessi.
- **[Incrementale e in tempo reale](../../skills/building-with-decision-models/prior-art/incremental-realtime.md)**: doppiaggio, voce, webcam, interfacce guidate dai tasti premuti.
- **[Contesto e memoria dell'agente](../../skills/building-with-decision-models/prior-art/agent-context-memory.md)**: compattazione, gate sulla memoria, decisioni su quando fermarsi e chiedere, controllo dello sforzo.
- **[Abbinamento a un LLM](../../skills/building-with-decision-models/prior-art/llm-pairing.md)**: pianificatore ed esecutore, verifica e poi escalation, instradamento per livello di modello, distillazione.
- **[Risposte come dati](../../skills/building-with-decision-models/prior-art/research-and-features.md)**: feature per modelli classici, strumenti di ricerca, colonne di analytics, benchmark.
- **[Integrazione nell'infrastruttura](../../skills/building-with-decision-models/prior-art/embedding-in-infrastructure.md)**: funzioni SQL, gateway, server MCP, hook di CI, Home Assistant.
- **[Immagini e altri input non testuali](../../skills/building-with-decision-models/prior-art/images-and-multimodal.md)**: controlli sugli screenshot, moderazione delle immagini, loop da webcam, documenti.

Accanto alla libreria ci sono due guide: [pattern](../../skills/building-with-decision-models/patterns.md) per i pattern ufficiali e le soglie dei cookbook, e [scegliere e cambiare modello](../../skills/building-with-decision-models/choosing-and-switching-models.md) per benchmark, compatibilità, confronti diretti e il passaggio a un nuovo fornitore senza rompere le soglie.

L'indice elenca anche, una riga ciascuna, le idee che sul campo non hanno funzionato sui modelli decisionali in generale: scacchi, giudizio finale su matematica o codice, molte etichette quando hai già dati di addestramento e calibrazione presa sulla fiducia. I fallimenti di un singolo modello, come Laya zero-shot o Clef-flash in hosting nei cicli stretti, sono nel file di quel modello in `models/`. Un tentativo fallito evita al prossimo di ripeterlo.

## Come si rapporta alla skill ufficiale di TypeSafe

TypeSafe pubblica la propria skill su [typesafe-ai/skills](https://github.com/typesafe-ai/skills). È un unico file di indicazioni di design per Jev. Per i dettagli dell'API, rimanda l'agente alla documentazione live in ogni task. Le due skill hanno nomi diversi e non vanno in conflitto, quindi puoi installarle entrambe.

Questa skill copre ogni modello decisionale, non solo Jev. Contiene di più al suo interno: le forme esatte dell'API e le differenze tra i fornitori, le soglie dei cookbook, i casi di errore raccolti dalla community e la libreria di esempi. L'agente può progettare senza passare dalla rete e vedere quello che altri hanno costruito prima.

I modelli decisionali cambiano in fretta, e ogni settimana ne arrivano di nuovi. La skill è un'istantanea della documentazione dei fornitori e della community al 2026-10-06, e dice all'agente che in caso di conflitto vale la documentazione live del fornitore. Se un fatto è sbagliato, apri una issue con un link alla fonte.

## Crediti

I fatti su ogni API vengono dalla documentazione pubblica del rispettivo fornitore: la documentazione e i cookbook di TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, Ollama, System1 Models, Uprelic, OpenRouter, Vercel, LLM Gateway, Pydantic e i README dei modelli aperti. Gli esempi vengono da chi ha pubblicato i propri progetti, dalla community di Hacker News e da questi indici: [awesome-jev](https://github.com/yibie/awesome-jev), [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe), [JevDirectory](https://www.jevdirectory.org/resources), [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases), [awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev), [amplifying.ai](https://amplifying.ai/decision-models) e [BenchLM](https://benchlm.ai/decision-models). Ogni file di forma rimanda ai progetti originali.

TypeSafe, Jev e System One sono nomi di TypeSafe AI. Clef e Workers AI appartengono a Cloudflare, pplx-decider a Perplexity, e ogni altro nome di modello al suo produttore. Questo progetto li usa solo per dire a cosa serve la skill.

## Licenza

MIT. Vedi [LICENSE](../../LICENSE).
