# WORKFLOW_WEB.md — Web制作フロー運用文書

このファイルは `site/` リポジトリ内で Jekyll 公開対象から除外された運用文書です（`_config.yml: exclude: docs/`）。
チャットが変わった場合はまずこのファイルを読んでください。

---

## 役割分担

| 担当 | 役割 |
|---|---|
| **ChatGPT** | 内容設計・問題選定・数学的要件定義・記事構成の草案 |
| **Claude Code** | plan → 実装 → git push まで一貫して担当 |
| **ユーザー** | 公開後の最終確認（表示・数式・ナビゲーション） |

Claude Code は原則として push まで実施する。確認待ちで止まらない。

---

## 基本フロー（1単元・1記事追加の標準）

```
1. plan mode で設計を提示
2. ユーザーが "accept" → 実装開始
3. ファイル作成 / 編集
4. 図が必要なら scripts/gen_figures_qN.py を実行して PNG 生成
5. git add → git commit → git push
6. Cloudflare Pages が自動デプロイ
7. ユーザーが公開ページを確認してフィードバック
```

---

## 新規記事追加の標準手順

### 1. テンプレートを選ぶ

既存記事を必ずコピーして作る。問の種類に近い既存記事を選ぶ。

| 問題種別 | 参照テンプレート |
|---|---|
| 最小値・3ケース | `quadratic-min-moving-range.md` |
| 最大値・2ケース | `quadratic-max-moving-range.md` |

### 2. front matter

```yaml
---
layout: default
title: （記事タイトル）
permalink: /（ASCII-slug）/
---
```

- `permalink` は ASCII のみ（日本語不可）
- 末尾スラッシュ付き `/page-name/` — Cloudflare Pages の pretty URL 形式
- `layout: default` を必ず指定する

### 3. ファイル名

- ファイル名 = permalink のスラッグ + `.md`
- 例: permalink `/quadratic-max-moving-range/` → ファイル名 `quadratic-max-moving-range.md`
- 日本語ファイル名は使わない

### 4. 内部リンク

すべて絶対パスで記述する。

```markdown
[単元トップへ](/)
[次の記事](/quadratic-max-moving-range/)
[PDFをダウンロード](/assets/pdf/quadratic-max-min-pack.pdf)
[図](/assets/images/quadratic-max-moving-range-combined.png)
```

相対パス（`./assets/...`）は記事ページが `/page-name/` になったとき `/page-name/assets/...` に解釈されて壊れる。

### 5. ナビゲーション形式

```
← [単元トップへ：タイトル](/)　／　← [前の記事：タイトル](/prev-slug/)
（上部）

---
（本文）
---

← [単元トップへ：タイトル](/)

→ [次の記事：タイトル](/next-slug/)
（下部）
```

- 最初の記事（Q1）は上部に `← top` のみ（← prev 不要）
- 最後の記事は下部に `← top` のみ（→ next 不要）
- 各記事の下部に必ず `← top` を置く（Q1含む）

### 6. 数式の書き方

| 種別 | 書き方 |
|---|---|
| インライン | `\\( ... \\)` — 二重バックスラッシュ必須 |
| ディスプレイ | `<div>\n$$\n...\n$$\n</div>` |

インラインで `\(` 1本では kramdown が `\` を消費して MathJax に届かない。
ディスプレイ数式を `$$...$$` のみで書くと kramdown がブロック処理するため `<div>` で囲む。

場合分け（cases 環境）の例：
```html
<div>
$$
\text{最小値} =
\begin{cases}
a^2 + 1 & (a \leq 0) \\[4pt]
1 & (0 < a < 1) \\[4pt]
(a-1)^2 + 1 & (a \geq 1)
\end{cases}
$$
</div>
```

---

## 図生成の標準手順

### スクリプトの場所

`site/scripts/gen_figures_qN.py`（Jekyll 公開対象外）

### 実行方法

```bash
cd site/
python scripts/gen_figures_qN.py
```

出力は自動で 2箇所に書き出される：
- `site/figures/（ファイル名）.png` — 作業用
- `site/assets/images/（ファイル名）.png` — サイト公開用（こちらが本番）

### 新規スクリプト作成

1. 直近の問と同種のスクリプトをコピーする
   - 3ケース → `gen_figures_q3.py` をコピー（figsize=(13.5, 4.0)）
   - 2ケース → `gen_figures_q4.py` をコピー（figsize=(9.0, 4.0)）
2. `CASES` リストを変更（代表値・区間・最大/最小点・タイトル）
3. 出力ファイル名 `fname` を変更
4. 関数 `f()` が変わる問では `f()` も変更する

### matplotlib フォント設定

スクリプト冒頭に必ず含める（CLAUDE.md 準拠）：

```python
import platform
if platform.system() == "Darwin":
    plt.rcParams["font.family"] = "Hiragino Sans"
