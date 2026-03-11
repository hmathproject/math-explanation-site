---
layout: default
title: 不定積分の計算 — 展開・整理して公式に帰着
permalink: /integ-antiderivative-calc/
description: "不定積分の線形性と、積の形を展開してから基本公式を適用する計算手順を解説。∫(2x+1)² dx のような展開が必要なケースを中心に練習する（高校数II）。"
---

[サイトトップ](/) / [積分](/integral/) / [不定積分](/integ-indefinite/)

---

# 不定積分の計算 — 展開・整理して公式に帰着

---

## 線形性: 積分は足し算と定数倍を通す

不定積分の**線形性**（線形法則）は次の 2 つのルールからなります。

<div>
$$
\int (f(x) + g(x))\,dx = \int f(x)\,dx + \int g(x)\,dx
$$
</div>

<div>
$$
\int k f(x)\,dx = k \int f(x)\,dx \quad (k \text{ は定数})
$$
</div>

まとめると、

<div>
$$
\int (af(x) + bg(x))\,dx = a\int f(x)\,dx + b\int g(x)\,dx
$$
</div>

これにより、多項式は各項ごとに基本公式を適用して足し合わせることができます。

---

## なぜ展開が必要か — 積の積分は積にならない

微分では積の法則 \\( (fg)' = f'g + fg' \\) があります。しかし積分には対応する「積の法則」がなく、

<div>
$$
\int f(x)\,g(x)\,dx \neq \left(\int f(x)\,dx\right)\cdot\left(\int g(x)\,dx\right)
$$
</div>

です。これを確認してみましょう。\\( f(x) = x, g(x) = x \\) とすると、左辺は \\( \int x^2\,dx = \frac{x^3}{3} + C \\) ですが、右辺は \\( \frac{x^2}{2} \cdot \frac{x^2}{2} = \frac{x^4}{4} \\) となり一致しません。

したがって \\( \int(2x+1)^2\,dx \\) のような式は、**まず展開して多項式に直してから**各項を積分する必要があります。

---

## 計算手順: \\( \int(2x+1)^2\,dx \\)

**Step 1:** 展開する。

<div>
$$
(2x+1)^2 = 4x^2 + 4x + 1
$$
</div>

**Step 2:** 線形性を使って各項を積分する。

<div>
$$
\int (4x^2 + 4x + 1)\,dx = 4 \cdot \frac{x^3}{3} + 4 \cdot \frac{x^2}{2} + x + C
$$
</div>

**Step 3:** 整理する。

<div>
$$
= \frac{4x^3}{3} + 2x^2 + x + C
$$
</div>

確かめ: \\( \left(\frac{4x^3}{3} + 2x^2 + x\right)' = 4x^2 + 4x + 1 = (2x+1)^2 \\) ✓

---

## 計算例: \\( \int x(x-2)(x+1)\,dx \\)

**Step 1:** 展開する。

<div>
$$
x(x-2)(x+1) = x\bigl((x-2)(x+1)\bigr) = x(x^2 - x - 2) = x^3 - x^2 - 2x
$$
</div>

**Step 2:** 各項を積分する。

<div>
$$
\int (x^3 - x^2 - 2x)\,dx = \frac{x^4}{4} - \frac{x^3}{3} - x^2 + C
$$
</div>

確かめ: \\( \left(\frac{x^4}{4} - \frac{x^3}{3} - x^2\right)' = x^3 - x^2 - 2x \\) ✓

---

## よくある計算ミスのまとめ

| 状況 | 正しい手順 | 誤った手順 |
|---|---|---|
| \\( \int(ax+b)^n\,dx \\) | まず展開してから積分 | \\( \frac{(ax+b)^{n+1}}{n+1} \\) はこの範囲では不可 |
| \\( \int f(x)g(x)\,dx \\) | まず積を展開 | \\( \int f\,dx \cdot \int g\,dx \\) とするのは誤り |
| 積分定数 | 最後に必ず \\( + C \\) | \\( C \\) の書き忘れに注意 |

---

![多項式の不定積分例（左）/ 積の展開の必要性（右）](/assets/images/integ-antiderivative-calc-combined.png)

---

## もっと練習したい方へ

展開・整理を含む不定積分の計算問題を収録した解説 PDF を無料で配布しています。

<a class="pdf-btn" href="/assets/pdf/integ-indefinite-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [不定積分とは何か](/integ-antiderivative-basics/)　／　[不定積分](/integ-indefinite/)　／　→ [積分定数の決定](/integ-antiderivative-initial/)
