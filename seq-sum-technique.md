---
layout: default
title: 和の計算技法 — ずらし引きとテレスコーピング
permalink: /seq-sum-technique/
description: "k·r^{k-1} 型の和をずらし引き法で計算する方法と、b_k-b_{k-1}=f(k) を使ったテレスコーピングで Σ を計算する方法を解説（高校数B）。"
---

← [Σ記号の見方](/seq-sigma/)　／　[数列の和](/seq-sum/)　／　→ [部分分数分解](/seq-partial-fraction/)

---

# 和の計算技法 — ずらし引きとテレスコーピング

---

## 動機: 通常の Σ 公式では計算できない和

\\( \\sum_{k=1}^{n} k \cdot 2^{k-1} \\) のような「等差 \\( \\times \\) 等比」型の和は、\\( \\Sigma k \\) や \\( \\Sigma 2^k \\) の公式を直接組み合わせても計算できません。ここでは 2 つの強力な手法を学びます。

---

## 手法 1: ずらし引き法（シフト引き法）

**なぜ機能するか:** \\( S = \\sum_{k=1}^{n} k r^{k-1} \\) に \\( r \\) をかけると各項が 1 つずつずれます。\\( rS \\) を作って \\( S - rS \\) を計算すると等差の増分部分だけ残り、等比数列の和の問題に帰着します。

### 例 1: \\( S = \\displaystyle\\sum_{k=1}^{n} k \\cdot 2^{k-1} \\) を求めよ

\\( S = 1 \cdot 2^0 + 2 \cdot 2^1 + 3 \cdot 2^2 + \cdots + n \cdot 2^{n-1} \\) と書き、

\\( 2S = 1 \cdot 2^1 + 2 \cdot 2^2 + \cdots + (n-1) \cdot 2^{n-1} + n \cdot 2^n \\) を作る。

\\( S - 2S = -S \\) を計算（各列の差を取る）：

<div>
$$
-S = 2^0 + 2^1 + 2^2 + \cdots + 2^{n-1} - n \cdot 2^n
$$
</div>

等比数列の和（初項 \\( 1 \\)、公比 \\( 2 \\)、項数 \\( n \\)、\\( r = 2 \neq 1 \\)）：

<div>
$$
-S = \frac{2^n - 1}{2 - 1} - n \cdot 2^n = 2^n - 1 - n \cdot 2^n
$$
</div>

<div>
$$
S = n \cdot 2^n - 2^n + 1 = (n-1) \cdot 2^n + 1
$$
</div>

---

### 例 2: \\( S = \\displaystyle\\sum_{k=1}^{n}(2k+1) \\cdot 3^{k-1} \\) を求めよ

\\( 3S \\) を作って \\( S - 3S = -2S \\) を計算：

<div>
$$
S = 3 \cdot 3^0 + 5 \cdot 3^1 + 7 \cdot 3^2 + \cdots + (2n+1) \cdot 3^{n-1}
$$
</div>

<div>
$$
3S = 3 \cdot 3^1 + 5 \cdot 3^2 + \cdots + (2n-1) \cdot 3^{n-1} + (2n+1) \cdot 3^n
$$
</div>

<div>
$$
-2S = 3 + 2 \cdot 3^1 + 2 \cdot 3^2 + \cdots + 2 \cdot 3^{n-1} - (2n+1) \cdot 3^n
$$
</div>

<div>
$$
= 3 + 2 \cdot \frac{3(3^{n-1}-1)}{2} - (2n+1) \cdot 3^n = 3 + 3^n - 3 - (2n+1) \cdot 3^n = -(2n) \cdot 3^n
$$
</div>

<div>
$$
S = n \cdot 3^n
$$
</div>

---

## 手法 2: テレスコーピング（伸縮消去）

**なぜ機能するか:** \\( b_k - b_{k-1} = f(k) \\) を満たす \\( b_k \\) が見つかれば、

<div>
$$
\sum_{k=1}^{n} f(k) = (b_1 - b_0) + (b_2 - b_1) + \cdots + (b_n - b_{n-1}) = b_n - b_0
$$
</div>

中間項 \\( b_1, b_2, \ldots, b_{n-1} \\) がすべて消えて両端だけ残ります。

### 例 3: テレスコーピングで \\( \\displaystyle\\sum_{k=1}^{n} k(k+1) \\) を求めよ

\\( b_k = \\frac{k(k+1)(k+2)}{3} \\) とおくと：

<div>
$$
b_k - b_{k-1} = \frac{k(k+1)(k+2)}{3} - \frac{(k-1)k(k+1)}{3}
$$
</div>

<div>
$$
= \frac{k(k+1)\{(k+2)-(k-1)\}}{3} = \frac{k(k+1) \cdot 3}{3} = k(k+1) \quad \checkmark
$$
</div>

よって：

<div>
$$
\sum_{k=1}^{n} k(k+1) = b_n - b_0 = \frac{n(n+1)(n+2)}{3} - 0 = \frac{n(n+1)(n+2)}{3}
$$
</div>

---

## 図解: ずらし引きとテレスコーピング

![ずらし引き（左）/ テレスコーピングの相殺（右）](/assets/images/seq-sum-technique-combined.png)

---

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/seq-sum-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [Σ記号の見方](/seq-sigma/)　／　[数列の和](/seq-sum/)　／　→ [部分分数分解](/seq-partial-fraction/)
