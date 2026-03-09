# site/ — 二次関数の最大値・最小値 解説サイト雛形

このディレクトリは「二次関数の最大値・最小値」をテーマとした数学解説サイトの最小公開雛形です。
本番公開はまだ行っていません。GitHub Pages などへ移行しやすい構成を意識して整理しています。

---

## ディレクトリ構成

```
site/
  README.md                                  ← このファイル
  index.md                                   ← 単元トップページ
  quadratic-min-fixed-range.md               ← 記事1：最小値（固定区間・軸が動く）
  quadratic-max-fixed-range.md               ← 記事2：最大値（固定区間・軸が動く）
  assets/
    images/
      quadratic-min-fixed-range-combined.png ← 問1 方針図（3ケース）
      quadratic-max-fixed-range-combined.png ← 問2 方針図（2ケース）
    pdf/
      quadratic-max-min-pack.pdf             ← 4問パック解説PDF（無料配布用）
```

---

## 各ファイルの役割

| ファイル | 役割 |
|---|---|
| `index.md` | 単元の全体像と記事一覧。PDF案内も置く |
| `quadratic-min-fixed-range.md` | 問1解説（軸の位置で3ケース場合分け） |
| `quadratic-max-fixed-range.md` | 問2解説（軸から遠い端点で2ケース場合分け） |
| `assets/images/` | 記事内で使う方針図（matplotlibで生成） |
| `assets/pdf/` | 読者に配布する解説PDF |

---

## リンク構造

```
/ (index.md, permalink: /)
  ├─→ /quadratic-min-fixed-range/
  ├─→ /quadratic-max-fixed-range/
  └─→ /assets/pdf/quadratic-max-min-pack.pdf

/quadratic-min-fixed-range/ (quadratic-min-fixed-range.md)
  ├─← /
  ├─→ /quadratic-max-fixed-range/（次の記事）
  ├─→ /assets/images/quadratic-min-fixed-range-combined.png
  └─→ /assets/pdf/quadratic-max-min-pack.pdf

/quadratic-max-fixed-range/ (quadratic-max-fixed-range.md)
  ├─← /
  ├─← /quadratic-min-fixed-range/（前の記事）
  ├─→ /assets/images/quadratic-max-fixed-range-combined.png
  └─→ /assets/pdf/quadratic-max-min-pack.pdf
```

すべてのリンクはサイトルートからの絶対パスで記述しています。Jekyll の permalink 設定により、Cloudflare Pages 上で `.md` が見えない URL で動作します。

---

## 画像とPDFの管理方針

- **画像の元ファイル**は `../figures/` に置かれています（matplotlibで生成）
- `assets/images/` はそのコピーです。サイト公開時に必要なものだけをここに集めています
- **PDFの元ファイル**は `../pdf/packs/` にあります
- `assets/pdf/` はそのコピーです。元ファイルを更新した場合はコピーも更新してください

---

## 今後公開するときに必要なこと

### GitHub Pages で公開する場合

1. この `site/` ディレクトリを公開リポジトリに配置する
2. `.md` ファイルを `.html` に変換する（Jekyll / Pandoc / Astro などを使う）
3. 数式レンダリングの設定を追加する（MathJax または KaTeX）
4. 最小限のCSSを追加する（フォント・余白・コードブロック程度）
5. PDF配布URLを確定し、各記事の `[PDFをダウンロードする（無料）]` リンクを更新する

### 追加予定の記事（Phase 2）

- `二次関数_最小値_動区間.md` — 区間 \( a \leq x \leq a+1 \) が動くとき（3ケース）
- `二次関数_最大値_動区間.md` — 同設定で最大値（2ケース）

Phase 2 記事を追加したら `index.md` の「準備中の記事」テーブルをリンク付き記事一覧に更新してください。

---

## 元ファイルとの対応

| site/ のファイル | 元となった原稿 |
|---|---|
| `index.md` | `site/二次関数_最大最小_top.md`（整理前） |
| `二次関数_最小値_固定区間.md` | `manuscripts/二次関数_最小値_固定区間_integrated_exp.md` |
| `二次関数_最大値_固定区間.md` | `manuscripts/二次関数_最大値_固定区間_integrated_exp.md` |
| `assets/images/*.png` | `figures/` 以下の combined 図 |
| `assets/pdf/*.pdf` | `pdf/packs/二次関数_最大最小_完全版.pdf` |
