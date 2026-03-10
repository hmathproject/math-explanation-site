# GROWTH_PLAN.md — サイト成長設計（運用版）

このファイルは `site/docs/` に置かれた運用文書です（Jekyll 公開対象外）。

最終更新: 2026-03-10（Phase 2a 完了後）

---

## 現状スコア

| 軸 | スコア | 状態 |
|---|---|---|
| A 情報設計 | ✅ 良好 | 階層3層・上下ナビ完備。単元間リンク補強済み（Phase 2a） |
| B SEO | ✅ 基盤整備済み | title/description/canonical/OGP/sitemap/robots 全対応 |
| C UX/デザイン | ✅ 対処済み | PDF CTA ボタン化・favicon.svg 設置済み |
| D コンテンツ戦略 | ⚠️ 未拡張 | 二次関数31ページのみ（Phase 3 で数IIへ拡張） |
| E 計測/改善基盤 | ⚠️ データ蓄積待ち | SC 登録済み・sitemap 送信済み。クエリデータは1〜2ヶ月後 |
| F マネタイズ設計 | ❌ 未構築 | Phase 4 以降で着手 |

---

## フェーズロードマップ

### ✅ Phase 1（完了: 2026-03-10）

- robots.txt 作成
- sitemap.xml 作成（Liquid テンプレート・gem 不使用）
- meta description を全31ページに追加
- canonical タグを全ページに追加
- title タグ重複修正（index のみ単独表示）
- SEO_GUIDELINES.md 作成

### ✅ Phase 1.5（完了: 2026-03-10）

- OGP タグ追加（og:title / og:description / og:url / og:type / og:site_name / og:locale）
- favicon.svg 配置（assets/favicon.svg）
- PDF CTA ボタン化（.pdf-btn CSS + 全30記事に適用）

### ✅ Phase 2a（完了: 2026-03-10）

- Search Console 登録・sitemap.xml 送信（ユーザー操作済み）
- 単元トップ3ページの → 次の単元 リンク補強
- description 誤記修正（quadratic-word-problems-geometry）
- SC 運用フローを WORKFLOW_WEB.md §8 に追記
- 小ページ候補を THEME_ROADMAP.md §6 に追記

### Phase 2b（Search Console データ確認後・1〜2ヶ月後）

前提: SC でクエリ・順位データが 1〜2ヶ月分溜まっていること

確認指標:
- **Impressions**: 表示回数（どの記事が検索に出ているか）
- **Clicks**: クリック数（流入が発生しているか）
- **CTR**: クリック率（title/description が刺さっているか）
- **Average Position**: 平均掲載順位（10位以内に入っているか）

実施内容:
- CTR が低い記事の title / meta description をクエリに最適化
- 流入記事から下位・関連記事への内部リンク強化
- 順位 11〜20 位の記事（2ページ目）を優先的に改善

### Phase 3（コンテンツ拡張）

- THEME_ROADMAP.md §6 の小ページ候補から制作着手
- 次カテゴリ候補: 積分（数II）面積計算（Tier 2 最優先）

### Phase 4（月間 3,000+ PV 到達後）

- メール収集フォーム設置（Formspree + Gmail 等）
- note / YouTube との往復導線
- アフィリエイトリンク

---

## ユーザー確認が必要な事項

| 事項 | 状態 |
|---|---|
| 公開 URL の確定 | `math-explanation-site-v2.pages.dev` を使用中。カスタムドメイン設定時は `_config.yml` の url を 1 行変更するだけで canonical / sitemap が追従 |
| GA4 設置の要否 | 未決定（Phase 2b 開始前に判断。CF Analytics で十分であれば不要） |

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
