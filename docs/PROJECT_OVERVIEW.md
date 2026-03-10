# PROJECT_OVERVIEW.md — 数学解説サイトの入口

このファイルは、この repo の全体構想・制作方針・参照順を最初に把握するための入口です。
チャットが変わったときや、新規記事・図・PDF・導線更新に着手する前にまず確認してください。

---

## このサイトの目的

- 高校数学を、グラフと言葉で「なぜ」から理解できる静的解説サイトとして公開する
- leaf 記事・単元トップ・カテゴリトップ・PDF を一体で整備し、公開導線まで含めて更新する
- Codex / Claude Code は manuscript・記事本文・図・PDF・導線更新まで主担当とする

---

## 正本カテゴリ

- **正本は二次関数カテゴリ**
- 指数・対数、三角関数は二次関数カテゴリの書き方・導線・見出し設計に合わせる
- 新しいカテゴリや単元を作るときは、まず二次関数の既存公開ページを参照して揃える

---

## 記事の3類型

| 型 | 使う場面 | 代表記事 |
|---|---|---|
| グラフ主役型 | 図を見ると「なぜ場合分けが必要か」が分かる問題 | `quadratic-min-fixed-range.md` |
| 定義・概念型 | 定義や条件の意味を段階的に説明する問題 | `log-definition.md` |
| 計算・性質型 | 手順だけでなく「なぜこの方法か」を説明する問題 | `quadratic-determine-3points.md` |

leaf 記事を新規作成するときは、まず類型を選んでから `ARTICLE_TEMPLATE.md` を読む。

---

## ページ種別ごとの基本方針

### leaf 記事

- 「なぜ」の説明を計算・手順より前に置く
- PDF が実在する場合のみ末尾に `## もっと練習したい方へ` を置く
- bottom nav / breadcrumb は公開済みページだけに張る

### unit top

- `## この単元で学ぶこと` は「なぜ〇〇か」の問い形式で書く
- `## 解説記事` に公開済み leaf をすべて載せる
- PDF セクション名は `## 解説PDFについて`

### category top / home

- 公開面の表記は `全〇単元・〇〇記事・解説PDF付き` に固定する
- 指数・対数、三角関数も二次関数カテゴリと同じ見せ方に揃える

---

## PDF と画像の扱い

- 公開用画像は `assets/images/`、公開用 PDF は `assets/pdf/`
- 図生成スクリプトは `scripts/`、作業用画像は `figures/`
- PDF ボタンや画像参照は、公開用ファイルの実在確認後にのみ書く
- 未生成の PDF を前提に「準備中」導線を残さない

---

## push 前の最小コマンド

```bash
python3 scripts/quality_check.py
```

公開ページの front matter、禁止表記、内部リンク、画像/PDF 実在、sitemap 整合、数式崩れを最小限で検査する。

---

## チーム役割分担

| 担当 | 役割 |
|---|---|
| **Claude Code** | 記事本文・manuscript・図・PDF・導線更新まで主担当。既存 manuscripts のフォーマットを参照して自律的に完結する |
| **Codex** | 機械的検査・修正案生成・grep/差分監査（Claude Code が委譲・レビュー・採否決定） |
| **ChatGPT** | 設計・レビュー・失敗分析・方針整理（manuscript 作成は担当しない） |
| **ユーザー** | 数学的内容の最終確認（数式ミスがないか） |

---

## 次に何を読むか

1. 全体構想と役割分担: `PROJECT_OVERVIEW.md`
2. 記事執筆の入口: `WRITING_SYSTEM.md`
3. 公開フローと実装手順: `WORKFLOW_WEB.md`
4. leaf 記事の型選択: `ARTICLE_TEMPLATE.md`
5. 単元トップ更新: `UNIT_TOP_TEMPLATE.md`
6. 執筆後の確認: `WRITING_CHECKLIST.md`
7. 既知の失敗例: `FAILURE_PATTERNS.md`
8. Codex 向けガイダンス: `AGENTS.md`
9. Codex 委譲ポリシー（routing rules・wrapper・ログ）: `docs/CODEX_DELEGATION.md`
