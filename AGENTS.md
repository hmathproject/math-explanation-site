# AGENTS.md — Codex 向けプロジェクトガイダンス

このファイルは `codex exec` が自動的に読むプロジェクトガイダンスです。
**Claude Code による管理ファイル。Codex による単独変更禁止。**

---

## このリポジトリの概要

- 高校数学解説サイト（Jekyll + MathJax）の静的サイトソース
- Git remote: `https://github.com/hmathproject/math-explanation-site.git`
- 公開: Cloudflare Pages（`site/` がリポジトリルート兼公開ルート）

---

## Codex の役割

Codex は **Claude Code からの委譲タスクを実行する**役割のみ担う。

- 自律的な記事執筆・方針変更・commit/push は行わない
- Claude Code が委譲タスクの採否を決定する
- 委譲可カテゴリ以外のタスクは拒否する

---

## 実行してよいこと（委譲可 = Routing Rules B）

- `python3 scripts/quality_check.py` の実行と ERROR 集計・整理
- 機械的一括置換（FP パターン修正案の生成）
- リンク切れ・画像/PDF 実在確認
- front matter 整合確認（layout/title/permalink/description）
- sitemap.xml vs. permalink 突合
- grep / rg / diff による監査
- 定型 docs 骨子の下書き（Claude Code がレビュー・仕上げ）
- テスト/検査スクリプトの補助実装（Claude Code がレビュー後に採否）
- FP-01〜12 パターン検知・修正案提示

---

## してはいけないこと（委譲禁止 = Routing Rules C）

- 数学的内容・解法の最終判断
- 読者向け本文の最終版の文体決定
- `docs/` の source of truth の直接変更（WRITING_SYSTEM.md 等の方針変更）
- commit / push の実行
- 危険な削除・上書き（`git reset --hard`、`rm -rf` 等）
- interactive TUI の人間代行
- `AGENTS.md` 自体の変更

---

## 重要なディレクトリ構成

```
site/                          ← リポジトリルート
├── AGENTS.md                  ← このファイル
├── docs/
│   ├── WRITING_SYSTEM.md      ← 執筆ルール（source of truth）
│   ├── WORKFLOW_WEB.md        ← 実装→push パイプライン
│   ├── FAILURE_PATTERNS.md    ← 失敗パターン集 FP-01〜12
│   ├── CODEX_DELEGATION.md    ← Codex 委譲ポリシー（詳細）
│   └── ...
├── scripts/
│   ├── quality_check.py       ← 品質チェックスクリプト
│   ├── run_codex_task.sh      ← Claude Code → Codex 委譲 wrapper
│   └── ...
├── assets/
│   ├── images/                ← 公開用 PNG
│   └── pdf/                   ← 公開用 PDF
├── logs/codex/                ← 実行ログ（.gitignore 管理外）
└── manuscripts/               ← integrated_exp 形式 manuscript
```

---

## 禁止表記（公開ファイルに含めてはいけない文字列）

- 「公開中」「準備中」「解説PDF準備中」

---

## 数式記法ルール

| 種別 | 書き方 |
|---|---|
| インライン数式 | `\\( ... \\)` — 二重バックスラッシュ必須 |
| ディスプレイ数式 | `<div>\n$$\n...\n$$\n</div>` |
| Unicode 数学記号 | **直書き禁止**（≤, ≥, √, ∈ は `\leq`, `\geq`, `\sqrt{}`, `\in` を使う） |

FP-12: integrated_exp manuscript の plain text 部に ≤, ≥, √, ∈ を直書きしない。

---

## 品質チェックコマンド

```bash
# リポジトリルート（site/）から実行
python3 scripts/quality_check.py
```

ERROR は修正必須。WARNING は確認推奨。

---

## 詳細ポリシー

委譲ポリシー全文・routing rules・wrapper 使い方・ログの読み方は以下を参照:

**`docs/CODEX_DELEGATION.md`**
