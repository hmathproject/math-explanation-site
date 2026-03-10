---
layout: default
title: y = sinθ, cosθ, tanθ のグラフの形
permalink: /trig-graph-shape/
description: "sin・cos・tan 3つのグラフの形を比較し、周期・振幅・漸近線の理由を単位円の動きから解説。sin と cos の位相差の意味も確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [グラフ](/trig-graph/)

---

# y = sinθ, cosθ, tanθ のグラフの形

---

## 問題

\\( y = \sin\theta,\ y = \cos\theta,\ y = \tan\theta \\) それぞれの周期・値域・特徴点を求め、グラフの形を説明せよ。

---

## まず何を見るか

3つのグラフはどれも「単位円を回転するときの座標・比がどう変化するか」を展開したものです。まず図で全体の形を確認します。

次の図で、\\( y = \sin\theta \\)（左）・\\( y = \cos\theta \\)（中）・\\( y = \tan\theta \\)（右）の形を比べてください。

![y=sinθ, cosθ, tanθ の3つのグラフを横に並べた比較図](/assets/images/trig-graph-shape-combined.png)

sin と cos は滑らかな波（値域 \\( [-1, 1] \\)）、tan は π ごとに繰り返すが漸近線を持ちます。

---

## なぜ sin と cos は「波」の形になるか

単位円を反時計回りに回るとき：
- **sin**：点の **y 座標**が \\( 0 \to 1 \to 0 \to -1 \to 0 \\) と変化。これを θ に対してプロットすると波になります。
- **cos**：点の **x 座標**が \\( 1 \to 0 \to -1 \to 0 \to 1 \\) と変化。これも波ですが、sin より \\( \frac{\pi}{2} \\) だけ「先にスタート」した形です。

実際、\\( \cos\theta = \sin\!\left(\theta + \frac{\pi}{2}\right) \\) が成り立ちます（cos は sin を左に \\( \frac{\pi}{2} \\) だけ移動したもの）。

---

## 場合別の特徴

**y = sinθ**

| 性質 | 値 |
|---|---|
| 周期 | \\( 2\pi \\) |
| 値域 | \\( -1 \leq y \leq 1 \\) |
| 最大値 | \\( \theta = \frac{\pi}{2} + 2n\pi \\) で \\( y = 1 \\) |
| 最小値 | \\( \theta = \frac{3\pi}{2} + 2n\pi \\) で \\( y = -1 \\) |
| 零点 | \\( \theta = n\pi \\)（n は整数） |
| 奇関数 | \\( \sin(-\theta) = -\sin\theta \\) |

**y = cosθ**

| 性質 | 値 |
|---|---|
| 周期 | \\( 2\pi \\) |
| 値域 | \\( -1 \leq y \leq 1 \\) |
| 最大値 | \\( \theta = 2n\pi \\) で \\( y = 1 \\) |
| 最小値 | \\( \theta = (2n+1)\pi \\) で \\( y = -1 \\) |
| 零点 | \\( \theta = \frac{\pi}{2} + n\pi \\) |
| 偶関数 | \\( \cos(-\theta) = \cos\theta \\) |

**y = tanθ**

| 性質 | 値 |
|---|---|
| 周期 | \\( \pi \\) |
| 値域 | すべての実数 |
| 漸近線 | \\( \theta = \frac{\pi}{2} + n\pi \\) |
| 零点 | \\( \theta = n\pi \\) |
| 奇関数 | \\( \tan(-\theta) = -\tan\theta \\) |

---

## なぜ tan の周期は π か

\\( \tan\theta = \frac{\sin\theta}{\cos\theta} \\) です。\\( \theta \\) が \\( \pi \\) 増えると sin も cos もともに符号が反転するため（\\( \sin(\theta+\pi) = -\sin\theta \\)、\\( \cos(\theta+\pi) = -\cos\theta \\)）、比 \\( \frac{\sin\theta}{\cos\theta} \\) は変わりません。だから tan の周期は sin・cos の半分の \\( \pi \\) です。

---

## まとめ

| | sin | cos | tan |
|---|---|---|---|
| 周期 | \\( 2\pi \\) | \\( 2\pi \\) | \\( \pi \\) |
| 値域 | \\( [-1,1] \\) | \\( [-1,1] \\) | すべての実数 |
| 漸近線 | なし | なし | \\( \theta = \frac{\pi}{2} + n\pi \\) |
| 対称性 | 奇関数 | 偶関数 | 奇関数 |

sin と cos の違いは「どこをスタートにするか」（位相）だけで、形は同じ波。tan は sin を cos で割るため、cos = 0 の場所で値が発散します。

---

## もっと練習したい方へ

グラフの形・周期・代表角の値の確認問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-graph-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：単位円と三角関数の定義](/trig-graph-definition/)　／　[グラフ](/trig-graph/)　／　→ [次の記事：グラフの振幅・周期・平行移動](/trig-graph-transform/)
