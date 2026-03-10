---
layout: default
title: 周期と一般角
permalink: /trig-relations-period/
description: "三角関数の周期 2π を使って方程式の解を一般角（+2nπ の形）で表す方法を解説。sin の2つの解の組が生まれる理由も確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [性質と相互関係](/trig-relations/)

---

# 周期と一般角

---

## 問題

次の方程式のすべての解を一般角で表せ。

(1) \\( \sin\theta = \frac{1}{2} \\)　　(2) \\( \cos\theta = -\frac{\sqrt{3}}{2} \\)

---

## なぜ「一般角」が必要か

三角関数は周期的なので \\( \sin\theta = \frac{1}{2} \\) を満たす θ は無限個あります。「\\( \theta = \frac{\pi}{6},\ \frac{5\pi}{6} \\)」と書くだけでは \\( [0, 2\pi) \\) の解しか表せません。周期 \\( 2\pi \\) を足せばすべての解をまとめて表せます。

次の図で確認しましょう。左パネルは \\( [0, 2\pi) \\) の2つの解、右パネルは \\( [0, 4\pi) \\) でさらに2つ現れる様子です。

![左：[0,2π)でのsinθ=1/2の解2つ、右：[0,4π)で周期的に4つに増える様子](/assets/images/trig-period-combined.png)

右図から、解は周期 \\( 2\pi \\) ごとに繰り返し現れることが分かります。

---

## 問題の解き方

**(1) \\( \sin\theta = \frac{1}{2} \\)**

**基本角の特定：** \\( \sin\frac{\pi}{6} = \frac{1}{2} \\) より基本角は \\( \frac{\pi}{6} \\)。

**\\( [0, 2\pi) \\) での解：** sin グラフは \\( \theta = \frac{\pi}{2} \\) を軸に対称なので、

<div>
$$
\theta = \frac{\pi}{6}, \quad \theta = \pi - \frac{\pi}{6} = \frac{5\pi}{6}
$$
</div>

**一般角：** 周期 \\( 2\pi \\) を足して

<div>
$$
\theta = \frac{\pi}{6} + 2n\pi \quad \text{または} \quad \theta = \frac{5\pi}{6} + 2n\pi \quad (n \in \mathbb{Z})
$$
</div>

**(2) \\( \cos\theta = -\frac{\sqrt{3}}{2} \\)**

**基本角の特定：** \\( \cos\frac{\pi}{6} = \frac{\sqrt{3}}{2} \\) より \\( \cos\frac{5\pi}{6} = -\frac{\sqrt{3}}{2} \\)。基本角は \\( \frac{5\pi}{6} \\)。

**\\( [0, 2\pi) \\) での解：** cos グラフは \\( \theta = 0 \\) を軸に対称なので、

<div>
$$
\theta = \frac{5\pi}{6}, \quad \theta = 2\pi - \frac{5\pi}{6} = \frac{7\pi}{6}
$$
</div>

**一般角：** cos の対称性 \\( \cos\theta = \cos(-\theta) \\) から

<div>
$$
\theta = \pm\frac{5\pi}{6} + 2n\pi \quad (n \in \mathbb{Z})
$$
</div>

---

## なぜ sin の解は2つ組になるか

sin グラフは \\( \theta = \frac{\pi}{2} \\) を軸に対称です。水平線 \\( y = k \\) がこの軸と交わる角度 \\( \alpha \\) に対して、もう1つの交点は \\( \pi - \alpha \\) になります（y 軸対称性 \\( \sin(\pi - \theta) = \sin\theta \\) から）。

cos の場合は \\( \theta = 0 \\) を軸に対称なので、2つの解は \\( +\alpha \\) と \\( -\alpha \\)。

---

## まとめ

| 方程式 | \\( [0, 2\pi) \\) の解 | 一般角 |
|---|---|---|
| \\( \sin\theta = k \\)（\\( -1 < k < 1 \\)） | \\( \alpha \\) と \\( \pi - \alpha \\) | \\( \alpha + 2n\pi \\) または \\( (\pi-\alpha) + 2n\pi \\) |
| \\( \cos\theta = k \\)（\\( -1 < k < 1 \\)） | \\( \alpha \\) と \\( -\alpha \\)（\\( = 2\pi - \alpha \\)） | \\( \pm\alpha + 2n\pi \\) |

周期 \\( 2\pi \\) を足す操作が「一般角への拡張」の本質です。

---

## もっと練習したい方へ

一般角を使う方程式の問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-relations-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：対称性・補角・余角の変換公式](/trig-relations-symmetry/)　／　[性質と相互関係](/trig-relations/)
