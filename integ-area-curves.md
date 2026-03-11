---
layout: default
title: 2曲線の間の面積 — 上下判定と交点での区間分割
permalink: /integ-area-curves/
description: "y=f(x) と y=g(x) の間の面積を求める手順を解説。交点を求めて区間を決め、上下の関数を確認してから ∫(f−g)dx を計算する（高校数II）。"
---

[サイトトップ](/) / [積分](/integral/) / [積分と面積](/integ-area/)

---

# 2曲線の間の面積 — 上下判定と交点での区間分割

---

## 2曲線の間の面積の公式

2 つの曲線 \\( y = f(x) \\) と \\( y = g(x) \\) の間の面積は

<div>
$$
S = \int_\alpha^\beta |f(x) - g(x)|\,dx
$$
</div>

で与えられます。ここで \\( \alpha, \beta \\) は 2 曲線の交点の \\( x \\) 座標です。

\\( f(x) \geq g(x) \\) が区間全体で成り立つ場合は絶対値を外せて、

<div>
$$
S = \int_\alpha^\beta (f(x) - g(x))\,dx
$$
</div>

となります。区間内で上下が入れ替わる場合は、入れ替わる点で区間を分割する必要があります。

---

## 4 ステップ手順

**Step 1:** \\( f(x) = g(x) \\) を解いて交点の \\( x \\) 座標 \\( \alpha, \beta \\) を求める。

**Step 2:** 各区間で上の曲線（\\( f - g \\) の符号）を確認する。

**Step 3:** 上下が逆転する点で区間を分割する。

**Step 4:** \\( \int(\text{上} - \text{下})\,dx \\) を各区間で計算して合算する。

---

## 例 1: \\( y = x + 2 \\) と \\( y = x^2 \\) の間の面積

**Step 1:** 交点を求める。

<div>
$$
x^2 = x + 2 \implies x^2 - x - 2 = 0 \implies (x-2)(x+1) = 0
$$
</div>

<div>
$$
\implies x = -1,\quad x = 2
$$
</div>

**Step 2:** 上下の確認（\\( x = 0 \\) で確認）。

<div>
$$
f(0) = 0 + 2 = 2,\quad g(0) = 0^2 = 0
$$
</div>

\\( [-1,\,2] \\) では \\( y = x + 2 \\) が上。

**Step 3:** 区間分割は不要（上下の入れ替わりなし）。

**Step 4:** 面積を計算する。

<div>
$$
S = \int_{-1}^{2}\bigl((x+2) - x^2\bigr)\,dx = \int_{-1}^{2}(-x^2+x+2)\,dx
$$
</div>

<div>
$$
= \left[-\frac{x^3}{3} + \frac{x^2}{2} + 2x\right]_{-1}^{2}
$$
</div>

\\( x = 2 \\) での値: \\( -\frac{8}{3} + 2 + 4 = -\frac{8}{3} + 6 = \frac{10}{3} \\)

\\( x = -1 \\) での値: \\( \frac{1}{3} + \frac{1}{2} - 2 = \frac{2}{6} + \frac{3}{6} - \frac{12}{6} = -\frac{7}{6} \\)

<div>
$$
S = \frac{10}{3} - \left(-\frac{7}{6}\right) = \frac{20}{6} + \frac{7}{6} = \frac{27}{6} = \frac{9}{2}
$$
</div>

**答え:** \\( S = \frac{9}{2} \\)

---

## 例 2: \\( y = x^3 \\) と \\( y = x \\) の間の面積（\\( -1 \leq x \leq 1 \\)）

**Step 1:** 交点を求める。

<div>
$$
x^3 = x \implies x(x^2 - 1) = 0 \implies x = -1,\; 0,\; 1
$$
</div>

**Step 2:** 各区間での上下確認。

- \\( [-1,\,0] \\): \\( x = -\frac{1}{2} \\) で \\( x^3 - x = -\frac{1}{8} - \left(-\frac{1}{2}\right) = \frac{3}{8} > 0 \\) → \\( y = x^3 \\) が上
- \\( [0,\,1] \\): \\( x = \frac{1}{2} \\) で \\( x^3 - x = \frac{1}{8} - \frac{1}{2} = -\frac{3}{8} < 0 \\) → \\( y = x \\) が上

**Step 3:** \\( x = 0 \\) で区間を分割。

**Step 4:** 対称性（グラフが原点対称）を使う。

<div>
$$
S = 2\int_0^1 (x - x^3)\,dx = 2\left[\frac{x^2}{2} - \frac{x^4}{4}\right]_0^1 = 2\left(\frac{1}{2} - \frac{1}{4}\right) = 2 \cdot \frac{1}{4} = \frac{1}{2}
$$
</div>

**答え:** \\( S = \frac{1}{2} \\)

---

![f が g 以上の場合（左）/ 上下逆転する場合（右）](/assets/images/integ-area-curves-combined.png)

---

## もっと練習したい方へ

2 曲線の面積・区間分割・対称性の利用を含む問題を収録した解説 PDF を無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/integ-area-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [x軸との面積](/integ-area-xaxis/)　／　[積分と面積](/integ-area/)　／　→ [面積公式](/integ-area-formula/)
