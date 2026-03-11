"""
gen_figures_coord_line_relation.py — 直線の平行・垂直条件

Panel 1: 平行: 傾きが等しい
Panel 2: 垂直: 傾きの積 = -1

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_line_relation.py
出力: site/figures/coord-line-relation-combined.png
      site/assets/images/coord-line-relation-combined.png
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


def draw_parallel(ax):
    """Panel 1: 平行: 傾きが等しい"""
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-4.0, 5.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(3.3, 0), xytext=(-3.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(3.35, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 5.2), xytext=(0, -3.8),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, 5.25, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.2, "O", ha="right", va="top", fontsize=9)

    x = np.linspace(-3.0, 1.8, 300)

    # y = 2x + 3 (DARK_BLUE)
    y1 = 2 * x + 3
    ax.plot(x, y1, color=DARK_BLUE, linewidth=2.0, zorder=3)
    ax.text(0.9, 4.8, r"$y=2x+3$", ha="left", va="center",
            fontsize=9, color=DARK_BLUE)

    # y = 2x - 1 (RED)
    y2 = 2 * x - 1
    ax.plot(x, y2, color=RED, linewidth=2.0, zorder=3)
    ax.text(1.9, 3.5, r"$y=2x-1$", ha="left", va="center",
            fontsize=9, color=RED)

    # 等間隔を示す両矢印
    xm = -1.0
    y1m = 2 * xm + 3
    y2m = 2 * xm - 1
    ax.annotate("", xy=(xm, y2m), xytext=(xm, y1m),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.4,
                                mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.text(xm + 0.12, (y1m + y2m) / 2, "等間隔", ha="left", va="center",
            fontsize=8.5, color=GREEN)

    # 注釈テキスト
    ax.text(-3.3, -2.0,
            "$m_1 = m_2 = 2$\n$n_1 \\neq n_2$（$3 \\neq -1$）",
            ha="left", va="top", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.2))

    ax.set_title("平行: 傾きが等しい", fontsize=10, pad=4)


def draw_perpendicular(ax):
    """Panel 2: 垂直: 傾きの積 = -1"""
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-3.0, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.8, 0), xytext=(-2.8, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.85, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 2.8), xytext=(0, -2.8),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, 2.85, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.18, "O", ha="right", va="top", fontsize=9)

    x = np.linspace(-2.5, 2.5, 400)

    # y = 2x (DARK_BLUE)
    ax.plot(x, 2 * x, color=DARK_BLUE, linewidth=2.0, zorder=3)
    ax.text(1.05, 2.4, r"$y=2x$", ha="left", va="center",
            fontsize=9.5, color=DARK_BLUE)

    # y = -0.5x (RED)
    ax.plot(x, -0.5 * x, color=RED, linewidth=2.0, zorder=3)
    ax.text(1.8, -1.2, r"$y=-\frac{1}{2}x$", ha="left", va="center",
            fontsize=9.5, color=RED)

    # 原点に 90° 角のマーク（小さい正方形）
    # 2つの単位方向ベクトル: v1 = (1,2)/sqrt(5), v2 = (2,-1)/sqrt(5)
    s = 0.28
    v1 = np.array([1, 2]) / np.sqrt(5)
    v2 = np.array([2, -1]) / np.sqrt(5)
    square = np.array([
        [0, 0],
        s * v1,
        s * v1 + s * v2,
        s * v2,
        [0, 0]
    ])
    ax.plot(square[:, 0], square[:, 1], color=GREEN, linewidth=1.5, zorder=4)

    # 注釈テキスト
    ax.text(-2.9, -1.8,
            "$m_1 \\times m_2$\n$= 2 \\times (-\\frac{1}{2})$\n$= -1$",
            ha="left", va="top", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.2))

    ax.set_title("垂直: 傾きの積 $= -1$", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_parallel(axes[0])
    draw_perpendicular(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-line-relation-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
