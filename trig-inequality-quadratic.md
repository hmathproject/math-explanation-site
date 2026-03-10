---
layout: default
title: 置換して二次不等式に帰着
permalink: /trig-inequality-quadratic/
description: "2sin²θ − sinθ − 1 ≥ 0 を t = sinθ と置換して二次不等式で解き、t の結果を sin グラフから θ の範囲に戻す方法を解説。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [三角不等式](/trig-inequality/)

---

# 置換して二次不等式に帰着

---

## 問題

\\( 0 \leq \theta \leq 2\pi \\) のとき、\\( 2\sin^2\theta - \sin\theta - 1 \geq 0 \\) を解け。

---

## なぜ置換するか

左辺は \\( \sin\theta \\) の二次多項式です。\\( t = \sin\theta \\) と置くと \\( 2t^2 - t - 1 \geq 0 \\) という二次不等式になり、因数分解で解けます。ただし \\( t \\) の解を \\( \theta \\) の範囲に正確に戻す必要があります。

次の図で、t の数直線での解（左）と sin グラフ上での θ の解区間（右）を確認しましょう。

![左：t軸でt=-1〜-1/2と t=1 の解、右：sinグラフでθ=π/2とθ∈[7π/6,11π/6]の塗りつぶし](/assets/images/trig-ineq-quadratic.png)

右図の赤い塗りつぶし部分と緑の点が解です。

---

## 問題の解き方

**step 1：\\( t = \sin\theta \\) と置く（定義域を確認）**

\\( 0 \leq \theta \leq 2\pi \\) のとき \\( -1 \leq \sin\theta \leq 1 \\)、よって \\( -1 \leq t \leq 1 \\)。

**step 2：t の二次不等式を解く**

<div>
$$
2t^2 - t - 1 = (t-1)(2t+1) \geq 0
$$
</div>

<div>
$$
t \leq -\frac{1}{2} \quad \text{または} \quad t \geq 1
$$
</div>

**step 3：定義域 \\( -1 \leq t \leq 1 \\) との共通部分をとる**

<div>
$$
-1 \leq t \leq -\frac{1}{2} \quad \text{または} \quad t = 1
$$
</div>

**step 4：sin グラフから \\( \theta \\) の範囲を読む**

\\( \sin\theta = 1 \\)：\\( \theta = \dfrac{\pi}{2} \\)

\\( -1 \leq \sin\theta \leq -\dfrac{1}{2} \\)（\\( [0, 2\pi] \\) の範囲）：

sin グラフが \\( y = -\dfrac{1}{2} \\) 以下になる区間。

境界点：\\( \sin\theta = -\dfrac{1}{2} \\) → \\( \theta = \dfrac{7\pi}{6},\ \dfrac{11\pi}{6} \\)

sin グラフが最小値 \\( -1 \\) を取る \\( \theta = \dfrac{3\pi}{2} \\) を含む区間：

<div>
$$
\frac{7\pi}{6} \leq \theta \leq \frac{11\pi}{6}
$$
</div>

**答え：** \\( \theta = \dfrac{\pi}{2} \\) または \\( \dfrac{7\pi}{6} \leq \theta \leq \dfrac{11\pi}{6} \\)

---

## なぜ「定義域との共通部分」が必要か

二次不等式の解 \\( t \geq 1 \\) は \\( -1 \leq t \leq 1 \\) との共通部分で \\( t = 1 \\) のみになります（\\( t > 1 \\) は \\( \sin\theta \\) が取れない値）。定義域確認を怠ると \\( t > 1 \\) の部分を不等式に含めてしまい、対応する \\( \theta \\) が存在しない誤った解になります。

---

## 確認

\\( \theta = \dfrac{3\pi}{2} \\)（区間内）：\\( \sin\dfrac{3\pi}{2} = -1 \\) → \\( 2(1)+1-1=2 \geq 0 \\) ✓

\\( \theta = \pi \\)（区間外）：\\( \sin\pi = 0 \\) → \\( 0 - 0 - 1 = -1 < 0 \\) ✓（解でない）

---

## まとめ

置換を使う三角不等式の解法手順：

1. \\( t = \sin\theta \\)（または \\( t = \cos\theta \\)）と置く
2. \\( t \\) の定義域（\\( -1 \leq t \leq 1 \\)）を確認
3. t の二次不等式を解く
4. 定義域との共通部分をとる
5. 残った t の範囲から sin（または cos）グラフで θ の範囲を読む

---

## もっと練習したい方へ

置換を使う三角不等式の問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-inequality-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：合成を使う三角不等式](/trig-inequality-double/)　／　[三角不等式](/trig-inequality/)
