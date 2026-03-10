---
layout: default
title: 合成を使う三角方程式
permalink: /trig-equation-synthesis/
description: "sinθ + √3 cosθ = 1 を合成して R sin(θ+φ) = c の形にしてから解く手順を解説。合成後の θ+φ の範囲確認が解の過不足を防ぐ理由を確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [三角方程式](/trig-equation/)

---

# 合成を使う三角方程式

---

## 問題

\\( 0 \leq \theta < 2\pi \\) のとき、\\( \sin\theta + \sqrt{3}\cos\theta = 1 \\) を解け。

---

## なぜ合成するか

左辺は sin と cos の1次結合なので直接解けません。合成で \\( R\sin(\theta+\varphi) \\) にまとめると、\\( R\sin(\theta+\varphi) = 1 \\) という基本方程式に帰着します。

---

## 問題の解き方

**step 1：左辺を合成する**

<div>
$$
R = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1+3} = 2
$$
</div>

\\( \cos\varphi = \dfrac{1}{2},\ \sin\varphi = \dfrac{\sqrt{3}}{2} \\) より \\( \varphi = \dfrac{\pi}{3} \\)。

<div>
$$
\sin\theta + \sqrt{3}\cos\theta = 2\sin\!\left(\theta + \frac{\pi}{3}\right)
$$
</div>

**step 2：基本方程式を解く**

<div>
$$
2\sin\!\left(\theta + \frac{\pi}{3}\right) = 1 \implies \sin\!\left(\theta + \frac{\pi}{3}\right) = \frac{1}{2}
$$
</div>

**step 3：\\( \theta + \dfrac{\pi}{3} \\) の範囲を確認する**

\\( 0 \leq \theta < 2\pi \\) より \\( \dfrac{\pi}{3} \leq \theta + \dfrac{\pi}{3} < \dfrac{7\pi}{3} \\)。

この範囲で \\( \sin = \dfrac{1}{2} \\) を満たす角を探します。

- \\( \theta + \dfrac{\pi}{3} = \dfrac{\pi}{6} \\)：範囲外（\\( \dfrac{\pi}{6} < \dfrac{\pi}{3} \\)）→ **不採用**
- \\( \theta + \dfrac{\pi}{3} = \dfrac{5\pi}{6} \\)：範囲内 → **採用** → \\( \theta = \dfrac{5\pi}{6} - \dfrac{\pi}{3} = \dfrac{\pi}{2} \\)
- \\( \theta + \dfrac{\pi}{3} = \dfrac{\pi}{6} + 2\pi = \dfrac{13\pi}{6} \\)：\\( \dfrac{13\pi}{6} < \dfrac{7\pi}{3} = \dfrac{14\pi}{6} \\) → **採用** → \\( \theta = \dfrac{13\pi}{6} - \dfrac{\pi}{3} = \dfrac{11\pi}{6} \\)

**答え：** \\( \theta = \dfrac{\pi}{2},\ \dfrac{11\pi}{6} \\)

---

## なぜ「範囲確認」が重要か

\\( \theta + \dfrac{\pi}{3} = \dfrac{\pi}{6} \\) が範囲外なので、対応する \\( \theta = \dfrac{\pi}{6} - \dfrac{\pi}{3} = -\dfrac{\pi}{6} \\) は \\( [0, 2\pi) \\) の外です。このような解を誤って採用しないために、\\( \theta + \varphi \\) の範囲を先に書いてから解を絞り込む手順が必要です。

---

## 確認

\\( \theta = \dfrac{\pi}{2} \\)：\\( \sin\dfrac{\pi}{2} + \sqrt{3}\cos\dfrac{\pi}{2} = 1 + 0 = 1 \\) ✓

\\( \theta = \dfrac{11\pi}{6} \\)：\\( \sin\dfrac{11\pi}{6} + \sqrt{3}\cos\dfrac{11\pi}{6} = -\dfrac{1}{2} + \sqrt{3}\cdot\dfrac{\sqrt{3}}{2} = -\dfrac{1}{2} + \dfrac{3}{2} = 1 \\) ✓

---

## まとめ

合成を使う三角方程式の解法手順：

1. 左辺を \\( R\sin(\theta + \varphi) \\) に合成（\\( R,\ \varphi \\) を求める）
2. \\( \sin(\theta+\varphi) = c/R \\) の形にする
3. \\( \theta + \varphi \\) の範囲を書く
4. その範囲内で \\( \sin = c/R \\) を満たす値を全部列挙
5. θ に戻して答えを確認

「範囲を先に書いてから解を絞る」ことが解の過不足を防ぎます。

---

## もっと練習したい方へ

合成・置換を使う三角方程式の問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-equation-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：基本方程式 sinθ = k, cosθ = k](/trig-equation-basic/)　／　[三角方程式](/trig-equation/)　／　→ [次の記事：置換を使う三角方程式](/trig-equation-substitution/)
