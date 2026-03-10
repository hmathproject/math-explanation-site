# SEO_GUIDELINES.md — SEO 実装ガイドライン

このファイルは `site/docs/` に置かれた運用文書です（Jekyll 公開対象外）。

---

## front matter テンプレート

新しいページを作成するときは必ず以下の形式で front matter を記述する。

```yaml
---
layout: default
title: （検索クエリを含む記述的なタイトル）
permalink: /（ASCII-スラッグ）/
description: "（80〜120字の説明文。キーワードを含み、内容が一目でわかること）"
---
```

---

## description 作成ルール

| ルール | 内容 |
|---|---|
| 文字数 | 80〜120字を目標（短すぎると Google が書き換える。長すぎると切れる） |
| キーワード含有 | タイトルと同じキーワードを自然な文で含める |
| 禁止 | タイトルの単純な繰り返し・「〜のページです」という無意味な表現 |
| 末尾 | 「〜で解説します。」など行動を示す文で締める |

### 良い description の例

```
固定区間で軸が動く二次関数の最小値を、軸の位置による3ケースに分けてグラフと場合分けで解説します。
```

### 悪い description の例

```
二次関数の最小値（固定区間）について説明しているページです。  ← 無意味
```

---

## canonical タグ

`default.html` に組み込み済み（2026-03-10）:

```html
<link rel="canonical" href="{{ page.url | absolute_url }}">
```

- `_config.yml` の `url:` フィールドが正確な公開 URL に一致していること
- カスタムドメインに変更したら `_config.yml` の `url:` を 1 行変更するだけで全ページに反映される

---

## title タグ

`default.html` のロジック（2026-03-10 修正済み）:

```html
{% if page.url == "/" %}
  <title>{{ page.title }}</title>
{% else %}
  <title>{{ page.title }} | {{ site.title }}</title>
{% endif %}
```

- index.md は `page.title` のみ（サイト名との重複を防ぐ）
- 各記事は `記事タイトル | 高校数学 解説サイト` 形式

index.md の title は **記述的な内容**にすること:

```yaml
title: 高校数学 解説サイト — 二次関数をグラフで理解する  ← OK
title: 高校数学 解説サイト                               ← サイト名と同じになるので非推奨
title: トップページ                                       ← 禁止（検索結果で意味が伝わらない）
```

---

## sitemap.xml

`jekyll-sitemap` プラグインで自動生成（2026-03-10 導入）。

- `_config.yml` の `url:` フィールドを正確に設定すること
- デプロイ後 `/sitemap.xml` にアクセスして確認できる
- Search Console に登録後、sitemap.xml の URL を送信する

robots.txt にも sitemap の URL を記載済み:

```
Sitemap: https://math-explanation-site-v2.pages.dev/sitemap.xml
```

---

## Search Console 登録手順（ユーザー操作が必要）

1. https://search.google.com/search-console/ でプロパティを追加
2. URL プレフィックス方式: `https://math-explanation-site-v2.pages.dev/`
3. HTML ファイル認証 or `default.html` への meta タグ挿入で認証
4. サイトマップに `/sitemap.xml` を送信

認証 meta タグを使う場合は `default.html` の `<head>` に:
```html
<meta name="google-site-verification" content="（認証コード）">
```

---

## 構造化データ（Phase 2 以降で検討）

| ページ種別 | 検討スキーマ | 備考 |
|---|---|---|
| サイトトップ（/） | WebSite + SearchAction | Googleサイトリンク検索ボックス用 |
| 個別記事 | Article | クローラーへのコンテンツ種別明示 |

**今はまだ実装しない**: Phase 1 の SEO 基盤が定着し、Search Console でデータが蓄積してから着手する。
FAQ・HowTo スキーマは本サイトのコンテンツ形式と合わないため使用しない。
