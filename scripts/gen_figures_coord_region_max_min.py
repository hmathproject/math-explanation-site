"""
gen_figures_coord_region_max_min.py — 領域における最大・最小

Panel 1: 等高線 z = 2x+y = k が動く
Panel 2: 頂点で最大・最小が実現

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_region_max_min.py
出力: site/figures/coord-region-max-min-combined.png
      site/assets/images/coord-region-max-min-combined.png
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


def _draw_axes_and_region(ax):
    """座標軸と実行可能領域（三角形）を描く共通ヘルパー"""
    ax.set_xlim(-0.8, 5.5)
    ax.set_ylim(-0.8, 5.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(5.2, 0), xytext=(-0.6, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(5.25, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 5.2), xytext=(0, -0.6),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, 5.25, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)

    # 境界線（三角形: (0,0), (4,0), (0,4)）
    x_full = np.linspace(-0.5, 5.0, 400)
    ax.plot(x_full, 4 - x_full, color=DARK_BLUE, linewidth=1.6, zorder=4)
    ax.plot([0, 0], [-0.5, 5.0], color=DARK_BLUE, linewidth=1.6, zorder=4)
    ax.plot([-0.5, 5.0], [0, 0], color=DARK_BLUE, linewidth=1.6, zorder=4)

    # 実行可能領域を薄く塗る
    x_tri = np.linspace(0, 4, 400)
    ax.fill_between(x_tri, np.zeros_like(x_tri), 4 - x_tri,
                    alpha=0.18, color=DARK_BLUE, zorder=2)


def draw_contour_lines(ax):
    """Panel 1: 等高線 z = 2x+y = k が動く"""
    _draw_axes_and_region(ax)

    # 等高線 2x + y = k  →  y = k - 2x
    x_line = np.linspace(-0.5, 5.0, 300)
    contour_params = [
        (2,  "#9999cc", r"$k=2$"),
        (4,  ORANGE,    r"$k=4$"),
        (6,  RED,       r"$k=6$"),
    ]
    for k, color, lab in contour_params:
        y_line = k - 2 * x_line
        ax.plot(x_line, y_line, color=color, linewidth=1.8,
                linestyle="-", zorder=5, label=lab)
        # ラベルを右端に配置（y座標が可視範囲内の場所を探す）
        x_label = 0.0
        y_label = k - 2 * x_label
        if 0 <= y_label <= 5.2:
            ax.text(x_label - 0.35, y_label, lab, ha="right", va="center",
                    fontsize=9, color=color)

    # k が増加する方向の矢印
    ax.annotate("", xy=(1.8, 2.0), xytext=(0.8, 4.0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5,
                                mutation_scale=9, shrinkA=0, shrinkB=0))
    ax.text(2.1, 2.8, "$k$ が\n増加する方向",
            ha="left", va="center", fontsize=8.5, color=RED)

    # 説明テキスト
    ax.text(2.5, 5.0,
            r"$z = 2x+y = k$" + "\n（直線が平行移動）",
            ha="center", va="top", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))

    ax.set_title(r"等高線 $z = 2x+y = k$ が動く", fontsize=10, pad=4)


def draw_vertex_optimum(ax):
    """Panel 2: 頂点で最大・最小が実現"""
    _draw_axes_and_region(ax)

    # 頂点
    vertices = [(0, 0), (4, 0), (0, 4)]
    v_labels = [r"$(0,0)$", r"$(4,0)$", r"$(0,4)$"]
    z_vals = [0, 8, 4]  # z = 2x + y
    v_offsets = [(-0.25, -0.35), (0.15, -0.35), (-0.25, 0.25)]
    colors = [GREEN, RED, ORANGE]

    for (vx, vy), lab, z, (ox, oy), col in zip(
            vertices, v_labels, z_vals, v_offsets, colors):
        ms = 10 if z == 8 else 8
        ax.plot(vx, vy, "o", color=col, markersize=ms, zorder=6)
        ax.text(vx + ox, vy + oy, lab + f"\n$z={z}$",
                ha="center", va="center", fontsize=9, color=col,
                bbox=dict(boxstyle="round,pad=0.3",
                          facecolor="white", edgecolor=col,
                          linewidth=1.0, alpha=0.9))

    # 最大値の強調（(4,0) を囲む）
    ax.plot(4, 0, "o", color=RED, markersize=14, zorder=5,
            markerfacecolor="none", markeredgewidth=2.2)

    # 最大値テキスト
    ax.text(2.5, 3.8,
            "最大値 $z=8$\nは頂点 $(4,0)$ で実現",
            ha="center", va="center", fontsize=9.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=1.3))

    # 最小値テキスト
    ax.text(2.5, 2.8,
            "最小値 $z=0$\nは頂点 $(0,0)$ で実現",
            ha="center", va="center", fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=1.0))

    # 結論
    ax.text(0.5, 5.1,
            "線形計画: 最大・最小は必ず頂点で実現",
            ha="left", va="top", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))

    ax.set_title("頂点で最大・最小が実現", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_contour_lines(axes[0])
    draw_vertex_optimum(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-region-max-min-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
