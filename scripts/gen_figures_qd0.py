"""
gen_figures_qd0.py — 式の決定 単元トップ overview 図
3パネル横並び（一般形・頂点形・因数形）

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  clip() は範囲外の y 値を上限/下限に張り付かせ、水平な黒線に見える。
  代わりに ylim を実データ範囲から決めるか、x 範囲を絞って y 値が ylim 内に収まるようにする。

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


def curve_ylim(y_arr, extra_y=(), margin=0.15):
    """
    曲線データと注釈 y 座標から安全な ylim を計算する。

    np.clip() の代わりにこの関数で ylim を決め、ax.set_ylim() に渡す。
    - y_arr  : 曲線の y 値配列（np.ndarray）
    - extra_y: マーカー・ラベル等、ylim に含めたい追加の y 値のリスト
    - margin : y スパンに対する上下余白の割合（デフォルト 15%）
    Returns : (y_lo, y_hi)
    """
    y_all = list(y_arr) + list(extra_y)
    y_min, y_max = min(y_all), max(y_all)
    span = max(y_max - y_min, 1.0)
    return y_min - margin * span, y_max + margin * span


def draw_axes_custom(ax, xlim, ylim):
    xlo, xhi = xlim
    ylo, yhi = ylim
    arrow_kw = dict(color="black", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(xhi + 0.3, 0), xytext=(xlo - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xhi + 0.33, 0, r"$x$", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(0, yhi + 0.45), xytext=(0, ylo - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.12, yhi + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=8.5)


def draw_panel_general(ax):
    """一般形: 3点を通る放物線 y=2x²-5x+3 with points (0,3),(1,0),(2,1)
    x 範囲を -0.3〜2.8 に絞ることで放物線が y=5 以内に収まる（頂点付近だけを表示）。
    """
    # x 範囲を絞って y の急上昇を回避（x=3.5 では y=10 になりすぎる）
    x = np.linspace(-0.3, 2.8, 400)
    y = 2*x**2 - 5*x + 3  # np.clip() は使わない

    # ylim を実データ + ラベル y 値から計算
    extra_y = [3, 0, 1, 0.5]  # 3点の y 値 + 余白用
    y_lo, y_hi = curve_ylim(y, extra_y=extra_y, margin=0.15)
    y_lo = min(y_lo, -0.5)

    XL, XH = -0.5, 3.0
    ax.set_xlim(XL - 0.1, XH + 0.4)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.5)
    ax.axis("off")
    draw_axes_custom(ax, (XL, XH), (y_lo, y_hi))

    ax.plot(x, y, color="black", linewidth=1.8, zorder=2)

    pts = [(0, 3), (1, 0), (2, 1)]
    labels = [r"$(0,3)$", r"$(1,0)$", r"$(2,1)$"]
    offsets = [(0.15, 0.2), (0.15, 0.2), (0.15, 0.2)]
    for (px, py), lbl, (dx, dy) in zip(pts, labels, offsets):
        ax.plot(px, py, "o", color="#2563eb", markersize=6, zorder=6)
        ax.text(px + dx, py + dy, lbl, ha="left", va="bottom", fontsize=8,
                color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.15, -0.25, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "一般形：3点が与えられたとき",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(2.6, 4.0, r"$y=ax^2+bx+c$", ha="right", va="center", fontsize=7.5)


def draw_panel_vertex(ax):
    """頂点形: 頂点(-1,2)と点(1,10) → y=2(x+1)²+2
    x 範囲を -2.7〜1.1 として点(1,10)まで曲線が届くようにする。
    """
    x = np.linspace(-2.7, 1.1, 400)
    y = 2*(x+1)**2 + 2  # np.clip() は使わない

    # マーカー y 値も含めて ylim 計算
    extra_y = [2, 10, 0]
    y_lo, y_hi = curve_ylim(y, extra_y=extra_y, margin=0.12)
    y_lo = min(y_lo, -0.5)

    XL, XH = -3.0, 2.0
    ax.set_xlim(XL - 0.1, XH + 0.4)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.8)
    ax.axis("off")
    draw_axes_custom(ax, (XL, XH), (y_lo, y_hi))

    ax.plot(x, y, color="black", linewidth=1.8, zorder=2)

    ax.plot(-1, 2, "s", color="#dc2626", markersize=6, zorder=6)
    ax.text(-0.8, 2, r"頂点$(-1,2)$", ha="left", va="center", fontsize=7.5,
            color="#dc2626", bbox=_lbl_bbox, zorder=7)

    ax.plot(1, 10, "o", color="#2563eb", markersize=6, zorder=6)
    ax.text(1.1, 10, r"$(1,10)$", ha="left", va="center", fontsize=7.5,
            color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.3, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "頂点形：頂点・軸が与えられたとき",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(-2.8, y_hi * 0.85, r"$y=a(x-p)^2+q$", ha="left", va="center", fontsize=7.5)


def draw_panel_factor(ax):
    """因数形: x=1,x=3が解, y=2(x-1)(x-3), 点(0,6)
    x 範囲を -0.1〜4.1 に変更（-0.5 始まりでは左端 y=10.5 がオーバーした）。
    """
    # x=-0.5 では y=10.5 になりすぎるため、-0.1 始まりで y max ≈ 6.8 に抑える
    x = np.linspace(-0.1, 4.1, 400)
    y = 2*(x-1)*(x-3)  # np.clip() は使わない

    extra_y = [0, 6, -2]
    y_lo, y_hi = curve_ylim(y, extra_y=extra_y, margin=0.15)
    y_lo = min(y_lo, -2.5)

    XL, XH = -0.3, 4.3
    ax.set_xlim(XL - 0.1, XH + 0.4)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.5)
    ax.axis("off")
    draw_axes_custom(ax, (XL, XH), (y_lo, y_hi))

    ax.plot(x, y, color="black", linewidth=1.8, zorder=2)

    tick = 0.12
    for xr, lbl in [(1, r"$\alpha=1$"), (3, r"$\beta=3$")]:
        ax.plot([xr, xr], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.plot(xr, 0, "o", color="white", markeredgecolor="#dc2626",
                markersize=5, markeredgewidth=1.5, zorder=5)
        ax.text(xr, -0.35, lbl, ha="center", va="top", fontsize=7.5,
                color="#dc2626", bbox=_lbl_bbox, zorder=7)

    ax.plot(0, 6, "o", color="#2563eb", markersize=6, zorder=6)
    ax.text(0.15, 6, r"$(0,6)$", ha="left", va="center", fontsize=7.5,
            color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.35, "$O$", ha="left", va="top", fontsize=8,
            bbox=_lbl_bbox, zorder=7)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "因数形：2つの解が与えられたとき",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(4.2, y_hi * 0.78, r"$y=a(x-\alpha)(x-\beta)$",
            ha="right", va="center", fontsize=7.5)


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
