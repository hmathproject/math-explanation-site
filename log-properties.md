---
layout: default
title: 対数の性質 — 積・商・累乗と底の変換公式
permalink: /log-properties/
description: "log_a(MN)・log_a(M/N)・log_a(M^k) の3公式と底の変換公式を、指数法則から導きます。なぜ成り立つかの証明の流れと、底の変換が必要になる場面まで確認します。"
---

[サイトトップ](/) / [指数関数・対数関数](/exp-log/) / [対数関数](/logarithm-function/)

---

# 対数の性質 — 積・商・累乗と底の変換公式

---

## 3つの公式

\\( a > 0,\ a \neq 1,\ M > 0,\ N > 0 \\) のとき、次の3つの公式が成り立ちます。

<div>
$$
\log_a MN = \log_a M + \log_a N \quad \text{（積の公式）}
$$
</div>

<div>
$$
\log_a \frac{M}{N} = \log_a M - \log_a N \quad \text{（商の公式）}
$$
</div>

<div>
$$
\log_a M^k = k \log_a M \quad \text{（累乗の公式）}
$$
</div>

---

## なぜ積の公式が成り立つか

\\( p = \log_a M,\ q = \log_a N \\) とおきます。対数の定義から

<div>
$$
M = a^p, \quad N = a^q
$$
</div>

です。したがって

<div>
$$
MN = a^p \cdot a^q = a^{p+q}
$$
</div>

対数の定義に戻ると \\( \log_a MN = p + q = \log_a M + \log_a N \\) が得られます。

**証明の核心:** 対数は指数の言い換えなので、対数の和 = 指数の和 = 積の指数、という流れが成り立ちます。

---

## なぜ商・累乗の公式が成り立つか

同じく \\( p = \log_a M,\ q = \log_a N \\) とおくと

<div>
$$
\frac{M}{N} = \frac{a^p}{a^q} = a^{p-q}
$$
</div>

ゆえに \\( \log_a \frac{M}{N} = p - q = \log_a M - \log_a N \\)。

累乗については \\( M = a^p \\) より

<div>
$$
M^k = (a^p)^k = a^{kp}
$$
</div>

ゆえに \\( \log_a M^k = kp = k\log_a M \\)。

いずれも **指数法則 \\( a^m \cdot a^n = a^{m+n},\ (a^m)^n = a^{mn} \\)** がそのまま対数の公式に対応しています。

---

## 底の変換公式

異なる底の対数を計算するとき、共通の底に変換する公式があります。

\\( a > 0,\ a \neq 1,\ b > 0,\ c > 0,\ c \neq 1 \\) のとき

<div>
$$
\log_a b = \frac{\log_c b}{\log_c a}
$$
</div>

**導出:** \\( \log_a b = t \\) とおくと \\( b = a^t \\)。両辺の底 \\( c \\) の対数を取ると

<div>
$$
\log_c b = t \log_c a
$$
</div>

\\( \log_c a \neq 0 \\) で割ると \\( t = \frac{\log_c b}{\log_c a} \\) が得られます。

---

## なぜ底の変換公式が必要か

\\( \log_4 32 \\) のように底と真数が異なる累乗の基底で表される場合、底を統一すると計算が単純になります。

### 計算例

\\( \log_4 32 \\) を底 2 に変換する:

<div>
$$
\log_4 32 = \frac{\log_2 32}{\log_2 4} = \frac{5}{2}
$$
</div>

\\( \log_2 3 \cdot \log_3 8 \\) を計算する:

<div>
$$
\log_2 3 \cdot \log_3 8 = \log_2 3 \cdot \frac{\log_2 8}{\log_2 3} = \log_2 8 = 3
$$
</div>

この形（\\( \log_a b \cdot \log_b c = \log_a c \\)）は底の変換公式から導かれる連鎖公式です。

---

## 公式を使うときの条件

3公式も底の変換公式も、すべて次の条件が必要です:

| 記号 | 条件 | 理由 |
|---|---|---|
| 底 \\( a \\) | \\( a > 0,\ a \neq 1 \\) | 対数関数の定義域 |
| 真数 \\( M, N \\) | \\( M > 0,\ N > 0 \\) | 真数は正でなければ対数が定義されない |
| 指数 \\( k \\) | 実数ならよい | 制約なし |

---

## まとめ

| 公式 | 内容 |
|---|---|
| 積 | \\( \log_a MN = \log_a M + \log_a N \\) |
| 商 | \\( \log_a \frac{M}{N} = \log_a M - \log_a N \\) |
| 累乗 | \\( \log_a M^k = k\log_a M \\) |
| 底の変換 | \\( \log_a b = \frac{\log_c b}{\log_c a} \\) |

いずれも **指数法則の対数版**です。証明は「\\( \log_a M = p \\) とおくと \\( M = a^p \\)」という定義に戻ることで成り立ちます。

---

## もっと練習したい方へ

この単元の解説PDFを無料で配布しています。対数方程式・不等式の例題を中心に、真数条件の確認・底をそろえる手順・不等号の向きの判断まで、模範解答と意味説明を2段組で並べた構成で確認できます。

<a class="pdf-btn" href="/assets/pdf/logarithm-function-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：対数関数のグラフ — 指数関数との対称性と定義域](/log-function-graph/)　／　[対数関数](/logarithm-function/)　／　→ [次の記事：対数方程式・不等式 — 真数条件と不等号の向き](/log-equation/)
