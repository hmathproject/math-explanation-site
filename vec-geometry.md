---
layout: default
title: 位置ベクトルと図形
permalink: /vec-geometry/
description: "位置ベクトルの定義、内分・外分点の位置ベクトル、重心・共線・平行の図形条件まで（全3記事・解説PDF付き）（高校数B）。"
---

← [内積と図形](/vec-inner-product/)　／　[ベクトル](/vectors/)

---

# 位置ベクトルと図形

**位置ベクトルは「点の位置を式で扱う」道具。図形条件をベクトルの等式に翻訳する**

- [位置ベクトルの考え方 — 点を式で扱う](/vec-position/)
- [内分・外分 — 点の位置を比で表す](/vec-division/)
- [図形条件のベクトル式化 — 重心・平行・共線](/vec-figure-conditions/)

---

## この単元で学ぶこと

- 位置ベクトルは「原点 O から点 P への矢印 \\( \\overrightarrow{OP} \\)」として点の位置を表す
- \\( \\overrightarrow{AB} = \\vec{b} - \\vec{a} \\) が「終点の位置 − 始点の位置」として必然的に導かれる理由
- 内分点の公式が「比で引き寄せられる重みつき平均」として自然に出る理由
- 重心が \\( \\frac{\\vec{a}+\\vec{b}+\\vec{c}}{3} \\)（3点の「平均の位置」）になる理由
- 共線条件が \\( \\overrightarrow{OP} = \\vec{a} + t(\\vec{b}-\\vec{a}) \\)（AP が AB の実数倍）として書ける理由

---

## 位置ベクトルの考え方

位置ベクトルを使う利点は「点の位置を始点なしで扱える」ことです。座標のペアと違い、ベクトルの演算（加減・実数倍）で点の位置関係を直接計算できます。

\\( \\overrightarrow{AB} = \\overrightarrow{OB} - \\overrightarrow{OA} = \\vec{b} - \\vec{a} \\) は「道筋をたどる」式から自然に出ます：O から A に行って（\\( \\vec{a} \\)）、そこから B に行く（\\( \\overrightarrow{AB} \\)）と O から B への \\( \\vec{b} \\) と同じ。

内分点は「比で引き寄せられる点」です。m:n の内分点 P は A に \\( \\frac{n}{m+n} \\)、B に \\( \\frac{m}{m+n} \\) の割合で引き寄せられた点として \\( \\overrightarrow{OP} = \\frac{n\\vec{a}+m\\vec{b}}{m+n} \\) と書けます。

---

## 解説記事

### [位置ベクトルの考え方 — 点を式で扱う](/vec-position/)

「点の位置をベクトルで表す」利点と \\( \\overrightarrow{AB} = \\vec{b} - \\vec{a} \\) の導出。点が線分 AB 上にある条件を位置ベクトルで表します。

---

### [内分・外分 — 点の位置を比で表す](/vec-division/)

内分点の公式 \\( \\overrightarrow{OP} = \\frac{n\\vec{a}+m\\vec{b}}{m+n} \\) が「比で引き寄せられる」として自然に出る理由。外分点での符号の変化と中点（m=n の特殊ケース）を確認します。

---

### [図形条件のベクトル式化 — 重心・平行・共線](/vec-figure-conditions/)

重心が 3 点の「平均の位置」として \\( \\frac{\\vec{a}+\\vec{b}+\\vec{c}}{3} \\) になる理由。共線条件（AP が AB の実数倍）と平行条件（一方が他方の実数倍）の書き方を確認します。

---

## 解説PDFについて

<a class="pdf-btn" href="/assets/pdf/vec-geometry-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [内積と図形](/vec-inner-product/)　／　[ベクトル](/vectors/)
