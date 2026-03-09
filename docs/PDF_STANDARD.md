# PDF_STANDARD.md — サイト向け解説PDF制作標準

このファイルはサイト向け無料配布PDFの制作標準を定めた運用文書です。
チャットが変わった場合はまずこのファイルを読んでください。

---

## 1. 正本とする PDF

**正本**: `site/assets/pdf/quadratic-max-min-pack.pdf`（二次関数の最大値・最小値パック）

**正本の根拠:**
- 2段組（答案＋意味説明）・図埋め込み・1問1ファイル構成が揃っている
- `experiments/graph-guided-lessons/` の実験系パイプラインで完全に動作している
- 学習者が「答案を書く」手と「なぜそう考えるか」を同時に確認できる構造
- 今後の全単元 PDF はこのフォーマットに準拠する

**今後の方針:** 全単元の PDF は `integrated_exp` 形式（実験系）で作る。
本番系（`tutor-math/manuscripts/guides/`）の `build_pdf.py` では作らない。

---

## 2. ファイル構成（1単元 = 1パック）

```
experiments/graph-guided-lessons/
├── manuscripts/
│   ├── 単元名_問題タイトル_integrated_exp.md  ← 1問1ファイル（必須）
│   └── ...
├── figures/
│   ├── 問題タイトル_combined.png              ← 方針図（PNG）
│   └── ...
├── pdf/
│   ├── 単元名_問題タイトル_integrated_exp.pdf ← 個別PDF
│   └── packs/
│       └── 単元名_完全版.pdf                  ← パックPDF
└── scripts/
    ├── build_exp_pdf.py                       ← 個別PDF生成
    └── build_pack.sh                          ← パック組み立て

site/assets/pdf/
└── 単元slug-pack.pdf                          ← サイト公開用コピー
```

---

## 3. 標準マークダウン構成（1問1ファイル）

```markdown
# 統合教材：単元名（問題の詳細タイトル）
トピック: 単元名
難易度: 標準

## 問題

\( 数式 \) で問題を記述する。

## 解法の流れ

- ステップ1の概要（1行）
- ステップ2の概要（1行）
- ステップ3の概要（1行）

## 方針

1〜2段落。放物線の形・場合分けの根拠など「なぜその手順か」を書く。

<!-- FIGURE: 問題タイトル_combined.png width=0.88 -->

## 模範解答

<!-- COL_LEFT_BEGIN -->

（左列：答案として提出できる記述。52%幅）

<!-- COL_MID -->

**【なぜそう考えるか】**

（右列：各ステップの意味説明。43%幅・グレーボックス）

<!-- COL_END -->

---

<!-- COL_LEFT_BEGIN -->

**① ケースN のとき**

（計算）

<!-- COL_MID -->

**【ケースNの読み取り方】**

（説明）

<!-- COL_END -->

（ケース数だけ繰り返す）

したがって、
\[
\begin{cases}
\text{結論1} & (\text{条件1}) \\[4pt]
\text{結論2} & (\text{条件2})
\end{cases}
\]
```

---

## 4. 必須記法ルール

### 数式記法（これ以外は使わない）

| 種別 | 正しい記法 | 禁止 |
|---|---|---|
| インライン数式 | `\( x = a \)` | `$x = a$` |
| ディスプレイ数式 | `\[ \frac{...}{...} \]` | `$$...$$` |
| cases 環境 | `\\[4pt]` は禁止。`\\` のみ使う | `\\[4pt]` |

**理由:** `build_exp_pdf.py` の安全チェックは `$` 記法と `\\[` を誤検知する。

### 2段組マーカー

```markdown
<!-- COL_LEFT_BEGIN -->
（左列の内容）
<!-- COL_MID -->
（右列の内容）
<!-- COL_END -->
```

- `<!-- COL_LEFT_BEGIN -->` と `<!-- COL_MID -->` と `<!-- COL_END -->` の3点セット必須
- 1問の模範解答部分に複数の2段組ブロックを重ねてよい（ケースごとに繰り返す）
- 右列（COL_MID〜COL_END）では `\begin{itemize}` は使わない（縦方向に広がりすぎる）

### 図の埋め込み

```markdown
<!-- FIGURE: ファイル名_combined.png width=0.88 -->
```

- `## 方針` の直後に置く（必須）
- `figures/` ディレクトリからの相対パス（ファイル名だけ書く）
- width は `0.75`〜`0.88` の範囲。ページ超過時は縮小する

### 太字

```markdown
**テキスト**
```

- `build_exp_pdf.py` が正しく `\textbf{テキスト}` に変換する（本番系 `build_pdf.py` は変換バグあり）

