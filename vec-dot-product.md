---
layout: default
title: 内積の意味 — なぜ cos θ が出てくるか
permalink: /vec-dot-product/
description: "ベクトルの内積の定義（射影から導く）、成分公式、なす角の計算、内積の符号と方向の関係（高校数B）。"
---

[内積と図形](/vec-inner-product/)　／　→ [垂直条件](/vec-perpendicular/)

---

# 内積の意味 — なぜ cos θ が出てくるか

---

## 動機: 「2つのベクトルがどれだけ同方向を向いているか」

2 つのベクトルが「どの程度同じ方向を向いているか」を数値で表したいとき、内積が役立ちます。

\\( \\vec{a} \\) を \\( \\vec{b} \\) の方向に射影すると、長さ \\( |\\vec{a}|\\cos\\theta \\) の成分が得られます（\\( \\theta \\) はなす角）。この射影の長さに \\( |\\vec{b}| \\) をかけた量を内積と定義します。

---

## 内積の定義

<div>
$$
\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta \quad (0\leq\theta\leq\pi)
$$
</div>

![射影と内積の対応（左）/ cosθ の符号と内積の正負（右）](/assets/images/vec-dot-product-combined.png)

---

## 内積の符号の意味

- \\( \\theta < 90° \\) のとき \\( \\cos\\theta > 0 \\): 内積 \\( > 0 \\)（同方向寄り）
- \\( \\theta = 90° \\) のとき \\( \\cos\\theta = 0 \\): 内積 \\( = 0 \\)（垂直）
- \\( \\theta > 90° \\) のとき \\( \\cos\\theta < 0 \\): 内積 \\( < 0 \\)（逆方向寄り）

---

## 成分公式

\\( \\vec{a} = (a_1, a_2) \\), \\( \\vec{b} = (b_1, b_2) \\) のとき：

<div>
$$
\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2
$$
</div>

（導出は余弦定理を使います。[垂直条件](/vec-perpendicular/) で詳しく説明します。）

---

## 計算例

### 例 1: 2通りの計算で確認

\\( \\vec{a} = (1, \\sqrt{3}) \\), \\( \\vec{b} = (2, 0) \\) のとき：

**成分公式**: \\( \\vec{a}\\cdot\\vec{b} = 1\\cdot 2 + \\sqrt{3}\\cdot 0 = 2 \\)

**定義**: \\( |\\vec{a}| = \\sqrt{1+3} = 2 \\), \\( |\\vec{b}|=2 \\), なす角 \\( \\theta = 60° \\)

<div>
$$
\vec{a}\cdot\vec{b} = 2\cdot 2\cdot\cos 60° = 4\cdot\frac{1}{2} = 2 \checkmark
$$
</div>

### 例 2: なす角を求める

\\( \\vec{a}=(1,1) \\), \\( \\vec{b}=(1,-1) \\) のとき：

<div>
$$
\vec{a}\cdot\vec{b} = 1\cdot 1+1\cdot(-1) = 0
$$
</div>

<div>
$$
\cos\theta = 0 \implies \theta = 90°
$$
</div>

### 例 3: 射影の長さ

\\( \\vec{a}=(3,0) \\), \\( \\vec{b}=(2,2) \\) で \\( \\vec{b} \\) の \\( \\vec{a} \\) への射影の長さ：

<div>
$$
|\vec{b}|\cos\theta = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}|} = \frac{6+0}{3} = 2
$$
</div>

---

## 関連記事

- [三角関数のグラフ](/trigonometry/) — cos の値域と符号

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-inner-product-pack.pdf">PDFをダウンロードする（無料）</a>

---

[内積と図形](/vec-inner-product/)　／　→ [垂直条件](/vec-perpendicular/)
