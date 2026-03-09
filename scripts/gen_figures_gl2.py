"""
gen_figures_gl2.py — グラフと直線・記事2用図
放物線 y=x² と直線 y=2x+3 の共有点の座標を示す 1パネル図

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  ylim は curve_ylim() で実データ範囲から安全に計算する。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_gl2.py
出力:
    figures/quadratic-graph-line-coordinates-combined.png
    assets/images/quadratic-graph-line-coordinates-combined.png
    ../figures/quadratic-graph-line-coordinates-combined.png  （PDF用）
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
Y_YLABEL_OFFSET = 0.35
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


def main():
    # x 範囲は -1.8 〜 3.5 。x=3 で y=9, x=3.5 で y=12.25
    # 共有点 (-1,1) と (3,9) を収めるため x=3.5 まで描く
    x = np.linspace(-1.8, 3.5, 500)
    y_para = x**2           # np.clip() 不使用
    y_line = 2*x + 3        # np.clip() 不使用

    # 共有点 x=-1, y=1 / x=3, y=9
    pts = [(-1, 1), (3, 9)]

    y_lo, y_hi = curve_ylim(y_para, extra_y=[1, 9, 0, 2*(-1.8)+3], margin=0.15)
    y_lo = min(y_lo, -0.8)

    X_LO, X_HI = -2.0, 3.8

    fig, ax = plt.subplots(1, 1, figsize=(7.0, 4.5))
    fig.patch.set_facecolor("white")
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.42, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.46, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi + 0.48), xytext=(0, y_lo - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, y_hi + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)

    ax.plot(x, y_para, color="black", linewidth=2.0, zorder=2)
    ax.plot(x, y_line, color="#2563eb", linewidth=1.8, zorder=2, linestyle="--")

    # 共有点をマーク
    for px, py in pts:
        ax.plot(px, py, "o", color="#dc2626", markersize=8, zorder=6)

    # 座標ラベル
    ax.text(-1 - 0.2, 1 + 0.5, r"$(-1,\ 1)$", ha="right", va="bottom",
            fontsize=9.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(3 + 0.1, 9 + 0.2, r"$(3,\ 9)$", ha="left", va="bottom",
            fontsize=9.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)

    # 方程式ラベル
    ax.text(2.5, 4.0, r"$y = x^2$", ha="right", va="center",
            fontsize=9.5, bbox=_lbl_bbox, zorder=7)
    ax.text(2.5, 8.0, r"$y = 2x + 3$", ha="left", va="center",
            fontsize=9.5, color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.4, "$O$", ha="left", va="top", fontsize=9, bbox=_lbl_bbox, zorder=7)

    ax.text((X_LO + X_HI) / 2, y_hi + 0.15,
            r"連立して $x^2 = 2x + 3 \Rightarrow (x-3)(x+1) = 0$",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold")

    fig.tight_layout(pad=0.5)

    fname = "quadratic-graph-line-coordinates-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
