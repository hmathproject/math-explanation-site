---
layout: default
title: 内積と図形
permalink: /vec-inner-product/
description: "ベクトルの内積（射影から定義）、垂直条件（cos 90°=0から）、なす角と長さの計算まで（全3記事・解説PDF付き）（高校数B）。"
---

← [成分と演算](/vec-components/)　／　[ベクトル](/vectors/)　／　→ [位置ベクトルと図形](/vec-geometry/)

---

# 内積と図形

**内積は「2つのベクトルがどれだけ同方向を向いているか」を測る量**

- [内積の意味 — なぜ cos θ が出てくるか](/vec-dot-product/)
- [垂直条件 — a·b = 0 になる理由](/vec-perpendicular/)
- [なす角と長さの計算 — 内積の使い方](/vec-angle-calc/)

---

## この単元で学ぶこと

- 内積 \\( \\vec{a} \\cdot \\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta \\) の定義が「射影の長さ × 大きさ」として自然に導かれる理由
- なぜ \\( \\vec{a} \\perp \\vec{b} \\Leftrightarrow \\vec{a} \\cdot \\vec{b} = 0 \\) か（\\( \\cos 90° = 0 \\) より必然）
- 成分公式 \\( \\vec{a} \\cdot \\vec{b} = a_1 b_1 + a_2 b_2 \\) が余弦定理から導かれる理由
- \\( |\\vec{a} + \\vec{b}|^2 = |\\vec{a}|^2 + 2\\vec{a}\\cdot\\vec{b} + |\\vec{b}|^2 \\) の展開と余弦定理との対比

---

## 内積の考え方

内積の動機は「2つのベクトルがどれだけ同じ方向を向いているか」を数値で表したいという要求です。\\( \\vec{a} \\) を \\( \\vec{b} \\) の方向に射影すると長さ \\( |\\vec{a}|\\cos\\theta \\) の成分が得られます。これに \\( |\\vec{b}| \\) をかけた量が内積です。

\\( \\theta = 90° \\) のとき \\( \\cos 90° = 0 \\) なので、垂直なベクトルどうしの内積は 0 になります。これは定義から必然的に出る結論であり、「覚える公式」ではありません。

内積の成分公式 \\( a_1 b_1 + a_2 b_2 \\) は余弦定理を適用することで導けます。この導出を理解すると、なぜ成分の積和が角度情報を含むかが分かります。

---

## 解説記事

### [内積の意味 — なぜ cos θ が出てくるか](/vec-dot-product/)

「どれだけ同方向を向いているか」という動機から \\( \\vec{a} \\cdot \\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta \\) を定義します。\\( \\vec{a} \\) の \\( \\vec{b} \\) 方向への射影が \\( |\\vec{a}|\\cos\\theta \\) になる理由を図で確認します。

---

### [垂直条件 — a·b = 0 になる理由](/vec-perpendicular/)

\\( \\cos 90° = 0 \\) から \\( \\vec{a} \\perp \\vec{b} \\Leftrightarrow \\vec{a} \\cdot \\vec{b} = 0 \\) が必然的に導かれることを示します。成分公式 \\( a_1 b_1 + a_2 b_2 \\) の導出（余弦定理を使う）を確認します。

---

### [なす角と長さの計算 — 内積の使い方](/vec-angle-calc/)

\\( \\cos\\theta = \\frac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|} \\) でなす角を計算する手順と、\\( |\\vec{a}+\\vec{b}|^2 \\) の展開（余弦定理との対比）を確認します。

---

## 解説PDFについて

<a class="pdf-btn" href="/assets/pdf/vec-inner-product-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [成分と演算](/vec-components/)　／　[ベクトル](/vectors/)　／　→ [位置ベクトルと図形](/vec-geometry/)
