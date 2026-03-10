# GROWTH_PLAN.md — サイト成長設計（運用版）

このファイルは `site/docs/` に置かれた運用文書です（Jekyll 公開対象外）。

---

## 現状スコア

| 軸 | スコア | 主な問題 |
|---|---|---|
| A 情報設計 | ✅ 良好 | 階層3層・上下ナビ完備 |
| B SEO | ⚠️ 基盤整備済み（2026-03-10） | title/description/canonical/sitemap/robots 対応完了 |
| C UX/デザイン | ⚠️ 改善余地 | PDF CTA が地味・ファビコンなし（Phase 1.5 で対処） |
| D コンテンツ戦略 | ⚠️ 未拡張 | 二次関数31ページのみ（Phase 3 で数IIへ拡張） |
| E 計測/改善基盤 | ⚠️ Search Console 未接続 | CF Analytics 有効。SC 登録はユーザー操作が必要 |
| F マネタイズ設計 | ❌ 未構築 | Phase 4 以降で着手 |

---

## フェーズロードマップ

### Phase 1（完了: 2026-03-10）
- robots.txt 作成
- jekyll-sitemap 導入（sitemap.xml 自動生成）
- meta description を全31ページに追加
- canonical タグを全ページに追加
- title タグ重複修正（index のみ単独表示）
- SEO_GUIDELINES.md 作成

### Phase 1.5（次セッション）
- OGP タグ追加（og:title / og:description / og:url / og:type）
- favicon 配置
- PDF CTA ボタン化（.pdf-btn CSS）

### Phase 2（Search Console データ確認後・1〜3ヶ月後）
前提: SC でクエリ・順位データが 1〜2ヶ月分溜まっていること

- title / meta description をクエリに最適化
- 流入記事から下位記事への内部リンク強化
- GA4 設置 + PDF DL クリックイベント計測
- ANALYTICS_SETUP.md 作成

### Phase 3（コンテンツ拡張）
- 数II カテゴリ第1弾（積分・面積）着手
- ロングテール記事追加

### Phase 4（月間 3,000+ PV 到達後）
- メール収集フォーム設置（PDF ゲート化は任意）
- note / YouTube との往復導線
- アフィリエイトリンク

---

## ユーザー確認が必要な事項

| 事項 | 状態 | リスク |
|---|---|---|
| 公開 URL の確定 | `math-explanation-site-v2.pages.dev` を使用中 | カスタムドメイン設定時は `_config.yml` の url を 1 行変更するだけで canonical / sitemap が追従する |
| Search Console 登録 | 未実施（ユーザー操作が必要） | — |
| GA4 設置の要否 | 未決定（Phase 2 で判断） | — |

---

## マネタイズ導線（将来設計）

```
無料記事 → 無料 PDF（リード獲得）
               ↓（Phase 4 以降）
          メール登録 → 新テーマ通知
               ↓
          プレミアム PDF（¥500〜¥980 / テーマ）
               ↓
          年間パス（¥3,980 / 年）
```

Phase 4 着手条件: 月間 3,000 PV 以上 + PDF DL 計測データあり
