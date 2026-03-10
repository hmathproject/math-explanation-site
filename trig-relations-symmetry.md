---
layout: default
title: 対称性・補角・余角の変換公式
permalink: /trig-relations-symmetry/
description: "単位円の対称移動から sin(π−θ), cos(π+θ), sin(−θ) などの変換公式を導く方法を解説。公式を暗記せずに単位円から読む習慣を身につける。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [性質と相互関係](/trig-relations/)

---

# 対称性・補角・余角の変換公式

---

## 問題

次の式を \\( \theta \\) の三角関数で表せ。

(1) \\( \sin(\pi - \theta) \\)、\\( \cos(\pi - \theta) \\)
(2) \\( \sin(\pi + \theta) \\)、\\( \cos(\pi + \theta) \\)
(3) \\( \sin(-\theta) \\)、\\( \cos(-\theta) \\)

---

## なぜ「対称移動で読む」か

\\( \pi - \theta \\), \\( \pi + \theta \\), \\( -\theta \\) などの変換は、単位円上での「角度の操作」です。それぞれが単位円上のどの対称移動に対応するかを掴めば、公式を覚えなくても座標の変化から答えが出ます。

次の図で、3種類の対称移動を確認しましょう。赤い点が P(θ)、緑の点が変換後の点です。

![単位円上の3種類の対称移動：π−θ（y軸対称）、π+θ（原点対称）、−θ（x軸対称）](/assets/images/trig-symmetry-combined.png)

図から、x 座標（= cos）と y 座標（= sin）のどちらが符号反転するかが直接読み取れます。

---

## 問題の解き方

**単位円上で角度 θ の点 P の座標を \\( (\cos\theta, \sin\theta) \\) とします。**

**(1) \\( \pi - \theta \\)：y 軸対称**

角度 \\( \pi - \theta \\) の点は、角度 \\( \theta \\) の点を y 軸で折り返した点です。
→ x 座標（= cos）が逆符号、y 座標（= sin）はそのまま。

<div>
$$
\sin(\pi - \theta) = \sin\theta, \quad \cos(\pi - \theta) = -\cos\theta
$$
</div>

**(2) \\( \pi + \theta \\)：原点対称**

角度 \\( \pi + \theta \\) の点は、角度 \\( \theta \\) の点の原点対称（x, y ともに逆符号）。

<div>
$$
\sin(\pi + \theta) = -\sin\theta, \quad \cos(\pi + \theta) = -\cos\theta
$$
</div>

**(3) \\( -\theta \\)：x 軸対称**

角度 \\( -\theta \\) の点は、角度 \\( \theta \\) の点を x 軸で折り返した点。
→ x 座標はそのまま、y 座標（= sin）が逆符号。

<div>
$$
\sin(-\theta) = -\sin\theta, \quad \cos(-\theta) = \cos\theta
$$
</div>

---

## 確認

\\( \sin\!\left(\pi - \frac{\pi}{3}\right) = \sin\frac{2\pi}{3} = \frac{\sqrt{3}}{2} = \sin\frac{\pi}{3} \\) ✓

\\( \cos\!\left(\pi + \frac{\pi}{4}\right) = \cos\frac{5\pi}{4} = -\frac{\sqrt{2}}{2} = -\cos\frac{\pi}{4} \\) ✓

---

## まとめ

| 変換 | 対称軸 | sin | cos |
|---|---|---|---|
| \\( \pi - \theta \\) | y 軸 | \\( +\sin\theta \\) | \\( -\cos\theta \\) |
| \\( \pi + \theta \\) | 原点 | \\( -\sin\theta \\) | \\( -\cos\theta \\) |
| \\( -\theta \\) | x 軸 | \\( -\sin\theta \\) | \\( +\cos\theta \\) |

「どの軸で折り返すか」を意識すれば、x 座標（cos）と y 座標（sin）のどちらが符号反転するかは自然に決まります。

---

## もっと練習したい方へ

対称性の公式を使う計算問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-relations-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：3つの相互関係公式](/trig-relations-basics/)　／　[性質と相互関係](/trig-relations/)　／　→ [次の記事：周期と一般角](/trig-relations-period/)
