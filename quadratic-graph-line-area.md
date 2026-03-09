---
layout: default
title: 放物線と直線で囲まれた面積
permalink: /quadratic-graph-line-area/
---

<!-- 図設計メモ（gen_figures_gl3.py）
記事名: 放物線と直線で囲まれた面積
図の役割: y=x² と y=x+2 の間の面積を着色し、面積の値 9/2 を図中に示す
ケース数: 1（fill_between で着色）
figsize案: (7.0, 4.5)
スクリプト案: scripts/gen_figures_gl3.py
出力PNG案: assets/images/quadratic-graph-line-area-combined.png
図の挿入位置: 「面積の求め方」の前
-->

← [単元トップへ：二次関数のグラフと直線](/quadratic-graph-line/)　／　← [前の記事：放物線と直線の共有点の座標](/quadratic-graph-line-coordinates/)

---

# 放物線と直線で囲まれた面積 — 積分で正確に求める

---

## 問題

放物線 \\( y = x^2 \\) と直線 \\( y = x + 2 \\) で囲まれた図形の面積 \\( S \\) を求めよ。

---

## 面積の求め方

### ステップ1：共有点（積分の端点）を求める

<div>
$$
x^2 = x + 2 \implies x^2 - x - 2 = 0 \implies (x - 2)(x + 1) = 0
$$
</div>

解は \\( x = -1 \\) と \\( x = 2 \\) です。

### ステップ2：どちらが上か確認する

区間 \\( -1 \leq x \leq 2 \\) で、直線と放物線のどちらが上にあるか確認します。

\\( x = 0 \\) で比較：直線は \\( y = 2 \\)、放物線は \\( y = 0 \\)。

直線 \\( y = x + 2 \\) の方が上にあります（下の図参照）。

![放物線と直線で囲まれた面積（着色図）](/assets/images/quadratic-graph-line-area-combined.png)

### ステップ3：積分で面積を計算する

<div>
$$
S = \int_{-1}^{2} \left[(x + 2) - x^2\right]\, dx
$$
</div>

被積分関数を展開します：

<div>
$$
S = \int_{-1}^{2} \left(-x^2 + x + 2\right)\, dx
$$
</div>

積分を計算します：

<div>
$$
S = \left[-\frac{x^3}{3} + \frac{x^2}{2} + 2x\right]_{-1}^{2}
$$
</div>

<div>
$$
= \left(-\frac{8}{3} + 2 + 4\right) - \left(\frac{1}{3} + \frac{1}{2} - 2\right)
$$
</div>

<div>
$$
= \left(\frac{10}{3}\right) - \left(-\frac{7}{6}\right) = \frac{10}{3} + \frac{7}{6} = \frac{20}{6} + \frac{7}{6} = \frac{27}{6} = \frac{9}{2}
$$
</div>

---

## 面積の公式（放物線と直線）

放物線 \\( y = ax^2 + (\text{他の項}) \\) と直線で囲まれた面積には次の公式が使えます。

\\( f(x) - g(x) = a(x - \alpha)(x - \beta) \\)（\\( \alpha < \beta \\)）のとき：

<div>
$$
S = \frac{|a|}{6}(\beta - \alpha)^3
$$
</div>

この問題では \\( x^2 - (x+2) = x^2 - x - 2 = (x-2)(x+1) \\) なので \\( a = 1 \\)、\\( \alpha = -1 \\)、\\( \beta = 2 \\)。

<div>
$$
S = \frac{1}{6} \times (2 - (-1))^3 = \frac{1}{6} \times 27 = \frac{9}{2}
$$
</div>

積分の計算と一致します ✓

---

## まとめ

**放物線と直線で囲まれた面積を求める手順**：

1. 連立して共有点（積分端点）\\( \alpha, \beta \\) を求める
2. 区間内でどちらが上かを確認する（適当な \\( x \\) 値を代入）
3. \\( S = \displaystyle\int_{\alpha}^{\beta} [\text{上} - \text{下}]\, dx \\) を計算する
4. （または公式 \\( S = \dfrac{|a|}{6}(\beta - \alpha)^3 \\) を使う）

**この問題の結果**：

<div>
$$
S = \frac{9}{2}
$$
</div>

---

## もっと練習したい方へ

この単元全3問（共有点の個数・座標・面積）の解説PDFをダウンロードできます。

[PDFをダウンロードする（無料）](/assets/pdf/quadratic-graph-line-pack.pdf)

---

← [単元トップへ：二次関数のグラフと直線](/quadratic-graph-line/)
