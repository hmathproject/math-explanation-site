"""
gen_figures_coord_circle_equation.py — 円の方程式

Panel 1: 標準形: (x-a)²+(y-b)²=r²
Panel 2: 一般形→標準形: 平方完成

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_circle_equation.py
出力: site/figures/coord-circle-equation-combined.png
      site/assets/images/coord-circle-equation-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# ── フォント設定（CLAUDE.md 準拠）──────────────────────────────
if platform.system() == "Darwin":
    plt.rcParams["font.family"] = "Hiragino Sans"
elif platform.system() == "Windows":
    plt.rcParams["font.family"] = "MS Gothic"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["axes.unicode_minus"] = False

# ── 出力先 ──────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
FIGURES_DIR = BASE_DIR / "figures"
SITE_IMAGES_DIR = BASE_DIR / "assets" / "images"
FIGURES_DIR.mkdir(exist_ok=True)
SITE_IMAGES_DIR.mkdir(exist_ok=True)
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#bb6600"
GRAY = "#888888"
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_standard_form(ax):
    """Panel 1: 標準形: (x-a)²+(y-b)²=r²"""
    ax.set_xlim(-2.5, 5.5)
    ax.set_ylim(-1.5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(5.2, 0), xytext=(-2.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(5.25, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 5.3), xytext=(0, -1.3),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, 5.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.18, "O", ha="right", va="top", fontsize=9)

    # 円: 中心 (1, 2), 半径 3
    cx, cy, r = 1.0, 2.0, 3.0
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(cx + r * np.cos(theta), cy + r * np.sin(theta),
            color=DARK_BLUE, linewidth=2.2, zorder=3)

    # 中心マーク
    ax.plot(cx, cy, "o", color=DARK_BLUE, markersize=7, zorder=5)
    ax.text(cx + 0.15, cy + 0.15, r"$(1,\ 2)$", ha="left", va="bottom",
            fontsize=9.5, color=DARK_BLUE)

    # 半径の矢印（中心から右45°方向の点まで）
    angle = np.pi / 4
    ex = cx + r * np.cos(angle)
    ey = cy + r * np.sin(angle)
    ax.annotate("", xy=(ex, ey), xytext=(cx, cy),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6,
                                mutation_scale=10, shrinkA=4, shrinkB=0))
    ax.text((cx + ex) / 2 - 0.4, (cy + ey) / 2 + 0.2, r"$r=3$",
            ha="right", va="bottom", fontsize=9.5, color=RED)

    # 点 (ex, ey) にドット
    ax.plot(ex, ey, "o", color=RED, markersize=5, zorder=5)

    # 方程式ラベル
    ax.text(1.0, -1.1,
            r"$(x-1)^2 + (y-2)^2 = 9$",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.2))

    ax.set_title("標準形: $(x-a)^2+(y-b)^2=r^2$", fontsize=10, pad=4)


def draw_completing_square(ax):
    """Panel 2: 一般形→標準形: 平方完成"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    steps = [
        (r"$x^2+y^2-4x+2y-4=0$", "#f0f4ff", DARK_BLUE),
        (r"$(x^2-4x)+(y^2+2y)=4$", "#f8f4ff", ORANGE),
        (r"$(x^2-4x+4)+(y^2+2y+1)=4+4+1$", "#fff8f0", ORANGE),
        (r"$(x-2)^2+(y+1)^2=9$", "#f0fff4", GREEN),
        (r"中心 $(2,\ -1)$,\ 半径 $3$", "#fff0f0", RED),
    ]

    box_style_base = dict(boxstyle="round,pad=0.45", linewidth=1.3)
    y_positions = [7.0, 5.6, 4.2, 2.8, 1.4]

    prev_y = None
    for i, ((text, fc, ec), y_pos) in enumerate(zip(steps, y_positions)):
        bs = {**box_style_base, "facecolor": fc, "edgecolor": ec}
        ax.text(5.0, y_pos, text, ha="center", va="center",
                fontsize=10.5, color=ec,
                bbox=bs)
        if prev_y is not None:
            # 矢印を前のボックスから現在のボックスへ
            ax.annotate("", xy=(5.0, y_pos + 0.42),
                        xytext=(5.0, prev_y - 0.42),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        lw=1.3, mutation_scale=9,
                                        shrinkA=0, shrinkB=0))
        prev_y = y_pos

    # 平方完成の説明ラベル
    ax.text(7.8, 4.9, "各変数を\n平方完成",
            ha="center", va="center", fontsize=8.5, color=ORANGE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fffbe6",
                      edgecolor=ORANGE, linewidth=0.9))
    ax.annotate("", xy=(5.7, 4.9), xytext=(7.0, 4.9),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.0,
                                mutation_scale=7, shrinkA=4, shrinkB=4))

    ax.set_title("一般形 $\\to$ 標準形: 平方完成", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_standard_form(axes[0])
    draw_completing_square(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-circle-equation-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
