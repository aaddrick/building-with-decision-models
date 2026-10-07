<p align="center">
  <strong>Building with Decision Models</strong><br>
  <em>Decisões tipadas com confiança calibrada, para o seu agente de código.</em><br>
  <em>Jev, Clef, pplx-decider, ai_decide, Ollama e outros. Mais de 450 projetos com link, organizados por formato.</em>
</p>

<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/aaddrick/building-with-decision-models?style=flat" alt="License"></a>
  <a href="../workflows/checks.yml"><img src="https://img.shields.io/github/actions/workflow/status/aaddrick/building-with-decision-models/checks.yml?label=checks&style=flat" alt="Checks"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aaddrick/">Conecte-se no LinkedIn!</a>
</p>

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.vi.md">Tiếng Việt</a> ·
  <strong>Português (BR)</strong> ·
  <a href="README.it.md">Italiano</a>
</p>

> [!NOTE]
> Esta é uma skill não oficial, feita pela comunidade. Ela não foi criada, revisada nem endossada pela TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, AWS, Ollama ou qualquer outro provedor que ela cobre. Veja [Como esta skill se relaciona com a skill oficial da TypeSafe](#como-esta-skill-se-relaciona-com-a-skill-oficial-da-typesafe).

Os agentes de código tratam os modelos de decisão como mais um modelo de chat. Esta skill ensina o agente a projetar para eles: perguntas tipadas, confiança calibrada, as diferenças entre os provedores e links para mais de 450 projetos da comunidade, organizados pela forma como funcionam, com um esboço de código para cada padrão. Ela se instala no Claude Code, no Codex, no Antigravity CLI, no Muse e no Muse Code.

Um modelo de decisão, também chamado de modelo [System One](https://docs.typesafe.ai/concepts/system-one), não escreve texto. Você envia um conteúdo e um conjunto de perguntas tipadas, e ele responde a cada uma com um valor e uma probabilidade, normalmente em algumas centenas de milissegundos ou menos:

- **Choice** escolhe uma opção de uma lista. Exemplo: encaminhar um ticket para cobrança, envio ou suporte.
- **Score** posiciona o conteúdo numa escala que você descreve. Exemplo: avaliar um pull request de "ignora a especificação" a "atende a especificação".
- **Noul** dá a probabilidade de uma afirmação de sim ou não ser verdadeira. Exemplo: "este comando de shell apaga arquivos fora do projeto."

O [Jev](https://docs.typesafe.ai/introduction), da TypeSafe, inaugurou a categoria em 2026-09-15. Em três semanas, outros lançaram modelos que usam os mesmos três tipos de pergunta:

| Tipo | Modelos | Como chamar |
|---|---|---|
| Hospedado | TypeSafe Jev, Cloudflare Clef e Clef-flash, Perplexity pplx-decider, OpenAI Decisions API (`gpt-6-luna`), System1 Models, Strom | API HTTP, cada um com a sua chave |
| No seu data warehouse | Databricks `ai_decide()` | Função SQL ou REST |
| Na sua máquina | Nimble e Tev1 via Ollama, Kev, Laya, Strands Decider, CLM-8B | Servidor local, sem chave |
| Por um único gateway | OpenRouter, Vercel AI Gateway, LLM Gateway, Pydantic AI | Uma chave ou um cliente para vários modelos |

Eles compartilham ideias, nem sempre um formato de comunicação, e não a precisão. A skill dá ao agente as regras em comum, um arquivo de referência por provedor e as evidências de campo sobre qual modelo se saiu bem em quê.

## Instalação

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add aaddrick/building-with-decision-models
```

```bash
claude plugin install building-with-decision-models@building-with-decision-models
```

A skill carrega sozinha quando você trabalha com código de modelos de decisão. Para carregá-la manualmente, digite:

```
/building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Claude Desktop, Cowork e claude.ai</strong></summary>

**Passo 1.** Abra **Customize > Plugins**, selecione **Add** e depois **Add marketplace**.

<img src="../assets/plugin-marketplace/step-1.png" alt="A página Plugins em Customize com o menu Add aberto. Uma caixa e uma seta âmbar apontam para Add marketplace." width="100%">

**Passo 2.** Escolha **Add from a repository**.

<img src="../assets/plugin-marketplace/step-2.png" alt="A caixa de diálogo Add marketplace. Uma caixa e uma seta âmbar apontam para Add from a repository." width="100%">

**Passo 3.** Digite `aaddrick/building-with-decision-models`. Deixe **Sync automatically** ligado para o plugin se atualizar junto com este repositório. Depois selecione **Sync**.

<img src="../assets/plugin-marketplace/step-3.png" alt="A caixa de diálogo Add marketplace com aaddrick/building-with-decision-models no campo URL e Sync automatically ligado. Uma caixa e uma seta âmbar apontam para o campo URL, a chave e o botão Sync." width="100%">

**Passo 4.** Selecione **Add** ao lado de **Building with decision models**.

<img src="../assets/plugin-marketplace/step-4.png" alt="A lista Discover mostrando Building with decision models. Uma caixa e uma seta âmbar apontam para o botão Add." width="100%">

**Passo 5.** O Claude confirma que o plugin foi instalado. Ele também aparece no app para desktop e no Cowork da mesma conta.

<img src="../assets/plugin-marketplace/step-5.png" alt="A página do plugin Building with decision models com um aviso de que ele está instalado e pronto para uso. Uma caixa e uma seta âmbar apontam para o aviso." width="100%">

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add aaddrick/building-with-decision-models
```

```bash
codex plugin add building-with-decision-models@building-with-decision-models
```

Abra uma nova thread. O Codex carrega a skill quando a tarefa combina com ela. Para carregá-la manualmente, digite:

```
$building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Antigravity CLI</strong></summary>

```bash
agy plugin install https://github.com/aaddrick/building-with-decision-models
```

Confira se ela foi instalada:

```bash
agy plugin list
```

Abra uma nova sessão. O Antigravity CLI carrega a skill quando a tarefa combina. Para carregá-la manualmente, digite:

```
/building-with-decision-models:building-with-decision-models
```

Vindo do Gemini CLI? Se o `agy plugin import gemini` trouxe esta extensão, rode o comando de instalação acima mesmo assim, para que a cópia atual substitua a importada.

</details>

<details>
<summary><strong>Muse (muse.ai)</strong></summary>

O Muse carrega skills de `~/workspace/skills/` no próprio computador. Cole este comando em um chat do Muse e peça para o Muse executá-lo:

```bash
curl -fsSL https://raw.githubusercontent.com/aaddrick/building-with-decision-models/main/scripts/install_muse.sh | bash
```

O script copia a pasta da skill para lá e reescreve o cabeçalho do `SKILL.md` no formato que o Muse lê. Abra um novo chat. O Muse carrega a skill quando a tarefa corresponde. Para atualizar, rode o comando de novo.

</details>

<details>
<summary><strong>Muse Code</strong></summary>

Clone o repositório:

```bash
git clone https://github.com/aaddrick/building-with-decision-models.git
```

Instale a skill para todos os projetos:

```bash
muse skills install building-with-decision-models/skills/building-with-decision-models --scope user
```

Confira se foi instalada:

```bash
muse skills list
```

Abra uma nova sessão. O Muse Code carrega a skill quando a tarefa combina. Para carregá-la manualmente, digite:

```
/building-with-decision-models
```

</details>

<details>
<summary><strong>Qualquer outro agente que leia SKILL.md</strong></summary>

Copie a pasta `skills/building-with-decision-models/` para a pasta de skills do seu agente. Mantenha a pasta inteira. O `SKILL.md` aponta para os arquivos ao lado dele.

</details>


## Conecte um modelo (opcional, recomendado)

A skill funciona sem nenhum modelo conectado. Com um, o agente pode conferir o design contra um endpoint real antes de o código chegar ao seu projeto. Isso pega nomes de campo errados e perguntas que o modelo lê de um jeito diferente do que você queria.

<details>
<summary><strong>Local, grátis, sem chave</strong> (Ollama)</summary>

<br>

Instale o [Ollama](https://ollama.com/download) 0.35 ou mais recente e depois baixe um modelo de decisão:

```bash
ollama pull nimble
```

Confira se o agente consegue alcançá-lo:

```bash
curl -s http://localhost:11434/api/version
```

Um modelo local confere o formato da requisição de graça. A precisão e a calibração dele não são as de um modelo hospedado, então a skill diz ao agente para não copiar limiares de um para o outro.

</details>

<details>
<summary><strong>Hospedado: qual chave vai em qual variável</strong></summary>

<br>

| Provedor | Variável | Onde obter a chave |
|---|---|---|
| TypeSafe Jev | `TYPESAFE_API_KEY` | [console.typesafe.ai](https://console.typesafe.ai/) (passos abaixo) |
| Cloudflare Clef | `CLOUDFLARE_AUTH_TOKEN` e `CLOUDFLARE_ACCOUNT_ID` | Painel da Cloudflare, Workers AI |
| Perplexity pplx-decider | `PERPLEXITY_API_KEY` | Configurações da API da Perplexity |
| OpenAI Decisions API | `OPENAI_API_KEY` | Plataforma da OpenAI |
| System1 Models | `SYSTEM1_API_KEY` | system1models.ai |
| Strom (Uprelic) | `UPRELIC_API_KEY` | platform.uprelic.com |
| OpenRouter | `OPENROUTER_API_KEY` | openrouter.ai |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | Painel da Vercel |
| LLM Gateway | `LLM_GATEWAY_API_KEY` | llmgateway.io |
| Databricks `ai_decide` | As credenciais do seu workspace | Workspace do Databricks (um SQL warehouse não precisa de chave no shell do agente) |

Cada arquivo de provedor em `skills/building-with-decision-models/providers/` indica a sua variável e como chamá-lo. Guarde as chaves do jeito que a próxima seção mostra.

</details>

<details>
<summary><strong>Crie, guarde e resolva problemas com uma chave</strong></summary>

<br>

<details>
<summary><strong>Exemplo: crie uma chave da TypeSafe</strong> (quatro passos no console da TypeSafe)</summary>

**Passo 1.** Entre em [console.typesafe.ai](https://console.typesafe.ai/) e abra **API Keys** (chaves de API) na barra lateral.

<img src="../assets/api-key/step-1.png" alt="A página inicial do console da TypeSafe. Uma caixa e uma seta âmbar apontam para API Keys na barra lateral esquerda." width="100%">

**Passo 2.** Clique em **Create key** (criar chave) no canto superior direito.

<img src="../assets/api-key/step-2.png" alt="A página de chaves de API. As chaves existentes estão desfocadas. Uma caixa e uma seta âmbar apontam para o botão Create key no canto superior direito." width="100%">

**Passo 3.** Dê à chave o nome do lugar onde ela vai ficar, como a máquina ou o agente. Depois clique em **Create key**.

<img src="../assets/api-key/step-3.png" alt="A caixa de diálogo Create API key com o nome my-coding-agent digitado. Uma caixa e uma seta âmbar apontam para o campo de nome e para o botão Create key." width="100%">

**Passo 4.** Copie a chave agora. O console a mostra uma única vez. Se você a perder, crie uma nova e revogue a antiga.

<img src="../assets/api-key/step-4.png" alt="A caixa de diálogo de chave de API criada. O valor da chave está mascarado. Uma caixa e uma seta âmbar apontam para o botão Copy." width="100%">

</details>

<details>
<summary><strong>Guarde a chave</strong> (macOS, Linux, Windows)</summary>

Mantenha as chaves num único arquivo, que só você possa ler, com uma linha `export` por provedor. Os comandos abaixo usam `TYPESAFE_API_KEY` como exemplo. Para outro provedor, use a variável dele da tabela acima e adicione uma linha ao mesmo arquivo, em vez de criar um novo. Os agentes costumam abrir shells sem terminal, então cada seção coloca as chaves onde esses shells conseguem vê-las. Escolha o seu sistema.

<details>
<summary><strong>macOS</strong> (zsh, o shell padrão)</summary>

Salve a chave num arquivo privado:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Carregue-a a partir do `~/.zshenv`. Todo zsh lê esse arquivo, inclusive os shells que os agentes abrem sem terminal. O `~/.zshrc` só é lido por shells interativos.

```bash
echo '[ -f ~/.config/decision-models/env ] && . ~/.config/decision-models/env' >> ~/.zshenv
```

Abra um novo terminal e confira. O comando imprime o tamanho da chave, não a chave:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux com bash</strong> (Ubuntu, Debian, Mint, Fedora, Arch)</summary>

Salve a chave num arquivo privado:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Carregue-a a partir do **topo** do `~/.bashrc`. Ubuntu, Debian, Mint e Arch começam o `~/.bashrc` com uma linha que encerra o script cedo quando não há terminal conectado. Uma linha abaixo dessa proteção nunca roda nos shells dos agentes. O topo do arquivo é seguro em todas as distribuições:

```bash
sed -i '1i [ -f ~/.config/decision-models/env ] \&\& . ~/.config/decision-models/env' ~/.bashrc
```

Abra um novo terminal e confira:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux com zsh</strong></summary>

Siga os passos do macOS. O zsh lê o `~/.zshenv` da mesma forma no Linux.

</details>

<details>
<summary><strong>Linux com fish</strong></summary>

O fish lê todos os arquivos em `~/.config/fish/conf.d/`, com ou sem terminal:

```fish
mkdir -p ~/.config/fish/conf.d; and echo 'set -gx TYPESAFE_API_KEY YOUR_KEY' >> ~/.config/fish/conf.d/decision-models.fish; and chmod 600 ~/.config/fish/conf.d/decision-models.fish
```

```fish
string length -- $TYPESAFE_API_KEY
```

</details>

<details>
<summary><strong>Windows</strong> (PowerShell)</summary>

Guarde a chave como variável de ambiente do usuário. Novos terminais e aplicativos a enxergam. Terminais que já estão abertos não:

```powershell
[Environment]::SetEnvironmentVariable('TYPESAFE_API_KEY', 'YOUR_KEY', 'User')
```

Abra um novo terminal e confira:

```powershell
$env:TYPESAFE_API_KEY.Length
```

**WSL:** por padrão, as variáveis do Windows não chegam ao WSL. Dentro do WSL, siga os passos de Linux com bash.

</details>

<details>
<summary><strong>Aplicativos de desktop e extensões de IDE</strong></summary>

Um aplicativo que você abre pelo dock, pelo menu Iniciar ou por um atalho da área de trabalho não lê os seus arquivos de shell.

- **Windows:** a variável de ambiente do usuário acima já cobre esses aplicativos.
- **Linux (systemd):** adicione a linha `TYPESAFE_API_KEY=YOUR_KEY` em `~/.config/environment.d/decision-models.conf` e depois saia da sessão e entre de novo.
- **macOS:** abra o aplicativo a partir de um terminal ou defina a variável nas configurações do próprio aplicativo. O macOS não tem um arquivo simples por usuário que os aplicativos de desktop leiam.

</details>

</details>

<details>
<summary><strong>Se o agente não consegue ver a chave</strong></summary>

Peça ao agente para rodar `echo ${#TYPESAFE_API_KEY}` (ou `$env:TYPESAFE_API_KEY.Length` no Windows), com a variável do seu provedor no lugar de `TYPESAFE_API_KEY`. Se ele imprimir `0` ou nada, verifique estes pontos, nesta ordem:

- **Você abriu o agente antes de guardar a chave.** Os shells do agente copiam o ambiente do programa que os abriu. Feche o agente e abra-o a partir de um novo terminal.
- **Você abriu o agente pelo dock, pelo menu Iniciar ou por uma IDE.** Esses aplicativos não leem os seus arquivos de shell. Veja "Aplicativos de desktop e extensões de IDE" acima.
- **O Codex filtra o ambiente.** Se o `~/.codex/config.toml` define `include_only` em `[shell_environment_policy]`, adicione a sua variável a ele. Se ele define `ignore_default_excludes = false`, o Codex descarta toda variável com `KEY` ou `TOKEN` no nome. Remova essa linha.
- **WSL.** As variáveis do Windows não chegam ao WSL. Guarde a chave dentro do WSL com os passos de Linux.

</details>

</details>

## O que tem dentro

A skill carrega em camadas, então o agente lê só o que a tarefa pede.

| Arquivo | O que contém | Quando o agente lê |
|---|---|---|
| `SKILL.md` | Qual provedor e qual primitiva escolher, 11 regras de design, como usar probabilidades e confiança, como trocar de modelo com segurança, erros comuns | Em toda tarefa com modelos de decisão |
| `providers/jev.md` | O contrato de referência `/v1/systemone`: API HTTP, SDKs de Python e JavaScript, limites, erros, variáveis de ambiente | Quando escreve o código |
| `providers/*.md` | 10 arquivos de provedor (Clef, Perplexity, OpenAI, Databricks, Ollama e Kev, hosts na UE, gateways, Pydantic AI, modelos de pesos abertos): como cada um difere do Jev, com fontes | Quando o alvo é esse provedor |
| `models/*.md` | 9 arquivos de modelo (Clef, Nimble, Laya, Kev, CLM-8B, pplx-decider, GPT-6 Luna, Strands Decider e os demais) mais um índice: os limites encontrados na prática, a calibração, onde cada modelo vai bem e onde falha, e notas por formato | Quando roda em um modelo que não é o Jev |
| `patterns.md` | Os 4 padrões oficiais e as técnicas de 18 cookbooks, com seus limiares | Quando projeta um fluxo |
| `choosing-and-switching-models.md` | Como comparar modelos, reajustar os limiares, rodar o novo modelo em sombra e trocar, com as lições de quem trocou e os benchmarks que existem | Quando escolhe, compara ou troca de modelo |
| `prior-art/INDEX.md` | Um mapa de "o que eu quero construir" para um formato, mais títulos de uma linha das ideias que falharam em qualquer modelo | Antes de projetar algo novo |
| `prior-art/bad-fits.md` | Todas as ideias que falharam em qualquer modelo, com evidências e links. As falhas de um único modelo ficam no arquivo dele em `models/` | Quando um projeto parece um caso conhecido de má adequação |
| `prior-art/*.md` | 12 arquivos de formato: um esboço de código, lições de campo válidas para qualquer modelo e dois ou três projetos de destaque, cada um marcado com o seu modelo | Um ou dois por design |
| `prior-art/projects/*.md` | A lista completa de projetos com link de cada formato, agrupada por subtipo, cada um marcado com o seu modelo | Quando precisa de mais exemplos |
| `prior-art/more-indexes.md` | Catálogos externos maiores de projetos e benchmarks de modelos de decisão | Quando a biblioteca não tem correspondência |

## A biblioteca de referências

A maioria dos catálogos organiza os projetos por setor. Esta biblioteca os organiza pelo formato da implementação. Um bot de jogo, um drone e um bot de trading compartilham o mesmo formato: um loop de controle. Organizados assim, os três compartilham um esboço de código e um conjunto de lições de campo. Cada entrada indica o modelo em que rodou, para que uma lição aprendida no Laya não seja confundida com uma aprendida no Jev. Os 12 formatos:

- **[Loops de controle](../../skills/building-with-decision-models/prior-art/control-loops.md)**: jogos, drones, robôs, mercados.
- **[Seleção entre candidatos](../../skills/building-with-decision-models/prior-art/select-from-candidates.md)**: agentes de navegador e de celular, tool calling sem LLM, extração, roteadores.
- **[Portões](../../skills/building-with-decision-models/prior-art/gates.md)**: aprovação de tool calls, verificações de "pronto", CI, dinheiro, conteúdo.
- **[Filtros de fluxo](../../skills/building-with-decision-models/prior-art/stream-filters.md)**: filtros de conteúdo genérico, moderação, e-mail, logs, rotulagem em massa.
- **[Ranqueamento e correspondência](../../skills/building-with-decision-models/prior-art/ranking-and-matching.md)**: rerankers, correspondência de entidades, percursos em grafos e taxonomias.
- **[Juízes e avaliações](../../skills/building-with-decision-models/prior-art/judges-and-evals.md)**: juízes com rubrica, avaliação de traces, code review como triagem, benchmarks dos próprios modelos.
- **[Incremental e em tempo real](../../skills/building-with-decision-models/prior-art/incremental-realtime.md)**: dublagem, voz, webcam, interfaces guiadas pela digitação.
- **[Contexto e memória de agentes](../../skills/building-with-decision-models/prior-art/agent-context-memory.md)**: compactação, portões de memória, decisões de parar e perguntar, controle de esforço.
- **[Parceria com um LLM](../../skills/building-with-decision-models/prior-art/llm-pairing.md)**: planejador e executor, verificar e depois escalar, roteamento por nível de modelo, destilação.
- **[Respostas como dados](../../skills/building-with-decision-models/prior-art/research-and-features.md)**: features para modelos clássicos, instrumentos de pesquisa, colunas de analytics, benchmarks.
- **[Embutido na infraestrutura](../../skills/building-with-decision-models/prior-art/embedding-in-infrastructure.md)**: funções SQL, gateways, servidores MCP, hooks de CI, Home Assistant.
- **[Imagens e outras entradas não textuais](../../skills/building-with-decision-models/prior-art/images-and-multimodal.md)**: verificações de capturas de tela, moderação de imagens, loops de webcam, documentos.

Dois guias ficam ao lado da biblioteca: [padrões](../../skills/building-with-decision-models/patterns.md), com os padrões oficiais e os limiares dos cookbooks, e [escolher e trocar de modelo](../../skills/building-with-decision-models/choosing-and-switching-models.md), com benchmarks, compatibilidade, comparações diretas e como migrar para um novo provedor sem quebrar os limiares.

O índice também lista, uma linha cada, as ideias que falharam na prática em modelos de decisão em geral: xadrez, julgamento final sobre matemática ou código, muitos rótulos quando você já tem dados de treino e calibração aceita sem verificação. As falhas de um único modelo, como Laya em zero-shot ou Clef-flash hospedado em loops apertados, ficam no arquivo desse modelo em `models/`. Uma tentativa que falhou poupa o próximo construtor de repeti-la.

## Como esta skill se relaciona com a skill oficial da TypeSafe

A TypeSafe publica a própria skill em [typesafe-ai/skills](https://github.com/typesafe-ai/skills). Ela é um único arquivo de orientações de design para o Jev. Para os detalhes da API, ela manda o agente para a documentação ao vivo em toda tarefa. As duas skills têm nomes diferentes e não entram em conflito, então você pode instalar as duas.

Esta skill cobre todos os modelos de decisão, não só o Jev. Ela guarda mais coisa dentro dela mesma: os formatos exatos da API e as diferenças entre os provedores, os limiares dos cookbooks, as falhas relatadas pela comunidade e a biblioteca de referências. O agente consegue projetar sem ir à rede e ver o que outros já construíram antes.

Os modelos de decisão mudam rápido, e novos chegam toda semana. A skill é um retrato da documentação dos provedores e da comunidade em 2026-10-06, e ela diz ao agente que a documentação ao vivo de um provedor prevalece em qualquer conflito. Se algum fato estiver errado, abra uma issue com um link para a fonte.

## Créditos

Os fatos sobre cada API vêm da documentação pública do respectivo provedor: a documentação e os cookbooks da TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, Ollama, System1 Models, Uprelic, OpenRouter, Vercel, LLM Gateway, Pydantic e os READMEs dos modelos abertos. As referências vêm das pessoas que publicaram seus projetos, da comunidade do Hacker News e destes índices: [awesome-jev](https://github.com/yibie/awesome-jev), [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe), [JevDirectory](https://www.jevdirectory.org/resources), [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases), [awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev), [amplifying.ai](https://amplifying.ai/decision-models) e [BenchLM](https://benchlm.ai/decision-models). Cada arquivo de formato aponta para os projetos originais.

TypeSafe, Jev e System One são nomes da TypeSafe AI. Clef e Workers AI pertencem à Cloudflare, pplx-decider à Perplexity, e todos os outros nomes de modelo aos seus criadores. Este projeto os usa só para dizer para que serve a skill.

## Licença

MIT. Veja [LICENSE](../../LICENSE).
