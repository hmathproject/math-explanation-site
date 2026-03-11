---
layout: default
title: 面積公式 — 1/6公式
permalink: /integ-area-formula/
description: "∫_α^β (x−α)(x−β)dx = −(β−α)³/6 の1/6公式を導出し、2次関数と x 軸・2曲線の面積計算への応用を解説する（高校数II）。"
---

[サイトトップ](/) / [積分](/integral/) / [積分と面積](/integ-area/)

---

# 面積公式 — 1/6公式

---

## 適用条件

1/6 公式は次の条件を満たすときに使えます。

- 被積分関数が \\( (x - \alpha)(x - \beta) \\) の形（または定数倍）に因数分解できる
- 積分区間がちょうど \\( [\alpha,\,\beta] \\)（2 つの因子の零点に一致）

この条件を満たすときは、毎回展開して積分する手間を省いて計算できます。

---

## 1/6 公式の導出

\\( l = \beta - \alpha \\) とおいて \\( t = x - \alpha \\) と置き換えます（\\( dx = dt \\)、\\( x = \alpha \\) で \\( t = 0 \\)、\\( x = \beta \\) で \\( t = l \\)）。

<div>
$$
\int_\alpha^\beta (x-\alpha)(x-\beta)\,dx = \int_0^l t(t - l)\,dt = \int_0^l (t^2 - lt)\,dt
$$
</div>

<div>
$$
= \left[\frac{t^3}{3} - \frac{lt^2}{2}\right]_0^l = \frac{l^3}{3} - \frac{l^3}{2} = l^3\left(\frac{1}{3} - \frac{1}{2}\right) = -\frac{l^3}{6}
$$
</div>

<div>
$$
= -\frac{(\beta - \alpha)^3}{6}
$$
</div>

面積はこの絶対値ですから、

<div>
$$
\int_\alpha^\beta |(x-\alpha)(x-\beta)|\,dx = \frac{(\beta-\alpha)^3}{6}
$$
</div>

これが **1/6 公式**です。

---

## 公式の適用例: \\( y = x^2 - 3x + 2 \\) と \\( x \\) 軸の間の面積

**Step 1:** 因数分解する。

<div>
$$
x^2 - 3x + 2 = (x-1)(x-2)
$$
</div>

**Step 2:** \\( \alpha = 1, \beta = 2 \\) を公式に代入する。

<div>
$$
S = \frac{(\beta - \alpha)^3}{6} = \frac{(2-1)^3}{6} = \frac{1}{6}
$$
</div>

**答え:** \\( S = \frac{1}{6} \\)

確かめ（直接計算）:

<div>
$$
\int_1^2(x^2-3x+2)\,dx = \left[\frac{x^3}{3} - \frac{3x^2}{2} + 2x\right]_1^2
= \left(\frac{8}{3}-6+4\right)-\left(\frac{1}{3}-\frac{3}{2}+2\right)
= \frac{2}{3} - \frac{5}{6} = -\frac{1}{6}
$$
</div>

面積 \\( = \left|-\frac{1}{6}\right| = \frac{1}{6} \\) ✓

---

## 2曲線への拡張 — \\( a(x-\alpha)(x-\beta) \\) 型

\\( f(x) - g(x) = a(x-\alpha)(x-\beta) \\) と因数分解できるとき（\\( a \neq 0 \\)）、

<div>
$$
S = \int_\alpha^\beta |f(x) - g(x)|\,dx = |a| \cdot \frac{(\beta-\alpha)^3}{6}
$$
</div>

**例:** \\( y = x^2 \\) と \\( y = x + 2 \\) の間の面積

\\( f(x) - g(x) = x^2 - (x+2) = x^2 - x - 2 = (x+1)(x-2) \\)

\\( \alpha = -1,\; \beta = 2,\; a = 1 \\) なので、

<div>
$$
S = 1 \cdot \frac{(2-(-1))^3}{6} = \frac{3^3}{6} = \frac{27}{6} = \frac{9}{2}
$$
</div>

前の記事で展開計算した答え \\( \frac{9}{2} \\) と一致します ✓

---

## 1/6 公式が使えない場合

1/6 公式は「積分区間の両端が因子の零点に一致する」場合にのみ使えます。以下の場合は直接計算が必要です。

- 積分区間が \\( [\alpha, \beta] \\) 全体でなく一部だけの場合
- \\( f(x) - g(x) \\) が 3 次以上で、1 次式 2 つの積に因数分解できない場合
- 区間内で上下の入れ替わりがあり、複数区間に分割した後それぞれが異なる公式を必要とする場合

---

![1/6公式の図示（左）/ 2曲線への応用（右）](/assets/images/integ-area-formula-combined.png)

---

## もっと練習したい方へ

1/6 公式・\\( a(x-\alpha)(x-\beta) \\) 型・適用条件の確認を含む問題を収録した解説 PDF を無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/integ-area-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [2曲線の間の面積](/integ-area-curves/)　／　[積分と面積](/integ-area/)
