---
layout: default
title: 倍角公式・半角公式
permalink: /trig-double-angle/
description: "倍角公式 sin 2θ = 2sinθcosθ, cos 2θ = 1 − 2sin²θ の使い方を解説。加法定理からの導出と、与えられた sin・cos の値から計算する手順を確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [加法定理と変換公式](/trig-addition/)

---

# 倍角公式・半角公式

---

## 問題

\\( \sin\theta = \frac{2}{3} \\)、\\( \frac{\pi}{2} < \theta < \pi \\) のとき、\\( \sin 2\theta \\) と \\( \cos 2\theta \\) を求めよ。

---

## なぜ倍角公式か

\\( 2\theta \\) の三角関数を \\( \theta \\) の三角関数で表すには、加法定理の \\( \alpha = \beta = \theta \\) の特殊ケースを使います。

**倍角公式（加法定理から導く）：**

<div>
$$
\sin 2\theta = \sin(\theta + \theta) = 2\sin\theta\cos\theta
$$
$$
\cos 2\theta = \cos(\theta + \theta) = \cos^2\theta - \sin^2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1
$$
</div>

\\( \cos 2\theta \\) は3通りの表現があります。使いやすい方を選んでください（与えられた情報が sin だけなら \\( 1 - 2\sin^2\theta \\)、cos だけなら \\( 2\cos^2\theta - 1 \\)）。

---

## 問題の解き方

**step 1：\\( \cos\theta \\) を求める**

<div>
$$
\cos^2\theta = 1 - \sin^2\theta = 1 - \frac{4}{9} = \frac{5}{9}
$$
</div>

\\( \frac{\pi}{2} < \theta < \pi \\)（第2象限）より \\( \cos\theta < 0 \\)。

<div>
$$
\cos\theta = -\frac{\sqrt{5}}{3}
$$
</div>

**step 2：\\( \sin 2\theta \\) を計算する**

<div>
$$
\sin 2\theta = 2\sin\theta\cos\theta = 2 \cdot \frac{2}{3} \cdot \left(-\frac{\sqrt{5}}{3}\right) = -\frac{4\sqrt{5}}{9}
$$
</div>

**step 3：\\( \cos 2\theta \\) を計算する**

\\( \sin\theta \\) だけで表せる式を使うと、

<div>
$$
\cos 2\theta = 1 - 2\sin^2\theta = 1 - 2 \cdot \frac{4}{9} = 1 - \frac{8}{9} = \frac{1}{9}
$$
</div>

---

## 確認

\\( \sin^2 2\theta + \cos^2 2\theta = \frac{80}{81} + \frac{1}{81} = \frac{81}{81} = 1 \\) ✓

\\( 2\theta \\) の象限チェック：\\( \frac{\pi}{2} < \theta < \pi \\) なら \\( \pi < 2\theta < 2\pi \\)（第3・4象限）。\\( \sin 2\theta = -\frac{4\sqrt{5}}{9} < 0 \\) は第3・4象限と整合 ✓。\\( \cos 2\theta = \frac{1}{9} > 0 \\) は第4象限と整合 ✓。

---

## まとめ

| 公式 | 用途 |
|---|---|
| \\( \sin 2\theta = 2\sin\theta\cos\theta \\) | sin と cos が両方分かっているとき |
| \\( \cos 2\theta = 1 - 2\sin^2\theta \\) | sin だけ分かっているとき |
| \\( \cos 2\theta = 2\cos^2\theta - 1 \\) | cos だけ分かっているとき |
| \\( \cos 2\theta = \cos^2\theta - \sin^2\theta \\) | 両方分かっているとき（基本形） |

倍角公式は加法定理の特殊ケースなので、公式を「暗記」せずとも加法定理から導けます。

---

## もっと練習したい方へ

倍角公式を使う計算問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-addition-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [前の記事：加法定理](/trig-addition-formula/)　／　[加法定理と変換公式](/trig-addition/)　／　→ [次の記事：三角関数の合成](/trig-synthesis/)
