"""
gen_figures_wp1.py — 文章題・応用・記事1用図
2パネル横並び
  左: 収益最大化 f(x) = (x-40)(100-x)、最大点 x=70 を示す
  右: 面積最大化 S(x) = x(10-x)、最大点 x=5 を示す

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  ylim は curve_ylim() で実データ範囲から安全に計算する。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_wp1.py
出力:
    figures/quadratic-word-problems-optimization-combined.png
    assets/images/quadratic-word-problems-optimization-combined.png
    ../figures/quadratic-word-problems-optimization-combined.png  （PDF用）
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


def curve_ylim(y_arr, extra_y=(), margin=0.15):
    """
    曲線データと注釈 y 座標から安全な ylim を計算する。
    np.clip() の代わりにこの関数で ylim を決め、ax.set_ylim() に渡す。
    """
    y_all = list(y_arr) + list(extra_y)
    y_min, y_max = min(y_all), max(y_all)
    span = max(y_max - y_min, 1.0)
    return y_min - margin * span, y_max + margin * span


def draw_axes_custom(ax, xlim, ylim, xlabel=r"$x$", ylabel=r"$y$"):
    xlo, xhi = xlim
    ylo, yhi = ylim
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(xhi + 0.02 * (xhi - xlo), 0), xytext=(xlo - 0.01 * (xhi - xlo), 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xhi + 0.03 * (xhi - xlo), 0, xlabel, ha="left", va="center", fontsize=9)
    ax.annotate("", xy=(0, yhi + 0.05 * (yhi - ylo)), xytext=(0, ylo - 0.02 * (yhi - ylo)),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xlo * 0.02, yhi + Y_YLABEL_OFFSET * (yhi - ylo) / 5.0, ylabel,
            ha="left", va="bottom", fontsize=9)


def draw_panel_revenue(ax):
    """左パネル: 収益最大化 f(x) = (x-40)(100-x)"""
    # x ∈ [40, 100]（仕入れ値40円以上・販売数が0以上）
    x = np.linspace(38, 102, 500)
    y = (x - 40) * (100 - x)   # np.clip() 不使用

    y_lo, y_hi = curve_ylim(y, extra_y=[0, 900], margin=0.15)
    y_lo = min(y_lo, -80)

    XL, XH = 38, 102
    ax.set_xlim(XL - 2, XH + 6)
    ax.set_ylim(y_lo - 40, y_hi + 80)
    ax.axis("off")

    # x 軸・y 軸の矢印（原点ではなく x=38, y=y_lo の位置から）
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(XH + 4, 0), xytext=(XL - 1, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(XH + 5, 0, r"$x$（円）", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(XL, y_hi + 60), xytext=(XL, y_lo - 25),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(XL + 0.5, y_hi + Y_YLABEL_OFFSET * 15, r"$f(x)$（円）",
            ha="left", va="bottom", fontsize=8.5)

    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    # 最大点
    ax.plot(70, 900, "s", color="#dc2626", markersize=7, zorder=6)
    ax.plot([70, 70], [0, 900], "r--", linewidth=0.9, zorder=1)

    tick = 25
    for xv, lbl in [(40, "40"), (70, "70"), (100, "100")]:
        ax.plot([xv, xv], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(xv, -tick * 1.8, lbl, ha="center", va="top", fontsize=8, bbox=_lbl_bbox)

    ax.text(70 + 1, 900 + 25, r"最大$f(70) = 900$円", ha="left", va="bottom",
            fontsize=8.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(XL + 1, y_lo - 15, r"$f(x) = (x-40)(100-x)$",
            ha="left", va="top", fontsize=8.5, bbox=_lbl_bbox, zorder=7)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + 50, "収益最大化",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(cx, y_hi + 10, "頂点が最大点",
            ha="center", va="bottom", fontsize=8, color="#6b7280")


def draw_panel_area(ax):
    """右パネル: 面積最大化 S(x) = x(10-x)"""
    x = np.linspace(-0.5, 10.5, 500)
    y = x * (10 - x)   # np.clip() 不使用

    y_lo, y_hi = curve_ylim(y, extra_y=[0, 25], margin=0.15)
    y_lo = min(y_lo, -1.5)

    XL, XH = -0.5, 10.7
    ax.set_xlim(XL - 0.2, XH + 0.6)
    ax.set_ylim(y_lo - 1, y_hi + 3)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(XH + 0.45, 0), xytext=(XL - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(XH + 0.5, 0, r"$x$（m）", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(0, y_hi + 2), xytext=(0, y_lo - 0.8),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.15, y_hi + Y_YLABEL_OFFSET * 2.5, r"$S(x)$（m²）",
            ha="left", va="bottom", fontsize=8.5)

    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    # 最大点
    ax.plot(5, 25, "s", color="#dc2626", markersize=7, zorder=6)
    ax.plot([5, 5], [0, 25], "r--", linewidth=0.9, zorder=1)

    tick = 0.7
    for xv, lbl in [(0, "0"), (5, "5"), (10, "10")]:
        ax.plot([xv, xv], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(xv, -tick * 2, lbl, ha="center", va="top", fontsize=8.5, bbox=_lbl_bbox)

    ax.text(5 + 0.2, 25 + 0.5, r"最大 $S(5) = 25\text{ m}^2$", ha="left", va="bottom",
            fontsize=8.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(0.3, y_lo - 0.8, r"$S(x) = x(10 - x)$",
            ha="left", va="top", fontsize=8.5, bbox=_lbl_bbox, zorder=7)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + 2, "面積最大化",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(cx, y_hi + 0.5, "頂点が最大点",
            ha="center", va="bottom", fontsize=8, color="#6b7280")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")
    draw_panel_revenue(axes[0])
    draw_panel_area(axes[1])
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.0)

    fname = "quadratic-word-problems-optimization-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
