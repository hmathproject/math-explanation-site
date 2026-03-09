"""
gen_figures_gl1.py — グラフと直線・記事1用図
放物線 y=x² と直線 y=x+k の共有点の個数（D>0/D=0/D<0 の3パターン）

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  ylim は curve_ylim() で実データ範囲から安全に計算する。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_gl1.py
出力:
    figures/quadratic-graph-line-intersections-combined.png
    assets/images/quadratic-graph-line-intersections-combined.png
    ../figures/quadratic-graph-line-intersections-combined.png  （PDF用）
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


def draw_panel(ax, k, title, case_label, show_D):
    """
    放物線 y=x² と直線 y=x+k を描く共通ルーティン。
    - k   : 直線の定数項
    - title : パネルタイトル
    - case_label : D の値の説明文
    - show_D : D > 0 のとき交点を表示するか
    """
    x = np.linspace(-1.5, 2.5, 500)
    y_para = x**2           # np.clip() 不使用
    y_line = x + k          # np.clip() 不使用

    extra = [0, k, k + 2.5]  # 直線端点 y 値も含めて ylim を計算
    if show_D == "positive":
        # x = (1 ± sqrt(1+4k)) / 2
        sq = np.sqrt(1 + 4*k)
        x1 = (1 - sq) / 2
        x2 = (1 + sq) / 2
        extra += [x1**2, x2**2]
    elif show_D == "zero":
        xt = 0.5
        extra += [xt**2]

    y_lo, y_hi = curve_ylim(y_para, extra_y=extra, margin=0.15)
    y_lo = min(y_lo, -0.8)

    XL, XH = -1.5, 2.7
    ax.set_xlim(XL - 0.1, XH + 0.5)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.6)
    ax.axis("off")
    draw_axes_custom(ax, (XL, XH), (y_lo, y_hi))

    ax.plot(x, y_para, color="black", linewidth=2.0, zorder=2, label=r"$y=x^2$")
    ax.plot(x, y_line, color="#2563eb", linewidth=1.8, zorder=2,
            linestyle="--", label=rf"$y=x+k$")

    ax.text(0.12, -0.4, "$O$", ha="left", va="top", fontsize=9, bbox=_lbl_bbox, zorder=7)
    ax.text(2.2, 5.5, r"$y=x^2$", ha="right", va="center", fontsize=8.5, bbox=_lbl_bbox, zorder=7)

    if show_D == "positive":
        sq = np.sqrt(1 + 4*k)
        x1 = (1 - sq) / 2
        x2 = (1 + sq) / 2
        ax.plot(x1, x1**2, "o", color="#dc2626", markersize=7, zorder=6)
        ax.plot(x2, x2**2, "o", color="#dc2626", markersize=7, zorder=6)
        ax.text(-0.5, 1.0, "2点で交わる", ha="center", va="bottom",
                fontsize=8, color="#dc2626", bbox=_lbl_bbox, zorder=7)
        ax.text(XL + 0.1, y_hi * 0.88, f"$D = 1+4k > 0$\n$(k > -\\dfrac{{1}}{{4}})$",
                ha="left", va="top", fontsize=8.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)

    elif show_D == "zero":
        xt = 0.5
        yt = xt**2
        ax.plot(xt, yt, "o", color="#dc2626", markersize=8, zorder=6,
                markeredgecolor="#dc2626", markerfacecolor="white", markeredgewidth=2)
        ax.text(xt + 0.15, yt + 0.3, "接する（1点）",
                ha="left", va="bottom", fontsize=8, color="#dc2626", bbox=_lbl_bbox, zorder=7)
        ax.text(XL + 0.1, y_hi * 0.88, r"$D = 1+4k = 0$" + "\n" + r"$(k = -\dfrac{1}{4})$",
                ha="left", va="top", fontsize=8.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)

    elif show_D == "negative":
        ax.text(0.5, 2.0, "交わらない（0点）",
                ha="center", va="bottom", fontsize=8, color="#dc2626", bbox=_lbl_bbox, zorder=7)
        ax.text(XL + 0.1, y_hi * 0.88, r"$D = 1+4k < 0$" + "\n" + r"$(k < -\dfrac{1}{4})$",
                ha="left", va="top", fontsize=8.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, title,
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.5))
    fig.patch.set_facecolor("white")

    draw_panel(axes[0], k=1,    title="D > 0（2点で交わる）",  case_label="D>0", show_D="positive")
    draw_panel(axes[1], k=-0.25, title="D = 0（接する）",       case_label="D=0", show_D="zero")
    draw_panel(axes[2], k=-1,   title="D < 0（交わらない）",    case_label="D<0", show_D="negative")

    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.0)

    fname = "quadratic-graph-line-intersections-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
