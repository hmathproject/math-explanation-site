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

## FP-12: integrated_exp manuscript の Unicode 数学記号が PDF で欠落

**症状:**
PDF を pdftotext で確認すると `sin θ = 3/2`（√3/2 の `√` が消える）や `0  θ < 2π`（`≤` が消える）のような文字化けが発生する。XeLaTeX + Hiragino フォントは Unicode の `√`（U+221A）・`≤`（U+2264）・`≥`（U+2265）・`∈`（U+2208）をテキストモードで処理できないため、LaTeX がこれらを**無音でドロップ**する。

**根本原因:**
`manuscripts/*_integrated_exp.md` の `## 問題`・`## 解法の流れ`・`## 方針` セクションの本文（plain text 段落）に Unicode 数学記号を直接記述すると、`build_exp_pdf.py` の `_convert_lines()` がそのまま LaTeX テキストモードに渡す。テキストモードでは Hiragino がこれらのグリフを持たないため脱落する。

**ルール（manuscript 執筆時）:**
- `## 模範解答` より前の本文（問題・解法の流れ・方針）で数学記号を含む場合は必ず `\( ... \)` に包む
- `√3/2` → `\(\dfrac{\sqrt{3}}{2}\)` または `\(\sqrt{3}/2\)`
- `0 ≤ θ < 2π` → `\(0 \leq \theta < 2\pi\)`
- `−1 ≤ t ≤ 1` → `\(-1 \leq t \leq 1\)`
- `θ ∈ (π/2, π)` → `\(\theta \in (\pi/2,\ \pi)\)`
- markdown テーブルのセル内も同様に `$\frac{\sqrt{3}}{2}$` 形式を使う

**検知（PDF ビルド後）:**
```bash
# pdftotext で各パック PDF を抽出し、欠落パターンを確認する
for f in site/assets/pdf/trig-*-pack.pdf; do
  echo "=== $f ===" && pdftotext "$f" - | grep -E "= [0-9]/[0-9]$"
done
```

**検知（manuscript ソース）:**
```bash
grep -rn "[≤≥√∈]" manuscripts/ --include="*_integrated_exp.md"
```
→ 何も出力されなければ OK。

---

## FP-13: インライン数式内の `\dfrac` と markdown テーブル内の `\|` 絶対値

**症状:**
`python3 scripts/quality_check.py` が以下の WARN を出力する。
- `\\dfrac in inline math can disturb line height; prefer \\frac`
- `inline absolute value can break markdown tables; prefer display math`

**原因:**
- `\dfrac` はインライン数式 `\\( ... \\)` 内で使うと前後テキストより行高が大きくなり、段落の行間が乱れる。
- `\|x\|` はマークダウンテーブルのセル内でパイプ `|` がカラム区切りと誤解釈される場合がある。

**ルール:**
- インライン数式では常に `\frac` を使う（display 数式 `$$...$$` 内は `\frac` で問題なし）
- テーブルセル内の絶対値には `\vert x\vert` を使う（`\|x\|` `\lvert x\rvert` は避ける）

**修正例:**
```
❌  \\( \dfrac{1}{2} \\)          →  ✅  \\( \frac{1}{2} \\)
❌  \\( \|A\| \\)（テーブル内）   →  ✅  \\( \vert A\vert \\)
```

**検知:**
```bash
python3 scripts/quality_check.py
```

---

## FP-14: 区間表記のブラケット残存（閉区間・開区間・半開区間すべて）

**症状:** 閉区間を \\( [0,3] \\)、開区間を \\( (-1,1) \\) のように括弧記号で表記する。

**正しい統一形式（全種類）:**
- 閉区間 \[a,b\]: \\( a \leq x \leq b \\)
- 開区間 (a,b): \\( a < x < b \\)
- 半開区間 \[a,b): \\( a \leq x < b \\)
- 半開区間 (a,b\]: \\( a < x \leq b \\)

**ルール:** reader-facing テキスト・問題文・説明文で区間を表すとき、閉/開/半開を問わず**括弧記法を一切使わない**。すべて不等号形式に統一する。
定積分の積分記号 \\( \int_a^b \\) は別途管理であり、このルールの対象外。

