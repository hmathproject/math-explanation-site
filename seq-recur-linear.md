---
layout: default
title: 1次変換型漸化式 — 何を引けば等比になるか
permalink: /seq-recur-linear/
description: "a_{n+1}=p*a_n+q から固定点 α（α=pα+q の解）を引くと等比型になる理由を導出。p<0 の振動ケースも解説（高校数B）。"
---

← [基本型漸化式](/seq-recur-basic/)　／　[漸化式](/seq-recurrence/)　／　→ [Σ型漸化式](/seq-recur-fn/)

---

# 1次変換型漸化式 — 何を引けば等比になるか

---

## 動機: 定数項を消して等比型に持ち込む

\\( a_{n+1} = pa_n + q \\) の形では、定数 \\( q \\) が邪魔で「比が一定」とは言えません。**「何かを引けば \\( q \\) が消えて等比型になるか」** を考えます。

\\( a_{n+1} - \\alpha = p(a_n - \\alpha) \\) が成り立てば、\\( b_n = a_n - \\alpha \\) は公比 \\( p \\) の等比数列になります。この条件を \\( \\alpha \\) について解くと：

<div>
$$
a_{n+1} - \alpha = pa_n + q - \alpha = p(a_n - \alpha) \iff q = \alpha - p\alpha = \alpha(1-p)
$$
</div>

よって **\\( \\alpha = p\\alpha + q \\) を解いて固定点 \\( \\alpha \\) を求める**。これは「漸化式の \\( a_n \\) を \\( \\alpha \\) に置き換えた方程式の解」です。

---

## 固定点の意味

\\( \\alpha \\) は「もし \\( a_n = \\alpha \\) なら \\( a_{n+1} \\) も \\( \\alpha \\) になる」点（不動点）です。この点からのずれ \\( b_n = a_n - \\alpha \\) が等比数列になります。

---

## 計算例

![a_n と固定点の関係（左）/ 変換フロー b_n = a_n - α（右）](/assets/images/seq-recur-linear-combined.png)

### 例 1: \\( a_1 = 1 \\)、\\( a_{n+1} = 2a_n + 3 \\) を解け

**固定点を求める:**

<div>
$$
\alpha = 2\alpha + 3 \implies -\alpha = 3 \implies \alpha = -3
$$
</div>

**\\( b_n = a_n - (-3) = a_n + 3 \\) とおく:**

<div>
$$
b_{n+1} = a_{n+1} + 3 = 2a_n + 3 + 3 = 2(a_n + 3) = 2b_n
$$
</div>

等比数列（公比 \\( 2 \\)）、\\( b_1 = 1 + 3 = 4 \\)：

<div>
$$
b_n = 4 \times 2^{n-1} = 2^{n+1}
$$
</div>

<div>
$$
a_n = b_n - 3 = 2^{n+1} - 3
$$
</div>

---

### 例 2: \\( a_1 = 3 \\)、\\( a_{n+1} = 3a_n - 4 \\) を解け

**固定点を求める:**

<div>
$$
\alpha = 3\alpha - 4 \implies -2\alpha = -4 \implies \alpha = 2
$$
</div>

**\\( b_n = a_n - 2 \\) とおく:**

<div>
$$
b_{n+1} = a_{n+1} - 2 = 3a_n - 4 - 2 = 3(a_n - 2) = 3b_n
$$
</div>

等比数列（公比 \\( 3 \\)）、\\( b_1 = 3 - 2 = 1 \\)：

<div>
$$
b_n = 3^{n-1}, \quad a_n = 3^{n-1} + 2
$$
</div>

確認: \\( n=1 \\): \\( 1+2=3=a_1 \\) ✓、\\( n=2 \\): \\( a_2 = 3 \times 3 - 4 = 5 \\)、公式 \\( 3^1+2=5 \\) ✓

---

### 例 3: \\( a_1 = 2 \\)、\\( a_{n+1} = -2a_n + 6 \\) を解け（\\( p < 0 \\) の振動）

**固定点を求める:**

<div>
$$
\alpha = -2\alpha + 6 \implies 3\alpha = 6 \implies \alpha = 2
$$
</div>

**\\( b_n = a_n - 2 \\) とおく:**

<div>
$$
b_{n+1} = -2a_n + 6 - 2 = -2(a_n - 2) = -2b_n
$$
</div>

等比数列（公比 \\( -2 \\)）、\\( b_1 = 2 - 2 = 0 \\)：

<div>
$$
b_n = 0 \times (-2)^{n-1} = 0 \implies a_n = 2 \quad (\text{全 } n \geq 1)
$$
</div>

\\( a_1 = 2 = \\alpha \\) なので最初から固定点にいた定数列。

**\\( p < 0 \\) 一般の場合:** 公比 \\( r = p < 0 \\) の等比数列 \\( b_n \\) は正・負を交互にとる（振動）。今回は \\( b_1 = 0 \\) なので振動しない。例えば \\( a_1 = 3 \\) なら \\( b_1 = 1 \\) で \\( b_n = (-2)^{n-1} \\) と振動します。

---

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/seq-recurrence-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [基本型漸化式](/seq-recur-basic/)　／　[漸化式](/seq-recurrence/)　／　→ [Σ型漸化式](/seq-recur-fn/)
