<p align="center">
  <strong>Building with Decision Models</strong><br>
  <em>コーディングエージェントのための、較正された確信度つきの型付き判断。</em><br>
  <em>Jev、Clef、pplx-decider、ai_decide、Ollama など。450 を超えるプロジェクトへのリンクを形ごとに整理。</em>
</p>

<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/aaddrick/building-with-decision-models?style=flat" alt="License"></a>
  <a href="../workflows/checks.yml"><img src="https://img.shields.io/github/actions/workflow/status/aaddrick/building-with-decision-models/checks.yml?label=checks&style=flat" alt="Checks"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aaddrick/">LinkedIn でつながりましょう！</a>
</p>

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <strong>日本語</strong> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.vi.md">Tiếng Việt</a> ·
  <a href="README.pt-BR.md">Português (BR)</a> ·
  <a href="README.it.md">Italiano</a>
</p>

> [!NOTE]
> これは非公式のコミュニティ製スキルです。TypeSafe AI、Cloudflare、Perplexity、OpenAI、Databricks、AWS、Ollama をはじめ、扱っているどのプロバイダーも、作成、レビュー、推奨していません。[公式 TypeSafe スキルとの関係](#公式-typesafe-スキルとの関係) も参照してください。

コーディングエージェントは、判断モデルをチャットモデルの 1 つとして扱います。このスキルは、判断モデルに合わせた設計をエージェントに教えます。型付きの質問、較正された確信度、プロバイダーごとの違い、そして仕組みごとに整理した 450 を超えるコミュニティプロジェクトへのリンクと、パターンごとのコードスケッチです。Claude Code、Codex、Antigravity CLI、Muse、Muse Code にインストールできます。

判断モデルは [System One](https://docs.typesafe.ai/concepts/system-one) モデルとも呼ばれ、文章は書きません。コンテンツと型付きの質問のセットを送ると、各質問に値と確率で答えます。通常は数百ミリ秒以内に返ります。

- **Choice** は、リストから選択肢を 1 つ選びます。例: チケットを請求、配送、サポートのいずれかに振り分けます。
- **Score** は、説明した尺度の上にコンテンツを位置づけます。例: プルリクエストを「仕様を無視している」から「仕様を満たしている」までの尺度で評価します。
- **Noul** は、はい/いいえで答える文が正しい確率を返します。例: 「このシェルコマンドはプロジェクト外のファイルを削除する」。

このカテゴリは、2026-09-15 に TypeSafe の [Jev](https://docs.typesafe.ai/introduction) が始めました。それから 3 週間で、同じ 3 つの質問の型を使うモデルを他社も出しました。

| 種類 | モデル | 呼び出し方 |
|---|---|---|
| ホスト型 | TypeSafe Jev、Cloudflare Clef と Clef-flash、Perplexity pplx-decider、OpenAI Decisions API (`gpt-6-luna`)、System1 Models、Strom | HTTP API。それぞれ専用のキー |
| データウェアハウス内 | Databricks `ai_decide()` | SQL 関数または REST |
| 自分のマシン上 | Ollama 経由の Nimble と Tev1、Kev、Laya、Strands Decider、CLM-8B | ローカルサーバー。キー不要 |
| 1 つのゲートウェイ経由 | OpenRouter、Vercel AI Gateway、LLM Gateway、Pydantic AI | 1 つのキーか 1 つのクライアントで複数のモデル |

共有しているのは考え方です。ワイヤーフォーマットが同じとは限らず、精度も同じではありません。このスキルは、共通のルール、プロバイダーごとのリファレンスファイル、そしてどのモデルが何を得意としたかという現場の証拠をエージェントに渡します。

## インストール

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add aaddrick/building-with-decision-models
```

```bash
claude plugin install building-with-decision-models@building-with-decision-models
```

判断モデルのコードを扱うと、スキルは自動で読み込まれます。手動で読み込むには、次のように入力します。

```
/building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Claude Desktop、Cowork、claude.ai</strong></summary>

**ステップ 1.** **Customize > Plugins** を開き、**Add**、**Add marketplace** の順に選びます。

<img src="../assets/plugin-marketplace/step-1.png" alt="Customize の Plugins ページで Add メニューを開いた画面。琥珀色の枠と矢印が Add marketplace を指しています。" width="100%">

**ステップ 2.** **Add from a repository** を選びます。

<img src="../assets/plugin-marketplace/step-2.png" alt="Add marketplace ダイアログ。琥珀色の枠と矢印が Add from a repository を指しています。" width="100%">

**ステップ 3.** `aaddrick/building-with-decision-models` か GitHub の URL 全体を入力し、**Sync** を選びます。ダイアログに **Sync automatically** があればオンのままにしておくと、このリポジトリの更新に合わせてプラグインも更新されます。

<img src="../assets/plugin-marketplace/step-3.png" alt="URL 欄に https://github.com/aaddrick/building-with-decision-models を入力した Add marketplace ダイアログ。琥珀色の枠と矢印が URL 欄と Sync ボタンを指しています。" width="100%">

**ステップ 4.** **Building with decision models** の横の **Add** を選びます。

<img src="../assets/plugin-marketplace/step-4.png" alt="Building with decision models が表示された Discover の一覧。琥珀色の枠と矢印がその Add ボタンを指しています。" width="100%">

**ステップ 5.** ボタンが **Added** に変わり、一覧にバージョンが表示されます。同じアカウントのデスクトップアプリと Cowork にもプラグインが表示されます。

<img src="../assets/plugin-marketplace/step-5.png" alt="Building with decision models v0.1.0 と Added ボタンが表示された Discover 一覧。琥珀色の枠と矢印が Added を指しています。" width="100%">

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add aaddrick/building-with-decision-models
```

```bash
codex plugin add building-with-decision-models@building-with-decision-models
```

新しいスレッドを始めます。タスクが合えば、Codex がスキルを読み込みます。手動で読み込むには、次のように入力します。

```
$building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Antigravity CLI</strong></summary>

```bash
agy plugin install https://github.com/aaddrick/building-with-decision-models
```

インストールされたか確認します。

```bash
agy plugin list
```

新しいセッションを始めます。Antigravity CLI はタスクに合うときにスキルを読み込みます。手動で読み込むには、次のように入力します。

```
/building-with-decision-models:building-with-decision-models
```

Gemini CLI から移行しましたか？ `agy plugin import gemini` でこの拡張機能を移した場合も、上のインストールコマンドを実行してください。インポートしたコピーが最新のものに置き換わります。

</details>

<details>
<summary><strong>Muse (muse.ai)</strong></summary>

Muse は自分専用のコンピューター上の `~/workspace/skills/` からスキルを読み込みます。このコマンドを Muse のチャットに貼り付け、実行するよう Muse に頼んでください。

```bash
curl -fsSL https://raw.githubusercontent.com/aaddrick/building-with-decision-models/main/scripts/install_muse.sh | bash
```

スクリプトはスキルフォルダをそこへコピーし、`SKILL.md` のヘッダーを Muse が読める形に書き換えます。新しいチャットを始めてください。タスクが合えば Muse がスキルを読み込みます。更新するときは、同じコマンドをもう一度実行します。

</details>

<details>
<summary><strong>Muse Code</strong></summary>

リポジトリをクローンします。

```bash
git clone https://github.com/aaddrick/building-with-decision-models.git
```

すべてのプロジェクトで使えるようにスキルをインストールします。

```bash
muse skills install building-with-decision-models/skills/building-with-decision-models --scope user
```

インストールされたか確認します。

```bash
muse skills list
```

新しいセッションを始めます。Muse Code はタスクに合うときにスキルを読み込みます。手動で読み込むには、次のように入力します。

```
/building-with-decision-models
```

</details>

<details>
<summary><strong>SKILL.md を読むその他のエージェント</strong></summary>

`skills/building-with-decision-models/` フォルダを、エージェントのスキルフォルダにコピーします。フォルダは丸ごと残してください。`SKILL.md` は隣にあるファイルへリンクしています。

</details>


## モデルをつなぐ (任意、推奨)

このスキルは、モデルをつながなくても動きます。モデルをつなげば、コードがプロジェクトに入る前に、エージェントが実際のエンドポイントで設計を確認できます。これで、フィールド名の間違いや、モデルが意図と違う意味に読む質問を見つけられます。

<details>
<summary><strong>ローカル、無料、キー不要</strong> (Ollama)</summary>

<br>

[Ollama](https://ollama.com/download) 0.35 以降をインストールし、判断モデルを pull します。

```bash
ollama pull nimble
```

エージェントから届くか確認します。

```bash
curl -s http://localhost:11434/api/version
```

ローカルモデルなら、リクエストの形を無料で確認できます。ただし精度と較正はホスト型のモデルとは違うので、しきい値をモデル間でコピーしないようスキルがエージェントに伝えます。

</details>

<details>
<summary><strong>ホスト型: どのキーをどの変数に入れるか</strong></summary>

<br>

| プロバイダー | 変数 | キーの入手先 |
|---|---|---|
| TypeSafe Jev | `TYPESAFE_API_KEY` | [console.typesafe.ai](https://console.typesafe.ai/) (手順は下記) |
| Cloudflare Clef | `CLOUDFLARE_AUTH_TOKEN` と `CLOUDFLARE_ACCOUNT_ID` | Cloudflare ダッシュボードの Workers AI |
| Perplexity pplx-decider | `PERPLEXITY_API_KEY` | Perplexity の API 設定 |
| OpenAI Decisions API | `OPENAI_API_KEY` | OpenAI プラットフォーム |
| System1 Models | `SYSTEM1_API_KEY` | system1models.ai |
| Strom (Uprelic) | `UPRELIC_API_KEY` | platform.uprelic.com |
| OpenRouter | `OPENROUTER_API_KEY` | openrouter.ai |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | Vercel ダッシュボード |
| LLM Gateway | `LLM_GATEWAY_API_KEY` | llmgateway.io |
| Databricks `ai_decide` | ワークスペースの認証情報 | Databricks ワークスペース (SQL ウェアハウスなら、エージェントのシェルにキーは不要) |

`skills/building-with-decision-models/providers/` 内の各プロバイダーファイルに、使う変数と呼び出し方が書いてあります。キーは次のセクションの方法で保存してください。

</details>

<details>
<summary><strong>キーを作成、保存、トラブルシューティングする</strong></summary>

<br>

<details>
<summary><strong>例: TypeSafe のキーを作成する</strong> (TypeSafe コンソールでの 4 ステップ)</summary>

**ステップ 1.** [console.typesafe.ai](https://console.typesafe.ai/) にサインインし、サイドバーの **API Keys** を開きます。

<img src="../assets/api-key/step-1.png" alt="TypeSafe コンソールのホームページ。琥珀色の枠と矢印が、左サイドバーの API Keys を指しています。" width="100%">

**ステップ 2.** 右上の **Create key** をクリックします。

<img src="../assets/api-key/step-2.png" alt="API キーのページ。既存のキーはぼかされています。琥珀色の枠と矢印が、右上の Create key ボタンを指しています。" width="100%">

**ステップ 3.** マシン名やエージェント名など、キーを置く場所にちなんだ名前を付けます。続けて **Create key** をクリックします。

<img src="../assets/api-key/step-3.png" alt="Create API key ダイアログ。名前欄に my-coding-agent と入力されています。琥珀色の枠と矢印が、名前欄と Create key ボタンを指しています。" width="100%">

**ステップ 4.** 今すぐキーをコピーしてください。コンソールがキーを表示するのは 1 回だけです。なくした場合は新しいキーを作成し、古いキーを無効化します。

<img src="../assets/api-key/step-4.png" alt="API key created ダイアログ。キーの値は伏せられています。琥珀色の枠と矢印が、Copy ボタンを指しています。" width="100%">

</details>

<details>
<summary><strong>キーを保存する</strong> (macOS, Linux, Windows)</summary>

キーは、自分だけが読める 1 つのファイルにまとめ、プロバイダーごとに `export` の行を 1 行ずつ書きます。下のコマンドでは `TYPESAFE_API_KEY` を例にしています。別のプロバイダーなら、上の表にあるその変数を使い、新しいファイルは作らずに同じファイルへ行を足してください。エージェントはターミナルなしでシェルを起動することが多いため、各セクションではそうしたシェルからも見える場所にキーを置きます。お使いのシステムを選んでください。

<details>
<summary><strong>macOS</strong> (zsh、デフォルトのシェル)</summary>

キーを非公開のファイルに保存します。

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

`~/.zshenv` から読み込みます。エージェントがターミナルなしで起動するシェルも含め、すべての zsh がこのファイルを読みます。`~/.zshrc` を読むのは対話シェルだけです。

```bash
echo '[ -f ~/.config/decision-models/env ] && . ~/.config/decision-models/env' >> ~/.zshenv
```

新しいターミナルを開いて確認します。このコマンドはキーそのものではなく、キーの長さを表示します。

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux で bash</strong> (Ubuntu, Debian, Mint, Fedora, Arch)</summary>

キーを非公開のファイルに保存します。

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

`~/.bashrc` の**先頭**から読み込みます。Ubuntu、Debian、Mint、Arch の `~/.bashrc` は、ターミナルがつながっていないときに早めに処理を止める行で始まります。この判定より下の行は、エージェントのシェルでは実行されません。ファイルの先頭なら、どのディストリビューションでも安全です。

```bash
sed -i '1i [ -f ~/.config/decision-models/env ] \&\& . ~/.config/decision-models/env' ~/.bashrc
```

新しいターミナルを開いて確認します。

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux で zsh</strong></summary>

macOS の手順に従ってください。Linux でも zsh は同じように `~/.zshenv` を読みます。

</details>

<details>
<summary><strong>Linux で fish</strong></summary>

fish は、ターミナルの有無にかかわらず `~/.config/fish/conf.d/` 内のすべてのファイルを読みます。

```fish
mkdir -p ~/.config/fish/conf.d; and echo 'set -gx TYPESAFE_API_KEY YOUR_KEY' >> ~/.config/fish/conf.d/decision-models.fish; and chmod 600 ~/.config/fish/conf.d/decision-models.fish
```

```fish
string length -- $TYPESAFE_API_KEY
```

</details>

<details>
<summary><strong>Windows</strong> (PowerShell)</summary>

キーをユーザー環境変数として保存します。新しく開くターミナルやアプリからは見えますが、すでに開いているターミナルからは見えません。

```powershell
[Environment]::SetEnvironmentVariable('TYPESAFE_API_KEY', 'YOUR_KEY', 'User')
```

新しいターミナルを開いて確認します。

```powershell
$env:TYPESAFE_API_KEY.Length
```

**WSL:** 既定では、Windows の変数は WSL に届きません。WSL の中では、Linux で bash の手順に従ってください。

</details>

<details>
<summary><strong>デスクトップアプリと IDE 拡張機能</strong></summary>

Dock、スタートメニュー、デスクトップのランチャーから起動したアプリは、シェルのファイルを読みません。

- **Windows:** 上で設定したユーザー環境変数が、これらのアプリにもすでに有効です。
- **Linux (systemd):** `~/.config/environment.d/decision-models.conf` に `TYPESAFE_API_KEY=YOUR_KEY` という行を追加し、ログアウトしてから再度ログインします。
- **macOS:** アプリをターミナルから起動するか、アプリ自体の設定で変数を設定します。macOS には、デスクトップアプリが読むユーザーごとの簡単なファイルがありません。

</details>

</details>

<details>
<summary><strong>エージェントからキーが見えない場合</strong></summary>

エージェントに `echo ${#TYPESAFE_API_KEY}` (Windows では `$env:TYPESAFE_API_KEY.Length`) を実行させます。`TYPESAFE_API_KEY` の部分は、お使いのプロバイダーの変数に置き換えてください。`0` と表示されるか何も表示されない場合は、次の順に確認してください。

- **キーを保存する前にエージェントを起動した。** エージェントのシェルは、起動したプログラムの環境をコピーします。エージェントを終了し、新しいターミナルから起動してください。
- **Dock、スタートメニュー、IDE からエージェントを起動した。** これらのアプリはシェルのファイルを読みません。上の「デスクトップアプリと IDE 拡張機能」を参照してください。
- **Codex が環境をフィルタしている。** `~/.codex/config.toml` の `[shell_environment_policy]` で `include_only` が設定されている場合は、そこに使う変数を追加します。`ignore_default_excludes = false` が設定されている場合、Codex は名前に `KEY` か `TOKEN` を含む変数をすべて取り除きます。その行を削除してください。
- **WSL.** Windows の変数は WSL に届きません。WSL の中で、Linux の手順に従ってキーを保存してください。

</details>

</details>

## 中身

スキルは層に分けて読み込まれます。エージェントはタスクに必要な部分だけを読みます。

| ファイル | 内容 | エージェントが読むタイミング |
|---|---|---|
| `SKILL.md` | どのプロバイダーとプリミティブを選ぶか、11 の設計ルール、確率と確信度の使い方、モデルを安全に切り替える方法、よくある間違い | 判断モデルのタスクのたび |
| `providers/jev.md` | 基準となる `/v1/systemone` の契約。HTTP API、Python と JavaScript の SDK、制限、エラー、環境変数 | コードを書くとき |
| `providers/*.md` | 10 のプロバイダーファイル (Clef、Perplexity、OpenAI、Databricks、Ollama と Kev、EU のホスト、ゲートウェイ、Pydantic AI、オープンウェイトのモデル)。それぞれが Jev とどう違うかを出典つきで | そのプロバイダーを対象にするとき |
| `models/*.md` | 9 のモデルファイル (Clef、Nimble、Laya、Kev、CLM-8B、pplx-decider、GPT-6 Luna、Strands Decider、その他) と索引。現場で当たった制限、キャリブレーション、各モデルが得意なことと失敗したこと、形ごとのメモ | Jev 以外のモデルで動かすとき |
| `patterns.md` | 4 つの公式パターンと 18 のクックブックのテクニック、そのしきい値 | ワークフローを設計するとき |
| `choosing-and-switching-models.md` | モデルの比較、しきい値の再調整、シャドー運用、切り替えの手順。切り替えた人たちの教訓と既存のベンチマークつき | モデルを選ぶ、比べる、変えるとき |
| `prior-art/INDEX.md` | 「作りたいもの」から形への地図と、どのモデルでも失敗したアイデアの一行見出し | 新しいものを設計する前 |
| `prior-art/bad-fits.md` | どのモデルでも失敗したアイデアのすべて、根拠とリンク付き。1 つのモデルだけの失敗はその `models/` のファイルにある | 設計が既知の不適合に似ているとき |
| `prior-art/*.md` | 12 の形のファイル。コードのスケッチ、どのモデルにも当てはまる現場の教訓、代表的なプロジェクト 2〜3 件。それぞれに使ったモデルのタグつき | 1 つの設計につき 1〜2 個 |
| `prior-art/projects/*.md` | 形ごとのリンク付きプロジェクトの全リスト。サブタイプ別にまとめ、それぞれに使ったモデルのタグつき | 例がもっと必要なとき |
| `prior-art/more-indexes.md` | 判断モデルのプロジェクトとベンチマークを集めた、より大きな外部カタログ | ライブラリに該当するものがないとき |

## 先行事例ライブラリ

多くのカタログは、プロジェクトを業界で分類します。このライブラリは実装の形で分類します。ゲームのボット、ドローン、トレーディングボットは同じ形を共有します。制御ループです。こう分類すると、3 つは 1 つのコードスケッチと 1 組の現場の教訓を共有できます。どの項目にも、動かしたモデルの名前が書いてあります。そのため、Laya で得た教訓を Jev で得た教訓と取り違えることはありません。12 の形は次のとおりです。

- **[制御ループ](../../skills/building-with-decision-models/prior-art/control-loops.md)**: ゲーム、ドローン、ロボット、市場。
- **[候補から選ぶ](../../skills/building-with-decision-models/prior-art/select-from-candidates.md)**: ブラウザやスマートフォンのエージェント、LLM なしのツール呼び出し、抽出、ルーター。
- **[ゲート](../../skills/building-with-decision-models/prior-art/gates.md)**: ツール呼び出しの承認、「完了」チェック、CI、お金、コンテンツ。
- **[ストリームフィルタ](../../skills/building-with-decision-models/prior-art/stream-filters.md)**: 低品質コンテンツのフィルタ、モデレーション、メール、ログ、一括ラベル付け。
- **[ランキングとマッチング](../../skills/building-with-decision-models/prior-art/ranking-and-matching.md)**: リランカー、エンティティマッチング、グラフや分類体系の探索。
- **[ジャッジと評価](../../skills/building-with-decision-models/prior-art/judges-and-evals.md)**: ルーブリックによるジャッジ、トレースの採点、トリアージとしてのコードレビュー、モデル自体のベンチマーク。
- **[逐次処理とリアルタイム](../../skills/building-with-decision-models/prior-art/incremental-realtime.md)**: 吹き替え、音声、Web カメラ、キー入力で動くインターフェース。
- **[エージェントのコンテキストとメモリ](../../skills/building-with-decision-models/prior-art/agent-context-memory.md)**: コンパクション、メモリのゲート、止まって尋ねるかの判断、労力の制御。
- **[LLM との組み合わせ](../../skills/building-with-decision-models/prior-art/llm-pairing.md)**: プランナーとアクター、検証してからエスカレーション、モデルの階層によるルーティング、蒸留。
- **[データとしての答え](../../skills/building-with-decision-models/prior-art/research-and-features.md)**: 古典的なモデルの特徴量、研究用の測定器、分析用の列、ベンチマーク。
- **[インフラへの組み込み](../../skills/building-with-decision-models/prior-art/embedding-in-infrastructure.md)**: SQL 関数、ゲートウェイ、MCP サーバー、CI フック、Home Assistant。
- **[画像とテキスト以外の入力](../../skills/building-with-decision-models/prior-art/images-and-multimodal.md)**: スクリーンショットのゲート、画像のモデレーション、Web カメラのループ、文書。

ライブラリの横には 2 つのガイドがあります。公式パターンとクックブックのしきい値をまとめた[パターン](../../skills/building-with-decision-models/patterns.md)と、ベンチマーク、互換性、直接比較、しきい値を壊さずに新しいプロバイダーへ移る方法をまとめた[モデルの選択と切り替え](../../skills/building-with-decision-models/choosing-and-switching-models.md)です。

インデックスには、判断モデル全般で現場で失敗したアイデアも 1 行ずつ載っています。チェス、数学やコードの最終判断、学習データがすでにあるときの多数のラベル、そして鵜呑みにした較正です。ゼロショットの Laya や密なループでのホスト型 Clef-flash のように、1 つのモデルだけの失敗は `models/` にあるそのモデルのファイルにあります。失敗の記録があれば、次の作り手は同じ失敗を繰り返さずに済みます。

## 公式 TypeSafe スキルとの関係

TypeSafe は独自のスキルを [typesafe-ai/skills](https://github.com/typesafe-ai/skills) で公開しています。Jev 向けの設計の指針をまとめた 1 つのファイルです。API の詳細については、タスクのたびにエージェントを最新のドキュメントへ誘導します。2 つのスキルは名前が異なり、競合しないので、両方をインストールできます。

このスキルは、Jev だけでなくすべての判断モデルを扱います。また、スキル自体により多くを持っています。正確な API の形とプロバイダーごとの違い、クックブックのしきい値、コミュニティで見つかった失敗パターン、そして先行事例ライブラリです。エージェントはネットワークの往復なしで設計でき、他の人が先に作ったものを見られます。

判断モデルは速く変わり、毎週新しいモデルが出ています。このスキルは、2026-10-06 時点の各プロバイダーのドキュメントとコミュニティのスナップショットで、食い違いがあればプロバイダーの最新のドキュメントが優先されるとエージェントに伝えます。事実が間違っていたら、出典へのリンクを添えて issue を開いてください。

## クレジット

各 API に関する事実は、そのプロバイダーの公開ドキュメントに基づいています。TypeSafe AI のドキュメントとクックブック、Cloudflare、Perplexity、OpenAI、Databricks、Ollama、System1 Models、Uprelic、OpenRouter、Vercel、LLM Gateway、Pydantic、そしてオープンモデルの README です。先行事例は、プロジェクトを公開した作り手、Hacker News のコミュニティ、そして次のインデックスから集めました。[awesome-jev](https://github.com/yibie/awesome-jev)、[awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe)、[JevDirectory](https://www.jevdirectory.org/resources)、[awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases)、[awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev)、[amplifying.ai](https://amplifying.ai/decision-models)、[BenchLM](https://benchlm.ai/decision-models)。各形のファイルは、元のプロジェクトにリンクしています。

TypeSafe、Jev、System One は TypeSafe AI の名称です。Clef と Workers AI は Cloudflare、pplx-decider は Perplexity、その他のモデル名はそれぞれの作り手のものです。このプロジェクトは、スキルの用途を示すためだけにこれらを使っています。

## ライセンス

MIT。[LICENSE](../../LICENSE) を参照してください。
