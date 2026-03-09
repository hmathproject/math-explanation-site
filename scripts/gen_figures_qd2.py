"""
gen_figures_qd2.py — 式の決定・記事2用概念図
頂点形 2パネル横並び
  左: 頂点(-1,2)と点(1,10) → y=2(x+1)²+2
  右: 軸x=1, 2点(0,-1),(3,5) → y=2(x-1)²-3

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  clip() は範囲外の y 値を上限/下限に張り付かせ、水平な黒線に見える。
  ylim は curve_ylim() で実データ範囲から安全に計算する。
  右パネルは x=3.5 で y=9.5 になるため、旧コードの Y_HI=7 では切れていた。

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


def curve_ylim(y_arr, extra_y=(), margin=0.15):
    """
    曲線データと注釈 y 座標から安全な ylim を計算する。

    np.clip() の代わりにこの関数で ylim を決め、ax.set_ylim() に渡す。
    - y_arr  : 曲線の y 値配列（np.ndarray）
    - extra_y: マーカー・ラベル等の追加 y 値リスト
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
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(xhi + 0.35, 0), xytext=(xlo - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xhi + 0.38, 0, r"$x$", ha="left", va="center", fontsize=9)
    ax.annotate("", xy=(0, yhi + 0.48), xytext=(0, ylo - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, yhi + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=9)


def draw_panel_vertex_plus_point(ax):
    """左パネル: 頂点(-1,2)と点(1,10) → y=2(x+1)²+2
    x を -2.8〜1.1 に設定し、点(1,10)まで曲線が届くようにする。
    """
    x = np.linspace(-2.8, 1.1, 500)
    y = 2*(x+1)**2 + 2  # np.clip() は使わない

    # マーカー y 値（頂点 y=2, 通過点 y=10）を含めて ylim を計算
    y_lo, y_hi = curve_ylim(y, extra_y=[2, 10, 0], margin=0.12)
    y_lo = min(y_lo, -0.5)

    X_LO, X_HI = -2.8, 1.5
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.8)
    ax.axis("off")
    draw_axes_custom(ax, (X_LO, X_HI), (y_lo, y_hi))

    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    ax.plot(-1, 2, "s", color="#dc2626", markersize=7, zorder=6)
    ax.text(-0.85, 2.3, r"頂点$(-1,\ 2)$", ha="left", va="bottom", fontsize=8.5,
            color="#dc2626", bbox=_lbl_bbox, zorder=7)

    ax.plot(1, 10, "o", color="#2563eb", markersize=7, zorder=6)
    ax.text(1.1, 10, r"$(1,\ 10)$", ha="left", va="center", fontsize=8.5,
            color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.35, "$O$", ha="left", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    cx = (X_LO + X_HI) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "頂点＋1点 → 頂点形",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(X_LO + 0.2, y_hi * 0.9, r"$y=2(x+1)^2+2$", ha="left", va="top",
            fontsize=8.5)


def draw_panel_axis_plus_two(ax):
    """右パネル: 軸x=1, 2点(0,-1),(3,5) → y=2(x-1)²-3
    旧コードは Y_HI=7 で x=3.5 のとき y=9.5 が切れていた。
    curve_ylim() で実データ範囲から安全に ylim を計算して修正。
    """
    x = np.linspace(-0.6, 3.5, 500)
    y = 2*(x-1)**2 - 3  # np.clip() は使わない

    # マーカー y 値（2点 y=-1,5 と頂点 y=-3）を含めて ylim を計算
    # x=3.5 では y=9.5 になるため、旧コードの Y_HI=7 では切れていた
    y_lo, y_hi = curve_ylim(y, extra_y=[-1, 5, -3, 0], margin=0.12)
    y_lo = min(y_lo, -4.0)

    X_LO, X_HI = -0.8, 4.0
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.8)
    ax.axis("off")
    draw_axes_custom(ax, (X_LO, X_HI), (y_lo, y_hi))

    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    ax.plot([1, 1], [y_lo * 0.9, y_hi - 0.5], "--",
            color="#6b7280", linewidth=1.0, zorder=1)
    ax.text(1.05, y_hi * 0.88, r"軸 $x=1$", ha="left", va="top", fontsize=8,
            color="#6b7280", bbox=_lbl_bbox, zorder=7)

    for px, py, lbl in [(0, -1, r"$(0,\ -1)$"), (3, 5, r"$(3,\ 5)$")]:
        ax.plot(px, py, "o", color="#2563eb", markersize=7, zorder=6)
        ax.text(px + 0.12, py + 0.2, lbl, ha="left", va="bottom", fontsize=8.5,
                color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.3, "$O$", ha="left", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    ax.plot(1, -3, "s", color="#9ca3af", markersize=5, zorder=5)
    ax.text(1.1, -3, r"頂点$(1,\ -3)$", ha="left", va="center", fontsize=7.5,
            color="#9ca3af", bbox=_lbl_bbox, zorder=7)

    cx = (X_LO + X_HI) / 2
    ax.text(cx, y_hi + Y_TITLE_OFFSET, "軸＋2点 → 頂点形",
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")
    ax.text(X_LO + 0.2, y_hi * 0.9, r"$y=2(x-1)^2-3$", ha="left", va="top",
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
