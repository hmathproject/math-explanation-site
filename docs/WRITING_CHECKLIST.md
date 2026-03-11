# 執筆後チェックリスト

Claude Code が記事ファイルを作成・更新した直後に実行する自己検査リストです。
commit する前に全項目を確認してください。

---

## leaf 記事チェックリスト

### front matter
```
□ layout: default が設定されている
□ title が設定されている（日本語可）
□ permalink が設定されている（例: /log-definition/）
□ description が設定されている（80-120字）
```

### 数式記法
```
□ インライン数式が \\( ... \\) 形式（シングルバックスラッシュは動作しない）
□ display 数式が <div>$$...$$</div> 形式
□ インライン数式内で \dfrac を使っていない（\frac を使う。\dfrac は行高を乱す）
□ テーブルセル内の絶対値に \| を使っていない（\vert x\vert を使う）
□ 区間を [a,b] 形式で書いていない（閉区間は \\( a \leq x \leq b \\)、開区間は (, ) のまま）
□ 絶対値は壊れた \left...\right になっていない（\\( \left|-\frac{1}{6}\right| \\) のように \left| と \right| を必ず対にする）
□ 計算結果に不要な小数を使っていない（特別な理由がない限り分数・整数で表す）
```

### 変数定義
```
□ 本文で使う変数・記号が初登場時に条件付きで定義されている
  例: \\( a > 0, a \neq 1 \\)、f(x) = ax^2 + bx + c (a ≠ 0)
□ 前の記事で定義した変数でも、この記事で初出なら再定義している
```

### 記事構造
```
□ 「なぜ」の説明セクションが計算・手順セクションより前にある
□ ## まとめ の見出しに括弧書きがない（## まとめ（a>0 の場合）は禁止）
□ ## もっと練習したい方へ が末尾にある（PDF が実在する場合）
```

### 図
```
□ 図が必要な記事（グラフ主役型）で PNG が site/assets/images/ に実在する
□ 図のパスが絶対パス /assets/images/[記事-slug].png 形式
□ PNG が存在しない状態で <img> タグを書いていない
```

### PDF ボタン
```
□ PDF ボタンを書く前に ls site/assets/pdf/[unit-slug]-pack.pdf で実在確認した
□ PDF が実在しない場合は PDF セクションを丸ごと省略している（「準備中」は禁止）
```

### ナビゲーション
```
□ breadcrumb top が正しい（current ページはリンクなし、上位ページはすべてリンクあり）
□ bottom nav が正しい（前記事は ← 、次記事は → 、単元リンクあり）
□ bottom nav のリンク先がすべて実在する公開済みページ
□ 未公開記事へのリンクを書いていない
```

### 禁止表記
```
□ 「準備中」が残っていない
□ 「公開中」が残っていない
□ 「解説PDF準備中」が残っていない
```

---

## 単元トップチェックリスト

```
□ ## この単元で学ぶこと の箇条書きが「なぜ〇〇か」の問い形式（「〇〇を学びます」は禁止）
□ ## 解説記事 に全公開記事のリンクがある
□ 記事数表記（全 N 記事）が実際の公開本数と一致している
□ PDF 見出しが ## 解説PDFについて になっている（## 解説PDF・## もっと練習したい方へ は禁止）
□ PDF ボタンを書く前に PDF が local に実在する
□ 「準備中」「公開中」が残っていない
□ 内部リンクがすべて絶対パス /page-name/ 形式
□ ## この解説の特徴 等の meta-commentary セクションがない
```

---

## manuscript チェックリスト（integrated_exp 形式）

```
□ 絶対値: \left| ... \right| か |...| を使っている（\left と \right が対になっている）
□ 不要な小数なし（計算結果・代入値・検証値はすべて分数か整数で表記）
□ 右欄説明ボックス内の長い行（文字列 + インライン数式の混在）を改行・段落分割している
□ 右欄 display 数式が1行に収まる長さか確認（長い場合は \[...\] を2ブロックに分割）
□ 表示幅が広い数式（複数の \frac が並ぶ等）は display（\[...\]）で表記している
□ Unicode 数学記号（≤ ≥ √ ∈）を使っていない（FP-12: \( \leq \) 等に変換）
□ 区間表記として [ ] ( ) を reader-facing 本文で使っていない（閉区間は \( a \leq x \leq b \)、開区間は \( a < x < b \) に統一）
```

**grep 再点検コマンド:**
```bash
# FP-15: 不要な小数
grep -rn "\b[0-9]\+\.[0-9]\+" manuscripts/積分_*_integrated_exp.md | grep -v "width=0\.[0-9]"

# FP-16: 孤立した \left または \right
python3 -c "
import re, pathlib
for f in sorted(pathlib.Path('manuscripts').glob('積分_*_integrated_exp.md')):
    for i, line in enumerate(f.read_text().splitlines(), 1):
        for m in re.finditer(r'\\\\left', line):
            a = line[m.end():]
            if a and a[0] not in '|([{.\\\\ ':
                print(f'{f}:{i}: {line.strip()[:80]}')
"

# FP-18: reader-facing 区間括弧表記（manuscript）
python3 -c "
import re, pathlib
for f in sorted(pathlib.Path('manuscripts').glob('積分_*_integrated_exp.md')):
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if re.search(r'\\\\left\[[-\d]', line):
            print(f'{f.name}:{i}: {line.strip()[:100]}')
"

# FP-18: reader-facing 区間括弧表記（web）
python3 -c "
import re, pathlib
for f in sorted(pathlib.Path('site').glob('integ-*.md')):
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if re.search(r'\[[-0-9],', line):
            print(f'{f.name}:{i}: {line.strip()[:100]}')
"

# FP-17: 右欄 100ch 超の長行
python3 -c "
import pathlib
for f in sorted(pathlib.Path('manuscripts').glob('積分_*.md')):
    in_right = False
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if '<!-- COL_MID -->' in line: in_right = True
        elif '<!-- COL_END -->' in line or '<!-- COL_LEFT_BEGIN -->' in line: in_right = False
        elif in_right and len(line.rstrip()) > 100:
            print(f'{f.name}:{i} ({len(line.rstrip())}ch): {line.strip()[:90]}')
"
```

---

## push 前の禁止表記チェック（コマンド）

```bash
# docs/ を除外して公開ページのみを対象にする
grep -R "公開中"       site/ --exclude-dir=docs
grep -R "準備中"       site/ --exclude-dir=docs
grep -R "解説PDF準備中" site/ --exclude-dir=docs
```

**いずれかに出力があれば push しない。** 該当箇所を修正してから再チェックする。
docs/ を除外するのは、FAILURE_PATTERNS.md 等の説明文でこれらの語句が出現するため。

---

## よくある書き忘れ（FAILURE_PATTERNS.md より抜粋）

- `## まとめ` の見出しに括弧書き → `## まとめ（a>0 の場合）` を `## まとめ` に修正
- `## 解説PDFについて` を使ってしまう → `## もっと練習したい方へ` に統一
- `## なぜ...か` の代わりに「どういうことか」 → 「なぜ」を使う
- `log-function-graph.md` 系の `## まとめ` 欠落 → 必ず追加する
- `f(x)` を定義なしで使う → 「f(x) = ax^2 + bx + c (a ≠ 0) とおきます」から始める

詳細は `FAILURE_PATTERNS.md` を参照。
