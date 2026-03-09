"""
gen_figures_qt0.py — 平行移動・対称移動 単元トップ overview 図
4パネル横並び（x方向移動 / y方向移動 / x軸対称 / y軸対称）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qt0.py
出力:
    figures/quadratic-transform-overview.png
    assets/images/quadratic-transform-overview.png
    ../figures/quadratic-transform-overview.png  （PDF用）
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
CASE_TITLE_FONTSIZE = 9
TIGHT_LAYOUT_PAD    = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")

X_LO, X_HI = -3.0, 4.5
Y_LO, Y_HI = -1.5, 5.5


def draw_axes(ax):
    arrow_kw = dict(color="black", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.3, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.33, 0, r"$x$", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(0, Y_HI + 0.45), xytext=(0, Y_LO - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.12, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=8.5)


def draw_panel_x_translate(ax):
    """x方向移動: y=x² → y=(x-2)²"""
    ax.set_xlim(X_LO - 0.1, X_HI + 0.4)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.5)
    ax.axis("off")
    draw_axes(ax)
    x = np.linspace(X_LO, X_HI, 600)

    y_o = np.clip(x**2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_o, color="#9ca3af", linewidth=1.3, linestyle="--", zorder=2)

    y_m = np.clip((x - 2)**2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_m, color="black", linewidth=1.8, zorder=2)

    ax.plot(0, 0, "o", color="white", markeredgecolor="#9ca3af", markersize=4, zorder=5)
    ax.plot(2, 0, "o", color="white", markeredgecolor="black", markersize=4, zorder=5)

    ax.text(0, -0.35, "$O$", ha="center", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)
    ax.text(2, -0.35, "$2$", ha="center", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)

    ax.annotate("", xy=(2, -0.35), xytext=(0.15, -0.35),
                arrowprops=dict(arrowstyle="-|>", color="#2563eb", lw=0.9,
                                mutation_scale=6, shrinkA=0, shrinkB=0))

    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "x方向移動",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(3.5, 2.5, r"$y=(x-2)^2$", ha="left", va="center", fontsize=7.5)


def draw_panel_y_translate(ax):
    """y方向移動: y=x² → y=x²+3"""
    ax.set_xlim(X_LO - 0.1, X_HI + 0.4)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.5)
    ax.axis("off")
    draw_axes(ax)
    x = np.linspace(X_LO, X_HI, 600)

    y_o = np.clip(x**2, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_o, color="#9ca3af", linewidth=1.3, linestyle="--", zorder=2)

    y_m = np.clip(x**2 + 3, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_m, color="black", linewidth=1.8, zorder=2)

    ax.plot(0, 0, "o", color="white", markeredgecolor="#9ca3af", markersize=4, zorder=5)
    ax.plot(0, 3, "o", color="white", markeredgecolor="black", markersize=4, zorder=5)

    ax.text(0, -0.35, "$O$", ha="center", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)
    ax.text(-0.18, 3, "$3$", ha="right", va="center", fontsize=8, bbox=_lbl_bbox, zorder=7)

    ax.annotate("", xy=(0.2, 2.9), xytext=(0.2, 0.15),
                arrowprops=dict(arrowstyle="-|>", color="#2563eb", lw=0.9,
                                mutation_scale=6, shrinkA=0, shrinkB=0))

    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "y方向移動",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(-0.2, 5.0, r"$y=x^2+3$", ha="right", va="center", fontsize=7.5)


def draw_panel_x_reflect(ax):
    """x軸対称: y=(x-2)^2-1 → y=-(x-2)^2+1"""
    ax.set_xlim(X_LO - 0.1, X_HI + 0.4)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.5)
    ax.axis("off")
    draw_axes(ax)
    x = np.linspace(X_LO, X_HI, 600)

    y_o = np.clip((x - 2)**2 - 1, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_o, color="#9ca3af", linewidth=1.3, linestyle="--", zorder=2)

    y_m = np.clip(-((x - 2)**2) + 1, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_m, color="black", linewidth=1.8, zorder=2)

    ax.plot(2, -1, "o", color="white", markeredgecolor="#9ca3af", markersize=4, zorder=5)
    ax.plot(2, 1, "o", color="white", markeredgecolor="black", markersize=4, zorder=5)

    ax.text(0.15, -0.35, "$O$", ha="left", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)

    # x軸対称ラベル（x軸を強調）
    ax.plot([X_LO, X_HI], [0, 0], color="#dc2626", linewidth=0.5, linestyle=":", zorder=1)

    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "x軸対称",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(3.8, 0.5, r"$y=-(x-2)^2+1$", ha="left", va="center", fontsize=7.5)


def draw_panel_y_reflect(ax):
    """y軸対称: y=(x-2)^2-1 → y=(x+2)^2-1"""
    ax.set_xlim(X_LO - 0.1, X_HI + 0.4)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.5)
    ax.axis("off")
    draw_axes(ax)
    x = np.linspace(X_LO, X_HI, 600)

    y_o = np.clip((x - 2)**2 - 1, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_o, color="#9ca3af", linewidth=1.3, linestyle="--", zorder=2)

    y_m = np.clip((x + 2)**2 - 1, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_m, color="black", linewidth=1.8, zorder=2)

    ax.plot(2, -1, "o", color="white", markeredgecolor="#9ca3af", markersize=4, zorder=5)
    ax.plot(-2, -1, "o", color="white", markeredgecolor="black", markersize=4, zorder=5)

    ax.text(0.15, -0.35, "$O$", ha="left", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)

    # y軸対称ラベル（y軸を強調）
    ax.plot([0, 0], [Y_LO, Y_HI], color="#dc2626", linewidth=0.5, linestyle=":", zorder=1)

    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "y軸対称",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(-0.2, 3.5, r"$y=(x+2)^2-1$", ha="right", va="center", fontsize=7.5)


def main():
    fig, axes = plt.subplots(1, 4, figsize=(18.0, 4.5))
    fig.patch.set_facecolor("white")
    draw_panel_x_translate(axes[0])
    draw_panel_y_translate(axes[1])
    draw_panel_x_reflect(axes[2])
    draw_panel_y_reflect(axes[3])
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=0.5)

    fname = "quadratic-transform-overview.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
