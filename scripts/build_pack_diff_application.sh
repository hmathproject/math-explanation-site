#!/bin/bash
# build_pack_diff_application.sh — 微分・方程式不等式応用単元 パック PDF を生成する
#
# 使い方:
#   cd experiments/graph-guided-lessons/site
#   bash scripts/build_pack_diff_application.sh
#
# 出力: site/assets/pdf/diff-application-pack.pdf

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$SCRIPT_DIR/.."
ROOT="$SITE_DIR/.."

COVER="$ROOT/pdf/pack_cover_template.pdf"
P1="$ROOT/pdf/微分_方程式への微分応用_integrated_exp.pdf"
P2="$ROOT/pdf/微分_不等式への微分応用_integrated_exp.pdf"
OUT_DIR="$SITE_DIR/assets/pdf"
OUT="$OUT_DIR/diff-application-pack.pdf"

# 各 PDF の存在チェック
for f in "$COVER" "$P1" "$P2"; do
    if [ ! -f "$f" ]; then
        echo "[build_pack] エラー: $f が見つかりません。先にビルドしてください。"
        exit 1
    fi
done

mkdir -p "$OUT_DIR"

echo "[build_pack] 結合中..."
pdfunite "$COVER" "$P1" "$P2" "$OUT"

echo "[build_pack] 完了: $OUT"
python3 -c "
import subprocess
r = subprocess.run(['pdfinfo', '$OUT'], capture_output=True, text=True)
pages = [l for l in r.stdout.split('\n') if 'Pages' in l]
print('[build_pack]', pages[0] if pages else 'ページ数不明')
"
