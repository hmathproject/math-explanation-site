---
layout: default
title: 部分分数分解と階差Σ — テレスコーピングで計算する
permalink: /seq-partial-fraction/
description: "1/(k(k+1)) を 1/k - 1/(k+1) に分解すると Σ がテレスコーピングで簡単になる理由を解説。中間項の消え方を具体的に追う（高校数B）。"
---

← [和の計算技法](/seq-sum-technique/)　／　[数列の和](/seq-sum/)

---

# 部分分数分解と階差Σ — テレスコーピングで計算する

---

## 動機: 分母が積の形のとき Σ 公式は使えない

\\( \\displaystyle\\sum_{k=1}^{n} \\frac{1}{k(k+1)} \\) は、\\( \\Sigma k \\) や \\( \\Sigma k^2 \\) の公式では直接計算できません。分母が積の形のとき、**部分分数分解**によってテレスコーピングが使える形に変形します。

---

## 部分分数分解の原理

\\( \\frac{1}{k(k+1)} \\) を \\( \\frac{A}{k} + \\frac{B}{k+1} \\) の形にします。

分子を \\( 1 \\) にするためには \\( (k+1) - k = 1 \\) を利用します：

<div>
$$
\frac{1}{k(k+1)} = \frac{(k+1) - k}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}
$$
</div>

確認: \\( \\frac{1}{k} - \\frac{1}{k+1} = \\frac{(k+1) - k}{k(k+1)} = \\frac{1}{k(k+1)} \\) ✓

この分解により、\\( \\Sigma \\) をとったときに隣の項と消え合うテレスコーピングが機能します。

---

## 計算例

![部分分数の消去表（左）/ テレスコーピング残存項（右）](/assets/images/seq-partial-fraction-combined.png)

### 例 1: \\( \\displaystyle\\sum_{k=1}^{n} \\frac{1}{k(k+1)} \\) を求めよ

分解してテレスコーピング：

<div>
$$
\sum_{k=1}^{n}\frac{1}{k(k+1)} = \sum_{k=1}^{n}\left(\frac{1}{k} - \frac{1}{k+1}\right)
$$
</div>

<div>
$$
= \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n+1}\right)
$$
</div>

<div>
$$
= 1 - \frac{1}{n+1} = \frac{n}{n+1}
$$
</div>

---

### 例 2: \\( \\displaystyle\\sum_{k=1}^{n} \\frac{1}{k(k+2)} \\) を求めよ

分母の差は \\( (k+2) - k = 2 \\) なので係数 \\( 1/2 \\) が出ます：

<div>
$$
\frac{1}{k(k+2)} = \frac{1}{2}\left(\frac{1}{k} - \frac{1}{k+2}\right)
$$
</div>

確認: \\( \\frac{(k+2) - k}{2k(k+2)} = \\frac{1}{k(k+2)} \\) ✓

1 つおきの消去（奇数列と偶数列が別々に消える）：

<div>
$$
\sum_{k=1}^{n}\frac{1}{k(k+2)} = \frac{1}{2}\sum_{k=1}^{n}\left(\frac{1}{k} - \frac{1}{k+2}\right)
$$
</div>

奇数列: \\( \\frac{1}{1} - \\frac{1}{n+1} \\)（または \\( -\\frac{1}{n+2} \\)）

偶数列: \\( \\frac{1}{2} - \\frac{1}{n+2} \\)（または \\( -\\frac{1}{n+1} \\)）

どちらの場合も残るのは \\( \\frac{1}{1} + \\frac{1}{2} - \\frac{1}{n+1} - \\frac{1}{n+2} \\) の 4 項：

<div>
$$
= \frac{1}{2}\left(\frac{3}{2} - \frac{1}{n+1} - \frac{1}{n+2}\right) = \frac{3}{4} - \frac{1}{2(n+1)} - \frac{1}{2(n+2)}
$$
</div>

---

### 例 3: \\( \\displaystyle\\sum_{k=1}^{n} \\frac{1}{(2k-1)(2k+1)} \\) を求めよ

分母の差は \\( (2k+1) - (2k-1) = 2 \\) なので：

<div>
$$
\frac{1}{(2k-1)(2k+1)} = \frac{1}{2}\left(\frac{1}{2k-1} - \frac{1}{2k+1}\right)
$$
</div>

テレスコーピング（連続した奇数分数が消える）：

<div>
$$
\sum_{k=1}^{n}\frac{1}{(2k-1)(2k+1)} = \frac{1}{2}\left(\frac{1}{1} - \frac{1}{2n+1}\right) = \frac{1}{2} \cdot \frac{2n}{2n+1} = \frac{n}{2n+1}
$$
</div>

---

## 理解の確認

部分分数分解ができる根拠は「分子を \\( 1 \\) にするために分母の差を使う」ことです。\\( \\frac{1}{k} - \\frac{1}{k+1} \\) の分子は \\( (k+1) - k = 1 \\) になるので、元の \\( \\frac{1}{k(k+1)} \\) に等しくなります。係数（\\( 1 \\) または \\( 1/2 \\)）は分母の差（\\( 1 \\) または \\( 2 \\)）の逆数です。

---

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/seq-sum-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [和の計算技法](/seq-sum-technique/)　／　[数列の和](/seq-sum/)
