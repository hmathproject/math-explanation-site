---
layout: default
title: 加法定理
permalink: /trig-addition-formula/
description: "sin(α+β), cos(α−β), tan(α+β) の加法定理を使って sin 75°, cos 15°, tan 105° を求める方法を解説。公式の構造と代入の手順を確認。"
---

[サイトトップ](/) / [三角関数](/trigonometry/) / [加法定理と変換公式](/trig-addition/)

---

# 加法定理

---

## 問題

次の値を求めよ。

(1) \\( \sin 75° \\)　　(2) \\( \cos 15° \\)　　(3) \\( \tan 105° \\)

---

## なぜ加法定理が必要か

75°, 15°, 105° は単位円の代表角（30°, 45°, 60°, 90°）ではないため、直接値を読めません。しかしこれらは代表角の和差（75° = 45° + 30°, 15° = 45° − 30°, 105° = 60° + 45°）として書けます。加法定理を使うと、代表角の値の組み合わせで計算できます。

**加法定理（公式）：**

<div>
$$
\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta
$$
$$
\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta
$$
$$
\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}
$$
</div>

重要：\\( \sin(\alpha+\beta) \neq \sin\alpha + \sin\beta \\)。必ず「クロスの積の和差」の形になります。

---

## 問題の解き方

**(1) \\( \sin 75° = \sin(45° + 30°) \\)**

<div>
$$
\sin 75° = \sin 45°\cos 30° + \cos 45°\sin 30°
= \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2}
= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6}+\sqrt{2}}{4}
$$
</div>

**(2) \\( \cos 15° = \cos(45° - 30°) \\)**

<div>
$$
\cos 15° = \cos 45°\cos 30° + \sin 45°\sin 30°
= \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2}
= \frac{\sqrt{6}+\sqrt{2}}{4}
$$
</div>

（sin 75° と同じ値になります。これは \\( \cos 15° = \sin 75° \\) という余角の関係から確認できます）

**(3) \\( \tan 105° = \tan(60° + 45°) \\)**

<div>
$$
\tan 105° = \frac{\tan 60° + \tan 45°}{1 - \tan 60°\tan 45°}
= \frac{\sqrt{3} + 1}{1 - \sqrt{3} \cdot 1} = \frac{\sqrt{3}+1}{1-\sqrt{3}}
$$
</div>

分子・分母に \\( (1+\sqrt{3}) \\) を掛けて有理化すると、

<div>
$$
= \frac{(\sqrt{3}+1)(1+\sqrt{3})}{(1-\sqrt{3})(1+\sqrt{3})} = \frac{(\sqrt{3}+1)^2}{1-3} = \frac{4+2\sqrt{3}}{-2} = -(2+\sqrt{3})
$$
</div>

---

## 確認

\\( \sin 75° = \sin(180° - 105°) = \sin 105° \\)。一方 \\( \sin 105° = \sin(60°+45°) = \frac{\sqrt{6}+\sqrt{2}}{4} \\) を加法定理で確認できます。

---

## まとめ

| 公式 | 構造 |
|---|---|
| \\( \sin(\alpha+\beta) \\) | sin と cos のクロス積の和 |
| \\( \cos(\alpha+\beta) \\) | cos どうしの積 − sin どうしの積 |
| \\( \tan(\alpha+\beta) \\) | tan の和 ÷（1 − tan の積） |

加法定理は倍角公式（次記事）と三角関数の合成（次々記事）の出発点になります。

---

## もっと練習したい方へ

加法定理の計算問題を収録した解説PDFを無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/trig-addition-pack.pdf">PDFをダウンロードする（無料）</a>

---

[加法定理と変換公式](/trig-addition/)　／　→ [次の記事：倍角公式・半角公式](/trig-double-angle/)
