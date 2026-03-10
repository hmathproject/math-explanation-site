---
layout: default
title: 基本不等式 sinθ と cosθ
permalink: /trig-inequality-basic/
description: "sin θ がある値以上、cos θ がある値以下となる基本三角不等式をグラフの「水平線以上の区間」として解く方法を解説。等号の有無で境界を含むかが決まる。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [三角不等式](/trig-inequality/)

---

# 基本不等式 sinθ と cosθ

---

## 問題

\\( 0 \leq \theta < 2\pi \\) のとき、次の不等式を解け。

(1) \\( \sin\theta \geq \dfrac{\sqrt{3}}{2} \\)　　(2) \\( \cos\theta < -\dfrac{1}{2} \\)

---

## まず何を見るか

三角不等式を解くとは「sin（または cos）グラフが水平線以上（または以下）になる \\( \theta \\) の区間を読む」操作です。

次の図で、左は \\( \sin\theta \geq \frac{\sqrt{3}}{2} \\) の解の区間（塗りつぶし）、右は \\( \cos\theta \leq -\frac{1}{2} \\) の解の区間を示しています。

![sin θ が \\( \\sqrt{3}/2 \\) 以上、cos θ が -1/2 以下となる解区間を塗り分けた2パネル図](/assets/images/trig-inequality-basic-combined.png)

塗りつぶされた区間が解の範囲です。

---

## なぜ解が「区間」になるか

方程式（= k）は交点（有限個の点）が解でしたが、不等式はグラフが水平線の上か下かの**連続した区間**が解になります。sin グラフは山・谷の形をしているため、\\( y \geq k \\) を満たす θ は山の頂上付近の区間になります。

---

## 場合別の計算

**(1) \\( \sin\theta \geq \dfrac{\sqrt{3}}{2} \\)**

**境界点（等号成立）：** \\( \sin\theta = \dfrac{\sqrt{3}}{2} \\) → \\( \theta = \dfrac{\pi}{3},\ \dfrac{2\pi}{3} \\)

sin グラフが \\( y = \dfrac{\sqrt{3}}{2} \\) 以上になる区間を読む：

<div>
$$
\frac{\pi}{3} \leq \theta \leq \frac{2\pi}{3}
$$
</div>

（\\( \geq \\) なので境界点を含む：閉区間）

**(2) \\( \cos\theta < -\dfrac{1}{2} \\)**

**境界点：** \\( \cos\theta = -\dfrac{1}{2} \\) → \\( \theta = \dfrac{2\pi}{3},\ \dfrac{4\pi}{3} \\)

cos グラフが \\( y = -\dfrac{1}{2} \\) より下になる区間を読む：

<div>
$$
\frac{2\pi}{3} < \theta < \frac{4\pi}{3}
$$
</div>

（\\( < \\) なので境界点を含まない：開区間）

---

## 確認

(1) \\( \theta = \dfrac{\pi}{2} \\)（区間内）：\\( \sin\dfrac{\pi}{2} = 1 \geq \dfrac{\sqrt{3}}{2} \\) ✓

(2) \\( \theta = \pi \\)（区間内）：\\( \cos\pi = -1 < -\dfrac{1}{2} \\) ✓

---

## まとめ

| 不等式 | \\( [0, 2\pi) \\) での解の区間 |
|---|---|
| \\( \sin\theta \geq k \\)（\\( 0 < k < 1 \\)） | \\( [\alpha, \pi-\alpha] \\) |
| \\( \sin\theta \leq k \\)（\\( 0 < k < 1 \\)） | \\( [0, \alpha] \cup [\pi-\alpha, 2\pi) \\) |
| \\( \cos\theta \leq k \\)（\\( -1 < k < 0 \\)） | \\( [\arccos k, 2\pi - \arccos k] \\) |

グラフを描いて「塗りつぶす区間」を目で確認することが、解の正確な範囲を得る確実な方法です。

---

## もっと練習したい方へ

基本不等式から合成・置換への応用問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-inequality-pack.pdf">PDFをダウンロードする（無料）</a>

---

[三角不等式](/trig-inequality/)　／　→ [次の記事：合成を使う三角不等式](/trig-inequality-double/)
