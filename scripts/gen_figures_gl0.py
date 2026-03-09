"""
gen_figures_gl0.py — グラフと直線 単元トップ overview 図
3パネル横並び（共有点の個数・共有点の座標・三角形の面積）

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  ylim は curve_ylim() で実データ範囲から安全に計算する。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_gl0.py
出力:
    figures/quadratic-graph-line-overview.png
    assets/images/quadratic-graph-line-overview.png
    ../figures/quadratic-graph-line-overview.png  （PDF用）
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
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


def curve_ylim(y_arr, extra_y=(), margin=0.15):
    y_all = list(y_arr) + list(extra_y)
    y_min, y_max = min(y_all), max(y_all)
    span = max(y_max - y_min, 1.0)
    return y_min - margin * span, y_max + margin * span


def draw_axes_custom(ax, xlim, ylim, fontsize=8):
    xlo, xhi = xlim
    ylo, yhi = ylim
    arrow_kw = dict(color="black", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(xhi + 0.3, 0), xytext=(xlo - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xhi + 0.33, 0, r"$x$", ha="left", va="center", fontsize=fontsize)
    ax.annotate("", xy=(0, yhi + 0.45), xytext=(0, ylo - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, yhi + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=fontsize)


def draw_panel_intersections(ax):
    """左パネル: 共有点の個数（D>0 の場合、y=x² と y=x+1）"""
    x = np.linspace(-1.3, 2.3, 400)
    y_para = x**2           # パラボラ np.clip() 不使用
    y_line = x + 1          # 直線 k=1

    # 共有点 x = (1±√5)/2
    x1 = (1 - np.sqrt(5)) / 2  # ≈ -0.618
    x2 = (1 + np.sqrt(5)) / 2  # ≈ 1.618
    y1, y2 = x1**2, x2**2

    y_lo, y_hi = curve_ylim(y_para, extra_y=[y1, y2, 0, y_line[-1]], margin=0.15)
    y_lo = min(y_lo, -0.5)

    XL, XH = -1.3, 2.5
    ax.set_xlim(XL - 0.1, XH + 0.4)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.5)
    ax.axis("off")
    draw_axes_custom(ax, (XL, XH), (y_lo, y_hi))

    ax.plot(x, y_para, color="black", linewidth=1.8, zorder=2)
    ax.plot(x, y_line, color="#2563eb", linewidth=1.5, zorder=2, linestyle="--")

    ax.plot(x1, y1, "o", color="#dc2626", markersize=6, zorder=6)
    ax.plot(x2, y2, "o", color="#dc2626", markersize=6, zorder=6)

    ax.text(0.1, -0.3, "$O$", ha="left", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)
    ax.text(2.0, 3.8, r"$y=x^2$", ha="left", va="center", fontsize=7.5, bbox=_lbl_bbox)
    ax.text(1.7, 2.5, r"$y=x+k$", ha="left", va="center", fontsize=7.5, color="#2563eb", bbox=_lbl_bbox)

    # 2点マーク
    ax.annotate("2点で交わる", xy=(x2, y2), xytext=(x2 + 0.3, y2 + 0.5),
                fontsize=7.5, color="#dc2626",
                arrowprops=dict(arrowstyle="->", color="#dc2626", lw=0.8))

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "共有点の個数",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(cx, y_hi - 0.5, "判別式 $D$ の符号で決まる",
            ha="center", va="top", fontsize=7.5, color="#6b7280")


def draw_panel_coordinates(ax):
    """中パネル: 共有点の座標（y=x² と y=2x+3）"""
    x = np.linspace(-2.0, 3.8, 400)
    y_para = x**2           # np.clip() 不使用
    y_line = 2*x + 3

    # 共有点 x=-1, x=3
    pts = [(-1, 1), (3, 9)]

    y_lo, y_hi = curve_ylim(y_para, extra_y=[1, 9, 0, y_line[-1]], margin=0.12)
    y_lo = min(y_lo, -0.5)

    XL, XH = -2.0, 4.0
    ax.set_xlim(XL - 0.1, XH + 0.4)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.5)
    ax.axis("off")
    draw_axes_custom(ax, (XL, XH), (y_lo, y_hi))

    ax.plot(x, y_para, color="black", linewidth=1.8, zorder=2)
    ax.plot(x, y_line, color="#2563eb", linewidth=1.5, zorder=2, linestyle="--")

    for px, py in pts:
        ax.plot(px, py, "o", color="#dc2626", markersize=6, zorder=6)

    ax.text(-1 - 0.15, 1 + 0.5, r"$(-1,\ 1)$", ha="right", va="bottom",
            fontsize=7.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(3 + 0.1, 9, r"$(3,\ 9)$", ha="left", va="center",
            fontsize=7.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)

    ax.text(0.1, -0.3, "$O$", ha="left", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)
    ax.text(-1.8, 8, r"$y=x^2$", ha="left", va="center", fontsize=7.5, bbox=_lbl_bbox)
    ax.text(2.5, 4.5, r"$y=2x+3$", ha="left", va="center", fontsize=7.5, color="#2563eb", bbox=_lbl_bbox)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "共有点の座標",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(cx, y_hi - 0.5, "連立方程式を解いて求める",
            ha="center", va="top", fontsize=7.5, color="#6b7280")


def draw_panel_area(ax):
    """右パネル: 三角形の面積（y=x² と y=2x+3 の交点と原点）"""
    x = np.linspace(-2.0, 3.8, 400)
    y_para = x**2           # np.clip() 不使用
    y_line = 2*x + 3

    # 三角形の頂点
    Ox, Oy = 0, 0
    Ax, Ay = -1, 1
    Bx, By = 3, 9

    y_lo, y_hi = curve_ylim(y_para, extra_y=[Oy, Ay, By, y_line[-1]], margin=0.12)
    y_lo = min(y_lo, -0.5)

    XL, XH = -2.0, 4.0
    ax.set_xlim(XL - 0.1, XH + 0.4)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.5)
    ax.axis("off")
    draw_axes_custom(ax, (XL, XH), (y_lo, y_hi))

    # 三角形の塗りつぶしと辺
    ax.fill([Ox, Ax, Bx], [Oy, Ay, By], alpha=0.25, color="#2563eb", zorder=1)
    ax.plot([Ox, Ax, Bx, Ox], [Oy, Ay, By, Oy],
            color="#1d4ed8", linewidth=1.0, linestyle="--", zorder=3)

    ax.plot(x, y_para, color="black", linewidth=1.8, zorder=2)
    ax.plot(x, y_line, color="#2563eb", linewidth=1.5, zorder=2, linestyle="--", alpha=0.6)

    ax.plot(Ax, Ay, "o", color="#dc2626", markersize=5, zorder=6)
    ax.plot(Bx, By, "o", color="#dc2626", markersize=5, zorder=6)
    ax.plot(Ox, Oy, "o", color="#dc2626", markersize=5, zorder=6)

    ax.text(Ax - 0.15, Ay + 0.4, r"$A(-1,1)$", ha="right", va="bottom",
            fontsize=7.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(Bx + 0.1, By - 0.5, r"$B(3,9)$", ha="left", va="top",
            fontsize=7.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(0.1, -0.3, "$O$", ha="left", va="top", fontsize=8, bbox=_lbl_bbox, zorder=7)

    # S ラベル（重心付近）
    ax.text(0.7, 3.5, r"$S=6$", ha="center", va="center",
            fontsize=9, color="#1d4ed8", bbox=_lbl_bbox, zorder=7)

    ax.text(-1.8, 8, r"$y=x^2$", ha="left", va="center", fontsize=7.5, bbox=_lbl_bbox)
    ax.text(2.3, 4.5, r"$y=2x+3$", ha="left", va="center", fontsize=7.5, color="#2563eb", bbox=_lbl_bbox)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "三角形の面積",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(cx, y_hi - 0.5, "座標から面積を計算",
            ha="center", va="top", fontsize=7.5, color="#6b7280")


def main():
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.5))
    fig.patch.set_facecolor("white")
    draw_panel_intersections(axes[0])
    draw_panel_coordinates(axes[1])
    draw_panel_area(axes[2])
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=0.5)

    fname = "quadratic-graph-line-overview.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