**検知:**
```bash
# manuscripts: \left[ の直後に数字が続く区間記法
python3 -c "
import re, pathlib
for f in sorted(pathlib.Path('manuscripts').glob('積分_*.md')):
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if re.search(r'\\\\left\[[-\d]', line):
            print(f'{f.name}:{i}: {line.strip()[:100]}')
"

# web: [number, で始まる区間記法
python3 -c "
import re, pathlib
for f in sorted(pathlib.Path('site').glob('integ-*.md')):
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if re.search(r'\[[-0-9],', line):
            print(f'{f.name}:{i}: {line.strip()[:100]}')
"
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

# FP-12: manuscript Unicode 数学記号の欠落
grep -rn "[≤≥√∈]" manuscripts/ --include="*_integrated_exp.md"

# FP-14: 区間表記 [a,b] ブラケット残存（markdown リンクと code block は除外）
grep -n '\[[0-9-][^]]*\]' site/*.md | grep -v '](http' | grep -v '/assets/'
```


---

## FP-15: 不要な小数計算

**症状:** 検証用のテスト値や代入結果を小数で書く（例: `x = 0.5` で `x³-x = 0.125 - 0.5 = -0.375`）

**原因:** テスト値に `x = 1/2` などの分数を使えば小数が出ないにもかかわらず、計算を十進小数で進めてしまった。また、解が無理数のときに近似値を付記した（例: `a ≈ 2.48`）。

**対策:**
- テスト値は小数を生まない分数（`\frac{1}{2}`, `\frac{1}{3}` など）を選ぶ
- 解が無理数の場合は近似値を記載せず、「実数解は唯一存在し、◯ < a < △ にある」等の形で表す
- 計算の途中も分数で通し、最後まで分数・整数で表記する

**検知:**
```bash
grep -rn "\b[0-9]\+\.[0-9]\+" manuscripts/積分_*_integrated_exp.md | grep -v "width=0\.[0-9]"
grep -rn "\b[0-9]\+\.[0-9]\+" site/integ-*.md site/integral.md
```

---

## FP-16: 壊れた絶対値記法（\left と \right の片落ち）

**症状:** `面積 \( = \left -\frac{1}{6} \right = \frac{1}{6} \)` のように `\left` の直後に `|` が欠落している、または `\left|` に対応する `\right|` が欠けている。

**原因:** コピー・編集の途中で `|` が脱落した、または `\left(` を絶対値のつもりで書いた。

**対策:**
- 絶対値は必ず `\left| ... \right|` または `|...|`（スカラーに限り）で書く
- `\left` の直後には必ず `|`, `(`, `[`, `\{` などの対応する区切り文字を置く
- `\vert x \vert` 形式は manuscript TeX では有効だが、web 記事では `|x|` か `\left|x\right|` を使う

**検知:**
```bash
python3 -c "
import re, pathlib
for f in sorted(pathlib.Path('site').glob('integ-*.md')) + sorted(pathlib.Path('manuscripts').glob('積分_*_integrated_exp.md')):
    for i, line in enumerate(f.read_text().splitlines(), 1):
        for m in re.finditer(r'\\\\left', line):
            a = line[m.end():]
            if a and a[0] not in '|([{.\\\\ ':
                print(f'{f}:{i}: {line.strip()[:80]}')
"
```

---

## FP-17: 右欄説明ボックスの横幅 overflow

**症状:** PDF の右欄（COL_MID〜COL_END の説明ボックス）で、テキストまたはインライン数式が枠の右端をはみ出す。

**原因:** 長い日本語文字列とインライン数式（`\( f(x) - g(x) = ... \)`）を1段落に詰め込んだため、TeX のライン分割が効かない部分が生じた。

**対策:**
- 1行が100文字超かつインライン数式を複数含む場合は段落を分割する
- 幅の広い数式（`\frac` が3つ以上連続する等）は `\[...\]` display ブロックに切り出す
- 目安: 右欄の prose 行は 80〜100 文字以内、インライン数式は1文に1〜2個まで

**検知:**
```bash
python3 - <<'PYEOF'
import pathlib
for f in sorted(pathlib.Path('manuscripts').glob('積分_*_integrated_exp.md')):
    in_right = False
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if '<!-- COL_MID -->' in line: in_right = True
        if '<!-- COL_END -->' in line: in_right = False
        if in_right and len(line) > 100:
            print(f'{f}:{i} ({len(line)}ch): {line[:80]}')
PYEOF
```

---

## FP-18: 右欄 display 数式の横幅 overflow

