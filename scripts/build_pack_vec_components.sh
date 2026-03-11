#!/bin/bash
# build_pack_vec_components.sh — ベクトル・成分と演算単元 パック PDF を生成する
#
# 使い方:
#   cd experiments/graph-guided-lessons/site
#   bash scripts/build_pack_vec_components.sh
#
# 出力: site/assets/pdf/vec-components-pack.pdf

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$SCRIPT_DIR/.."
ROOT="$SITE_DIR/.."

COVER="$ROOT/pdf/pack_cover_template.pdf"
P1="$ROOT/pdf/ベクトル_成分表示と大きさ_integrated_exp.pdf"
P2="$ROOT/pdf/ベクトル_成分による演算_integrated_exp.pdf"
P3="$ROOT/pdf/ベクトル_1次結合と分解_integrated_exp.pdf"
OUT_DIR="$SITE_DIR/assets/pdf"
OUT="$OUT_DIR/vec-components-pack.pdf"

# 各 PDF の存在チェック
for f in "$COVER" "$P1" "$P2" "$P3"; do
    if [ ! -f "$f" ]; then
        echo "[build_pack] エラー: $f が見つかりません。先にビルドしてください。"
        exit 1
    fi
done

mkdir -p "$OUT_DIR"

echo "[build_pack] 結合中..."
pdfunite "$COVER" "$P1" "$P2" "$P3" "$OUT"

echo "[build_pack] 完了: $OUT"
python3 -c "
import subprocess
r = subprocess.run(['pdfinfo', '$OUT'], capture_output=True, text=True)
pages = [l for l in r.stdout.split('\n') if 'Pages' in l]
print('[build_pack]', pages[0] if pages else 'ページ数不明')
"
