---
layout: default
title: 合成を使う三角不等式
permalink: /trig-inequality-double/
description: "sinθ − cosθ \\( \\geq 1 \\) を合成で \\( \\sqrt{2}\\sin(\\theta - \\pi/4) \\geq 1 \\) に変換して解く方法を解説。合成後の変数範囲の確認と解区間の読み方を確認。"
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

次の図で、合成後の変数 \\( u = \theta - \frac{\pi}{4} \\) の視点での解区間（左）と θ に戻した解区間（右）を確認しましょう。

![左：sin(u) が \\( \\sqrt{2}/2 \\) 以上の解区間、右：θに戻して \\( \\pi/2 \\leq \\theta \\leq \\pi \\) となる塗りつぶし区間](/assets/images/trig-ineq-double.png)

右図の塗りつぶし部分が解区間 \\( \frac{\pi}{2} \leq \theta \leq \pi \\) です。

---

## 問題の解き方

**step 1：左辺を合成する**

<div>
$$
R = \sqrt{1^2 + (-1)^2} = \sqrt{2}
$$
</div>

\\( R\cos\varphi = 1,\ R\sin\varphi = -1 \\) より \\( \cos\varphi = \frac{1}{\sqrt{2}},\ \sin\varphi = -\frac{1}{\sqrt{2}} \\)。

これは第4象限なので \\( \varphi = -\frac{\pi}{4} \\)。

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

**step 3：\\( \theta - \frac{\pi}{4} \\) の範囲を確認する**

\\( 0 \leq \theta < 2\pi \\) より \\( -\frac{\pi}{4} \leq \theta - \frac{\pi}{4} < \frac{7\pi}{4} \\)。

**step 4：この範囲で \\( \sin \geq \frac{\sqrt{2}}{2} \\) の区間を読む**

\\( \sin\varphi \geq \frac{\sqrt{2}}{2} \\) の基本解：\\( \frac{\pi}{4} \leq \varphi \leq \frac{3\pi}{4} \\)

\\( \frac{\pi}{4} \leq \theta - \frac{\pi}{4} \leq \frac{3\pi}{4} \\) が範囲（\\( -\frac{\pi}{4} \\) 以上 \\( \frac{7\pi}{4} \\) 未満）内に収まることを確認 → OK

<div>
$$
\frac{\pi}{4} \leq \theta - \frac{\pi}{4} \leq \frac{3\pi}{4} \implies \frac{\pi}{2} \leq \theta \leq \pi
$$
</div>

---

## 確認

\\( \theta = \frac{\pi}{2} \\)：\\( \sin\frac{\pi}{2} - \cos\frac{\pi}{2} = 1 - 0 = 1 \geq 1 \\) ✓（境界）

\\( \theta = \pi \\)：\\( \sin\pi - \cos\pi = 0 - (-1) = 1 \geq 1 \\) ✓（境界）

\\( \theta = \frac{3\pi}{4} \\)：\\( \sin\frac{3\pi}{4} - \cos\frac{3\pi}{4} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2} > 1 \\) ✓（内部）

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

← [前の記事：基本不等式 sinθ と cosθ](/trig-inequality-basic/)　／　[三角不等式](/trig-inequality/)　／　→ [次の記事：置換して二次不等式に帰着](/trig-inequality-quadratic/)
