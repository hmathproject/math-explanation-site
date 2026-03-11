"""
gen_figures_coord_region_inequality.py — 不等式の表す領域

Panel 1: 直線の不等式: y > x+1 の領域
Panel 2: 円の不等式: x²+y²<9 の領域

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_region_inequality.py
出力: site/figures/coord-region-inequality-combined.png
      site/assets/images/coord-region-inequality-combined.png
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


def draw_linear_inequality(ax):
    """Panel 1: 直線の不等式: y > x+1 の領域"""
    ax.set_xlim(-4.0, 4.0)
    ax.set_ylim(-3.5, 5.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(3.8, 0), xytext=(-3.8, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(3.85, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 5.3), xytext=(0, -3.3),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, 5.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)

    x = np.linspace(-4.0, 4.0, 400)
    y_boundary = x + 1

    # 境界線（破線）
    ax.plot(x, y_boundary, color=DARK_BLUE, linewidth=2.0,
            linestyle="--", zorder=4, label=r"$y=x+1$（境界）")
    ax.text(2.2, 3.7, r"$y = x+1$", ha="left", va="center",
            fontsize=9.5, color=DARK_BLUE)

    # y > x+1 の領域（上方向）を塗る
    y_top = np.full_like(x, 5.5)
    ax.fill_between(x, y_boundary, y_top, alpha=0.25, color=DARK_BLUE,
                    zorder=2)

    # 領域ラベル
    ax.text(-2.5, 4.5, r"$y > x+1$" + "\nの領域",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0, alpha=0.9))

    # テスト点 (0, 3)
    ax.plot(0, 3, "o", color=RED, markersize=8, zorder=5)
    ax.text(0.2, 3.3, r"$(0,\ 3)$" + "\n$y=3 > 0+1$ ✓",
            ha="left", va="bottom", fontsize=8.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.9))

    # 境界は含まない説明
    ax.text(-3.8, -2.5,
            "境界線は含まない（破線）",
            ha="left", va="center", fontsize=8.5, color=GRAY,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor=GRAY, linewidth=0.7))

    ax.set_title("直線の不等式: $y > x+1$ の領域", fontsize=10, pad=4)


def draw_circle_inequality(ax):
    """Panel 2: 円の不等式: x²+y²<9 の領域"""
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(4.2, 0), xytext=(-4.2, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(4.25, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 4.2), xytext=(0, -4.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, 4.25, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)

    # 円 x²+y²=9 (r=3)
    r = 3.0
    theta = np.linspace(0, 2 * np.pi, 400)
    circle_x = r * np.cos(theta)
    circle_y = r * np.sin(theta)

    # 内部塗り（x²+y²<9）
    circle_patch = mpatches.Circle((0, 0), r, facecolor=DARK_BLUE,
                                   alpha=0.22, zorder=2)
    ax.add_patch(circle_patch)

    # 境界（破線）
    ax.plot(circle_x, circle_y, color=DARK_BLUE, linewidth=2.0,
            linestyle="--", zorder=4)
    ax.text(r * np.cos(np.pi / 4) + 0.15, r * np.sin(np.pi / 4) + 0.15,
            r"$x^2+y^2=9$", ha="left", va="bottom", fontsize=9, color=DARK_BLUE)

    # テスト点 (1, 1)
    ax.plot(1, 1, "o", color=RED, markersize=8, zorder=5)
    ax.text(1.2, 1.3, r"$(1,\ 1)$" + "\n$1+1=2 < 9$ ✓",
            ha="left", va="bottom", fontsize=8.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.9))

    # 半径ラベル
    ax.annotate("", xy=(r, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.2,
                                mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.text(1.5, -0.3, r"$r=3$", ha="center", va="top",
            fontsize=9, color=GRAY)

    # 境界は含まない説明
    ax.text(0, -4.0,
            "境界は含まない（破線）",
            ha="center", va="center", fontsize=8.5, color=GRAY,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor=GRAY, linewidth=0.7))

    ax.set_title(r"円の不等式: $x^2+y^2 < 9$ の領域", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_linear_inequality(axes[0])
    draw_circle_inequality(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-region-inequality-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
