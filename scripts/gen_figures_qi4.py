"""
gen_figures_qi4.py — 記事4用概念図（数直線図）
連立二次不等式の解を数直線3段で示す
  ①: -2 < x < 3
  ②:  1 < x < 4
  共通部分: 1 < x < 3

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qi4.py
出力: site/assets/images/quadratic-inequality-system-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if platform.system() == "Darwin":
    plt.rcParams["font.family"] = "Hiragino Sans"
elif platform.system() == "Windows":
    plt.rcParams["font.family"] = "MS Gothic"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["axes.unicode_minus"] = False

BASE_DIR = Path(__file__).parent.parent
FIGURES_DIR = BASE_DIR / "figures"
SITE_IMAGES_DIR = BASE_DIR / "assets" / "images"
FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150

# 数直線の表示範囲
X_LO, X_HI = -3.5, 5.5

# 数直線の3行と各行の y 座標（上から順）
ROWS = [
    {
        "y": 2.2,
        "label": r"①: $x^2-x-6<0$",
        "interval": (-2.0, 3.0),
        "color": "#2563eb",   # 青
    },
    {
        "y": 1.1,
        "label": r"②: $x^2-5x+4<0$",
        "interval": (1.0, 4.0),
        "color": "#16a34a",   # 緑
    },
    {
        "y": 0.0,
        "label": r"共通部分",
        "interval": (1.0, 3.0),
        "color": "#d97706",   # 橙（解の色に統一）
    },
]

# 解の式ラベル（行右側に表示）
ROW_ANSWERS = [
    r"$-2 < x < 3$",
    r"$1 < x < 4$",
    r"$1 < x < 3$",
]

# 数直線上にラベルを打つ x 座標
TICK_XS = [-2.0, 1.0, 3.0, 4.0]
TICK_LABELS = [r"$-2$", r"$1$", r"$3$", r"$4$"]


def main() -> None:
    fig, ax = plt.subplots(figsize=(8.0, 3.2))
    fig.patch.set_facecolor("white")
    ax.set_xlim(X_LO - 0.3, X_HI + 2.0)
    ax.set_ylim(-0.7, 3.0)
    ax.axis("off")

    arrow_kw = dict(color="#888888", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    tick_h = 0.10   # 目盛りの高さ

    for row, ans_lbl in zip(ROWS, ROW_ANSWERS):
        y = row["y"]
        lo, hi = row["interval"]
        color = row["color"]

        # 数直線本体（灰色）
        ax.annotate("", xy=(X_HI + 0.1, y), xytext=(X_LO - 0.05, y),
                    arrowprops=dict(arrowstyle="-|>", **arrow_kw))

        # 解区間（太い色付き線分）
        ax.plot([lo, hi], [y, y],
                color=color, linewidth=4.5, solid_capstyle="butt", zorder=3)

        # 端点マーカー（strict → open circle）
        for xv in [lo, hi]:
            ax.plot(xv, y, "o", color="white", markeredgecolor=color,
                    markersize=7, markeredgewidth=2.0, zorder=4)

        # 行ラベル（左端）
        ax.text(X_LO - 0.15, y, row["label"],
                ha="right", va="center", fontsize=9, color="black")

        # 解の式ラベル（右端）
        ax.text(X_HI + 0.2, y, ans_lbl,
                ha="left", va="center", fontsize=9, color=color, fontweight="bold")

    # 共通のx軸ラベル（最下段の数直線の下）
    y_tick = ROWS[-1]["y"]
    lbl_bbox = dict(boxstyle="square,pad=0.04", facecolor="white", edgecolor="none")
    for xv, lbl in zip(TICK_XS, TICK_LABELS):
        # 全行に目盛り（最下段のみラベル付き）
        for row in ROWS:
            ax.plot([xv, xv], [row["y"] - tick_h, row["y"] + tick_h],
                    color="#888888", linewidth=0.8, zorder=2)
        # ラベルは最下段の下に
        ax.text(xv, y_tick - 0.22, lbl,
                ha="center", va="top", fontsize=9, bbox=lbl_bbox, zorder=5)

    # 共通部分の強調（薄い縦帯で x=1〜3 を示す）
    ax.fill_betweenx(
        [ROWS[0]["y"] - 0.15, ROWS[2]["y"] + 0.15],
        1.0, 3.0,
        color="#fef3c7", zorder=1, alpha=0.7
    )

    fig.tight_layout(pad=0.3)

    fname = "quadratic-inequality-system-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    out_site = SITE_IMAGES_DIR / fname
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
