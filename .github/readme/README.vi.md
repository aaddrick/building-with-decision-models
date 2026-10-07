<p align="center">
  <strong>Building with Decision Models</strong><br>
  <em>Quyết định có kiểu với độ tin cậy đã hiệu chỉnh, dành cho tác nhân lập trình của bạn.</em><br>
  <em>Jev, Clef, pplx-decider, ai_decide, Ollama và nhiều model khác. Hơn 450 dự án liên kết, xếp theo dạng.</em>
</p>

<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/aaddrick/building-with-decision-models?style=flat" alt="License"></a>
  <a href="../workflows/checks.yml"><img src="https://img.shields.io/github/actions/workflow/status/aaddrick/building-with-decision-models/checks.yml?label=checks&style=flat" alt="Checks"></a>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aaddrick/">Kết nối trên LinkedIn!</a>
</p>

<p align="center">
  <a href="../../README.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <strong>Tiếng Việt</strong> ·
  <a href="README.pt-BR.md">Português (BR)</a> ·
  <a href="README.it.md">Italiano</a>
</p>

> [!NOTE]
> Đây là một skill không chính thức do cộng đồng làm. TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, AWS, Ollama và mọi nhà cung cấp khác mà nó đề cập đều không làm, không duyệt và không bảo trợ nó. Xem [Liên hệ với skill chính thức của TypeSafe](#liên-hệ-với-skill-chính-thức-của-typesafe).

Các tác nhân lập trình đối xử với decision model như thêm một chat model nữa. Skill này dạy chúng thiết kế cho đúng loại model này: câu hỏi có kiểu, độ tin cậy đã hiệu chỉnh, khác biệt giữa các nhà cung cấp, và liên kết tới hơn 450 dự án cộng đồng, xếp theo cách chúng hoạt động, mỗi mẫu có một bản phác thảo code. Nó cài được trong Claude Code, Codex, Antigravity CLI, Muse và Muse Code.

Một decision model, còn gọi là model [System One](https://docs.typesafe.ai/concepts/system-one), không viết văn bản. Bạn gửi cho nó một nội dung cùng một bộ câu hỏi có kiểu, và nó trả lời mỗi câu hỏi bằng một giá trị kèm xác suất, thường trong vài trăm mili giây hoặc ít hơn:

- **Choice** chọn một lựa chọn từ một danh sách. Ví dụ: định tuyến một ticket tới billing, shipping hoặc support.
- **Score** đặt nội dung lên một thang đo mà bạn mô tả. Ví dụ: chấm một pull request từ "bỏ qua spec" tới "đáp ứng spec".
- **Noul** cho biết xác suất một mệnh đề có/không là đúng. Ví dụ: "lệnh shell này xóa file nằm ngoài dự án."

[Jev](https://docs.typesafe.ai/introduction) của TypeSafe mở ra hạng mục này vào ngày 2026-09-15. Chỉ trong ba tuần, những bên khác đã phát hành các model dùng cùng ba kiểu câu hỏi:

| Loại | Model | Cách gọi |
|---|---|---|
| Được host | TypeSafe Jev, Cloudflare Clef và Clef-flash, Perplexity pplx-decider, OpenAI Decisions API (`gpt-6-luna`), System1 Models, Strom | HTTP API, mỗi bên một key riêng |
| Trong kho dữ liệu của bạn | Databricks `ai_decide()` | Hàm SQL hoặc REST |
| Trên máy của bạn | Nimble và Tev1 qua Ollama, Kev, Laya, Strands Decider, CLM-8B | Server cục bộ, không cần key |
| Qua một gateway | OpenRouter, Vercel AI Gateway, LLM Gateway, Pydantic AI | Một key hoặc một client cho nhiều model |

Chúng chia sẻ ý tưởng, nhưng không phải lúc nào cũng chung định dạng dữ liệu, và không chung độ chính xác. Skill cung cấp cho tác nhân các quy tắc chung, một file tham chiếu cho mỗi nhà cung cấp, và bằng chứng thực tế về model nào làm tốt việc gì.

## Cài đặt

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add aaddrick/building-with-decision-models
```

```bash
claude plugin install building-with-decision-models@building-with-decision-models
```

Skill tự tải khi bạn làm việc với code dùng decision model. Muốn tải thủ công, hãy gõ:

```
/building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Claude Desktop, Cowork và claude.ai</strong></summary>

**Bước 1.** Mở **Customize > Plugins**, chọn **Add**, rồi **Add marketplace**.

<img src="../assets/plugin-marketplace/step-1.png" alt="Trang Plugins trong Customize với menu Add đang mở. Khung và mũi tên màu hổ phách chỉ vào Add marketplace." width="100%">

**Bước 2.** Chọn **Add from a repository**.

<img src="../assets/plugin-marketplace/step-2.png" alt="Hộp thoại Add marketplace. Khung và mũi tên màu hổ phách chỉ vào Add from a repository." width="100%">

**Bước 3.** Nhập `aaddrick/building-with-decision-models` hoặc URL GitHub đầy đủ, rồi chọn **Sync**. Nếu hộp thoại có **Sync automatically**, hãy giữ nó bật để plugin cập nhật khi repo này cập nhật.

<img src="../assets/plugin-marketplace/step-3.png" alt="Hộp thoại Add marketplace với https://github.com/aaddrick/building-with-decision-models trong ô URL. Khung và mũi tên màu hổ phách chỉ vào ô URL và nút Sync." width="100%">

**Bước 4.** Chọn **Add** cạnh **Building with decision models**.

<img src="../assets/plugin-marketplace/step-4.png" alt="Danh sách Discover hiển thị Building with decision models. Khung và mũi tên màu hổ phách chỉ vào nút Add của nó." width="100%">

**Bước 5.** Nút chuyển thành **Added** và danh sách hiện phiên bản. Plugin cũng xuất hiện trong ứng dụng desktop và Cowork trên cùng tài khoản.

<img src="../assets/plugin-marketplace/step-5.png" alt="Danh sách Discover hiện Building with decision models v0.1.0 với nút Added. Khung và mũi tên màu hổ phách chỉ vào Added." width="100%">

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add aaddrick/building-with-decision-models
```

```bash
codex plugin add building-with-decision-models@building-with-decision-models
```

Mở một thread mới. Codex tải skill khi tác vụ phù hợp. Muốn tải thủ công, hãy gõ:

```
$building-with-decision-models:building-with-decision-models
```

</details>

<details>
<summary><strong>Antigravity CLI</strong></summary>

```bash
agy plugin install https://github.com/aaddrick/building-with-decision-models
```

Kiểm tra xem nó đã được cài chưa:

```bash
agy plugin list
```

Bắt đầu một phiên mới. Antigravity CLI tải skill khi tác vụ phù hợp. Muốn tải thủ công, hãy gõ:

```
/building-with-decision-models:building-with-decision-models
```

Chuyển từ Gemini CLI sang? Nếu `agy plugin import gemini` đã mang extension này qua, bạn vẫn nên chạy lệnh cài đặt ở trên để bản hiện tại thay thế bản đã import.

</details>

<details>
<summary><strong>Muse (muse.ai)</strong></summary>

Muse nạp skill từ `~/workspace/skills/` trên máy tính riêng của nó. Dán lệnh này vào một cuộc trò chuyện với Muse và yêu cầu Muse chạy nó:

```bash
curl -fsSL https://raw.githubusercontent.com/aaddrick/building-with-decision-models/main/scripts/install_muse.sh | bash
```

Script sao chép thư mục skill vào đó và viết lại phần đầu của `SKILL.md` theo dạng Muse đọc được. Mở một cuộc trò chuyện mới. Muse nạp skill khi tác vụ phù hợp. Để cập nhật, chạy lại lệnh.

</details>

<details>
<summary><strong>Muse Code</strong></summary>

Sao chép (clone) repository:

```bash
git clone https://github.com/aaddrick/building-with-decision-models.git
```

Cài skill cho mọi dự án:

```bash
muse skills install building-with-decision-models/skills/building-with-decision-models --scope user
```

Kiểm tra đã cài xong:

```bash
muse skills list
```

Bắt đầu một phiên mới. Muse Code tải skill khi tác vụ phù hợp. Muốn tải thủ công, hãy gõ:

```
/building-with-decision-models
```

</details>

<details>
<summary><strong>Tác nhân khác có đọc SKILL.md</strong></summary>

Sao chép thư mục `skills/building-with-decision-models/` vào thư mục skill của tác nhân. Giữ nguyên cả thư mục. `SKILL.md` liên kết tới các file nằm cạnh nó.

</details>


## Kết nối một model (không bắt buộc, nên có)

Skill vẫn hoạt động khi không kết nối model nào. Khi có một model, tác nhân có thể kiểm tra thiết kế của nó với một endpoint thật trước khi code tới dự án của bạn. Cách này bắt được tên trường sai, và những câu hỏi mà model hiểu khác với ý bạn.

<details>
<summary><strong>Cục bộ, miễn phí, không cần key</strong> (Ollama)</summary>

<br>

Cài [Ollama](https://ollama.com/download) bản 0.35 trở lên, rồi tải một decision model:

```bash
ollama pull nimble
```

Kiểm tra xem tác nhân có kết nối tới nó được không:

```bash
curl -s http://localhost:11434/api/version
```

Một model cục bộ kiểm tra dạng request miễn phí. Độ chính xác và hiệu chỉnh của nó không giống một model được host, nên skill dặn tác nhân không sao chép ngưỡng giữa hai loại.

</details>

<details>
<summary><strong>Được host: key nào vào biến nào</strong></summary>

<br>

| Nhà cung cấp | Biến | Lấy key |
|---|---|---|
| TypeSafe Jev | `TYPESAFE_API_KEY` | [console.typesafe.ai](https://console.typesafe.ai/) (các bước bên dưới) |
| Cloudflare Clef | `CLOUDFLARE_AUTH_TOKEN` và `CLOUDFLARE_ACCOUNT_ID` | Bảng điều khiển Cloudflare, Workers AI |
| Perplexity pplx-decider | `PERPLEXITY_API_KEY` | Cài đặt API của Perplexity |
| OpenAI Decisions API | `OPENAI_API_KEY` | Nền tảng OpenAI |
| System1 Models | `SYSTEM1_API_KEY` | system1models.ai |
| Strom (Uprelic) | `UPRELIC_API_KEY` | platform.uprelic.com |
| OpenRouter | `OPENROUTER_API_KEY` | openrouter.ai |
| Vercel AI Gateway | `AI_GATEWAY_API_KEY` | Bảng điều khiển Vercel |
| LLM Gateway | `LLM_GATEWAY_API_KEY` | llmgateway.io |
| Databricks `ai_decide` | Thông tin xác thực workspace của bạn | Workspace Databricks (SQL warehouse không cần key trong shell của tác nhân) |

Mỗi file nhà cung cấp trong `skills/building-with-decision-models/providers/` nêu tên biến của nó và cách gọi. Lưu key theo cách phần tiếp theo hướng dẫn.

</details>

<details>
<summary><strong>Tạo, lưu trữ và xử lý sự cố key</strong></summary>

<br>

<details>
<summary><strong>Ví dụ: tạo một key TypeSafe</strong> (bốn bước trong console TypeSafe)</summary>

**Bước 1.** Đăng nhập tại [console.typesafe.ai](https://console.typesafe.ai/) và mở **API Keys** ở thanh bên.

<img src="../assets/api-key/step-1.png" alt="Trang chủ console TypeSafe. Một khung và mũi tên màu hổ phách chỉ vào API Keys ở thanh bên trái." width="100%">

**Bước 2.** Nhấn **Create key** ở góc trên bên phải.

<img src="../assets/api-key/step-2.png" alt="Trang API keys. Các key hiện có bị làm mờ. Một khung và mũi tên màu hổ phách chỉ vào nút Create key ở góc trên bên phải." width="100%">

**Bước 3.** Đặt tên key theo nơi nó sẽ được dùng, chẳng hạn tên máy hoặc tên tác nhân. Sau đó nhấn **Create key**.

<img src="../assets/api-key/step-3.png" alt="Hộp thoại Create API key với tên my-coding-agent đã được nhập. Một khung và mũi tên màu hổ phách chỉ vào ô tên và nút Create key." width="100%">

**Bước 4.** Sao chép key ngay bây giờ. Console chỉ hiển thị nó một lần. Nếu làm mất, hãy tạo key mới và thu hồi key cũ.

<img src="../assets/api-key/step-4.png" alt="Hộp thoại API key created. Giá trị key bị che. Một khung và mũi tên màu hổ phách chỉ vào nút Copy." width="100%">

</details>

<details>
<summary><strong>Lưu trữ key</strong> (macOS, Linux, Windows)</summary>

Giữ các key trong một file mà chỉ bạn đọc được, mỗi nhà cung cấp một dòng `export`. Các lệnh bên dưới lấy `TYPESAFE_API_KEY` làm ví dụ. Với nhà cung cấp khác, hãy dùng biến của nó trong bảng ở trên, và thêm một dòng vào cùng file đó thay vì tạo file mới. Tác nhân thường khởi động shell mà không có terminal, nên mỗi phần dưới đây đặt key ở nơi các shell đó nhìn thấy được. Chọn hệ thống của bạn.

<details>
<summary><strong>macOS</strong> (zsh, shell mặc định)</summary>

Lưu key vào một file riêng:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Nạp nó từ `~/.zshenv`. Mọi zsh đều đọc file này, kể cả các shell mà tác nhân khởi động không có terminal. `~/.zshrc` chỉ được đọc bởi shell tương tác.

```bash
echo '[ -f ~/.config/decision-models/env ] && . ~/.config/decision-models/env' >> ~/.zshenv
```

Mở một terminal mới và kiểm tra. Lệnh này in ra độ dài của key, không in key:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux với bash</strong> (Ubuntu, Debian, Mint, Fedora, Arch)</summary>

Lưu key vào một file riêng:

```bash
mkdir -p ~/.config/decision-models && umask 077 && printf 'export TYPESAFE_API_KEY=%s\n' 'YOUR_KEY' >> ~/.config/decision-models/env
```

Nạp nó ở **đầu** `~/.bashrc`. Ubuntu, Debian, Mint và Arch mở đầu `~/.bashrc` bằng một dòng dừng sớm khi không có terminal. Một dòng nằm dưới điều kiện đó sẽ không bao giờ chạy với shell của tác nhân. Đầu file thì an toàn trên mọi bản phân phối:

```bash
sed -i '1i [ -f ~/.config/decision-models/env ] \&\& . ~/.config/decision-models/env' ~/.bashrc
```

Mở một terminal mới và kiểm tra:

```bash
echo ${#TYPESAFE_API_KEY}
```

</details>

<details>
<summary><strong>Linux với zsh</strong></summary>

Làm theo các bước cho macOS. zsh đọc `~/.zshenv` theo cùng cách trên Linux.

</details>

<details>
<summary><strong>Linux với fish</strong></summary>

fish đọc mọi file trong `~/.config/fish/conf.d/`, dù có terminal hay không:

```fish
mkdir -p ~/.config/fish/conf.d; and echo 'set -gx TYPESAFE_API_KEY YOUR_KEY' >> ~/.config/fish/conf.d/decision-models.fish; and chmod 600 ~/.config/fish/conf.d/decision-models.fish
```

```fish
string length -- $TYPESAFE_API_KEY
```

</details>

<details>
<summary><strong>Windows</strong> (PowerShell)</summary>

Lưu key dưới dạng biến môi trường người dùng. Terminal và ứng dụng mới sẽ thấy nó. Terminal đang mở thì không:

```powershell
[Environment]::SetEnvironmentVariable('TYPESAFE_API_KEY', 'YOUR_KEY', 'User')
```

Mở một terminal mới và kiểm tra:

```powershell
$env:TYPESAFE_API_KEY.Length
```

**WSL:** Theo mặc định, biến của Windows không truyền vào WSL. Bên trong WSL, hãy làm theo các bước cho Linux với bash.

</details>

<details>
<summary><strong>Ứng dụng desktop và tiện ích mở rộng IDE</strong></summary>

Ứng dụng bạn khởi động từ dock, start menu hay trình khởi chạy desktop không đọc các file shell của bạn.

- **Windows:** biến môi trường người dùng ở trên đã bao gồm các ứng dụng này.
- **Linux (systemd):** thêm dòng `TYPESAFE_API_KEY=YOUR_KEY` vào `~/.config/environment.d/decision-models.conf`, rồi đăng xuất và đăng nhập lại.
- **macOS:** khởi động ứng dụng từ terminal, hoặc đặt biến trong phần cài đặt riêng của ứng dụng. macOS không có file đơn giản theo từng người dùng mà ứng dụng desktop đọc.

</details>

</details>

<details>
<summary><strong>Nếu tác nhân không thấy key</strong></summary>

Yêu cầu tác nhân chạy `echo ${#TYPESAFE_API_KEY}` (hoặc `$env:TYPESAFE_API_KEY.Length` trên Windows), thay `TYPESAFE_API_KEY` bằng biến của nhà cung cấp bạn dùng. Nếu nó in ra `0` hoặc không in gì, hãy kiểm tra lần lượt:

- **Bạn khởi động tác nhân trước khi lưu key.** Shell của tác nhân sao chép môi trường của chương trình đã khởi động chúng. Thoát tác nhân và khởi động lại từ một terminal mới.
- **Bạn khởi động tác nhân từ dock, start menu hoặc một IDE.** Các ứng dụng đó không đọc các file shell của bạn. Xem "Ứng dụng desktop và tiện ích mở rộng IDE" ở trên.
- **Codex lọc môi trường.** Nếu `~/.codex/config.toml` đặt `include_only` trong `[shell_environment_policy]`, hãy thêm biến của bạn vào đó. Nếu nó đặt `ignore_default_excludes = false`, Codex bỏ mọi biến có `KEY` hoặc `TOKEN` trong tên. Hãy xóa dòng đó.
- **WSL.** Biến của Windows không truyền vào WSL. Hãy lưu key bên trong WSL theo các bước cho Linux.

</details>

</details>

## Bên trong có gì

Skill tải theo từng lớp, nên tác nhân chỉ đọc những gì tác vụ cần.

| File | Nội dung | Khi nào tác nhân đọc |
|---|---|---|
| `SKILL.md` | Chọn nhà cung cấp và primitive nào, 11 quy tắc thiết kế, cách dùng xác suất và độ tin cậy, cách đổi model an toàn, các lỗi thường gặp | Mọi tác vụ dùng decision model |
| `providers/jev.md` | Hợp đồng tham chiếu `/v1/systemone`: HTTP API, SDK Python và JavaScript, giới hạn, lỗi, biến môi trường | Khi viết code |
| `providers/*.md` | 10 file nhà cung cấp (Clef, Perplexity, OpenAI, Databricks, Ollama và Kev, các host ở EU, gateway, Pydantic AI, model open-weight): mỗi bên khác Jev thế nào, kèm nguồn | Khi nhắm tới nhà cung cấp đó |
| `models/*.md` | 9 file model (Clef, Nimble, Laya, Kev, CLM-8B, pplx-decider, GPT-6 Luna, Strands Decider và các model còn lại) cùng một file chỉ mục: các giới hạn gặp phải khi dùng thực tế, độ hiệu chỉnh, mỗi model làm tốt và thất bại ở đâu, và ghi chú theo từng dạng | Khi chạy trên một model không phải Jev |
| `patterns.md` | 4 pattern chính thức và các kỹ thuật từ 18 cookbook, kèm ngưỡng của chúng | Khi thiết kế một workflow |
| `choosing-and-switching-models.md` | Cách so sánh model, chỉnh lại ngưỡng, chạy thử song song (shadow) rồi chuyển đổi, kèm bài học từ những người đã đổi model và các benchmark hiện có | Khi chọn, so sánh hoặc đổi model |
| `prior-art/INDEX.md` | Bản đồ từ "thứ tôi muốn làm" tới một dạng, cùng tiêu đề một dòng của các ý tưởng đã thất bại trên mọi model | Trước khi thiết kế thứ gì mới |
| `prior-art/bad-fits.md` | Mọi ý tưởng đã thất bại trên bất kỳ model nào, kèm bằng chứng và liên kết. Thất bại chỉ của một model nằm trong file `models/` của model đó | Khi một thiết kế giống một trường hợp không phù hợp đã biết |
| `prior-art/*.md` | 12 file dạng: một đoạn code mẫu, bài học thực tế đúng với mọi model, và hai hoặc ba dự án tiêu biểu, mỗi dự án gắn nhãn model của nó | Một hoặc hai file cho mỗi thiết kế |
| `prior-art/projects/*.md` | Danh sách đầy đủ các dự án liên kết cho từng dạng, nhóm theo loại con, mỗi dự án gắn nhãn model của nó | Khi cần thêm ví dụ |
| `prior-art/more-indexes.md` | Các danh mục bên ngoài lớn hơn về dự án và benchmark decision model | Khi thư viện không có mục phù hợp |

## Thư viện tham khảo

Hầu hết các danh mục xếp dự án theo ngành. Thư viện này xếp chúng theo dạng triển khai. Một bot chơi game, một drone và một bot giao dịch có chung một dạng: vòng điều khiển. Xếp theo cách đó, cả ba dùng chung một đoạn code mẫu và một bộ bài học thực tế. Mỗi mục đều nêu model mà nó đã chạy, để một bài học rút ra trên Laya không bị nhầm với bài học rút ra trên Jev. 12 dạng:

- **[Vòng điều khiển](../../skills/building-with-decision-models/prior-art/control-loops.md)**: game, drone, robot, thị trường.
- **[Chọn từ các ứng viên](../../skills/building-with-decision-models/prior-art/select-from-candidates.md)**: tác nhân trình duyệt và điện thoại, gọi công cụ không cần LLM, trích xuất, bộ định tuyến.
- **[Cổng kiểm soát](../../skills/building-with-decision-models/prior-art/gates.md)**: duyệt lệnh gọi công cụ, kiểm tra "đã xong", CI, tiền, nội dung.
- **[Bộ lọc luồng](../../skills/building-with-decision-models/prior-art/stream-filters.md)**: lọc nội dung rác, kiểm duyệt, email, log, gán nhãn hàng loạt.
- **[Xếp hạng và so khớp](../../skills/building-with-decision-models/prior-art/ranking-and-matching.md)**: reranker, so khớp thực thể, duyệt đồ thị và phân loại.
- **[Giám khảo và đánh giá](../../skills/building-with-decision-models/prior-art/judges-and-evals.md)**: giám khảo theo rubric, chấm trace, review code để phân loại, benchmark cho chính các model.
- **[Tăng dần và thời gian thực](../../skills/building-with-decision-models/prior-art/incremental-realtime.md)**: lồng tiếng, giọng nói, webcam, giao diện chạy theo phím gõ.
- **[Ngữ cảnh và bộ nhớ của tác nhân](../../skills/building-with-decision-models/prior-art/agent-context-memory.md)**: nén ngữ cảnh, cổng bộ nhớ, quyết định dừng lại và hỏi, điều chỉnh mức nỗ lực.
- **[Kết hợp với LLM](../../skills/building-with-decision-models/prior-art/llm-pairing.md)**: planner và actor, kiểm tra rồi mới chuyển lên, định tuyến theo tầng model, chưng cất (distillation).
- **[Câu trả lời là dữ liệu](../../skills/building-with-decision-models/prior-art/research-and-features.md)**: đặc trưng cho model cổ điển, công cụ nghiên cứu, cột phân tích, benchmark.
- **[Nhúng vào hạ tầng](../../skills/building-with-decision-models/prior-art/embedding-in-infrastructure.md)**: hàm SQL, gateway, server MCP, hook CI, Home Assistant.
- **[Hình ảnh và đầu vào không phải văn bản](../../skills/building-with-decision-models/prior-art/images-and-multimodal.md)**: cổng kiểm tra ảnh chụp màn hình, kiểm duyệt hình ảnh, vòng lặp webcam, tài liệu.

Bên cạnh thư viện có hai hướng dẫn: [mẫu thiết kế](../../skills/building-with-decision-models/patterns.md) gồm các mẫu chính thức và ngưỡng từ cookbook, và [chọn và đổi model](../../skills/building-with-decision-models/choosing-and-switching-models.md) gồm benchmark, khả năng tương thích, so sánh trực tiếp, và cách chuyển sang nhà cung cấp mới mà không làm hỏng ngưỡng.

Chỉ mục cũng liệt kê, mỗi mục một dòng, các ý tưởng đã thất bại trong thực tế với decision model nói chung: cờ vua, phán quyết cuối cùng về toán hoặc code, quá nhiều nhãn khi bạn đã có dữ liệu huấn luyện, và tin vào hiệu chỉnh mà không kiểm tra. Thất bại chỉ của một model, như Laya zero-shot hay Clef-flash được host trong vòng lặp chặt, nằm trong file của model đó ở `models/`. Một lần thử thất bại giúp người làm sau khỏi lặp lại nó.

## Liên hệ với skill chính thức của TypeSafe

TypeSafe công bố skill riêng tại [typesafe-ai/skills](https://github.com/typesafe-ai/skills). Đó là một tệp hướng dẫn thiết kế cho Jev. Với chi tiết API, nó đưa tác nhân tới tài liệu trực tuyến ở mọi tác vụ. Hai skill có tên khác nhau và không xung đột, nên bạn có thể cài cả hai.

Skill này bao gồm mọi decision model, không chỉ Jev. Nó chứa nhiều hơn ngay bên trong: hình dạng chính xác của API và khác biệt giữa các nhà cung cấp, các ngưỡng từ cookbook, các lỗi mà cộng đồng gặp phải, và thư viện tham khảo. Tác nhân có thể thiết kế mà không cần gọi mạng, và xem những gì người khác đã làm trước.

Decision model thay đổi nhanh, và tuần nào cũng có model mới. Skill là bản chụp tài liệu của các nhà cung cấp và của cộng đồng vào ngày 2026-10-06, và nó bảo tác nhân rằng tài liệu trực tuyến của nhà cung cấp luôn đúng hơn khi có mâu thuẫn. Nếu một sự thật bị sai, hãy mở issue kèm liên kết tới nguồn.

## Ghi công

Các sự thật về mỗi API lấy từ tài liệu công khai của nhà cung cấp đó: tài liệu và cookbook của TypeSafe AI, Cloudflare, Perplexity, OpenAI, Databricks, Ollama, System1 Models, Uprelic, OpenRouter, Vercel, LLM Gateway, Pydantic, và README của các model mở. Phần tham khảo đến từ những người đã công bố dự án của mình, từ cộng đồng Hacker News, và từ các chỉ mục sau: [awesome-jev](https://github.com/yibie/awesome-jev), [awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe), [JevDirectory](https://www.jevdirectory.org/resources), [awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases), [awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev), [amplifying.ai](https://amplifying.ai/decision-models), và [BenchLM](https://benchlm.ai/decision-models). Mỗi file dạng đều liên kết tới các dự án gốc.

TypeSafe, Jev và System One là tên của TypeSafe AI. Clef và Workers AI thuộc về Cloudflare, pplx-decider thuộc về Perplexity, và mọi tên model khác thuộc về bên tạo ra nó. Dự án này chỉ dùng chúng để nói skill dùng cho việc gì.

## Giấy phép

MIT. Xem [LICENSE](../../LICENSE).
