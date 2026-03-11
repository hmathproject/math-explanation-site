---
layout: default
title: 垂直条件 — a·b = 0 になる理由
permalink: /vec-perpendicular/
description: "垂直条件a·b=0の導出（cos90°=0から必然）、内積の成分公式の導出（余弦定理を使う）、応用例（高校数B）。"
---

← [内積の意味](/vec-dot-product/)　／　[内積と図形](/vec-inner-product/)　／　→ [なす角と長さの計算](/vec-angle-calc/)

---

# 垂直条件 — a·b = 0 になる理由

---

## 動機: 垂直のとき内積がゼロになるのはなぜか

内積の定義 \\( \\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta \\) から、\\( \\theta = 90° \\) のとき \\( \\cos 90° = 0 \\) なので：

<div>
$$
\vec{a} \perp \vec{b} \implies \vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos 90° = 0
$$
</div>

これは「公式を覚える」のではなく、定義から必然的に出る結論です。

---

## 垂直条件の証明

\\( \\vec{a} \\neq \\vec{0} \\), \\( \\vec{b} \\neq \\vec{0} \\) のとき：

<div>
$$
\vec{a} \perp \vec{b} \iff \theta = 90° \iff \cos\theta = 0 \iff \vec{a}\cdot\vec{b} = 0
$$
</div>

---

## 成分公式の導出 — 余弦定理を使う

![垂直条件の確認（左）/ 余弦定理から成分公式を導く（右）](/assets/images/vec-perpendicular-combined.png)

\\( \\vec{a} = (a_1, a_2) \\), \\( \\vec{b} = (b_1, b_2) \\) として、\\( \\vec{a}-\\vec{b} \\) の大きさの 2 乗に余弦定理を適用します：

<div>
$$
|\vec{a}-\vec{b}|^2 = |\vec{a}|^2 + |\vec{b}|^2 - 2|\vec{a}||\vec{b}|\cos\theta
$$
</div>

左辺を成分で計算：

<div>
$$
|\vec{a}-\vec{b}|^2 = (a_1-b_1)^2+(a_2-b_2)^2
$$
</div>

<div>
$$
= a_1^2 - 2a_1 b_1 + b_1^2 + a_2^2 - 2a_2 b_2 + b_2^2
$$
</div>

右辺: \\( |\\vec{a}|^2 + |\\vec{b}|^2 - 2|\\vec{a}||\\vec{b}|\\cos\\theta = a_1^2+a_2^2 + b_1^2+b_2^2 - 2|\\vec{a}||\\vec{b}|\\cos\\theta \\)

両辺を等しくおくと：

<div>
$$
-2a_1 b_1 - 2a_2 b_2 = -2|\vec{a}||\vec{b}|\cos\theta
$$
</div>

<div>
$$
\therefore\quad \vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1 b_1 + a_2 b_2
$$
</div>

---

## 計算例

### 例 1: 垂直の確認（2通りで）

\\( \\vec{a}=(3,1) \\), \\( \\vec{b}=(-1,3) \\) のとき：

**成分公式**: \\( \\vec{a}\\cdot\\vec{b} = 3\\cdot(-1)+1\\cdot 3 = -3+3 = 0 \\)

\\( \\cos\\theta = \\frac{0}{|\\vec{a}||\\vec{b}|} = 0 \\) → \\( \\theta = 90° \\) ✓

**確認**: \\( \\vec{a} = (3,1) \\) と \\( \\vec{b}=(-1,3) \\) は傾きが \\( \\frac{1}{3} \\) と \\( -3 \\)（積 = -1）→ 垂直 ✓

### 例 2: 垂直なベクトルを求める

\\( \\vec{a}=(2,3) \\) に垂直なベクトルを求めよ。

\\( \\vec{b}=(b_1,b_2) \\) が \\( \\vec{a}\\cdot\\vec{b}=0 \\) を満たすとき:

<div>
$$
2b_1 + 3b_2 = 0 \implies b_1 = -\frac{3}{2}b_2
$$
</div>

例えば \\( b_2=2 \\) とすると \\( \\vec{b}=(-3,2) \\)。確認: \\( 2\\cdot(-3)+3\\cdot 2 = 0 \\) ✓

### 例 3: 直角三角形の確認

O(0,0), A(4,0), B(0,3) において \\( \\angle AOB \\) が直角か確認:

<div>
$$
\overrightarrow{OA}\cdot\overrightarrow{OB} = 4\cdot 0+0\cdot 3 = 0 \implies \overrightarrow{OA}\perp\overrightarrow{OB} \checkmark
$$
</div>

---

## 関連記事

- [図形と方程式（円の接線）](/coord-circle-tangent/) — 法線・接線の垂直条件

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-inner-product-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [内積の意味](/vec-dot-product/)　／　[内積と図形](/vec-inner-product/)　／　→ [なす角と長さの計算](/vec-angle-calc/)
