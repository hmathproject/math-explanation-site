---
layout: default
title: ベクトルの加法・減法 — 矢印の連結と逆方向
permalink: /vec-addition/
description: "ベクトルの加法（頭尾連結・平行四辺形則）、減法（逆ベクトルを加える）、AB = OB - OA の意味（高校数B）。"
---

← [ベクトルとは何か](/vec-definition/)　／　[ベクトルの基本](/vec-basics/)　／　→ [実数倍と平行](/vec-scalar/)

---

# ベクトルの加法・減法 — 矢印の連結と逆方向

---

## 動機: 「移動の合成」を数式で表したい

「東に 3 km 進んでから北に 4 km 進む」と、合計の移動はどこに向かうか。この「移動の合成」がベクトルの加法です。

---

## 加法の定義 — 頭尾連結

\\( \\vec{a} \\) の終点から \\( \\vec{b} \\) を出発したとき、\\( \\vec{a} \\) の始点から \\( \\vec{b} \\) の終点への矢印が \\( \\vec{a} + \\vec{b} \\) です。

![頭尾連結の加法と平行四辺形則（左）/ OB - OA = AB の位置関係（右）](/assets/images/vec-addition-combined.png)

これを**頭尾連結**（tail-to-head）といいます。**平行四辺形則**（両方の始点を合わせて描く方法）と結果は同じです。

---

## \\( \\overrightarrow{AB} = \\overrightarrow{OB} - \\overrightarrow{OA} \\) の意味

O から A へ行き（\\( \\overrightarrow{OA} = \\vec{a} \\)）、そこから B へ行く（\\( \\overrightarrow{AB} \\)）と、O から B への \\( \\overrightarrow{OB} = \\vec{b} \\) と同じ道筋です：

<div>
$$
\overrightarrow{OA} + \overrightarrow{AB} = \overrightarrow{OB}
$$
</div>

したがって：

<div>
$$
\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \vec{b} - \vec{a}
$$
</div>

「**終点の位置 − 始点の位置**」という形です。

---

## 減法 — 逆ベクトルを加える

<div>
$$
\vec{a} - \vec{b} = \vec{a} + (-\vec{b})
$$
</div>

\\( -\\vec{b} \\) は \\( \\vec{b} \\) の逆ベクトル（向きを反転）。減法は「逆ベクトルを頭尾連結する」操作です。

---

## 計算例

### 例 1: 成分で加法を確認

\\( \\vec{a} = (2, 3) \\), \\( \\vec{b} = (1, -1) \\) のとき：

<div>
$$
\vec{a} + \vec{b} = (2+1,\ 3+(-1)) = (3,\ 2)
$$
</div>

### 例 2: AB の成分

A(1, 2), B(4, 5) のとき：

<div>
$$
\overrightarrow{AB} = (4-1,\ 5-2) = (3,\ 3)
$$
</div>

「終点 − 始点」の成分差です。

### 例 3: 3 つのベクトルの和

<div>
$$
\overrightarrow{AB} + \overrightarrow{BC} + \overrightarrow{CA} = \overrightarrow{AC} + \overrightarrow{CA} = \vec{0}
$$
</div>

頭尾連結で A → B → C → A と戻ってくるので零ベクトルになります。

---

## もっと練習したい方へ

<a class="pdf-btn" href="/assets/pdf/vec-basics-pack.pdf">PDFをダウンロードする（無料）</a>

---

← [ベクトルとは何か](/vec-definition/)　／　[ベクトルの基本](/vec-basics/)　／　→ [実数倍と平行](/vec-scalar/)
