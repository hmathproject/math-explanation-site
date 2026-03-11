---
layout: default
title: 図形条件のベクトル式化 — 重心・平行・共線
permalink: /vec-figure-conditions/
description: "重心が3点の平均の位置になる理由、共線条件（APがABの実数倍）、平行条件のベクトル式（高校数B）。"
---

← [内分・外分](/vec-division/)　／　[位置ベクトルと図形](/vec-geometry/)

---

# 図形条件のベクトル式化 — 重心・平行・共線

---

## 動機: 「図形の条件を等式に翻訳する」

図形の性質（「3点が一直線上」「2直線が平行」「点が重心」）をベクトルの等式として書くことで、計算で確認・証明できます。

---

## 重心 — 3点の「平均の位置」

三角形 ABC の重心 G の位置ベクトル：

<div>
$$
\overrightarrow{OG} = \frac{\vec{a}+\vec{b}+\vec{c}}{3}
$$
</div>

**導出**: 中線 AM（M は BC の中点）を 2:1 に内分する点が G：

<div>
$$
\overrightarrow{OM} = \frac{\vec{b}+\vec{c}}{2}
$$
</div>

<div>
$$
\overrightarrow{OG} = \vec{a} + \frac{2}{3}(\overrightarrow{OM}-\vec{a}) = \frac{\vec{a}+\vec{b}+\vec{c}}{3}
$$
</div>

![重心 G の導出図（左）/ 共線条件の図（右）](/assets/images/vec-figure-conditions-combined.png)

---

## 共線条件 — P が直線 AB 上にある

P が直線 AB 上にある \\( \\Leftrightarrow \\) \\( \\overrightarrow{AP} \\) が \\( \\overrightarrow{AB} \\) の実数倍

<div>
$$
\overrightarrow{OP} = (1-t)\vec{a}+t\vec{b} \quad (t\in\mathbb{R})
$$
</div>

線分 AB（\\( 0 \\leq t \\leq 1 \\)）に対し、直線全体は \\( t \\) が全実数を動きます。

---

## 平行条件のベクトル式

\\( \\overrightarrow{PQ} \\parallel \\overrightarrow{RS} \\) \\( \\Leftrightarrow \\) \\( \\overrightarrow{PQ} = k\\overrightarrow{RS} \\)（\\( k \\) は実数）

---

## 計算例

### 例 1: 重心の位置ベクトルと確認

A(1,0), B(0,2), C(2,1)（位置ベクトル \\( \\vec{a}=(1,0) \\), \\( \\vec{b}=(0,2) \\), \\( \\vec{c}=(2,1) \\)）の重心 G：

<div>
$$
\overrightarrow{OG} = \frac{(1,0)+(0,2)+(2,1)}{3} = \frac{(3,3)}{3} = (1,1)
$$
</div>

確認（中線 AM, M は BC の中点）: \\( M=\\frac{(0,2)+(2,1)}{2}=(1,\\frac{3}{2}) \\)

AM の 2:1 内分点: \\( A+\\frac{2}{3}(M-A) = (1,0)+\\frac{2}{3}(0,\\frac{3}{2}) = (1,1) \\) ✓

### 例 2: 共線条件を利用

\\( \\vec{a}=(1,0) \\), \\( \\vec{b}=(0,1) \\) で、点 P が直線 AB 上にある条件:

<div>
$$
\overrightarrow{OP} = (1-t)(1,0)+t(0,1) = (1-t,\ t)
$$
</div>

P の x 座標と y 座標の和 = \\( (1-t)+t = 1 \\)（常に 1）→ P は直線 \\( x+y=1 \\) 上。

### 例 3: 重心と中点の違い

三角形 OAB（O が原点）の重心 G と辺 OA の中点 M\_OA を比較:

<div>
$$
\overrightarrow{OG} = \frac{\vec{0}+\vec{a}+\vec{b}}{3} = \frac{\vec{a}+\vec{b}}{3}
$$
</div>

<div>
$$
M_{OA} = \frac{\vec{a}}{2}
$$
</div>

\\( G \\neq M_{OA} \\)（重心は辺の中点ではなく、中線の 2:1 内分点）。

---

## 関連記事

- [図形と方程式（軌跡）](/coord-locus/) — 軌跡の条件式との対比

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-geometry-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [内分・外分](/vec-division/)　／　[位置ベクトルと図形](/vec-geometry/)