---

## 5. サイト記事からの流用ルール

### 流用してよい要素

| 要素 | 処理 |
|---|---|
| 問題文（数式） | `\\(...\\)` → `\(...\)` に変換して使用 |
| 方針の骨格（1段落） | そのまま流用、冗長な説明は圧縮 |
| 解の最終形 | `$...$` → `\(...\)` に変換して使用 |
| 解法のビュレット | `- item` のまま使用可 |

### 流用してはいけない要素

| 要素 | 理由 |
|---|---|
| `<div>$$...$$</div>` | HTML要素。`\[...\]` に書き直す |
| `\\(...\\)` | TeX 内でバックスラッシュが重複する。`\(...\)` に変換必須 |
| HTML タグ全般 | LaTeX に無効 |
| `---` 区切り（数式の直後） | safety_check の[D]警告を引き起こす。数式の後に空行か本文を挟む |
| 「もっと練習したい方へ」セクション | PDF本体には不要 |
| ナビゲーションリンク | PDF本体には不要 |

---

## 6. よくある崩れと防止策

| 崩れ | 原因 | 防止策 |
|---|---|---|
| 太字が `\textbackslash{}\textbf` になる | `build_pdf.py`（本番系）を使った | `build_exp_pdf.py`（実験系）を使う |
| `\\[4pt]` が安全チェックで止まる | cases 環境内の行間指定 | `\\[4pt]` → `\\` に変換 |
| 数式直後の `---` が[D]警告 | safety_check が数式断片と誤認識 | `---` を `### 次セクション` に変えるか空行を増やす |
| 右列がページをはみ出す | itemize / 長い説明 | itemize を使わずインライン文にする |
| 図がコンパイルで見つからない | `figures/` にファイルがない | ビルド前に `figures/` へコピー確認 |
| ページ数が3ページを超える | 説明が多すぎる | LAYOUT_RULES.md の圧縮優先順位に従う |

**LAYOUT_RULES.md の圧縮優先順位（ページ超過時）:**
1. 右列の冗長な説明を削る
2. 右列幅を 43% → 35% に縮小
3. 図の width を 0.85 → 0.75 に縮小
4. 最終ケースを前のケースと統合
5. itemize をインライン文に変える

---

## 7. ビルドコマンド（標準手順）

```bash
# 作業ディレクトリ
cd /Users/harahisato/tutor-math/experiments/graph-guided-lessons

# Step 1: 図の確認（figures/ に PNG があるか）
ls figures/

# Step 2: 個別 PDF 生成（1問ずつ）
python scripts/build_exp_pdf.py manuscripts/単元名_問題_integrated_exp.md

# Step 3: 全問完了後、パック組み立て
bash scripts/build_pack_単元名.sh
# （内部: pdfunite cover.pdf qi1.pdf qi2.pdf qi3.pdf qi4.pdf packs/完全版.pdf）

# Step 4: サイトに配置
cp pdf/packs/単元名_完全版.pdf site/assets/pdf/単元slug-pack.pdf

# Step 5: git
cd site
git add assets/pdf/単元slug-pack.pdf
git commit -m "feat: 単元PDF追加"
git push
```

---

## 8. 各単元 PDF の管理状況

| 単元 | PDFファイル名 | フォーマット | 状態 |
|---|---|---|---|
| 二次関数の最大値・最小値 | `quadratic-max-min-pack.pdf` | integrated_exp ✅ | 完成・正本 |
| 二次不等式の解法 | `quadratic-inequality-pack.pdf` | guide（旧） ⚠️ | 再構成予定 |

**二次不等式 PDF の再構成予定:**
- 新フォーマット: `integrated_exp`（qi1〜qi4 を 1問1ファイル）
- 図: `figures/quadratic-inequality-*-combined.png`（`site/assets/images/` からコピー）
- 原稿: `manuscripts/二次不等式_*_integrated_exp.md`（新規作成予定）

---

## 9. 参照すべき既存ドキュメント

| ファイル | 内容 |
|---|---|
| `docs/MASTER_RULES.md` | 2段組・図・表現の詳細ルール（16KB） |
| `docs/LAYOUT_RULES.md` | 2ページ収め方のトラブルシュート |
| `docs/PRODUCTION_FLOW.md` | 制作フロー（step-by-step） |
| `docs/README_integrated_format.md` | フォーマット仕様の全体像 |
| `manuscripts/二次関数_最小値_固定区間_integrated_exp.md` | 書式の手本（最も参照すべき） |
| `scripts/build_exp_pdf.py` | ビルドスクリプト本体 |
