# Codex 委譲ポリシー

最終更新: 2026-03-11

---

## 1. 基本モデル（1窓口運用）

- **ユーザーは Claude Code にのみ指示する**
- Claude Code が Codex 委譲を判断・実行し、結果をレビューして最終版に仕上げる
- Codex は `codex exec`（non-interactive モード）のみで使う
- TUI の擬似操作禁止。commit/push は常に Claude Code が行う

| 担当 | 責任範囲 |
|---|---|
| **Claude Code** | 記事本文・manuscript・図・PDF・導線・docs 更新・Codex 出力レビュー・commit/push |
| **Codex** | 機械的検査・修正案生成・grep/差分監査（委譲可カテゴリのみ。採否は Claude Code） |
| **ChatGPT** | 設計・レビュー・失敗分析・方針整理 |
| **ユーザー** | 数学的内容の最終確認 |

---

## 2. 実行モデル（codex non-interactive のみ）

```bash
# analyze モード（read-only 前提）
bash scripts/run_codex_task.sh analyze "質問・指示文"

# apply モード（ファイル変更あり。CODEX_APPLY_ALLOWED=1 必須）
CODEX_APPLY_ALLOWED=1 bash scripts/run_codex_task.sh apply "修正指示文"
```

| モード | 内部コマンド | 用途 |
|---|---|---|
| analyze | `codex exec --json -o <msg_file> -s read-only "prompt"` | read-only 検査・集計・監査 |
| apply | `codex exec --full-auto "prompt"` | 機械的修正の適用 |

- `--dangerously-bypass-approvals-and-sandbox` は使わない
- `--json` + `-o/--output-last-message` により最終メッセージを JSON ファイルに保存
- analyze の event log と最終メッセージは別ファイルに保存

---

## 3. Routing Rules

### A. Claude Code 主担当（委譲禁止）

- 記事本文執筆（leaf article body）
- integrated_exp manuscript 作成
- 図スクリプト作成・実行
- PDF 化（build_exp_pdf.py / pdfunite）
- 導線更新（unit top、index.md、sitemap.xml）
- docs の source of truth 更新（WRITING_SYSTEM.md 等）
- Codex 出力の final review・採否決定
- git add / commit / push

### B. Codex 委譲可

- `scripts/quality_check.py` 実行 + ERROR 集計・整理
- 機械的一括置換（FP パターン修正案の生成）
- リンク切れ・画像/PDF 実在確認
- front matter 整合確認（layout/title/permalink/description）
- sitemap.xml vs. permalink 突合
- grep / rg / diff による監査
- 定型 docs 骨子の下書き（Claude Code がレビュー・仕上げ）
- テスト/検査スクリプトの補助実装（Claude Code がレビュー後に採否）
- FP-01〜12 パターン検知・修正案提示

### C. Codex 委譲禁止

- 数学的内容・解法の最終判断
- 読者向け本文の最終版の文体決定
- docs の source of truth の直接変更
- commit / push の最終判断
- 危険な削除・上書き（`git reset --hard`、`rm -rf` 等）
- interactive TUI の人間代行

---

## 4. wrapper の使い方

### インストール確認

```bash
which codex          # /opt/homebrew/bin/codex 等が返ればOK
codex exec --help    # フラグ確認
```

### analyze モード（read-only）

```bash
bash scripts/run_codex_task.sh analyze "プロンプト"

# --prompt-file でファイルからプロンプトを読む場合
bash scripts/run_codex_task.sh analyze --prompt-file path/to/prompt.txt
```

### apply モード（ファイル変更あり）

```bash
CODEX_APPLY_ALLOWED=1 bash scripts/run_codex_task.sh apply "修正指示文"
```

apply 後は**必ず** Claude Code が以下で差分確認する:

```bash
git diff --stat        # 変更ファイル一覧
git diff               # 必要なら差分詳細
# 問題なければ git add / commit / push
# 問題があれば git checkout -- . で差し戻し
```

---

## 5. ログの場所と読み方

| ファイル | 内容 |
|---|---|
| `logs/codex/YYYYMMDD_HHMMSS_analyze_events.log` | analyze の event log（stdout） |
| `logs/codex/YYYYMMDD_HHMMSS_analyze_message.json` | analyze の最終メッセージ（JSON） |
| `logs/codex/YYYYMMDD_HHMMSS_apply_events.log` | apply の event log（stdout） |

- `logs/` は `.gitignore` 管理外（ローカル専用）
- `run_codex_task.sh` が `logs/codex/` を自動生成する（mkdir 不要）
- exit_code が最終行に記録される（`exit_code=0` なら成功）

---

## 6. 失敗時の復旧手順

### analyze 失敗

```bash
# ログを確認
cat logs/codex/YYYYMMDD_HHMMSS_analyze_events.log
# 原因を特定してプロンプトを修正し再実行
```

### apply 失敗・想定外変更

```bash
git diff --stat        # 何が変わったか確認
git checkout -- .      # 変更を差し戻し（コミット前のみ）
# または個別ファイルを差し戻し
git checkout -- path/to/file.md
```

### codex 未インストール / フラグ不一致

```bash
# wrapper の CODEX_ANALYZE_FLAGS / CODEX_APPLY_FLAGS を確認・調整
# または CODEX_CMD を環境変数でオーバーライド
CODEX_CMD=/path/to/codex bash scripts/run_codex_task.sh analyze "..."
```

---

## 7. push 前の最小コマンド

```bash
python3 scripts/quality_check.py
```

apply モード使用後は追加で:

```bash
git diff --stat
```

---

## 8. 委譲タスクの例（用途別コマンド）

### quality_check.py の ERROR を集計して報告

```bash
bash scripts/run_codex_task.sh analyze \
  "Run python3 scripts/quality_check.py from the repo root and summarize all ERRORs by file."
```

### FP-01〜12 パターン検知・修正案提示

```bash
bash scripts/run_codex_task.sh analyze \
  "Search for FP-01 to FP-12 patterns per docs/FAILURE_PATTERNS.md. List each match with file path and line number. Propose fixes."
```

### sitemap.xml と permalink の突合

```bash
bash scripts/run_codex_task.sh analyze \
  "Compare sitemap.xml <loc> entries with permalink values in all .md files. Report any missing or extra entries."
```

### front matter 整合確認

```bash
bash scripts/run_codex_task.sh analyze \
  "Check all .md files in the repo root for required front matter fields: layout, title, permalink, description. Report any missing."
```

### Unicode 数学記号の検知（FP-12）

```bash
bash scripts/run_codex_task.sh analyze \
  "Search for Unicode math symbols (≤, ≥, √, ∈) in all manuscripts/ files. List each match with file and line number."
```
