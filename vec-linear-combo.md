---
layout: default
title: 1次結合と分解 — 2つのベクトルで平面を記述する
permalink: /vec-linear-combo/
description: "非平行な2ベクトルによる平面表現、1次結合の係数の一意性、基底ベクトルと線形独立性（高校数B）。"
---

← [成分による演算](/vec-component-ops/)　／　[成分と演算](/vec-components/)

---

# 1次結合と分解 — 2つのベクトルで平面を記述する

---

## 動機: 「2本の矢印で平面全体を記述できるか」

非平行な 2 つのベクトル \\( \\vec{a} \\), \\( \\vec{b} \\) があれば、それらを組み合わせて平面上の**任意のベクトル**を表せます。これが 1 次結合の核心です。

---

## 1次結合 \\( s\\vec{a} + t\\vec{b} \\)

実数 \\( s, t \\) を変えると、\\( s\\vec{a} + t\\vec{b} \\) は平面上のあらゆる方向・大きさのベクトルを表せます。なぜなら \\( \\vec{a} \\) 方向と \\( \\vec{b} \\) 方向が異なる（非平行）ので、2 方向の組み合わせで全方向をカバーできるからです。

![基本ベクトル e₁, e₂ の 1 次結合（左）/ 任意ベクトルの sa+tb 分解（右）](/assets/images/vec-linear-combo-combined.png)

---

## 係数の一意性 — なぜ表し方が 1 通りか

**定理**: \\( \\vec{a}, \\vec{b} \\) が非平行なら、\\( s\\vec{a}+t\\vec{b} = \\vec{c} \\) を満たす \\( s, t \\) は一意に定まる。

**証明（\\( s = t = 0 \\) でなければ零ベクトルになれない）**:

\\( s\\vec{a}+t\\vec{b}=\\vec{0} \\) のとき、もし \\( s \\neq 0 \\) なら \\( \\vec{a} = -\\frac{t}{s}\\vec{b} \\)（平行を意味する）→ 矛盾。したがって \\( s=0 \\)、同様に \\( t=0 \\)。

---

## 基本ベクトル \\( \\vec{e}_1, \\vec{e}_2 \\)

最もシンプルな基底は：

<div>
$$
\vec{e}_1 = (1, 0), \quad \vec{e}_2 = (0, 1)
$$
</div>

任意のベクトル \\( (a_1, a_2) \\) は：

<div>
$$
(a_1, a_2) = a_1\vec{e}_1 + a_2\vec{e}_2
$$
</div>

成分表示はこの 1 次結合の係数に他なりません。

---

## 計算例

### 例 1: \\( \\vec{p}=(5,4) \\) を \\( s\\vec{a}+t\\vec{b} \\) で表す

\\( \\vec{a}=(1,2) \\), \\( \\vec{b}=(3,1) \\) のとき成分ごとに：

<div>
$$
s + 3t = 5, \quad 2s + t = 4
$$
</div>

① \\( \\times 2 - \\) ②: \\( 5t = 6 \\), \\( t = \\frac{6}{5} \\)

<div>
$$
s = \frac{4-\frac{6}{5}}{2} = \frac{7}{5}
$$
</div>

<div>
$$
\vec{p} = \frac{7}{5}\vec{a}+\frac{6}{5}\vec{b}
$$
</div>

確認: \\( \\frac{7}{5}(1,2)+\\frac{6}{5}(3,1) = \\left(\\frac{7+18}{5},\\ \\frac{14+6}{5}\\right) = (5,\\ 4) \\) ✓

### 例 2: 三角形 OAB の PQ を \\( \\vec{a}, \\vec{b} \\) で表す

\\( \\overrightarrow{OA}=\\vec{a} \\), \\( \\overrightarrow{OB}=\\vec{b} \\) で、P が OA の 2:1 内分点、Q が OB の中点のとき：

<div>
$$
\overrightarrow{OP} = \frac{2}{3}\vec{a}, \quad \overrightarrow{OQ} = \frac{1}{2}\vec{b}
$$
</div>

<div>
$$
\overrightarrow{PQ} = \overrightarrow{OQ}-\overrightarrow{OP} = \frac{1}{2}\vec{b}-\frac{2}{3}\vec{a}
$$
</div>

### 例 3: 非平行なら \\( s=t=0 \\) のみで零ベクトル

\\( \\vec{a}=(1,2) \\), \\( \\vec{b}=(3,1) \\)（非平行）のとき \\( s\\vec{a}+t\\vec{b}=\\vec{0} \\) は \\( s=t=0 \\) のみ。

連立方程式 \\( s+3t=0, 2s+t=0 \\) を解くと \\( s=t=0 \\)。

---

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-components-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [成分による演算](/vec-component-ops/)　／　[成分と演算](/vec-components/)
