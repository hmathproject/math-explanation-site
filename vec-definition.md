---
layout: default
title: ベクトルとは何か — 向きと大きさをもつ量
permalink: /vec-definition/
description: "ベクトルの定義（向きと大きさをもつ量）、ベクトルの相等（始点の位置は無関係）、零ベクトルと逆ベクトルの意味（高校数B）。"
---

[ベクトルの基本](/vec-basics/)　／　→ [ベクトルの加法・減法](/vec-addition/)

---

# ベクトルとは何か — 向きと大きさをもつ量

---

## 動機: 「場所によらない移動量」を表したい

「1 km 北に進む」という情報を数で表せるでしょうか。スカラー（普通の数）では方向が表せません。そこで「向き」と「大きさ」を一緒に持つ量、**ベクトル**を導入します。

矢印はまさにこの 2 つの情報を持っています。矢印の**向き**がベクトルの向き、矢印の**長さ**がベクトルの大きさ（長さ）です。

---

## ベクトルの相等 — なぜ始点が違っても同じか

![複数の矢印でベクトルの相等を示す図（左）/ 零ベクトル・逆ベクトルの図（右）](/assets/images/vec-definition-combined.png)

ベクトル \\( \\vec{a} \\) は「どこから出発するか」に依存しない移動量です。したがって：

\\( \\overrightarrow{AB} = \\overrightarrow{CD} \\) の意味は「AB と CD が**平行・等長・同向き**」

始点の位置は関係ありません。平行四辺形 ABCD では \\( \\overrightarrow{AB} = \\overrightarrow{DC} \\)（向きに注意：D から C の方向）。

---

## 零ベクトル — 大きさ 0 のベクトル

始点と終点が一致するベクトルを**零ベクトル** \\( \\vec{0} \\) といいます。大きさが 0 なので向きは定義しません。

<div>
$$
\vec{a} + \vec{0} = \vec{a}, \quad \vec{a} + (-\vec{a}) = \vec{0}
$$
</div>

---

## 逆ベクトル — 向きを反転させる

\\( \\vec{a} \\) と大きさが等しく向きが逆のベクトルを**逆ベクトル** \\( -\\vec{a} \\) といいます。

<div>
$$
-\overrightarrow{AB} = \overrightarrow{BA}
$$
</div>

---

## 計算例

### 例 1: 平行四辺形 ABCD での相等

平行四辺形の性質（対辺が平行・等長）より：

<div>
$$
\overrightarrow{AB} = \overrightarrow{DC}
$$
</div>

注意: \\( \\overrightarrow{CD} \\) は **D から C** なので \\( -\\overrightarrow{AB} \\)（向きが逆）。

### 例 2: OA = CB のとき OACB の形状

\\( \\overrightarrow{OA} = \\overrightarrow{CB} \\) は「O から A への移動」と「C から B への移動」が同じ、つまり OA \\( \\parallel \\) CB かつ \\( |\\overrightarrow{OA}| = |\\overrightarrow{CB}| \\)。したがって四角形 OACB は**平行四辺形**。

### 例 3: \\( \\vec{a} + \\vec{b} + \\vec{c} = \\vec{0} \\)、\\( \\vec{a} = -2\\vec{c} \\) のとき \\( \\vec{b} \\)

代入すると：

<div>
$$
-2\vec{c} + \vec{b} + \vec{c} = \vec{0}
$$
</div>

<div>
$$
\vec{b} - \vec{c} = \vec{0} \implies \vec{b} = \vec{c}
$$
</div>

確認: \\( -2\\vec{c} + \\vec{c} + \\vec{c} = (-2+1+1)\\vec{c} = \\vec{0} \\) ✓

---

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-basics-pack.pdf">PDFをダウンロードする（無料）</a>

---

[ベクトルの基本](/vec-basics/)　／　→ [ベクトルの加法・減法](/vec-addition/)
