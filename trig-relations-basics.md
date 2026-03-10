---
layout: default
title: 3つの相互関係公式
permalink: /trig-relations-basics/
description: "sin²θ + cos²θ = 1 を使って sin, cos, tan を相互に求める方法を解説。3公式の由来と使い方、象限による符号の決め方を確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [性質と相互関係](/trig-relations/)

---

# 3つの相互関係公式

---

## 問題

\\( \sin\theta = \frac{3}{5} \\)、\\( 0 < \theta < \frac{\pi}{2} \\) のとき、\\( \cos\theta \\) と \\( \tan\theta \\) を求めよ。

---

## なぜ「相互関係」が使えるか

sin, cos, tan の3つは単位円の同じ点の座標・比から定義されているため、一方が分かれば他方も計算できます。その計算の橋渡しをするのが相互関係公式です。

**3つの相互関係公式：**

<div>
$$
\sin^2\theta + \cos^2\theta = 1 \tag{1}
$$
$$
\tan\theta = \frac{\sin\theta}{\cos\theta} \tag{2}
$$
$$
1 + \tan^2\theta = \frac{1}{\cos^2\theta} \tag{3}
$$
</div>

(3) は (1) を \\( \cos^2\theta \\) で割ると導けます。

---

## 問題の解き方

**step 1：\\( \cos\theta \\) を求める**

公式 (1) より、

<div>
$$
\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}
$$
</div>

\\( 0 < \theta < \frac{\pi}{2} \\) より第1象限なので \\( \cos\theta > 0 \\)。

<div>
$$
\cos\theta = \frac{4}{5}
$$
</div>

**step 2：\\( \tan\theta \\) を求める**

公式 (2) より、

<div>
$$
\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\frac{3}{5}}{\frac{4}{5}} = \frac{3}{4}
$$
</div>

---

## 確認

\\( \sin^2\theta + \cos^2\theta = \frac{9}{25} + \frac{16}{25} = \frac{25}{25} = 1 \\) ✓

---

## なぜ cos の符号を象限で決めるか

\\( \cos^2\theta = \frac{16}{25} \\) から \\( \cos\theta = \pm\frac{4}{5} \\) の2候補があります。\\( 0 < \theta < \frac{\pi}{2} \\)（第1象限）という条件があるから \\( \cos\theta > 0 \\) と確定できます。

**象限と符号まとめ：**

| 象限 | \\( \sin\theta \\) | \\( \cos\theta \\) | \\( \tan\theta \\) |
|---|---|---|---|
| 第1（\\( 0 < \theta < \frac{\pi}{2} \\)） | \\( + \\) | \\( + \\) | \\( + \\) |
| 第2（\\( \frac{\pi}{2} < \theta < \pi \\)） | \\( + \\) | \\( - \\) | \\( - \\) |
| 第3（\\( \pi < \theta < \frac{3\pi}{2} \\)） | \\( - \\) | \\( - \\) | \\( + \\) |
| 第4（\\( \frac{3\pi}{2} < \theta < 2\pi \\)） | \\( - \\) | \\( + \\) | \\( - \\) |

---

## まとめ

| 公式 | 用途 |
|---|---|
| \\( \sin^2\theta + \cos^2\theta = 1 \\) | sin から cos を求める（または逆） |
| \\( \tan\theta = \sin\theta/\cos\theta \\) | sin・cos が分かれば tan も求まる |
| \\( 1 + \tan^2\theta = 1/\cos^2\theta \\) | tan から cos を求めるとき |

相互関係公式 + 象限による符号の決定、この2ステップが sin・cos・tan の相互変換の基本手順です。

---

## もっと練習したい方へ

相互関係を使う計算問題の解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-relations-pack.pdf">PDFをダウンロードする（無料）</a>

---

[性質と相互関係](/trig-relations/)　／　→ [次の記事：対称性・補角・余角の変換公式](/trig-relations-symmetry/)
