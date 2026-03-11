---
layout: default
title: 成分表示と大きさ — 図を計算に変換する
permalink: /vec-component-form/
description: "ベクトルの成分表示（x軸・y軸への射影）、大きさの公式（ピタゴラスの定理）、単位ベクトルの求め方（高校数B）。"
---

[成分と演算](/vec-components/)　／　→ [成分による演算](/vec-component-ops/)

---

# 成分表示と大きさ — 図を計算に変換する

---

## 動機: 「矢印を数のペアに変換する」

矢印（ベクトル）を計算で扱うには、数値で表す必要があります。x 軸方向の移動量と y 軸方向の移動量に分解することで、矢印を \\( (a_1, a_2) \\) という数のペアで表せます。

---

## 成分表示 — 座標軸への射影

ベクトル \\( \\vec{a} \\) の x 成分・y 成分は「矢印を各座標軸に射影した長さ」です。

![成分分解の座標図（左）/ 大きさとピタゴラスの定理（右）](/assets/images/vec-component-form-combined.png)

\\( \\overrightarrow{AB} \\) の成分は「**終点の座標 − 始点の座標**」：

<div>
$$
\overrightarrow{AB} = (B_x - A_x,\ B_y - A_y)
$$
</div>

---

## 大きさ — ピタゴラスの定理から

x 成分と y 成分を 2 辺とする直角三角形の斜辺が矢印の長さです：

<div>
$$
|\vec{a}| = \sqrt{a_1^2 + a_2^2}
$$
</div>

これは「天下り」の公式ではなく、ピタゴラスの定理の直接の応用です。

---

## 成分が同じ \\( \\Leftrightarrow \\) ベクトルが等しい

\\( \\vec{a} = (a_1, a_2) \\) と \\( \\vec{b} = (b_1, b_2) \\) が等しい \\( \\Leftrightarrow \\) \\( a_1 = b_1 \\) かつ \\( a_2 = b_2 \\)

x 方向と y 方向が独立しているため、成分ごとに等式を立てられます。

---

## 単位ベクトル — 大きさ 1 のベクトル

\\( \\vec{a} \\) と同じ向きで大きさが 1 のベクトルを**単位ベクトル**といいます：

<div>
$$
\frac{\vec{a}}{|\vec{a}|}
$$
</div>

大きさの確認：

<div>
$$
\left|\frac{\vec{a}}{|\vec{a}|}\right| = \frac{|\vec{a}|}{|\vec{a}|} = 1
$$
</div>

---

## 計算例

### 例 1: AB の成分と大きさ

A(1, 3), B(4, 7) のとき：

<div>
$$
\overrightarrow{AB} = (4-1,\ 7-3) = (3,\ 4)
$$
</div>

<div>
$$
|\overrightarrow{AB}| = \sqrt{3^2+4^2} = \sqrt{9+16} = \sqrt{25} = 5
$$
</div>

（3-4-5 の直角三角形）

### 例 2: 方程式から成分を求める

\\( \\vec{a} = (2, -1) \\), \\( 2\\vec{a} - 3\\vec{b} = (1, 5) \\) のとき \\( \\vec{b} \\) を求めよ。

<div>
$$
3\vec{b} = 2\vec{a} - (1,5) = (4,-2) - (1,5) = (3,\ -7)
$$
</div>

<div>
$$
\vec{b} = \left(1,\ -\frac{7}{3}\right)
$$
</div>

### 例 3: \\( \\vec{a} = (3, 4) \\) の単位ベクトル

<div>
$$
|\vec{a}| = \sqrt{9+16} = 5
$$
</div>

<div>
$$
\frac{\vec{a}}{|\vec{a}|} = \frac{1}{5}(3,4) = \left(\frac{3}{5},\ \frac{4}{5}\right)
$$
</div>

確認: \\( \\left(\\frac{3}{5}\\right)^2 + \\left(\\frac{4}{5}\\right)^2 = \\frac{9+16}{25} = 1 \\) ✓

---

## 関連記事

- [微分の接線](/diff-tangent/) — 接線の傾きと法線ベクトル（成分）の対応

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-components-pack.pdf">PDFをダウンロードする（無料）</a>

---

[成分と演算](/vec-components/)　／　→ [成分による演算](/vec-component-ops/)