**症状:** PDF の右欄（COL_MID〜COL_END）に書いた `\[...\]` display 数式が1行に収まらず、右端が切れる（例: `= 9 - 27/2 =` で行末に消える）。

**原因（重要）:** TeX の `\[...\]` 環境ではソースの改行が**完全に無視**される。つまり
```
\[
\int_0^{b} f\,dt
= \int_0^{b} g\,dt
\]
```
と複数行に書いても PDF では `∫f dt = ∫g dt` が**1行**に組版される。右欄の幅は本文幅の約 45% しかないため、長い等号チェーンは枠外にはみ出す。

**対策:**
- 右欄の display 式を複数ステップ（等号 2 個以上）で書く場合、**必ず `\[...\]` ブロックを分割する**
- 例: `\[ A = B = C = D \]` → `\[ A = B \]` + `\[ = C = D \]`
- 等号の続く確認計算は特に注意（`= F(b) - F(a) = ... = ...` のような1行3ステップ）
- 2つの integral を `=` でつないだブロック（`\int_0^a f\,dt = \int_0^a g\,dt`）も同様に分割する
- `\\` を使った多行 `align` 等は TeX の設定次第。分割 `\[...\]` の方が安全

**検知（src 行長 > 80ch の右欄 display math）:**
```bash
python3 -c "
import pathlib, re
for f in sorted(pathlib.Path('manuscripts').glob('積分_*.md')):
    in_right = in_display = False
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if '<!-- COL_MID -->' in line: in_right = True
        elif '<!-- COL_END -->' in line or '<!-- COL_LEFT_BEGIN -->' in line: in_right = False
        if in_right:
            if re.match(r'\s*\\\[', line): in_display = True
            elif re.match(r'\s*\\\]', line): in_display = False
            elif in_display and len(line.rstrip()) > 80:
                print(f'{f.name}:{i} ({len(line.rstrip())}ch): {line.strip()[:90]}')
"
```

---

## FP-19: 直線の方程式での垂直線ケース漏れ

**症状:**
- 「直線の方程式は y = mx + n で表せる」と書き、x = a のケースを忘れる
- 平行・垂直の条件式で「どちらかが垂直線のとき」の例外を見落とす

**原因:** y = mx + n に意識が向きすぎて、傾きが定義されないケースを考慮しなかった。

**正しい対応:**
- coord-line-equation では冒頭で「x = a のケースは傾き m が定義されない」と明記する
- coord-line-relation では「どちらかが垂直線のとき」の例外を記述する
- 一般形 ax + by + c = 0 でまとめると、垂直線を含む全ての直線を統一的に表せる

**検知:**
```bash
grep -rn "y = mx" site/coord-line*.md
```
（y = mx + n のみの記述で x = a への言及がない場合、FP-19 の可能性）


---

## FP-20: 等比数列の和で r=1 の場合を省略する

**症状:**
- `S_n = a_1(1-r^n)/(1-r)` を書き、r=1 の場合（S_n = na_1）を記述しない
- 「r≠1 のとき」の断り書きなしに公式を適用する

**原因:** r=1 のときはずらし引きで (1-r)=0 になって割り算ができないことを見落とした。

**正しい対応:**
- 等比数列の和を扱う記事・manuscript で必ず「r=1 のとき」「r≠1 のとき」の 2 ケース分岐を明示する
- r=1 を代入した式 S_n = a_1(1-1^n)/(1-1) は 0/0 の不定形になるため使えない

**検知:**
```bash
grep -rn "1-r\^" manuscripts/数列_等比数列_*.md
```
（r=1 ケースへの言及もあるか確認）

---

## FP-21: a_n = S_n - S_{n-1} を n=1 に誤適用する

**症状:**
- S_n から a_n の式を導いたとき、n=1 を別確認せずに公式が n=1 でも成立すると仮定する
- 「n≥2 のとき」の明記を省略する

**原因:** S_{n-1} は n=1 のとき S_0（定義されない）になることを見落とした。

**正しい対応:**
- 該当 manuscript と web 記事で常に「n≥2 のとき」と明記する
- a_1 = S_1 を別計算するブロックを含める
- 公式値と S_1 が一致する場合は「全 n≥1 で成立」、一致しない場合は場合分けで書く

**検知:**
```bash
grep -rn "S_n - S" manuscripts/数列_*.md
```
（「n≥2」への言及が近傍にあるか確認）

