"""
gen_figures_qt1.py — 平行移動（x軸方向・y軸方向）記事用概念図
x方向移動 / y方向移動 2パネル横並び

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qt1.py
出力:
    figures/quadratic-transform-translate-combined.png
    assets/images/quadratic-transform-translate-combined.png
    ../figures/quadratic-transform-translate-combined.png  （PDF用）
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

BASE_DIR = Path(__file__).parent.parent        # = site/
FIGURES_DIR = BASE_DIR / "figures"
SITE_IMAGES_DIR = BASE_DIR / "assets" / "images"
EXP_FIGURES_DIR = BASE_DIR.parent / "figures"  # = graph-guided-lessons/figures/
FIGURES_DIR.mkdir(exist_ok=True)
EXP_FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150

# ── ラベル位置定数 ────────────────────────────────────────────────
Y_TITLE_OFFSET      = 0.20
Y_YLABEL_OFFSET     = 0.27
CASE_TITLE_FONTSIZE = 10
TIGHT_LAYOUT_PAD    = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")

X_LO, X_HI = -2.5, 5.0
Y_LO, Y_HI = -0.5, 6.0


def draw_axes(ax):
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.32, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.36, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, Y_HI + 0.48), xytext=(0, Y_LO - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)


def draw_tick(ax, x=None, y=None, label="", label_side="bottom"):
    tick = 0.12
    if x is not None:
        ax.plot([x, x], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        if label:
            va = "top" if label_side == "bottom" else "bottom"
            dy = -0.28 if label_side == "bottom" else 0.28
            ax.text(x, dy, label, ha="center", va=va, fontsize=9,
                    bbox=_lbl_bbox, zorder=7)
    if y is not None:
        ax.plot([-tick, tick], [y, y], "k-", linewidth=0.9, zorder=3)
        if label:
            ax.text(-0.15, y, label, ha="right", va="center", fontsize=9,
                    bbox=_lbl_bbox, zorder=7)


def draw_case_x(ax):
    """ケース1: x方向平行移動 y=x² → y=(x-3)²"""
    ax.set_xlim(X_LO - 0.1, X_HI + 0.45)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.6)
    ax.axis("off")
    draw_axes(ax)

    x = np.linspace(X_LO, X_HI, 600)

    # 元の放物線 y=x²（灰色）
    y_orig = np.clip(x**2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_orig, color="#9ca3af", linewidth=1.5, zorder=2, linestyle="--")
    ax.text(-0.2, 3.5, r"$y=x^2$", ha="right", va="center", fontsize=9,
            color="#9ca3af")

    # 移動後の放物線 y=(x-3)²（黒）
    y_moved = np.clip((x - 3)**2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_moved, color="black", linewidth=2.0, zorder=2)
    ax.text(4.6, 2.0, r"$y=(x-3)^2$", ha="left", va="center", fontsize=9)

    # 頂点マーク
    ax.plot(0, 0, "o", color="white", markeredgecolor="#9ca3af",
            markersize=5, markeredgewidth=1.2, zorder=5)
    ax.plot(3, 0, "o", color="white", markeredgecolor="black",
            markersize=5, markeredgewidth=1.2, zorder=5)

    # 目盛り
    draw_tick(ax, x=0, label="$O$")
    draw_tick(ax, x=3, label="$3$")

    # 移動量の矢印
    ax.annotate("", xy=(3, -0.35), xytext=(0.1, -0.35),
                arrowprops=dict(arrowstyle="-|>", color="#2563eb", lw=1.0,
                                mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(1.5, -0.55, r"$x$ 方向に $+3$", ha="center", va="top",
            fontsize=8.5, color="#2563eb", bbox=_lbl_bbox, zorder=7)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "x方向平行移動：右に3移動",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def draw_case_y(ax):
    """ケース2: y方向平行移動 y=x² → y=x²+2"""
    ax.set_xlim(X_LO - 0.1, X_HI + 0.45)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.6)
    ax.axis("off")
    draw_axes(ax)

    x = np.linspace(X_LO, X_HI, 600)

    # 元の放物線 y=x²（灰色）
    y_orig = np.clip(x**2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_orig, color="#9ca3af", linewidth=1.5, zorder=2, linestyle="--")
    ax.text(-0.2, 3.5, r"$y=x^2$", ha="right", va="center", fontsize=9,
            color="#9ca3af")

    # 移動後の放物線 y=x²+2（黒）
    y_moved = np.clip(x**2 + 2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_moved, color="black", linewidth=2.0, zorder=2)
    ax.text(-0.2, 5.5, r"$y=x^2+2$", ha="right", va="center", fontsize=9)

    # 頂点マーク
    ax.plot(0, 0, "o", color="white", markeredgecolor="#9ca3af",
            markersize=5, markeredgewidth=1.2, zorder=5)
    ax.plot(0, 2, "o", color="white", markeredgecolor="black",
            markersize=5, markeredgewidth=1.2, zorder=5)

    # 目盛り
    draw_tick(ax, x=0, label="$O$")
    draw_tick(ax, y=2, label="$2$")

    # 移動量の矢印
    ax.annotate("", xy=(0.25, 1.9), xytext=(0.25, 0.1),
                arrowprops=dict(arrowstyle="-|>", color="#2563eb", lw=1.0,
                                mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(0.8, 1.0, r"$y$ 方向に $+2$", ha="left", va="center",
            fontsize=8.5, color="#2563eb", bbox=_lbl_bbox, zorder=7)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "y方向平行移動：上に2移動",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")
    draw_case_x(axes[0])
    draw_case_y(axes[1])
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.0)

    fname = "quadratic-transform-translate-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
