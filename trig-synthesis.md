---
layout: default
title: 三角関数の合成
permalink: /trig-synthesis/
description: "a sinθ + b cosθ を R sin(θ + φ) の形に合成する方法を解説。R の求め方・φ の決め方・合成後の最大値・最小値の読み方を確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [加法定理と変換公式](/trig-addition/)

---

# 三角関数の合成

---

## 問題

\\( \sqrt{3}\sin\theta + \cos\theta \\) を \\( R\sin(\theta + \varphi) \\) の形に変換し、\\( 0 \leq \theta < 2\pi \\) でのこの式の最大値・最小値と、それを取る \\( \theta \\) の値を求めよ。

---

## なぜ合成するか

\\( \sqrt{3}\sin\theta + \cos\theta \\) の最大値を直接求めるのは困難ですが、\\( R\sin(\theta + \varphi) \\) の形にまとめると振幅 \\( R \\) が最大値になるため、即座に最大値・最小値が読めます。

次の図で、R と φ の決め方（左）と合成後の波の形（右）を確認しましょう。

![左：a, b, \\( R=\\sqrt{a^2+b^2} \\) の直角三角形でφを決める図、右：合成後 \\( y=2\\sin(\\theta+\\pi/6) \\) のグラフ](/assets/images/trig-synthesis-combined.png)

左図から、係数 a, b を直角三角形の 2辺に見立てると R と φ が幾何的に決まることが分かります。

---

## 問題の解き方

**step 1：R を求める**

<div>
$$
R = \sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{3 + 1} = 2
$$
</div>

**step 2：合成する**

加法定理の展開 \\( R\sin(\theta+\varphi) = R\cos\varphi\cdot\sin\theta + R\sin\varphi\cdot\cos\theta \\) と係数を比較します。

<div>
$$
R\cos\varphi = \sqrt{3}, \quad R\sin\varphi = 1
$$
</div>

\\( R = 2 \\) を代入すると \\( \cos\varphi = \dfrac{\sqrt{3}}{2} \\), \\( \sin\varphi = \dfrac{1}{2} \\) より \\( \varphi = \dfrac{\pi}{6} \\)。

よって、

<div>
$$
\sqrt{3}\sin\theta + \cos\theta = 2\sin\!\left(\theta + \frac{\pi}{6}\right)
$$
</div>

**step 3：最大値・最小値を求める**

\\( 0 \leq \theta < 2\pi \\) のとき \\( \dfrac{\pi}{6} \leq \theta + \dfrac{\pi}{6} < \dfrac{13\pi}{6} \\)。

- **最大値**：\\( \sin\!\left(\theta + \dfrac{\pi}{6}\right) = 1 \\) のとき \\( \theta + \dfrac{\pi}{6} = \dfrac{\pi}{2} \\) → \\( \theta = \dfrac{\pi}{3} \\)

  最大値 \\( = 2 \times 1 = 2 \\)

- **最小値**：\\( \sin\!\left(\theta + \dfrac{\pi}{6}\right) = -1 \\) のとき \\( \theta + \dfrac{\pi}{6} = \dfrac{3\pi}{2} \\) → \\( \theta = \dfrac{4\pi}{3} \\)

  最小値 \\( = 2 \times (-1) = -2 \\)

---

## なぜ φ の条件を両式から確認するか

\\( \tan\varphi = \dfrac{R\sin\varphi}{R\cos\varphi} = \dfrac{1}{\sqrt{3}} \\) から \\( \varphi = \dfrac{\pi}{6} \\) または \\( \varphi = \pi + \dfrac{\pi}{6} = \dfrac{7\pi}{6} \\) の2候補があります。\\( R\cos\varphi = \sqrt{3} > 0 \\) かつ \\( R\sin\varphi = 1 > 0 \\) から第1象限に確定するので \\( \varphi = \dfrac{\pi}{6} \\)。

**φ を決める手順：**

1. \\( \tan\varphi = b/a \\) を計算
2. \\( \cos\varphi = a/R \\) と \\( \sin\varphi = b/R \\) の符号から象限を確定

---

## まとめ

<div>
$$
a\sin\theta + b\cos\theta = R\sin(\theta + \varphi)
$$
</div>

ただし \\( R = \sqrt{a^2 + b^2} \\)、\\( \varphi \\) は \\( \cos\varphi = \dfrac{a}{R},\ \sin\varphi = \dfrac{b}{R} \\) を満たす角。

合成すると振幅が \\( R \\) になるため、最大値 = \\( R \\)、最小値 = \\( -R \\) が即座に読めます。方程式・不等式への応用では次の単元で使います。

---

## もっと練習したい方へ

合成の計算問題（最大値・最小値・方程式への応用）を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-addition-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：倍角公式・半角公式](/trig-double-angle/)　／　[加法定理と変換公式](/trig-addition/)
