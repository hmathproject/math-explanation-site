"""
gen_figures_qt3.py — 平行移動と対称移動の合成記事用概念図
変換順序A（y軸対称→x+3移動）vs 変換順序B（x+3移動→y軸対称）2パネル横並び

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qt3.py
出力:
    figures/quadratic-transform-compose-combined.png
    assets/images/quadratic-transform-compose-combined.png
    ../figures/quadratic-transform-compose-combined.png  （PDF用）
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

# 元の放物線: y = (x-2)^2 - 1, 頂点 (2, -1)
def f_orig(x):
    return (x - 2)**2 - 1

# 順序A: y軸対称→x方向+3 → y=(x-1)^2-1, 頂点 (1,-1)
def f_case_a(x):
    return (x - 1)**2 - 1

# 順序B: x方向+3→y軸対称 → y=(x+5)^2-1, 頂点 (-5,-1)
def f_case_b(x):
    return (x + 5)**2 - 1

X_LO, X_HI = -7.5, 4.5
Y_LO, Y_HI = -1.8, 6.0


def draw_axes(ax):
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.35, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.38, 0, r"$x$", ha="left", va="center", fontsize=9)
    ax.annotate("", xy=(0, Y_HI + 0.5), xytext=(0, Y_LO - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.15, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=9)


def draw_tick(ax, x, label=""):
    tick = 0.12
    ax.plot([x, x], [-tick, tick], "k-", linewidth=0.8, zorder=3)
    if label:
        ax.text(x, -0.28, label, ha="center", va="top", fontsize=8,
                bbox=_lbl_bbox, zorder=7)


def draw_vertex(ax, vx, vy, color, label):
    ax.plot(vx, vy, "o", color=color, markersize=5, zorder=6)
    ax.text(vx + 0.2, vy + 0.15, label, ha="left", va="bottom", fontsize=8,
            color=color, bbox=_lbl_bbox, zorder=7)


def draw_panel(ax, f_result, title, result_label,
               result_vertex, result_color):
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.6)
    ax.axis("off")
    draw_axes(ax)

    x = np.linspace(X_LO, X_HI, 800)

    # 元の放物線（灰色・破線）
    y_o = np.clip(f_orig(x), Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_o, color="#9ca3af", linewidth=1.5, zorder=2, linestyle="--")

    # 結果の放物線（黒・実線）
    y_r = np.clip(f_result(x), Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y_r, color=result_color, linewidth=2.0, zorder=2)

    # 頂点マーク
    draw_vertex(ax, 2, -1, color="#9ca3af", label="$(2,-1)$")
    draw_vertex(ax, result_vertex[0], result_vertex[1],
                color=result_color,
                label=f"$({result_vertex[0]},{result_vertex[1]})$")

    # 原点表示
    ax.text(0.15, -0.28, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    # 結果ラベル（式）
    ax.text(X_LO + 0.3, Y_HI - 0.2, result_label, ha="left", va="top",
            fontsize=8, color=result_color)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, title,
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")

    # ケース1: 順序A — y軸対称してからx方向に3移動 → y=(x-1)^2-1
    draw_panel(axes[0],
               f_result=f_case_a,
               title="順序A：y軸対称 → x方向+3移動",
               result_label=r"$y=(x-1)^2-1$",
               result_vertex=(1, -1),
               result_color="black")

    # ケース2: 順序B — x方向に3移動してからy軸対称 → y=(x+5)^2-1
    draw_panel(axes[1],
               f_result=f_case_b,
               title="順序B：x方向+3移動 → y軸対称",
               result_label=r"$y=(x+5)^2-1$",
               result_vertex=(-5, -1),
               result_color="black")

    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.0)

    fname = "quadratic-transform-compose-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
