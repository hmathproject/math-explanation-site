"""
gen_figures_coord_region_system.py — 連立不等式の領域

Panel 1: 各不等式の領域
Panel 2: 連立不等式 → 共通部分

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_region_system.py
出力: site/figures/coord-region-system-combined.png
      site/assets/images/coord-region-system-combined.png
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


def _draw_axes(ax, xlim, ylim):
    """共通の座標軸描画ヘルパー"""
    ax.annotate("", xy=(xlim[1] * 0.95, 0), xytext=(xlim[0] * 0.95, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xlim[1] * 0.97, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, ylim[1] * 0.95), xytext=(0, ylim[0] * 0.95),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, ylim[1] * 0.97, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)


def draw_individual_regions(ax):
    """Panel 1: 各不等式の領域"""
    ax.set_xlim(-0.8, 5.5)
    ax.set_ylim(-0.8, 5.5)
    ax.axis("off")

    _draw_axes(ax, (-0.8, 5.5), (-0.8, 5.5))

    x = np.linspace(-0.5, 5.2, 400)
    y_max = 5.2

    # 不等式1: x+y ≤ 4  → y ≤ 4-x  (DARK_BLUE)
    y_ineq1 = 4 - x
    ax.plot(x, y_ineq1, color=DARK_BLUE, linewidth=1.8, zorder=4)
    ax.fill_between(x, np.zeros_like(x), np.minimum(y_ineq1, y_max),
                    where=(y_ineq1 >= 0),
                    alpha=0.15, color=DARK_BLUE, zorder=2)
    ax.text(0.3, 4.5, r"$x+y \leq 4$", ha="left", va="center",
            fontsize=9, color=DARK_BLUE)

    # 不等式2: x ≥ 0 (RED)
    ax.plot([0, 0], [-0.5, 5.2], color=RED, linewidth=1.8, zorder=4)
    ax.fill_betweenx(np.linspace(-0.5, 5.2, 200),
                     np.zeros(200), np.full(200, 5.2),
                     alpha=0.12, color=RED, zorder=1)
    ax.text(0.3, 0.3, r"$x \geq 0$", ha="left", va="bottom",
            fontsize=9, color=RED)

    # 不等式3: y ≥ 0 (GREEN)
    ax.plot([-0.5, 5.2], [0, 0], color=GREEN, linewidth=1.8, zorder=4)
    ax.fill_between(np.linspace(-0.5, 5.2, 200),
                    np.zeros(200), np.full(200, 5.2),
                    alpha=0.10, color=GREEN, zorder=1)
    ax.text(4.5, 0.2, r"$y \geq 0$", ha="right", va="bottom",
            fontsize=9, color=GREEN)

    ax.set_title("各不等式の領域（半平面）", fontsize=10, pad=4)


def draw_intersection_region(ax):
    """Panel 2: 連立不等式 → 共通部分"""
    ax.set_xlim(-0.8, 5.5)
    ax.set_ylim(-0.8, 5.5)
    ax.axis("off")

    _draw_axes(ax, (-0.8, 5.5), (-0.8, 5.5))

    x = np.linspace(0, 4.0, 400)

    # 3本の境界線を描く
    x_full = np.linspace(-0.5, 5.2, 400)
    ax.plot(x_full, 4 - x_full, color=DARK_BLUE, linewidth=1.8, zorder=4)
    ax.plot([0, 0], [-0.5, 5.2], color=RED, linewidth=1.8, zorder=4)
    ax.plot([-0.5, 5.2], [0, 0], color=GREEN, linewidth=1.8, zorder=4)

    # 共通部分（三角形領域）を塗る: x≥0, y≥0, x+y≤4
    x_tri = np.linspace(0, 4, 400)
    y_upper = 4 - x_tri
    ax.fill_between(x_tri, np.zeros_like(x_tri), y_upper,
                    alpha=0.45, color=ORANGE, zorder=3)

    # 頂点のマーク
    vertices = [(0, 0), (4, 0), (0, 4)]
    v_labels = [r"$(0,0)$", r"$(4,0)$", r"$(0,4)$"]
    v_offsets = [(-0.2, -0.3), (0.15, -0.3), (-0.2, 0.2)]
    for (vx, vy), lab, (ox, oy) in zip(vertices, v_labels, v_offsets):
        ax.plot(vx, vy, "o", color=DARK_BLUE, markersize=8, zorder=6)
        ax.text(vx + ox, vy + oy, lab, ha="center", va="center",
                fontsize=9, color=DARK_BLUE)

    # 解領域ラベル
    ax.text(1.2, 1.2, "共通部分\n= 解領域",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fffbe6",
                      edgecolor=ORANGE, linewidth=1.2))

    # 連立不等式ラベル
    ax.text(3.0, 4.5,
            "$x+y \\leq 4$\n$x \\geq 0$\n$y \\geq 0$",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.2))

    ax.set_title("連立不等式 $\\to$ 共通部分", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_individual_regions(axes[0])
    draw_intersection_region(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-region-system-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
