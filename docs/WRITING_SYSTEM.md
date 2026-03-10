# 数学サイト 執筆システム概要

このファイルは Claude Code が新記事を執筆するたびに最初に参照する入口です。

---

## Claude Code の役割

| 担当 | 役割 |
|---|---|
| Claude Code | **記事本文・manuscript・図・PDF・導線更新まで主担当**。既存 manuscripts のフォーマットを参照して自律的に完結する |
| ChatGPT | 設計・レビュー・失敗分析・方針整理（integrated_exp manuscript の作成は担当しない） |
| ユーザー | 数学的内容の最終確認（数式ミスがないか） |

---

## 新記事執筆時の参照順

1. **このファイル（WRITING_SYSTEM.md）** — 全体を把握する
2. **`ARTICLE_TEMPLATE.md`** — 3類型から型を選び、テンプレートを適用する
3. **`FAILURE_PATTERNS.md`** — 既知の失敗を犯していないか確認する
4. **`WRITING_CHECKLIST.md`** — 執筆後に自己検査する
5. **`UNIT_TOP_TEMPLATE.md`** — 単元トップを更新するとき
6. **`WORKFLOW_WEB.md` の §11** — 執筆フロー全体を確認するとき

---

## 記事の3類型（選択方法）

新記事を書く前に、次の表から型を選ぶ。

| 型 | 選ぶ条件 | 代表記事 |
|---|---|---|
| **グラフ主役型** | グラフを見ることで「なぜ場合分けが必要か」が分かる | quadratic-min-fixed-range.md |
| **定義・概念型** | 定義の条件ごとに「なぜ必要か」を掘り下げる | log-definition.md |
| **計算・性質型** | 「なぜこの形式/手法を使うか」を問い、手順を示す | quadratic-determine-3points.md |

詳細なテンプレートは `ARTICLE_TEMPLATE.md` を参照。

---

## 絶対ルール（どの型でも共通）

- **「なぜ」の説明を計算セクションより前に置く**
- `## まとめ` の見出しに括弧書きをしない（`## まとめ（a>0 の場合）` は禁止）
- `## もっと練習したい方へ` が leaf 記事の PDF セクション標準名（unit top は `## 解説PDFについて`、両者は別名で使い分ける）
- PDF ボタンは `ls site/assets/pdf/[unit-slug]-pack.pdf` で local ファイルの実在確認後にのみ書く
- 未公開記事への nav リンクは書かない
- 「準備中」「公開中」「解説PDF準備中」を残さない

---

## サイト構成の数値（2026-03-10 時点）

| 種別 | 本数 |
|---|---|
| leaf 記事 | 44 本 |
| 単元トップ | 14 本 |
| カテゴリトップ | 3 本 |
| ホーム | 1 本 |
| 合計 | 62 ページ |

---

## 関連 docs 一覧

| ファイル | 内容 |
|---|---|
| `ARTICLE_TEMPLATE.md` | leaf 記事の3類型テンプレート（骨格・各セクションの書き方） |
| `UNIT_TOP_TEMPLATE.md` | 単元トップの標準骨格 |
| `WRITING_CHECKLIST.md` | 執筆後の自己検査リスト（13 項目） |
| `FAILURE_PATTERNS.md` | 失敗パターン集（FP-01〜FP-11） |
| `WORKFLOW_WEB.md` §11 | Claude Code 主体執筆フロー |
