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

### インライン数式の表記ルール（行の高さ・余白崩れを防ぐ）

| ルール | 正しい書き方 | 禁止 | 理由 |
|---|---|---|---|
| 分数はインラインでは `\frac` | `\\( \frac{1}{4} \\)` | `\\( \dfrac{1}{4} \\)` | `\dfrac` は行の高さを前後テキストより大きくする |
| 絶対値を含む式はインラインで書かない | display 数式 `<div>$$...$$</div>` に移動する | `\\( \lvert x \rvert \\)` または `\\( \|x\| \\)` | kramdown が `\|` を表組み区切りと誤解釈し `|` を削除する場合がある |
| 複雑な数式を箇条書き項目に直接埋め込まない | 箇条書き本文は自然文、数式を直後に display ブロックで表示 | 箇条書き内に `\frac`・`\lvert` 等を混在させる | 当該項目が他の項目より高くなり視覚的に不揃いになる |
| 単純な結果はインラインで表現 | `\\( S = 6 \\)` | `<div>$$\nS = 6\n$$</div>` | display 数式はフロー外の大きな余白を生む |
| 日本語は数式の外に書く | `共有点は \\( (-1,\ 1) \\) と \\( (3,\ 9) \\) です。` | `<div>$$\text{共有点}：...\$$</div>` | `\text{}` で日本語を display 数式に入れると読みにくい |

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

---

## §7 SEO front matter ルール（2026-03-10 追加）

新しいページの front matter には必ず `description:` を含める。

```yaml
---
layout: default
title: （記事タイトル）
permalink: /（ASCII-スラッグ）/
description: "（80〜120字の説明文）"
---
```

| ルール | 内容 |
|---|---|
| description の文字数 | 80〜120字 |
| キーワード含有 | タイトルと同じキーワードを自然に含める |
| index.md の title | 「トップページ」禁止。記述的な内容にする |
| canonical | `default.html` が自動出力（変更不要） |

詳細は **[docs/SEO_GUIDELINES.md](docs/SEO_GUIDELINES.md)** を参照。

---

## §8 Search Console 導入後の運用フロー（2026-03-10 追加）

### SC 登録後にやること（初回のみ）

1. SC 管理画面でプロパティを追加し、認証を完了する（ユーザー操作）
2. 「サイトマップ」から `https://math-explanation-site-v2.pages.dev/sitemap.xml` を送信する（ユーザー操作）
3. 認証メタタグが必要な場合は Claude Code に content 値を伝えて `default.html` に1行追加する

### 月次チェックの手順

Search Console 管理画面 → 「検索パフォーマンス」 で以下を確認する。

| 指標 | 見るべきポイント |
|---|---|
| **Impressions（表示回数）** | どの記事が検索に露出しているか。ゼロの記事はクロールされていない可能性 |
| **Clicks（クリック数）** | 流入が発生している記事を特定する |
| **CTR（クリック率）** | 3%未満 → title / description を改善する候補 |
| **Average Position（平均掲載順位）** | 11〜20 位（2ページ目）の記事は改善で1ページ目に上がりやすい |

### データ活用のタイミング

- データ蓄積 1〜2ヶ月後に Phase 2b を実施する
- 「どのクエリで露出しているか」を見て、title / description にそのキーワードを自然に含める
- CTR が特に低い記事（表示はされているがクリックされない）を優先的に改善する

### Claude Code に渡す情報の形式

Phase 2b で title / description を改善するとき、以下の形式でデータを渡すと効率よく作業できる：

```
記事URL: /quadratic-min-fixed-range/
上位クエリ: 「二次関数 最小値 場合分け」「最小値 固定区間 グラフ」
現状 CTR: 1.2%（低い）
現状 Average Position: 14.3
→ title / description にクエリを含める改善をしてほしい
```

---

## §9 記事品質の再発防止ルール（2026-03-10 追加）

### ルール1: 変数・記号は初出で必ず定義する

記事本文で数学記号や変数を使う場合、**最初に登場する文または直前の文で定義を与える**こと。

| 悪い例 | 良い例 |
|---|---|
| 「Step 1. \\( a \\) を括り出す」と唐突に登場 | 冒頭で「\\( y = ax^2 + bx + c \\)（\\( a \\) は \\( x^2 \\) の係数、\\( a \neq 0 \\)）」と示す |
| \\( p, q \\) が頂点形の途中から登場 | 「\\( y = a(x-p)^2 + q \\) の形（\\( p, q \\) は定数）にすると…」 |

特に **一般形の係数（\\( a, b, c \\)）・頂点形のパラメータ（\\( p, q \\)）・区間端点（\\( a, b, t \\) など）** は冒頭で定義する。

### ルール2: 図プレースホルダーのまま commit しない

`![...](/assets/images/XXX.png)` の行を書いた場合、**その commit の前に必ず PNG を生成して `assets/images/` に配置する**。

手順：
```bash
python scripts/gen_figures_XXX.py  # PNG を生成
git add assets/images/XXX.png      # PNG をステージング
# その後 .md ファイルとまとめて commit
```

「骨格だけ commit → PNG は次フェーズ」という分割は、本番に broken image が出るため禁止。
PNG が未完成の場合は、`<img>` タグ行自体を commit に含めない（コメントアウトも可）。

### ルール3: 新規ページ公開前チェックリスト

| 項目 | チェック内容 |
|---|---|
| 変数定義 | 本文で使う記号・文字は初出時点で定義されているか |
| 図の実体 | `assets/images/` に実 PNG が存在するか（placeholder ではないか） |
| 数式レンダリング | display 数式は `<div>$$...$$</div>` 形式になっているか |
| 内部リンク | 「この技術を使う記事」のリンク先が実際に存在するか |
| sitemap.xml | 新 URL が追加されているか |
| index.md | 新ページへのリンクが index.md に存在するか |

---

## §10 段階公開時の単元トップ管理ルール（2026-03-10 追加）

新規単元を記事を追加するたびに段階的に公開する場合、以下のルールを守る。

**「準備中」表記は放置しない**

単元トップ（`xxx-unit.md`）の記事リストに「準備中」と書いた項目は、対応する記事を追加した commit と**同じ commit** の中で実リンクに差し替える。「準備中」のまま merge しない。

**単元トップの学習順説明文も同時に更新する**

`## 解説記事` セクションの各記事見出し下の説明文を、準備中テキストから実際の内容説明（学習のポイント）に書き換える。学習順（1本目 → 2本目 → 3本目）の文脈が読めるよう、各記事の説明は前の記事の知識を前提とした形にする。
