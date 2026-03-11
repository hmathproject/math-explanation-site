---
layout: default
title: 位置ベクトルの考え方 — 点を式で扱う
permalink: /vec-position/
description: "位置ベクトルの定義（原点Oからの矢印）、AB=b-aの導出、点が線分AB上にある条件（高校数B）。"
---

[位置ベクトルと図形](/vec-geometry/)　／　→ [内分・外分](/vec-division/)

---

# 位置ベクトルの考え方 — 点を式で扱う

---

## 動機: 「点の位置をベクトルで表す利点」

座標 \\( (x, y) \\) で点を表すと、点と点の関係を計算するとき毎回座標を使う必要があります。位置ベクトルを使うと、点の位置関係を「ベクトルの演算」で直接扱えます。

---

## 位置ベクトルの定義

原点 O を固定し、点 P に対して \\( \\overrightarrow{OP} \\) を P の**位置ベクトル**といいます。慣例として \\( \\overrightarrow{OP} = \\vec{p} \\) と書きます。

![OA, OB, OP の位置ベクトル（左）/ AB = b - a の導出図（右）](/assets/images/vec-position-combined.png)

---

## \\( \\overrightarrow{AB} = \\vec{b} - \\vec{a} \\) の導出

「O から A へ行き（\\( \\vec{a} \\)）、そこから B へ行く（\\( \\overrightarrow{AB} \\)）」と「O から B へ行く（\\( \\vec{b} \\)）」は同じ道筋：

<div>
$$
\overrightarrow{OA} + \overrightarrow{AB} = \overrightarrow{OB}
$$
</div>

<div>
$$
\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \vec{b} - \vec{a}
$$
</div>

「**終点の位置ベクトル − 始点の位置ベクトル**」という形です。

---

## 線分 AB 上の点 P の条件

P が線分 AB 上にある \\( \\Leftrightarrow \\) \\( \\overrightarrow{AP} = t\\overrightarrow{AB} \\)（\\( 0 \\leq t \\leq 1 \\)）

<div>
$$
\overrightarrow{OP} = \overrightarrow{OA} + t\overrightarrow{AB} = \vec{a} + t(\vec{b}-\vec{a}) = (1-t)\vec{a} + t\vec{b}
$$
</div>

- \\( t=0 \\): P = A（点 A）
- \\( t=1 \\): P = B（点 B）
- \\( t=\\frac{1}{2} \\): P は中点（\\( \\overrightarrow{OP}=\\frac{\\vec{a}+\\vec{b}}{2} \\)）

---

## 計算例

### 例 1: OA, OB, AB と \\( |AB| \\)

O を原点、A(2, 3), B(-1, 5) のとき：

<div>
$$
\overrightarrow{OA} = (2, 3),\quad \overrightarrow{OB} = (-1, 5)
$$
</div>

<div>
$$
\overrightarrow{AB} = \vec{b}-\vec{a} = (-1-2,\ 5-3) = (-3,\ 2)
$$
</div>

<div>
$$
|\overrightarrow{AB}| = \sqrt{9+4} = \sqrt{13}
$$
</div>

### 例 2: \\( \\vec{a}+\\vec{b} \\) の終点と AB の中点の比較

\\( \\vec{a}=(2,1) \\), \\( \\vec{b}=(0,4) \\) のとき：

\\( \\vec{a}+\\vec{b}=(2,5) \\)（終点）、AB の中点: \\( \\frac{\\vec{a}+\\vec{b}}{2}=(1,\\frac{5}{2}) \\)

\\( (2,5) \\neq (1,\\frac{5}{2}) \\) → AB の中点ではない。

\\( \\vec{a}+\\vec{b} \\) は平行四辺形の対角線の終点です（AB の中点ではない）。

### 例 3: 線分 AB 上の点

A の位置ベクトル \\( \\vec{a} \\)、B の位置ベクトル \\( \\vec{b} \\) のとき、P が AB 上（\\( t=\\frac{1}{3} \\)）：

<div>
$$
\overrightarrow{OP} = \frac{2}{3}\vec{a}+\frac{1}{3}\vec{b}
$$
</div>

（係数の和 = \\( \\frac{2}{3}+\\frac{1}{3}=1 \\): 常に 1 になります）

---

## 関連記事

- [図形と方程式](/coordinate-geometry/) — 座標平面での点の表現との対比

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-geometry-pack.pdf">PDFをダウンロードする（無料）</a>

---

[位置ベクトルと図形](/vec-geometry/)　／　→ [内分・外分](/vec-division/)
