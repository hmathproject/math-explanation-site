"""
gen_figures_coord_line_equation.py — 直線の方程式

Panel 1: 傾き-切片形 y = mx + n
Panel 2: 垂直線 x = a（傾き未定義）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_line_equation.py
出力: site/figures/coord-line-equation-combined.png
      site/assets/images/coord-line-equation-combined.png
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


def draw_slope_intercept(ax):
    """Panel 1: 傾き-切片形 y = mx + n"""
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(3.3, 0), xytext=(-3.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(3.35, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 5.3), xytext=(0, -3.3),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, 5.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.2, "O", ha="right", va="top", fontsize=9)

    # y = 2x + 1 を描画
    x = np.linspace(-2.0, 2.0, 300)
    y = 2 * x + 1
    ax.plot(x, y, color=DARK_BLUE, linewidth=2.2, zorder=3)

    # y切片 (0, 1) のマーク
    ax.plot(0, 1, "o", color=DARK_BLUE, markersize=7, zorder=4)
    ax.text(0.12, 1.0, r"$(0,\ 1)$", ha="left", va="center", fontsize=9, color=DARK_BLUE)

    # 傾きを示す直角三角形: 点 (0.5, 2) を基点に Δx=1, Δy=2
    bx, by = 0.5, 2.0
    ax.annotate("", xy=(bx + 1.0, by), xytext=(bx, by),
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.5))
    ax.annotate("", xy=(bx + 1.0, by + 2.0), xytext=(bx + 1.0, by),
                arrowprops=dict(arrowstyle="-", color=RED, lw=1.5))
    ax.annotate("", xy=(bx + 1.0, by + 2.0), xytext=(bx, by),
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8, linestyle="dashed"))

    ax.text(bx + 0.5, by - 0.25, r"$\Delta x=1$", ha="center", va="top",
            fontsize=8.5, color=ORANGE)
    ax.text(bx + 1.15, by + 1.0, r"$\Delta y=2$", ha="left", va="center",
            fontsize=8.5, color=RED)

    # 注釈テキスト
    ax.text(-3.2, 4.8,
            "傾き $m = 2$\n切片 $n = 1$",
            ha="left", va="top", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.2))

    # 式ラベル
    ax.text(1.6, 4.2, r"$y = 2x+1$", ha="left", va="center",
            fontsize=10, color=DARK_BLUE)

    ax.set_title("傾き-切片形 $y = mx + n$", fontsize=10, pad=4)


def draw_vertical_line(ax):
    """Panel 2: 垂直線 x = a（傾き未定義）"""
    ax.set_xlim(-2.5, 5.5)
    ax.set_ylim(-3.5, 4.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(5.2, 0), xytext=(-2.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(5.25, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 4.3), xytext=(0, -3.3),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, 4.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.2, "O", ha="right", va="top", fontsize=9)

    # 参考: y = x + 1（DARK_BLUE）
    x_c = np.linspace(-2.0, 3.0, 300)
    ax.plot(x_c, x_c + 1, color=DARK_BLUE, linewidth=1.8, label=r"$y=x+1$")
    ax.text(2.6, 3.8, r"$y = x+1$", ha="left", va="center",
            fontsize=9, color=DARK_BLUE)

    # 垂直線 x = 3（RED）
    ax.plot([3, 3], [-3.0, 4.0], color=RED, linewidth=2.4, zorder=3)
    ax.text(3.12, -2.5, r"$x = 3$", ha="left", va="center",
            fontsize=10, color=RED)

    # 注釈
    ax.text(0.3, -2.8,
            "傾き $m$ は定義されない\n（$\\Delta x = 0$ で除算不可）",
            ha="left", va="bottom", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=1.0))

    # 一般形の表示
    ax.text(-2.2, 3.8,
            "一般形: $ax + by + c = 0$",
            ha="left", va="top", fontsize=9, color=GRAY,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor=GRAY, linewidth=0.8))

    ax.set_title("垂直線 $x = a$（傾き未定義）", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_slope_intercept(axes[0])
    draw_vertical_line(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-line-equation-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
