---
layout: default
title: 合成を使う三角不等式
permalink: /trig-inequality-double/
description: "sinθ − cosθ ≥ 1 を合成で √2 sin(θ − π/4) ≥ 1 に変換して解く方法を解説。合成後の変数範囲の確認と解区間の読み方を確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [三角不等式](/trig-inequality/)

---

# 合成を使う三角不等式

---

## 問題

\\( 0 \leq \theta < 2\pi \\) のとき、\\( \sin\theta - \cos\theta \geq 1 \\) を解け。

---

## なぜ合成するか

左辺は sin と cos の1次結合です。合成で \\( \sqrt{2}\sin(\theta - \varphi) \\) にまとめると、基本不等式 \\( \sin(\theta - \varphi) \geq k \\) に帰着します。

---

## 問題の解き方

**step 1：左辺を合成する**

<div>
$$
R = \sqrt{1^2 + (-1)^2} = \sqrt{2}
$$
</div>

\\( R\cos\varphi = 1,\ R\sin\varphi = -1 \\) より \\( \cos\varphi = \dfrac{1}{\sqrt{2}},\ \sin\varphi = -\dfrac{1}{\sqrt{2}} \\)。

これは第4象限なので \\( \varphi = -\dfrac{\pi}{4} \\)。

<div>
$$
\sin\theta - \cos\theta = \sqrt{2}\sin\!\left(\theta - \frac{\pi}{4}\right)
$$
</div>

**step 2：基本不等式に帰着する**

<div>
$$
\sqrt{2}\sin\!\left(\theta - \frac{\pi}{4}\right) \geq 1 \implies \sin\!\left(\theta - \frac{\pi}{4}\right) \geq \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}
$$
</div>

**step 3：\\( \theta - \dfrac{\pi}{4} \\) の範囲を確認する**

\\( 0 \leq \theta < 2\pi \\) より \\( -\dfrac{\pi}{4} \leq \theta - \dfrac{\pi}{4} < \dfrac{7\pi}{4} \\)。

**step 4：この範囲で \\( \sin \geq \dfrac{\sqrt{2}}{2} \\) の区間を読む**

\\( \sin\varphi \geq \dfrac{\sqrt{2}}{2} \\) の基本解：\\( \dfrac{\pi}{4} \leq \varphi \leq \dfrac{3\pi}{4} \\)

\\( \dfrac{\pi}{4} \leq \theta - \dfrac{\pi}{4} \leq \dfrac{3\pi}{4} \\) が範囲（\\( -\dfrac{\pi}{4} \\) 以上 \\( \dfrac{7\pi}{4} \\) 未満）内に収まることを確認 → OK

<div>
$$
\frac{\pi}{4} \leq \theta - \frac{\pi}{4} \leq \frac{3\pi}{4} \implies \frac{\pi}{2} \leq \theta \leq \pi
$$
</div>

---

## 確認

\\( \theta = \dfrac{\pi}{2} \\)：\\( \sin\dfrac{\pi}{2} - \cos\dfrac{\pi}{2} = 1 - 0 = 1 \geq 1 \\) ✓（境界）

\\( \theta = \pi \\)：\\( \sin\pi - \cos\pi = 0 - (-1) = 1 \geq 1 \\) ✓（境界）

\\( \theta = \dfrac{3\pi}{4} \\)：\\( \sin\dfrac{3\pi}{4} - \cos\dfrac{3\pi}{4} = \dfrac{\sqrt{2}}{2} + \dfrac{\sqrt{2}}{2} = \sqrt{2} > 1 \\) ✓（内部）

---

## まとめ

合成を使う三角不等式の解法手順：

1. 左辺を \\( R\sin(\theta + \varphi) \\) に合成
2. \\( \sin(\theta+\varphi) \geq c/R \\) の形にする
3. \\( \theta + \varphi \\) の範囲を書く
4. その範囲内で \\( \sin \geq c/R \\) を満たす区間を読む
5. θ に戻して区間を確定

---

## もっと練習したい方へ

合成を使う不等式の問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-inequality-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：基本不等式 sinθ ≥ k, cosθ ≤ k](/trig-inequality-basic/)　／　[三角不等式](/trig-inequality/)　／　→ [次の記事：置換して二次不等式に帰着](/trig-inequality-quadratic/)
