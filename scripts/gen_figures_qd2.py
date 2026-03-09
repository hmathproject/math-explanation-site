"""
gen_figures_qd2.py — 式の決定・記事2用概念図
頂点形 2パネル横並び
  左: 頂点(-1,2)と点(1,10) → y=2(x+1)²+2
  右: 軸x=1, 2点(0,-1),(3,5) → y=2(x-1)²-3

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qd2.py
出力:
    figures/quadratic-determine-vertex-combined.png
    assets/images/quadratic-determine-vertex-combined.png
    ../figures/quadratic-determine-vertex-combined.png  （PDF用）
"""

import platform
import shutil
from pathlib import Path

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
EXP_FIGURES_DIR = BASE_DIR.parent / "figures"
FIGURES_DIR.mkdir(exist_ok=True)
EXP_FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150
Y_TITLE_OFFSET      = 0.20
Y_YLABEL_OFFSET     = 0.27
CASE_TITLE_FONTSIZE = 10
TIGHT_LAYOUT_PAD    = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")


def draw_axes_custom(ax, xlim, ylim):
    xlo, xhi = xlim
    ylo, yhi = ylim
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(xhi + 0.35, 0), xytext=(xlo - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xhi + 0.38, 0, r"$x$", ha="left", va="center", fontsize=9)
    ax.annotate("", xy=(0, yhi + 0.48), xytext=(0, ylo - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, yhi + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=9)


def draw_panel_vertex_plus_point(ax):
    """左パネル: 頂点(-1,2)と点(1,10) → y=2(x+1)²+2"""
    X_LO, X_HI = -2.8, 1.5
    Y_LO, Y_HI = -0.5, 12.0
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.8)
    ax.axis("off")
    draw_axes_custom(ax, (X_LO, X_HI), (Y_LO, Y_HI))

    x = np.linspace(-2.8, 0.8, 500)
    y = np.clip(2*(x+1)**2 + 2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    # 頂点（赤い四角）
    ax.plot(-1, 2, "s", color="#dc2626", markersize=7, zorder=6)
    ax.text(-0.85, 2.3, r"頂点$(-1,\ 2)$", ha="left", va="bottom", fontsize=8.5,
            color="#dc2626", bbox=_lbl_bbox, zorder=7)

    # 通る点（青い丸）
    ax.plot(1, 10, "o", color="#2563eb", markersize=7, zorder=6)
    ax.text(1.1, 10, r"$(1,\ 10)$", ha="left", va="center", fontsize=8.5,
            color="#2563eb", bbox=_lbl_bbox, zorder=7)

    # 原点
    ax.text(0.12, -0.4, "$O$", ha="left", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "頂点＋1点 → 頂点形",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(X_LO + 0.2, Y_HI - 0.3, r"$y=2(x+1)^2+2$", ha="left", va="top",
            fontsize=8.5)


def draw_panel_axis_plus_two(ax):
    """右パネル: 軸x=1, 2点(0,-1),(3,5) → y=2(x-1)²-3"""
    X_LO, X_HI = -1.0, 4.0
    Y_LO, Y_HI = -4.0, 7.0
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.8)
    ax.axis("off")
    draw_axes_custom(ax, (X_LO, X_HI), (Y_LO, Y_HI))

    x = np.linspace(-0.6, 3.5, 500)
    y = np.clip(2*(x-1)**2 - 3, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    # 軸（破線）
    ax.plot([1, 1], [Y_LO, Y_HI - 0.5], "--", color="#6b7280", linewidth=1.0, zorder=1)
    ax.text(1.05, Y_HI - 0.8, r"軸 $x=1$", ha="left", va="top", fontsize=8,
            color="#6b7280", bbox=_lbl_bbox, zorder=7)

    # 2点（青い丸）
    for px, py, lbl in [(0, -1, r"$(0,\ -1)$"), (3, 5, r"$(3,\ 5)$")]:
        ax.plot(px, py, "o", color="#2563eb", markersize=7, zorder=6)
        ax.text(px + 0.12, py + 0.2, lbl, ha="left", va="bottom", fontsize=8.5,
                color="#2563eb", bbox=_lbl_bbox, zorder=7)

    # 原点
    ax.text(0.12, -0.35, "$O$", ha="left", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    # 頂点（薄い表示）
    ax.plot(1, -3, "s", color="#9ca3af", markersize=5, zorder=5)
    ax.text(1.1, -3, r"頂点$(1,\ -3)$", ha="left", va="center", fontsize=7.5,
            color="#9ca3af", bbox=_lbl_bbox, zorder=7)

    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "軸＋2点 → 頂点形",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(X_LO + 0.2, Y_HI - 0.3, r"$y=2(x-1)^2-3$", ha="left", va="top",
            fontsize=8.5)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")
    draw_panel_vertex_plus_point(axes[0])
    draw_panel_axis_plus_two(axes[1])
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.0)

    fname = "quadratic-determine-vertex-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
