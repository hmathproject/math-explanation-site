---
layout: default
title: 基本方程式 sinθ = k, cosθ = k
permalink: /trig-equation-basic/
description: "sin θ = k, cos θ = k の形の三角方程式をグラフで解く方法を解説。sin の2解が α と π−α になる理由、cos の2解が ±α になる理由を図で確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [三角方程式](/trig-equation/)

---

# 基本方程式 sinθ = k, cosθ = k

---

## 問題

\\( 0 \leq \theta < 2\pi \\) のとき、次の方程式を解け。

(1) \\( \sin\theta = \dfrac{\sqrt{3}}{2} \\)　　(2) \\( \cos\theta = -\dfrac{1}{2} \\)

---

## まず何を見るか

三角方程式を解くとは「sin（または cos）グラフに水平線を引いて交点の θ を読む」操作です。図で確認します。

次の図で、左は \\( \sin\theta = \frac{\sqrt{3}}{2} \\) の解、右は \\( \cos\theta = -\frac{1}{2} \\) の解を示しています。

![sin θ = \\( \\sqrt{3}/2 \\) と cos θ = -1/2 の解をグラフ上で示した2パネル図](/assets/images/trig-equation-basic-combined.png)

グラフと水平線の交点が解です。どちらも \\( [0, 2\pi) \\) に2つの解があります。

---

## なぜ解が2つになるか

**sin の場合（\\( \sin\theta = k \\)）：**

sin グラフは \\( \theta = \dfrac{\pi}{2} \\) を対称軸とする山型です。水平線 \\( y = k \\)（\\( -1 < k < 1 \\)）はこの山に左右2か所で交わります。

- 1つ目の解を \\( \theta = \alpha \\) とすると
- 2つ目は対称性から \\( \theta = \pi - \alpha \\)

**cos の場合（\\( \cos\theta = k \\)）：**

cos グラフは \\( \theta = 0 \\)（および \\( \theta = 2\pi \\)）を対称軸とします。

- 1つ目の解を \\( \theta = \alpha \\) とすると
- 2つ目は \\( \theta = -\alpha = 2\pi - \alpha \\)

---

## 場合別の計算

**(1) \\( \sin\theta = \dfrac{\sqrt{3}}{2} \\)**

基準角：\\( \sin\dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2} \\) より \\( \alpha = \dfrac{\pi}{3} \\)

<div>
$$
\theta = \frac{\pi}{3}, \quad \theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}
$$
</div>

**(2) \\( \cos\theta = -\dfrac{1}{2} \\)**

基準角：\\( \cos\dfrac{\pi}{3} = \dfrac{1}{2} \\) より \\( \cos\left(\pi - \dfrac{\pi}{3}\right) = \cos\dfrac{2\pi}{3} = -\dfrac{1}{2} \\)。\\( \alpha = \dfrac{2\pi}{3} \\)

<div>
$$
\theta = \frac{2\pi}{3}, \quad \theta = 2\pi - \frac{2\pi}{3} = \frac{4\pi}{3}
$$
</div>

---

## 確認

(1) \\( \sin\dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2} \\) ✓、\\( \sin\dfrac{2\pi}{3} = \sin\!\left(\pi - \dfrac{\pi}{3}\right) = \sin\dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2} \\) ✓

(2) \\( \cos\dfrac{2\pi}{3} = -\dfrac{1}{2} \\) ✓、\\( \cos\dfrac{4\pi}{3} = \cos\!\left(2\pi - \dfrac{2\pi}{3}\right) = \cos\dfrac{2\pi}{3} = -\dfrac{1}{2} \\) ✓

---

## まとめ

| 方程式 | \\( [0, 2\pi) \\) の解 |
|---|---|
| \\( \sin\theta = k \\)（\\( -1 < k < 1 \\)） | \\( \theta = \alpha \\) と \\( \pi - \alpha \\) |
| \\( \cos\theta = k \\)（\\( -1 < k < 1 \\)） | \\( \theta = \alpha \\) と \\( 2\pi - \alpha \\) |

グラフの対称軸（sin は \\( \frac{\pi}{2} \\)、cos は \\( 0 \\) と \\( 2\pi \\)）から、2つの解の組が決まります。

---

## もっと練習したい方へ

基本方程式から合成・置換への応用問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-equation-pack.pdf">PDFをダウンロードする（無料）</a>

---

[三角方程式](/trig-equation/)　／　→ [次の記事：合成を使う三角方程式](/trig-equation-synthesis/)