elif platform.system() == "Windows":
    plt.rcParams["font.family"] = "MS Gothic"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["axes.unicode_minus"] = False
```

---

## index.md 単元説明文の標準書式

### 基本形

新テーマを index.md に追加するとき、単元説明文は必ず以下の書式で統一する。

```markdown
### [テーマ名](/slug/)

キャッチコピー（全N記事・解説PDF付き）
```

### 状態別バリエーション

| 状態 | 書式 |
|---|---|
| PDF 公開済み | `（全N記事・解説PDF付き）` |
| PDF 未完成 | `（全N記事・解説PDF準備中）` |
| 記事制作中 | `（全N記事・順次公開中）` |

### 新テーマ公開時のチェック

index.md の単元説明文更新は、記事本文・PDF 配置と**同じ commit** に含める。
「記事は公開したが index.md の書式が旧いまま」を防ぐために、
公開 commit の前に必ず index.md の当該行を確認する。

---

## 公開後点検の標準手順

### 数学的内容

- 境界値で場合が一致することを確認
  - 例: 3ケースなら境界 a=a₁ で①②一致、a=a₂ で②③一致
- 頂点・端点・場合分け条件の符号を再確認

### ナビゲーション

- 各記事の上部・下部リンクを確認（断絶がないこと）
- Q1 下部に `← top` があること（よくある漏れ）
- 全記事が index.md からリンクされていること
- **index.md の単元説明文が統一書式になっているか**（`全N記事・解説PDF付き` / `準備中` のいずれか）

### 表示・レンダリング

- 図が表示されていること（broken image になっていないこと）
- MathJax が数式をレンダリングしていること（特に cases 環境）
- PDF ダウンロードリンクが動作すること

---

## git 運用方針

- git リポジトリルート = `site/`
- Cloudflare Pages が `site/` を自動デプロイ（push 後数十秒で反映）
- commit メッセージは日本語でよい（例: `記事Q4を追加`）
- Claude Code は confirm なしで push まで実施する（ユーザーが明示的に止めない限り）

```bash
cd /Users/harahisato/tutor-math/experiments/graph-guided-lessons/site
git add -A
git commit -m "（変更内容）"
git push
```

---

## 成功例：二次関数単元（Q1〜Q4）

| ファイル | 内容 |
|---|---|
| `index.md` | 単元トップ（4記事リンク + PDF案内） |
| `quadratic-min-fixed-range.md` | 問1: 最小値・固定区間・軸が動く（3ケース） |
| `quadratic-max-fixed-range.md` | 問2: 最大値・固定区間・軸が動く（2ケース） |
| `quadratic-min-moving-range.md` | 問3: 最小値・動く区間・軸が固定（3ケース） |
| `quadratic-max-moving-range.md` | 問4: 最大値・動く区間・軸が固定（2ケース） |
| `scripts/gen_figures_q3.py` | 問3用図生成（3ケース横並び） |
| `scripts/gen_figures_q4.py` | 問4用図生成（2ケース横並び） |
| `assets/images/` | 4問分の方針図 PNG |
| `assets/pdf/` | 4問パック解説 PDF |

この単元で確立したパターン（front matter / permalink / 数式記法 / 図生成 / ナビゲーション）が
次単元でも再利用できる標準フォーマットになっている。

---

## PDF制作標準

サイト向け PDF の制作標準（integrated_exp フォーマット・ビルド手順・記法ルール）は以下を参照。

**[docs/PDF_STANDARD.md](docs/PDF_STANDARD.md)**

---

## 図設計自立判定ルール

テーマ骨格を作る前に `docs/FIGURE_DESIGN.md` の判定フロー（§1）を実行する。
図必須と判定したテーマでは、骨格段階で図設計メモ・スクリプト命名・placeholder まで出す。

**[docs/FIGURE_DESIGN.md](docs/FIGURE_DESIGN.md)**

---

## テーマ体系・制作ロードマップ

公開テーマの全体像・粒度基準・制作優先順位（Tier 1〜3）は以下を参照。

**[docs/THEME_ROADMAP.md](docs/THEME_ROADMAP.md)**

---

## _layouts/default.html の現状

MathJax 設定・CSS の要点：

```html
<script>
  window.MathJax = {
    tex: {
      inlineMath:  [['\\(', '\\)'], ['$', '$']],
      displayMath: [['\\[', '\\]'], ['$$', '$$']]
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
    }
  };
</script>
```

CSS:
```css
body { max-width: 720px; margin: 2rem auto; padding: 0 1rem; font-family: sans-serif; line-height: 1.7; }
img  { max-width: 100%; height: auto; display: block; margin: 1.5rem auto; }
hr   { border: none; border-top: 1px solid #e5e7eb; margin: 1.5rem 0; }
a    { color: #2563eb; }
```
