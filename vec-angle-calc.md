---
layout: default
title: なす角と長さの計算 — 内積の使い方
permalink: /vec-angle-calc/
description: "内積を使ったなす角の計算、|a+b|²の展開（余弦定理との対比）、長さの計算への応用（高校数B）。"
---

← [垂直条件](/vec-perpendicular/)　／　[内積と図形](/vec-inner-product/)

---

# なす角と長さの計算 — 内積の使い方

---

## 動機: 内積から角度・長さを引き出す

内積の定義 \\( \\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta \\) を変形すると：

<div>
$$
\cos\theta = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}
$$
</div>

この式でなす角 \\( \\theta \\) を計算できます。また \\( |\\vec{a}+\\vec{b}|^2 \\) を内積で展開すると余弦定理が自然に出てきます。

---

## \\( |\\vec{a}+\\vec{b}|^2 \\) の展開

<div>
$$
|\vec{a}+\vec{b}|^2 = (\vec{a}+\vec{b})\cdot(\vec{a}+\vec{b})
$$
</div>

<div>
$$
= \vec{a}\cdot\vec{a} + 2\vec{a}\cdot\vec{b} + \vec{b}\cdot\vec{b}
$$
</div>

<div>
$$
= |\vec{a}|^2 + 2\vec{a}\cdot\vec{b} + |\vec{b}|^2
$$
</div>

**余弦定理との対比**: \\( c^2 = a^2 + b^2 - 2ab\\cos C \\) は \\( |\\vec{a}-\\vec{b}|^2 = |\\vec{a}|^2 - 2\\vec{a}\\cdot\\vec{b} + |\\vec{b}|^2 \\) と同じ形です。

![なす角の計算とcosθ（左）/ |a+b|²展開と余弦定理の対比（右）](/assets/images/vec-angle-calc-combined.png)

---

## 計算例

### 例 1: なす角を求める

\\( \\vec{a}=(1,\\sqrt{3}) \\), \\( \\vec{b}=(2,0) \\) のとき：

<div>
$$
\vec{a}\cdot\vec{b} = 1\cdot 2+\sqrt{3}\cdot 0 = 2
$$
</div>

<div>
$$
|\vec{a}|=\sqrt{1+3}=2,\quad |\vec{b}|=2
$$
</div>

<div>
$$
\cos\theta = \frac{2}{2\cdot 2} = \frac{1}{2} \implies \theta = 60°
$$
</div>

### 例 2: \\( |\\vec{a}+\\vec{b}| \\) と \\( |\\vec{a}-\\vec{b}| \\) を求める

\\( \\vec{a}=(3,1) \\), \\( \\vec{b}=(1,2) \\) のとき：

<div>
$$
|\vec{a}|^2 = 10,\quad |\vec{b}|^2 = 5,\quad \vec{a}\cdot\vec{b} = 3+2 = 5
$$
</div>

<div>
$$
|\vec{a}+\vec{b}|^2 = 10+2\cdot 5+5 = 25 \implies |\vec{a}+\vec{b}|=5
$$
</div>

<div>
$$
|\vec{a}-\vec{b}|^2 = 10-2\cdot 5+5 = 5 \implies |\vec{a}-\vec{b}|=\sqrt{5}
$$
</div>

### 例 3: \\( |\\vec{a}|=2 \\), \\( |\\vec{b}|=3 \\), \\( \\vec{a}\\cdot\\vec{b}=3 \\) のとき \\( |2\\vec{a}-\\vec{b}| \\)

<div>
$$
|2\vec{a}-\vec{b}|^2 = 4|\vec{a}|^2 - 4\vec{a}\cdot\vec{b} + |\vec{b}|^2
$$
</div>

<div>
$$
= 4\cdot 4 - 4\cdot 3 + 9 = 16-12+9 = 13
$$
</div>

<div>
$$
|2\vec{a}-\vec{b}| = \sqrt{13}
$$
</div>

---

## 関連記事

- [三角関数の性質と相互関係](/trig-relations/) — 余弦定理との対比

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-inner-product-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [垂直条件](/vec-perpendicular/)　／　[内積と図形](/vec-inner-product/)
