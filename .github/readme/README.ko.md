<p align="center">
  <strong>Building with Decision Models</strong><br>
  <em>코딩 에이전트를 위한, 보정된 신뢰도를 갖춘 타입 있는 결정.</em><br>
  <em>Jev, Clef, pplx-decider, ai_decide, Ollama 등. 450개가 넘는 프로젝트 링크를 형태별로 정리했습니다.</em>
</p>

<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/aaddrick/building-with-decision-models?style=flat" alt="License"></a>
  <a href="../workflows/checks.yml"><img src="https://img.shields.io/github/actions/workflow/status/aaddrick/building-with-decision-models/checks.yml?label=checks&style=flat" alt="Checks"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aaddrick/">LinkedIn에서 연결해요!</a>
</p>

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <strong>한국어</strong> ·
  <a href="README.vi.md">Tiếng Việt</a> ·
  <a href="README.pt-BR.md">Português (BR)</a> ·
  <a href="README.it.md">Italiano</a>
</p>

> [!NOTE]
> 이 스킬은 비공식 커뮤니티 스킬입니다. TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, AWS, Ollama를 비롯해 이 스킬이 다루는 어떤 제공사도 만들거나 검토하거나 보증하지 않았습니다. [공식 TypeSafe 스킬과의 관계](#공식-typesafe-스킬과의-관계)를 참고하세요.

코딩 에이전트는 결정 모델을 채팅 모델 하나쯤으로 다룹니다. 이 스킬은 에이전트가 결정 모델에 맞게 설계하도록 가르칩니다. 타입 있는 질문, 보정된 신뢰도, 제공사 사이의 차이, 그리고 동작 방식별로 정리한 450개가 넘는 커뮤니티 프로젝트 링크와 패턴별 코드 스케치를 담았습니다. Claude Code, Codex, Antigravity CLI, Muse, Muse Code에 설치할 수 있습니다.

결정 모델은 [System One](https://docs.typesafe.ai/concepts/system-one) 모델이라고도 부르며, 글을 쓰지 않습니다. 콘텐츠와 타입 있는 질문 몇 개를 보내면, 각 질문에 값과 확률로 답합니다. 보통 수백 밀리초 이내에 끝납니다.

- **Choice**는 목록에서 선택지 하나를 고릅니다. 예: 티켓을 billing, shipping, support 중 한 곳으로 보냅니다.
- **Score**는 설명한 척도 위에 콘텐츠를 놓습니다. 예: 풀 리퀘스트를 "사양 무시"부터 "사양 충족"까지의 척도로 평가합니다.
- **Noul**은 예/아니요 진술이 참일 확률을 알려 줍니다. 예: "이 셸 명령은 프로젝트 밖의 파일을 삭제한다."

이 범주는 2026-09-15에 TypeSafe의 [Jev](https://docs.typesafe.ai/introduction)가 열었습니다. 3주 안에 다른 회사들도 같은 세 가지 질문 타입을 쓰는 모델을 내놓았습니다.

| 종류 | 모델 | 호출 방법 |
|---|---|---|
| 호스팅 | TypeSafe Jev, Cloudflare Clef와 Clef-flash, Perplexity pplx-decider, OpenAI Decisions API (`gpt-6-luna`), System1 Models, Strom | HTTP API, 제공사마다 별도 키 |
| 데이터 웨어하우스 안 | Databricks `ai_decide()` | SQL 함수 또는 REST |
| 내 컴퓨터 | Ollama로 돌리는 Nimble과 Tev1, Kev, Laya, Strands Decider, CLM-8B | 로컬 서버, 키 없음 |
| 게이트웨이 하나로 | OpenRouter, Vercel AI Gateway, LLM Gateway, Pydantic AI | 키 하나 또는 클라이언트 하나로 여러 모델 |

이 모델들은 아이디어를 공유하지만, 와이어 형식이 늘 같지는 않고 정확도도 다릅니다. 이 스킬은 에이전트에게 공통 규칙, 제공사별 참조 파일, 그리고 어떤 모델이 어디에서 잘했는지에 대한 현장의 증거를 줍니다.

## 설치

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add aaddrick/building-with-decision-models
```

```bash
claude plugin install building-with-decision-models@building-with-decision-models
```

결정 모델 코드를 작업하면 스킬이 알아서 로드됩니다. 직접 로드하려면 다음을 입력하세요.

```
/building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Claude Desktop, Cowork, claude.ai</strong></summary>

**1단계.** **Customize > Plugins**를 열고 **Add**, **Add marketplace**를 차례로 선택하세요.

<img src="../assets/plugin-marketplace/step-1.png" alt="Customize의 Plugins 페이지에서 Add 메뉴를 연 화면. 호박색 상자와 화살표가 Add marketplace를 가리킵니다." width="100%">

**2단계.** **Add from a repository**를 선택하세요.

<img src="../assets/plugin-marketplace/step-2.png" alt="Add marketplace 대화상자. 호박색 상자와 화살표가 Add from a repository를 가리킵니다." width="100%">

**3단계.** `aaddrick/building-with-decision-models` 또는 전체 GitHub URL을 입력한 다음 **Sync**를 선택하세요. 대화상자에 **Sync automatically**가 보이면 켜 두세요. 이 저장소가 업데이트될 때 플러그인도 업데이트됩니다.

<img src="../assets/plugin-marketplace/step-3.png" alt="URL 필드에 https://github.com/aaddrick/building-with-decision-models를 입력한 Add marketplace 대화상자. 호박색 상자와 화살표가 URL 필드와 Sync 버튼을 가리킵니다." width="100%">

**4단계.** **Building with decision models** 옆의 **Add**를 선택하세요.

<img src="../assets/plugin-marketplace/step-4.png" alt="Building with decision models가 보이는 Discover 목록. 호박색 상자와 화살표가 Add 버튼을 가리킵니다." width="100%">

**5단계.** 버튼이 **Added**로 바뀌고 목록에 버전이 표시됩니다. 같은 계정의 데스크톱 앱과 Cowork에도 플러그인이 나타납니다.

<img src="../assets/plugin-marketplace/step-5.png" alt="Building with decision models v0.1.0과 Added 버튼이 보이는 Discover 목록. 호박색 상자와 화살표가 Added를 가리킵니다." width="100%">

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add aaddrick/building-with-decision-models
```

```bash
codex plugin add building-with-decision-models@building-with-decision-models
```

새 스레드를 시작하세요. 작업이 맞으면 Codex가 스킬을 로드합니다. 직접 로드하려면 다음을 입력하세요.

```
$building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Antigravity CLI</strong></summary>

```bash
agy plugin install https://github.com/aaddrick/building-with-decision-models
```

설치되었는지 확인하세요.

```bash
agy plugin list
```

새 세션을 시작하세요. 작업이 맞으면 Antigravity CLI가 스킬을 로드합니다. 직접 로드하려면 다음을 입력하세요.

```
/building-with-decision-models:building-with-decision-models
```

Gemini CLI에서 옮겨 오셨나요? `agy plugin import gemini`로 이 확장을 가져왔더라도 위의 설치 명령을 실행해서 현재 복사본이 가져온 복사본을 대체하게 하세요.

</details>

<details>
<summary><strong>Muse (muse.ai)</strong></summary>

Muse는 자체 컴퓨터의 `~/workspace/skills/`에서 스킬을 불러옵니다. 이 명령을 Muse 채팅에 붙여 넣고 Muse에게 실행해 달라고 요청하세요.

```bash
curl -fsSL https://raw.githubusercontent.com/aaddrick/building-with-decision-models/main/scripts/install_muse.sh | bash
```

스크립트가 스킬 폴더를 그곳에 복사하고 `SKILL.md`의 머리말을 Muse가 읽는 형태로 다시 씁니다. 새 채팅을 시작하세요. 작업이 맞으면 Muse가 스킬을 불러옵니다. 업데이트하려면 명령을 다시 실행하세요.

</details>

<details>
<summary><strong>Muse Code</strong></summary>

저장소를 클론하세요.

```bash
git clone https://github.com/aaddrick/building-with-decision-models.git
```

모든 프로젝트에서 쓰도록 스킬을 설치하세요.

```bash
muse skills install building-with-decision-models/skills/building-with-decision-models --scope user
```

설치되었는지 확인하세요.

```bash
muse skills list
```

새 세션을 시작하세요. 작업이 맞으면 Muse Code가 스킬을 로드합니다. 직접 로드하려면 다음을 입력하세요.

```
/building-with-decision-models
```

</details>

<details>
<summary><strong>SKILL.md를 읽는 다른 에이전트</strong></summary>

`skills/building-with-decision-models/` 폴더를 에이전트의 스킬 폴더에 복사하세요. 폴더 전체를 유지하세요. `SKILL.md`는 옆에 있는 파일들을 링크합니다.

</details>


## 모델 연결 (선택, 권장)

이 스킬은 모델을 연결하지 않아도 작동합니다. 모델을 하나 연결하면, 에이전트는 코드가 프로젝트에 들어가기 전에 설계를 실제 엔드포인트로 확인할 수 있습니다. 그 과정에서 잘못된 필드 이름이나, 의도와 다르게 모델이 읽는 질문을 잡아냅니다.

<details>
<summary><strong>로컬, 무료, 키 없음</strong> (Ollama)</summary>

<br>

[Ollama](https://ollama.com/download) 0.35 이상을 설치한 뒤, 결정 모델을 받으세요.

```bash
ollama pull nimble
```

에이전트가 접근할 수 있는지 확인하세요.

```bash
curl -s http://localhost:11434/api/version
```

로컬 모델로 요청 형태를 무료로 확인할 수 있습니다. 하지만 정확도와 보정은 호스팅 모델과 같지 않습니다. 그래서 스킬은 에이전트에게 둘 사이에 임곗값을 그대로 옮기지 말라고 알려 줍니다.

</details>

<details>
<summary><strong>호스팅: 어떤 키를 어떤 변수에 넣을까</strong></summary>

<br>

| 제공사 | 변수 | 키 받는 곳 |
|---|---|---|
| TypeSafe Jev | `TYPESAFE_API_KEY` | [console.typesafe.ai](https://console.typesafe.ai/) (아래 단계 참고) |
| Cloudflare Clef | `CLOUDFLARE_AUTH_TOKEN`과 `CLOUDFLARE_ACCOUNT_ID` | Cloudflare 대시보드, Workers AI |
| Perplexity pplx-decider | `PERPLEXITY_API_KEY` | Perplexity API 설정 |
| OpenAI Decisions API | `OPENAI_API_KEY` | OpenAI 플랫폼 |
| System1 Models | `SYSTEM1_API_KEY` | system1models.ai |
| Strom (Uprelic) | `UPRELIC_API_KEY` | platform.uprelic.com |
| OpenRouter | `OPENROUTER_API_KEY` | openrouter.ai |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | Vercel 대시보드 |
| LLM Gateway | `LLM_GATEWAY_API_KEY` | llmgateway.io |
| Databricks `ai_decide` | 워크스페이스 자격 증명 | Databricks 워크스페이스 (SQL 웨어하우스는 에이전트 셸에 키가 필요 없습니다) |

`skills/building-with-decision-models/providers/`의 제공사 파일마다 변수 이름과 호출 방법이 적혀 있습니다. 키는 다음 항목에 나온 방식으로 저장하세요.

</details>

<details>
<summary><strong>키 만들기, 저장하기, 문제 해결</strong></summary>

<br>

<details>
<summary><strong>예시: TypeSafe 키 만들기</strong> (TypeSafe 콘솔에서 네 단계)</summary>

**1단계.** [console.typesafe.ai](https://console.typesafe.ai/)에 로그인한 뒤 사이드바에서 **API Keys**를 여세요.

<img src="../assets/api-key/step-1.png" alt="TypeSafe 콘솔 홈 화면. 주황색 상자와 화살표가 왼쪽 사이드바의 API Keys를 가리킵니다." width="100%">

**2단계.** 오른쪽 위의 **Create key**를 클릭하세요.

<img src="../assets/api-key/step-2.png" alt="API 키 페이지. 기존 키는 흐리게 처리되어 있습니다. 주황색 상자와 화살표가 오른쪽 위의 Create key 버튼을 가리킵니다." width="100%">

**3단계.** 키가 쓰일 곳, 예를 들어 컴퓨터나 에이전트 이름으로 키 이름을 정하세요. 그런 다음 **Create key**를 클릭하세요.

<img src="../assets/api-key/step-3.png" alt="이름 칸에 my-coding-agent가 입력된 Create API key 대화 상자. 주황색 상자와 화살표가 이름 칸과 Create key 버튼을 가리킵니다." width="100%">

**4단계.** 지금 키를 복사하세요. 콘솔은 키를 한 번만 보여 줍니다. 키를 잃어버리면 새 키를 만들고 이전 키를 폐기하세요.

<img src="../assets/api-key/step-4.png" alt="API key created 대화 상자. 키 값은 가려져 있습니다. 주황색 상자와 화살표가 Copy 버튼을 가리킵니다." width="100%">

</details>

<details>
<summary><strong>키 저장하기</strong> (macOS, Linux, Windows)</summary>

키는 본인만 읽을 수 있는 파일 하나에 모아 두고, 제공사마다 `export` 줄을 하나씩 쓰세요. 아래 명령은 `TYPESAFE_API_KEY`를 예로 듭니다. 다른 제공사라면 위 표의 변수를 쓰고, 새 파일을 만들지 말고 같은 파일에 줄을 추가하세요. 에이전트는 터미널 없이 셸을 시작하는 경우가 많으므로, 각 항목은 그런 셸에서도 보이는 곳에 키를 둡니다. 사용하는 시스템을 고르세요.

<details>
<summary><strong>macOS</strong> (zsh, 기본 셸)</summary>

키를 비공개 파일에 저장하세요.

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

`~/.zshenv`에서 로드하세요. 에이전트가 터미널 없이 시작하는 셸을 포함해 모든 zsh가 이 파일을 읽습니다. `~/.zshrc`는 대화형 셸만 읽습니다.

```bash
echo '[ -f ~/.config/decision-models/env ] && . ~/.config/decision-models/env' >> ~/.zshenv
```

새 터미널을 열어 확인하세요. 이 명령은 키가 아니라 키의 길이를 출력합니다.

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux와 bash</strong> (Ubuntu, Debian, Mint, Fedora, Arch)</summary>

키를 비공개 파일에 저장하세요.

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

`~/.bashrc`의 **맨 위**에서 로드하세요. Ubuntu, Debian, Mint, Arch는 터미널이 연결되지 않으면 일찍 멈추는 줄로 `~/.bashrc`를 시작합니다. 그 보호 줄 아래에 있는 줄은 에이전트 셸에서 절대 실행되지 않습니다. 파일 맨 위는 모든 배포판에서 안전합니다.

```bash
sed -i '1i [ -f ~/.config/decision-models/env ] \&\& . ~/.config/decision-models/env' ~/.bashrc
```

새 터미널을 열어 확인하세요.

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux와 zsh</strong></summary>

macOS 단계를 따르세요. zsh는 Linux에서도 `~/.zshenv`를 똑같이 읽습니다.

</details>

<details>
<summary><strong>Linux와 fish</strong></summary>

fish는 터미널 유무와 관계없이 `~/.config/fish/conf.d/` 안의 모든 파일을 읽습니다.

```fish
mkdir -p ~/.config/fish/conf.d; and echo 'set -gx TYPESAFE_API_KEY YOUR_KEY' >> ~/.config/fish/conf.d/decision-models.fish; and chmod 600 ~/.config/fish/conf.d/decision-models.fish
```

```fish
string length -- $TYPESAFE_API_KEY
```

</details>

<details>
<summary><strong>Windows</strong> (PowerShell)</summary>

키를 사용자 환경 변수로 저장하세요. 새 터미널과 앱은 이 값을 봅니다. 이미 열려 있는 터미널은 보지 못합니다.

```powershell
[Environment]::SetEnvironmentVariable('TYPESAFE_API_KEY', 'YOUR_KEY', 'User')
```

새 터미널을 열어 확인하세요.

```powershell
$env:TYPESAFE_API_KEY.Length
```

**WSL:** Windows 변수는 기본적으로 WSL에 전달되지 않습니다. WSL 안에서는 Linux와 bash 단계를 따르세요.

</details>

<details>
<summary><strong>데스크톱 앱과 IDE 확장</strong></summary>

Dock, 시작 메뉴, 데스크톱 런처에서 시작한 앱은 셸 파일을 읽지 않습니다.

- **Windows:** 위의 사용자 환경 변수가 이미 이런 앱까지 적용됩니다.
- **Linux (systemd):** `~/.config/environment.d/decision-models.conf`에 `TYPESAFE_API_KEY=YOUR_KEY` 줄을 추가한 뒤, 로그아웃했다가 다시 로그인하세요.
- **macOS:** 터미널에서 앱을 시작하거나, 앱 자체 설정에서 변수를 지정하세요. macOS에는 데스크톱 앱이 읽는 간단한 사용자별 파일이 없습니다.

</details>

</details>

<details>
<summary><strong>에이전트가 키를 보지 못할 때</strong></summary>

에이전트에게 `echo ${#TYPESAFE_API_KEY}`(Windows에서는 `$env:TYPESAFE_API_KEY.Length`)를 실행하라고 하세요. `TYPESAFE_API_KEY` 자리에는 사용하는 제공사의 변수를 넣으세요. `0`이 나오거나 아무것도 나오지 않으면 다음을 순서대로 확인하세요.

- **키를 저장하기 전에 에이전트를 시작했습니다.** 에이전트 셸은 자신을 시작한 프로그램의 환경을 복사합니다. 에이전트를 종료하고 새 터미널에서 다시 시작하세요.
- **Dock, 시작 메뉴, IDE에서 에이전트를 시작했습니다.** 이런 앱은 셸 파일을 읽지 않습니다. 위의 "데스크톱 앱과 IDE 확장"을 참고하세요.
- **Codex가 환경을 걸러 냅니다.** `~/.codex/config.toml`의 `[shell_environment_policy]` 아래에 `include_only`가 설정되어 있다면, 거기에 변수를 추가하세요. `ignore_default_excludes = false`가 설정되어 있다면 Codex는 이름에 `KEY`나 `TOKEN`이 들어간 변수를 모두 버립니다. 그 줄을 지우세요.
- **WSL.** Windows 변수는 WSL에 전달되지 않습니다. Linux 단계를 따라 WSL 안에 키를 저장하세요.

</details>

</details>

## 안에 든 것

스킬은 여러 층으로 로드됩니다. 그래서 에이전트는 작업에 필요한 것만 읽습니다.

| 파일 | 담긴 내용 | 에이전트가 읽는 때 |
|---|---|---|
| `SKILL.md` | 어떤 제공사와 기본 요소를 고를지, 설계 규칙 11개, 확률과 신뢰도 쓰는 법, 모델을 안전하게 바꾸는 법, 흔한 실수 | 모든 결정 모델 작업 |
| `providers/jev.md` | 기준이 되는 `/v1/systemone` 계약: HTTP API, Python과 JavaScript SDK, 제한, 오류, 환경 변수 | 코드를 작성할 때 |
| `providers/*.md` | 제공사 파일 10개(Clef, Perplexity, OpenAI, Databricks, Ollama와 Kev, EU 호스트, 게이트웨이, Pydantic AI, 오픈 웨이트 모델): 각각 Jev와 어떻게 다른지, 출처와 함께 | 그 제공사를 대상으로 할 때 |
| `models/*.md` | 모델 파일 9개(Clef, Nimble, Laya, Kev, CLM-8B, pplx-decider, GPT-6 Luna, Strands Decider, 그 밖의 모델)와 색인: 현장에서 부딪힌 제한, 보정, 모델마다 잘하는 곳과 실패한 곳, 형태별 메모 | Jev가 아닌 모델로 실행할 때 |
| `patterns.md` | 공식 패턴 4개와 쿡북 18개의 기법, 그리고 각 임곗값 | 워크플로를 설계할 때 |
| `choosing-and-switching-models.md` | 모델 비교, 임곗값 재조정, 섀도 운영, 전환 절차. 모델을 바꾼 사람들의 교훈과 기존 벤치마크 포함 | 모델을 고르거나 비교하거나 바꿀 때 |
| `prior-art/INDEX.md` | "만들고 싶은 것"에서 형태로 가는 지도, 그리고 모든 모델에서 실패한 아이디어의 한 줄 요약 | 새로운 것을 설계하기 전 |
| `prior-art/bad-fits.md` | 어떤 모델에서든 실패한 아이디어 전체에 근거와 링크를 붙인 목록. 한 모델에서만 실패한 사례는 그 모델의 `models/` 파일에 있음 | 설계가 알려진 부적합 사례와 비슷할 때 |
| `prior-art/*.md` | 형태 파일 12개: 코드 스케치, 어떤 모델에도 통하는 현장의 교훈, 대표 프로젝트 두세 개, 각각 사용한 모델 표시 | 설계마다 한두 개 |
| `prior-art/projects/*.md` | 형태별 전체 프로젝트 링크 목록, 하위 유형별로 묶고 각각 사용한 모델 표시 | 예시가 더 필요할 때 |
| `prior-art/more-indexes.md` | 결정 모델 프로젝트와 벤치마크를 모은 더 큰 외부 카탈로그 | 라이브러리에 맞는 항목이 없을 때 |

## 선행 사례 라이브러리

대부분의 카탈로그는 프로젝트를 산업별로 나눕니다. 이 라이브러리는 구현 형태로 나눕니다. 게임 봇, 드론, 트레이딩 봇은 같은 형태를 공유합니다. 바로 제어 루프입니다. 이렇게 나누면 세 프로젝트가 코드 스케치 하나와 현장의 교훈 한 묶음을 공유합니다. 항목마다 어떤 모델에서 돌렸는지 적혀 있어서, Laya에서 얻은 교훈을 Jev에서 얻은 교훈으로 착각하지 않습니다. 형태 12개는 다음과 같습니다.

- **[제어 루프](../../skills/building-with-decision-models/prior-art/control-loops.md)**: 게임, 드론, 로봇, 시장.
- **[후보 중 선택](../../skills/building-with-decision-models/prior-art/select-from-candidates.md)**: 브라우저와 휴대폰 에이전트, LLM 없는 도구 호출, 추출, 라우터.
- **[게이트](../../skills/building-with-decision-models/prior-art/gates.md)**: 도구 호출 승인, "완료" 확인, CI, 돈, 콘텐츠.
- **[스트림 필터](../../skills/building-with-decision-models/prior-art/stream-filters.md)**: 저품질 콘텐츠 필터, 모더레이션, 이메일, 로그, 대량 라벨.
- **[순위와 매칭](../../skills/building-with-decision-models/prior-art/ranking-and-matching.md)**: 리랭커, 엔티티 매칭, 그래프와 분류 체계 탐색.
- **[심사와 평가](../../skills/building-with-decision-models/prior-art/judges-and-evals.md)**: 루브릭 심사, 트레이스 채점, 분류 작업으로서의 코드 리뷰, 모델 자체의 벤치마크.
- **[점진적 처리와 실시간](../../skills/building-with-decision-models/prior-art/incremental-realtime.md)**: 더빙, 음성, 웹캠, 키 입력으로 움직이는 인터페이스.
- **[에이전트 컨텍스트와 메모리](../../skills/building-with-decision-models/prior-art/agent-context-memory.md)**: 압축, 메모리 게이트, 멈추고 물어볼지 정하기, 노력 수준 조절.
- **[LLM과 짝짓기](../../skills/building-with-decision-models/prior-art/llm-pairing.md)**: 계획자와 실행자, 검증 후 에스컬레이션, 모델 등급 라우팅, 증류.
- **[데이터로서의 답](../../skills/building-with-decision-models/prior-art/research-and-features.md)**: 고전 모델용 특징, 연구 도구, 분석용 열, 벤치마크.
- **[인프라에 넣기](../../skills/building-with-decision-models/prior-art/embedding-in-infrastructure.md)**: SQL 함수, 게이트웨이, MCP 서버, CI 훅, Home Assistant.
- **[이미지와 텍스트가 아닌 입력](../../skills/building-with-decision-models/prior-art/images-and-multimodal.md)**: 스크린샷 게이트, 이미지 모더레이션, 웹캠 루프, 문서.

라이브러리 옆에는 가이드 두 개가 있습니다. 공식 패턴과 쿡북 임곗값을 담은 [패턴](../../skills/building-with-decision-models/patterns.md), 그리고 벤치마크, 호환성, 직접 비교, 임곗값을 깨뜨리지 않고 새 제공사로 옮기는 방법을 담은 [모델 고르기와 바꾸기](../../skills/building-with-decision-models/choosing-and-switching-models.md)입니다.

인덱스에는 결정 모델 전반에서 현장에서 실패한 아이디어도 한 줄씩 정리되어 있습니다. 체스, 수학이나 코드에 대한 최종 판정, 학습 데이터가 이미 있을 때의 많은 라벨, 그리고 믿고 받아들인 보정입니다. 제로샷 Laya나 촘촘한 루프 안의 호스팅 Clef-flash처럼 한 모델에서만 실패한 사례는 `models/`에 있는 그 모델의 파일에 있습니다. 실패한 시도는 다음 빌더가 같은 실수를 반복하지 않게 해 줍니다.

## 공식 TypeSafe 스킬과의 관계

TypeSafe는 자체 스킬을 [typesafe-ai/skills](https://github.com/typesafe-ai/skills)에 공개하고 있습니다. Jev용 설계 지침을 담은 파일 하나입니다. API 세부 사항은 작업마다 에이전트를 실시간 문서로 보냅니다. 두 스킬은 이름이 다르고 서로 충돌하지 않으므로 둘 다 설치할 수 있습니다.

이 스킬은 Jev뿐 아니라 모든 결정 모델을 다룹니다. 그리고 스킬 안에 더 많은 것을 담고 있습니다. 정확한 API 형태와 제공사 사이의 차이, 쿡북의 임곗값, 커뮤니티에서 모은 실패 유형, 그리고 선행 사례 라이브러리입니다. 에이전트는 네트워크 왕복 없이 설계할 수 있고, 다른 사람들이 먼저 만든 것을 볼 수 있습니다.

결정 모델은 빠르게 바뀌고, 매주 새 모델이 나옵니다. 이 스킬은 2026-10-06 기준 제공사 문서와 커뮤니티의 스냅샷이며, 충돌이 있으면 제공사의 실시간 문서가 우선한다고 에이전트에게 알려 줍니다. 사실이 틀렸다면 출처 링크와 함께 이슈를 열어 주세요.

## 크레딧

각 API에 관한 사실은 해당 제공사의 공개 문서에서 왔습니다. TypeSafe AI의 문서와 쿡북, Cloudflare, Perplexity, OpenAI, Databricks, Ollama, System1 Models, Uprelic, OpenRouter, Vercel, LLM Gateway, Pydantic, 그리고 오픈 모델 README입니다. 선행 사례는 프로젝트를 공개한 빌더들, Hacker News 커뮤니티, 그리고 다음 인덱스에서 왔습니다. [awesome-jev](https://github.com/yibie/awesome-jev), [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe), [JevDirectory](https://www.jevdirectory.org/resources), [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases), [awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev), [amplifying.ai](https://amplifying.ai/decision-models), [BenchLM](https://benchlm.ai/decision-models). 각 형태 파일은 원래 프로젝트를 링크합니다.

TypeSafe, Jev, System One은 TypeSafe AI의 이름입니다. Clef와 Workers AI는 Cloudflare의, pplx-decider는 Perplexity의 이름이며, 그 밖의 모든 모델 이름은 각 제작사의 것입니다. 이 프로젝트는 스킬의 용도를 설명할 때만 이 이름들을 씁니다.

## 라이선스

MIT. [LICENSE](../../LICENSE)를 참고하세요.
