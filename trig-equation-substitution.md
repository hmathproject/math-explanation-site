---
layout: default
title: 置換を使う三角方程式
permalink: /trig-equation-substitution/
description: "2cos²θ − cosθ − 1 = 0 を t = cosθ と置換して二次方程式で解く手順を解説。置換後の定義域チェックと複数の θ への戻し方を確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [三角方程式](/trig-equation/)

---

# 置換を使う三角方程式

---

## 問題

\\( 0 \leq \theta < 2\pi \\) のとき、\\( 2\cos^2\theta - \cos\theta - 1 = 0 \\) を解け。

---

## なぜ置換するか

左辺は \\( \cos\theta \\) の二次多項式です。\\( t = \cos\theta \\) と置くと \\( 2t^2 - t - 1 = 0 \\) という二次方程式になり、因数分解で解けます。

---

## 問題の解き方

**step 1：\\( t = \cos\theta \\) と置く（定義域を確認）**

\\( -1 \leq \cos\theta \leq 1 \\) なので \\( t \\) の範囲は \\( -1 \leq t \leq 1 \\)。

**step 2：二次方程式を解く**

<div>
$$
2t^2 - t - 1 = (t-1)(2t+1) = 0
$$
$$
t = 1 \quad \text{または} \quad t = -\frac{1}{2}
$$
</div>

どちらも \\( -1 \leq t \leq 1 \\) を満たします（採用）。

**step 3：\\( \cos\theta \\) の値から \\( \theta \\) を求める**

\\( \cos\theta = 1 \\)：\\( 0 \leq \theta < 2\pi \\) で \\( \theta = 0 \\)

\\( \cos\theta = -\dfrac{1}{2} \\)：\\( 0 \leq \theta < 2\pi \\) で \\( \theta = \dfrac{2\pi}{3},\ \dfrac{4\pi}{3} \\)

**答え：** \\( \theta = 0,\ \dfrac{2\pi}{3},\ \dfrac{4\pi}{3} \\)

---

## なぜ定義域のチェックが必要か

二次方程式の解が \\( t = 2 \\) などになった場合、\\( \cos\theta = 2 \\) を満たす実数 \\( \theta \\) は存在しないため棄却しなければなりません。置換後に \\( -1 \leq t \leq 1 \\) の確認を忘れると余分な解（または解なし）を見落とす恐れがあります。

---

## 確認

\\( \theta = 0 \\)：\\( 2\cdot 1 - 1 - 1 = 0 \\) ✓

\\( \theta = \dfrac{2\pi}{3} \\)：\\( \cos\dfrac{2\pi}{3} = -\dfrac{1}{2} \\) なので \\( 2\cdot\dfrac{1}{4} - \left(-\dfrac{1}{2}\right) - 1 = \dfrac{1}{2} + \dfrac{1}{2} - 1 = 0 \\) ✓

\\( \theta = \dfrac{4\pi}{3} \\)：同じく \\( \cos\dfrac{4\pi}{3} = -\dfrac{1}{2} \\) なので同様 ✓

---

## まとめ

置換を使う三角方程式の解法手順：

1. \\( t = \sin\theta \\)（または \\( t = \cos\theta \\)）と置く
2. \\( t \\) の定義域（\\( -1 \leq t \leq 1 \\)）を書く
3. t についての方程式（多くは二次）を解く
4. 解が定義域を満たすか確認（満たさないものは棄却）
5. 採用した t の値から θ を求める

---

## もっと練習したい方へ

置換を使う三角方程式・不等式の問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-equation-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：合成を使う三角方程式](/trig-equation-synthesis/)　／　[三角方程式](/trig-equation/)