---

## FP-22: 数列の図に連続な曲線を使う（離散性の無視）

**症状:**
- `ax.plot(x, y)` で x が浮動小数点の連続値（数列なのに連続曲線を描く）
- 折れ線グラフで数列の項を接続し、離散的な性質を隠す

**原因:** 関数のグラフと数列のグラフを混同した。数列は整数インデックスの点の集合であり、連続曲線ではない。

**正しい対応:**
- 数列の図スクリプトでは `ax.scatter(range(1,n+1), values)` または `ax.bar(range(1,n+1), values)` を使う
- x 軸は整数のみ（`ax.set_xticks(range(1,n+1))`）
- フロー図・テーブル図は `ax.axis('off')` + `ax.text()` で実装する

**検知:**
```bash
grep -rn "ax.plot" scripts/gen_figures_seq_*.py
```
（浮動小数点 x を使っていないか確認）

---

## FP-23: 平行条件で零ベクトルの扱いを曖昧にする

**症状:**
- `b ∥ a ⟺ b = ka（k は任意の実数）` と書き、零ベクトルを除外しない
- 「k≠0」と書くだけで「なぜ零ベクトルを除くか」を説明しない

**原因:** 零ベクトルは大きさが 0 で向きが定義されないため、平行の定義（「向きが同じまたは逆」）を満たさない。しかし「b=0·a=0ベクトル」は技術的に形式を満たすため、除外を忘れやすい。

**正しい対応:**
- ベクトルの平行条件は「**非零ベクトルどうし**なら平行 ⟺ 一方が他方の実数倍」と明記する
- 「k≠0 のみ」と書くのではなく「零ベクトルは向きが定義されないため除く」と理由を添える
- 零ベクトルを含む可能性がある問題では「ベクトルが零でないとき」を確認してから平行条件を使う

**検知:**
```bash
grep -rn "平行.*ka\|b = ka" manuscripts/ベクトル_*.md
```
（「非零ベクトル」または「零ベクトルを除く」への言及があるか確認）

---

## FP-24: 垂直条件を公式として天下りに与える

**症状:**
- `a⊥b ⟺ a·b = 0` を定理として「覚えよ」と書き、cos 90°=0 からの導出を省略する
- 内積の成分公式 `a₁b₁+a₂b₂` を天下りで与え、余弦定理による導出を省略する

**原因:** 定義（`a·b = |a||b|cosθ`）から出発すれば θ=90° → cos90°=0 → a·b=0 が必然的に出るにも関わらず、「公式の暗記」として処理してしまう。

**正しい対応:**
- `vec-perpendicular` 記事では必ず「cos 90°=0 → 定義に代入 → a·b=0」の流れで示す
- 成分公式は余弦定理を `|a-b|²` に適用して導出する（天下りにしない）
- 「a·b=0 と覚える」の前に「なぜ 0 になるか」を図と定義で確認する

**検知:**
```bash
grep -rn "垂直.*a·b\|a·b.*垂直" manuscripts/ベクトル_垂直条件_integrated_exp.md
```
（cos 90°への言及があるか確認）

---

## FP-25: \\overrightarrow{} を ### 見出し内で使う（XeLaTeX エラー）

**症状:**
- `### (1) \(\overrightarrow{OA}=\overrightarrow{CB}\) のとき OACB の形状` のような見出しを書く
- XeLaTeX ビルド時に `! Illegal parameter number in definition of \reserved@a` エラーが出る

**原因:** `\overrightarrow{X}` 内の `{}` が XeLaTeX のセクション引数処理で展開され、等号を含む式が TeX パラメータ番号と混同される。`\vec{a}` は単一文字なので安全だが、`\overrightarrow{AB}` や `\overrightarrow{OA}=\overrightarrow{CB}` は危険。

**正しい対応:**
- `### ###` 見出し内の `\overrightarrow{}` は平文に置き換える
  - `\overrightarrow{OA}=\overrightarrow{CB}` → `OA = CB`
  - `|\overrightarrow{AB}|` → `|AB|`
  - `\overrightarrow{PQ}` → `PQ`
- `\vec{a}`, `\vec{b}` は見出し内でも使用可能

**検知:**
```bash
grep -n "^### .*\\\\overrightarrow" manuscripts/ベクトル_*.md
```
（ヒットした行の見出しを平文に変換する）
