---
layout: default
title: 内分・外分 — 点の位置を比で表す
permalink: /vec-division/
description: "内分点の位置ベクトル公式（比による重みつき平均）、外分点の符号の変化、中点の導出（高校数B）。"
---

← [位置ベクトルの考え方](/vec-position/)　／　[位置ベクトルと図形](/vec-geometry/)　／　→ [図形条件のベクトル式化](/vec-figure-conditions/)

---

# 内分・外分 — 点の位置を比で表す

---

## 動機: 「比で引き寄せられる」点を式で表したい

線分 AB を m:n に内分する点 P は「A と B の間で m:n の比率にある」点です。A に近いほど \\( \\vec{a} \\) の影響が大きく、B に近いほど \\( \\vec{b} \\) の影響が大きい — これが内分点の位置ベクトルです。

---

## 内分点の公式

\\( \\overrightarrow{OA}=\\vec{a} \\), \\( \\overrightarrow{OB}=\\vec{b} \\) のとき、AB を m:n に内分する点 P の位置ベクトル：

<div>
$$
\overrightarrow{OP} = \frac{n\vec{a}+m\vec{b}}{m+n}
$$
</div>

**導出**: \\( \\overrightarrow{AP} = \\frac{m}{m+n}\\overrightarrow{AB} = \\frac{m}{m+n}(\\vec{b}-\\vec{a}) \\) より：

<div>
$$
\overrightarrow{OP} = \vec{a} + \frac{m}{m+n}(\vec{b}-\vec{a}) = \frac{n\vec{a}+m\vec{b}}{m+n}
$$
</div>

![内分点の比による位置（左）/ 外分点の図（右）](/assets/images/vec-division-combined.png)

---

## 中点の公式

m = n = 1 のとき（1:1 の内分 = 中点）：

<div>
$$
\overrightarrow{OM} = \frac{\vec{a}+\vec{b}}{2}
$$
</div>

「A と B の平均の位置」という意味です。

---

## 外分点の公式

AB を m:n に外分する点 Q の位置ベクトル（\\( m \\neq n \\)）：

<div>
$$
\overrightarrow{OQ} = \frac{-n\vec{a}+m\vec{b}}{m-n}
$$
</div>

内分点の公式で n を −n に置き換えた形です。符号が変わるのは「線分の外に出る」からです。

---

## 計算例

### 例 1: 3:1 内分・外分

\\( \\vec{a}=(1,0) \\), \\( \\vec{b}=(5,4) \\) のとき AB を 3:1 に内分する点 P と外分する点 Q：

**内分**: \\( \\overrightarrow{OP} = \\frac{1\\cdot\\vec{a}+3\\cdot\\vec{b}}{4} = \\frac{(1,0)+(15,12)}{4} = \\frac{(16,12)}{4} = (4,3) \\)

**外分**: \\( \\overrightarrow{OQ} = \\frac{-1\\cdot\\vec{a}+3\\cdot\\vec{b}}{2} = \\frac{(-1,0)+(15,12)}{2} = \\frac{(14,12)}{2} = (7,6) \\)

### 例 2: 三角形 OAB の中線

\\( \\overrightarrow{OA}=\\vec{a} \\), \\( \\overrightarrow{OB}=\\vec{b} \\) で辺 AB の中点 M：

<div>
$$
\overrightarrow{OM} = \frac{\vec{a}+\vec{b}}{2}
$$
</div>

### 例 3: OA を 2:1 に内分する点 P

<div>
$$
\overrightarrow{OP} = \frac{1\cdot\vec{0}+2\cdot\vec{a}}{3} = \frac{2}{3}\vec{a}
$$
</div>

（O の位置ベクトルは \\( \\vec{0} \\)）

確認: \\( \\overrightarrow{OP}:\\overrightarrow{PA} = \\frac{2}{3}:\\frac{1}{3} = 2:1 \\) ✓

---

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-geometry-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [位置ベクトルの考え方](/vec-position/)　／　[位置ベクトルと図形](/vec-geometry/)　／　→ [図形条件のベクトル式化](/vec-figure-conditions/)
