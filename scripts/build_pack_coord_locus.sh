#!/bin/bash
# build_pack_coord_locus.sh — 図形と方程式・軌跡単元 パック PDF を生成する
#
# 使い方:
#   cd experiments/graph-guided-lessons/site
#   bash scripts/build_pack_coord_locus.sh
#
# 出力: site/assets/pdf/coord-locus-pack.pdf

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$SCRIPT_DIR/.."
ROOT="$SITE_DIR/.."

COVER="$ROOT/pdf/pack_cover_template.pdf"
P1="$ROOT/pdf/図形と方程式_軌跡の概念_integrated_exp.pdf"
P2="$ROOT/pdf/図形と方程式_軌跡の求め方_integrated_exp.pdf"
OUT_DIR="$SITE_DIR/assets/pdf"
OUT="$OUT_DIR/coord-locus-pack.pdf"

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
