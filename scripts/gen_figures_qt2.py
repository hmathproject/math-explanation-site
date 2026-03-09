"""
gen_figures_qt2.py — 対称移動（x軸・y軸・原点）記事用概念図
x軸対称 / y軸対称 / 原点対称 3パネル横並び

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qt2.py
出力:
    figures/quadratic-transform-reflect-combined.png
    assets/images/quadratic-transform-reflect-combined.png
    ../figures/quadratic-transform-reflect-combined.png  （PDF用）
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

# 元の放物線: y = (x+2)^2 - 5, 頂点 (-2, -5)
def f_orig(x):
    return (x + 2)**2 - 5

# x軸対称: y = -(x+2)^2 + 5, 頂点 (-2, 5)
def f_xrefl(x):
    return -((x + 2)**2) + 5

# y軸対称: y = (x-2)^2 - 5, 頂点 (2, -5)
def f_yrefl(x):
    return (x - 2)**2 - 5

# 原点対称: y = -(x-2)^2 + 5, 頂点 (2, 5)
def f_orefl(x):
    return -((x - 2)**2) + 5

X_LO, X_HI = -5.5, 5.5
Y_LO, Y_HI = -6.5, 6.5


def draw_axes(ax):
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.35, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.38, 0, r"$x$", ha="left", va="center", fontsize=9)
    ax.annotate("", xy=(0, Y_HI + 0.5), xytext=(0, Y_LO - 0.25),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.15, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=9)


def draw_tick(ax, x=None, y=None, label=""):
    tick = 0.18
    if x is not None and x != 0:
        ax.plot([x, x], [-tick, tick], "k-", linewidth=0.8, zorder=3)
        if label:
            ax.text(x, -0.4, label, ha="center", va="top", fontsize=8,
                    bbox=_lbl_bbox, zorder=7)
    if y is not None and y != 0:
        ax.plot([-tick, tick], [y, y], "k-", linewidth=0.8, zorder=3)
        if label:
            ax.text(-0.25, y, label, ha="right", va="center", fontsize=8,
                    bbox=_lbl_bbox, zorder=7)


def draw_vertex(ax, vx, vy, color="black", label=None):
    ax.plot(vx, vy, "o", color=color, markersize=5, zorder=6)
    if label:
        ax.text(vx + 0.3, vy + 0.3, label, ha="left", va="bottom", fontsize=8,
                color=color, bbox=_lbl_bbox, zorder=7)


def draw_panel(ax, f_moved, title, moved_label,
               orig_vertex, moved_vertex,
               moved_color="black"):
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(Y_LO - 0.5, Y_HI + 0.6)
    ax.axis("off")
    draw_axes(ax)

    x = np.linspace(X_LO, X_HI, 800)

    # 元の放物線（灰色・破線）
    y_o = np.clip(f_orig(x), Y_LO - 0.3, Y_HI + 0.3)
    ax.plot(x, y_o, color="#9ca3af", linewidth=1.5, zorder=2, linestyle="--")

    # 変換後の放物線（黒・実線）
    y_m = np.clip(f_moved(x), Y_LO - 0.3, Y_HI + 0.3)
    ax.plot(x, y_m, color=moved_color, linewidth=2.0, zorder=2)

    # 頂点マーク
    draw_vertex(ax, orig_vertex[0], orig_vertex[1], color="#9ca3af",
                label=f"$({orig_vertex[0]},{orig_vertex[1]})$")
    draw_vertex(ax, moved_vertex[0], moved_vertex[1], color=moved_color,
                label=f"$({moved_vertex[0]},{moved_vertex[1]})$")

    # 目盛り（原点）
    ax.text(0.15, -0.4, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    # 変換後ラベル
    ax.text(X_LO + 0.3, Y_HI - 0.2, moved_label, ha="left", va="top",
            fontsize=8, color=moved_color)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, title,
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.5))
    fig.patch.set_facecolor("white")

    # ケース1: x軸対称
    draw_panel(axes[0],
               f_moved=f_xrefl,
               title="x軸対称",
               moved_label=r"$y=-(x+2)^2+5$",
               orig_vertex=(-2, -5),
               moved_vertex=(-2, 5))

    # ケース2: y軸対称
    draw_panel(axes[1],
               f_moved=f_yrefl,
               title="y軸対称",
               moved_label=r"$y=(x-2)^2-5$",
               orig_vertex=(-2, -5),
               moved_vertex=(2, -5))

    # ケース3: 原点対称
    draw_panel(axes[2],
               f_moved=f_orefl,
               title="原点対称",
               moved_label=r"$y=-(x-2)^2+5$",
               orig_vertex=(-2, -5),
               moved_vertex=(2, 5))

    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=0.5)

    fname = "quadratic-transform-reflect-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
