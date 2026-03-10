# 失敗パターン集

全公開記事（2026-03-10 時点: 29 leaf + 9 単元トップ + 2 カテゴリトップ）の全件査読から抽出した失敗パターンです。
新記事を執筆するたびに、このリストと照合してください。

---

## FP-01: PDF セクション名の2種混在（単元間揺れ）

**症状:**
- `## もっと練習したい方へ`（16 本: 最大最小×4, 不等式×4, 決定×3, グラフ直線×3, 文章題×2）
- `## 解説PDFについて`（7 本: 解の配置×4, 変換×3）
- なし・欠落（5 本: 指数×3, 対数×2 — PDF 未作成のため）

**原因:** 単元ごとに異なる命名を使ってしまった。

**正しい統一形式:** 今後の記事は `## もっと練習したい方へ` のみ使う。

**検知:**
```bash
grep -R "解説PDFについて" site/ --include="*.md" --exclude-dir=docs
```

---

## FP-02: `## まとめ` の見出しに括弧書き

**症状:** `## まとめ（a>0 の場合）`（quadratic-inequality-discriminant.md で確認）

**原因:** 条件を見出しに書いてしまった。

**修正:** `## まとめ` のみ（括弧なし）。条件は本文中の表や箇条書きに書く。

**検知:**
```bash
grep -R "## まとめ（" site/ --include="*.md" --exclude-dir=docs
```

---

## FP-03: 「どういうことか」見出し（「なぜ」パターン外）

**症状:** `## 共通部分を取るとはどういうことか`（quadratic-inequality-system.md で確認）

**原因:** 「なぜ」ではなく「どういうことか」という説明形式を使った。

**修正:** `## なぜ「共通部分」で解が定まるのか` のように「なぜ」を軸にする。

**ルール:** 見出しで「何か」「どういうことか」の代わりに「なぜ〇〇か」を使う。

---

## FP-04: `## まとめ` の欠落

**症状:** log-function-graph.md に `## まとめ` がなかった（2026-03-10 修正済み）。

**原因:** 書き忘れ、または「接続セクションで締まっている」と誤判断した。

**ルール:**
- leaf 記事は原則として `## まとめ` を持つ
- 省略可能な唯一の条件: 末尾が「次の記事・単元への接続」そのものになっており、まとめが冗長になる場合（定義・概念型でのみ起こりうる）

**検知:** 執筆後に `WRITING_CHECKLIST.md` の構造チェックを実行する。

---

## FP-05: 指数・対数 leaf 記事の PDF セクション欠落（5 本）

**症状:** exp-function-graph, exp-function-transform, exp-function-equation, log-definition, log-function-graph の PDF セクションがない。

**原因:** PDF pack が未完成の段階で記事を公開した（部分公開）。

**修正方針:** exponential-function-pack.pdf / logarithm-function-pack.pdf が完成したら一括追加。

**ルール:**
- PDF が未作成なら PDF セクションを書かない（「準備中」も書かない）
- PDF が完成したら単元トップ + 全 leaf 記事に同時追加する（部分追加しない）

---

## FP-06: `f(x)` の暗黙使用

**症状:** quadratic-inequality 系3本（basics, negative, system）で `f(x)` を定義なしで使用。

**原因:** 「前の記事で定義した」と想定した。

**修正方針:** 各記事の冒頭か最初のセクションで「`f(x) = ax^2 + bx + c（a > 0）とおきます`」を追加する。

**ルール:** 前の記事で定義した変数でも、この記事で初めて使うなら必ず再定義する。

---

## FP-07: 「how」止まりの説明（「なぜ」なし）

**症状:** exp-function-transform.md — 移動量・移動方向の説明はあるが「なぜ x-p の形に p が現れるのか」を言わない。

**原因:** 手順の正確な記述に集中し、「なぜその式変形をするのか」を説明しなかった。

**修正方針:** `## なぜ x-p の形になるのか` セクションを追加し、`y = a^x` の `x` を `(x-p)` に置換する意味から説明する。

**ルール:** 「〇〇するとどうなるか」ではなく「なぜ〇〇するのか」が説明の軸。

---

## FP-08: 未完成 PDF 導線の先出し

**症状:** PDF ボタンを書いたが、対応する pack PDF が site/assets/pdf/ に存在しない状態で commit/push してしまう。

**原因:** 「後で PDF を作れば OK」という判断。

**修正方針:**
```bash
ls site/assets/pdf/[unit-slug]-pack.pdf
```
でローカル実在確認後にのみ PDF ボタンを書く。確認前に書いた場合は commit に含めない。

**ルール:** PDF ボタンとローカルファイルは同じ commit に含める。

---

## FP-09: 「準備中」の常態化

**症状:** exponential-function.md, logarithm-function.md に「解説PDF準備中」が残存している（2026-03-10 時点）。

**原因:** manuscript 待ちの状態で単元トップを公開した。

**修正方針:** manuscript が揃い次第、PDF を作成して一括更新する。

**ルール:**
- 「準備中」を書いたまま push しない
- PDF が未作成なら PDF セクションを省略する（書かない = 「準備中」とは書かない）
- push 前に `grep -R "準備中" site/ --exclude-dir=docs` でチェックする

---

## FP-10: unit top の PDF 見出しが `## 解説PDF` になっている

**症状:** exponential-function.md / logarithm-function.md で `## 解説PDF` を使っていた。

**原因:** leaf 記事の命名（`## もっと練習したい方へ`）と unit top の命名（`## 解説PDFについて`）を混同した。

**修正:** unit top では必ず `## 解説PDFについて`（leaf は `## もっと練習したい方へ`）。

**検知:**
```bash
grep -R "^## 解説PDF$" site/ --include="*.md" --exclude-dir=docs
```

---

## FP-11: `## この解説の特徴` 等の meta-commentary セクションを追加している

**症状:** exponential-function.md に `## この解説の特徴` セクションが存在していた（2026-03-10 削除済み）。

**原因:** 正本（quadratic-inequality.md / quadratic-root-location.md）には存在しないセクションを追加してしまった。

**修正:** `## この解説の特徴`・`## このサイトの特徴` 等の meta-commentary セクションは unit top・leaf ともに禁止。

**検知:**
```bash
grep -R "## この解説の特徴\|## このサイトの特徴" site/ --include="*.md" --exclude-dir=docs
```

---

## パターン別の検知コマンドまとめ

```bash
# FP-01: PDF セクション名揺れ
grep -R "解説PDFについて" site/ --include="*.md" --exclude-dir=docs

# FP-02: まとめ括弧書き
grep -R "## まとめ（" site/ --include="*.md" --exclude-dir=docs

# FP-08 / FP-09: 禁止表記
grep -R "公開中"       site/ --exclude-dir=docs
grep -R "準備中"       site/ --exclude-dir=docs
grep -R "解説PDF準備中" site/ --exclude-dir=docs

# FP-10: unit top の PDF 見出し揺れ
grep -R "^## 解説PDF$" site/ --include="*.md" --exclude-dir=docs

# FP-11: meta-commentary セクション
grep -R "## この解説の特徴\|## このサイトの特徴" site/ --include="*.md" --exclude-dir=docs
```
