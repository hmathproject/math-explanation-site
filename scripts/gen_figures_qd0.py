"""
gen_figures_qd0.py — 式の決定 単元トップ overview 図
3パネル横並び（一般形・頂点形・因数形）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qd0.py
出力:
    figures/quadratic-determine-overview.png
    assets/images/quadratic-determine-overview.png
    ../figures/quadratic-determine-overview.png  （PDF用）
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
CASE_TITLE_FONTSIZE = 9
TIGHT_LAYOUT_PAD    = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")

X_LO, X_HI = -2.5, 4.5
Y_LO, Y_HI = -1.5, 6.0


def draw_axes(ax):
    arrow_kw = dict(color="black", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.3, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.33, 0, r"$x$", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(0, Y_HI + 0.45), xytext=(0, Y_LO - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.12, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=8.5)


def draw_panel_general(ax):
    """一般形: 3点を通る放物線 y=2x²-5x+3 with points (0,3),(1,0),(2,1)"""
    ax.set_xlim(X_LO - 0.1, X_HI + 0.4)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.5)
    ax.axis("off")
    draw_axes(ax)

    x = np.linspace(-0.5, 3.5, 400)
    y = 2*x**2 - 5*x + 3
    y_clip = np.clip(y, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_clip, color="black", linewidth=1.8, zorder=2)

    # 3点
    pts = [(0, 3), (1, 0), (2, 1)]
    labels = [r"$(0,3)$", r"$(1,0)$", r"$(2,1)$"]
    offsets = [(0.2, 0.3), (0.2, 0.3), (0.2, 0.3)]
    for (px, py), lbl, (dx, dy) in zip(pts, labels, offsets):
        ax.plot(px, py, "o", color="#2563eb", markersize=6, zorder=6)
        ax.text(px + dx, py + dy, lbl, ha="left", va="bottom", fontsize=8,
                color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.15, -0.35, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, "一般形：3点が与えられたとき",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(3.5, 4.5, r"$y=ax^2+bx+c$", ha="right", va="center", fontsize=7.5)


def draw_panel_vertex(ax):
    """頂点形: 頂点(-1,2)と点(1,10) → y=2(x+1)²+2"""
    X_LO2, X_HI2, Y_LO2, Y_HI2 = -3.5, 2.5, -0.5, 12.0
    ax.set_xlim(X_LO2 - 0.1, X_HI2 + 0.4)
    ax.set_ylim(Y_LO2 - 0.4, Y_HI2 + 0.8)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI2 + 0.3, 0), xytext=(X_LO2 - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI2 + 0.33, 0, r"$x$", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(0, Y_HI2 + 0.6), xytext=(0, Y_LO2 - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.12, Y_HI2 + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=8.5)

    x = np.linspace(-2.7, 0.7, 400)
    y = np.clip(2*(x+1)**2 + 2, Y_LO2 - 0.2, Y_HI2 + 0.2)
    ax.plot(x, y, color="black", linewidth=1.8, zorder=2)

    # 頂点
    ax.plot(-1, 2, "s", color="#dc2626", markersize=6, zorder=6)
    ax.text(-0.8, 2, r"頂点$(-1,2)$", ha="left", va="center", fontsize=7.5,
            color="#dc2626", bbox=_lbl_bbox, zorder=7)

    # 通る点
    ax.plot(1, 10, "o", color="#2563eb", markersize=6, zorder=6)
    ax.text(1.1, 10, r"$(1,10)$", ha="left", va="center", fontsize=7.5,
            color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.4, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    cx = (X_LO2 + X_HI2) / 2
    ax.text(cx, Y_HI2 + Y_TITLE_OFFSET, "頂点形：頂点・軸が与えられたとき",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(-3.2, 10, r"$y=a(x-p)^2+q$", ha="left", va="center", fontsize=7.5)


def draw_panel_factor(ax):
    """因数形: x=1,x=3が解, y=2(x-1)(x-3), 点(0,6)"""
    X_LO3, X_HI3, Y_LO3, Y_HI3 = -1.0, 4.5, -2.0, 7.0
    ax.set_xlim(X_LO3 - 0.1, X_HI3 + 0.4)
    ax.set_ylim(Y_LO3 - 0.4, Y_HI3 + 0.5)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI3 + 0.3, 0), xytext=(X_LO3 - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI3 + 0.33, 0, r"$x$", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(0, Y_HI3 + 0.45), xytext=(0, Y_LO3 - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.12, Y_HI3 + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=8.5)

    x = np.linspace(-0.5, 4.0, 400)
    y = np.clip(2*(x-1)*(x-3), Y_LO3 - 0.2, Y_HI3 + 0.2)
    ax.plot(x, y, color="black", linewidth=1.8, zorder=2)

    # x軸との交点（解）
    tick = 0.12
    for xr, lbl in [(1, r"$\alpha=1$"), (3, r"$\beta=3$")]:
        ax.plot([xr, xr], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.plot(xr, 0, "o", color="white", markeredgecolor="#dc2626",
                markersize=5, markeredgewidth=1.5, zorder=5)
        ax.text(xr, -0.35, lbl, ha="center", va="top", fontsize=7.5,
                color="#dc2626", bbox=_lbl_bbox, zorder=7)

    # 通る点
    ax.plot(0, 6, "o", color="#2563eb", markersize=6, zorder=6)
    ax.text(0.15, 6, r"$(0,6)$", ha="left", va="center", fontsize=7.5,
            color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.35, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    cx = (X_LO3 + X_HI3) / 2
    ax.text(cx, Y_HI3 + Y_TITLE_OFFSET, "因数形：2つの解が与えられたとき",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(3.8, 5.5, r"$y=a(x-\alpha)(x-\beta)$", ha="right", va="center", fontsize=7.5)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.5))
    fig.patch.set_facecolor("white")
    draw_panel_general(axes[0])
    draw_panel_vertex(axes[1])
    draw_panel_factor(axes[2])
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=0.5)

    fname = "quadratic-determine-overview.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
