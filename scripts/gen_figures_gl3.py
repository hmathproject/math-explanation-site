"""
gen_figures_gl3.py — グラフと直線・記事3用図
放物線 y=x² と直線 y=2x+3 の2交点 A(-1,1)、B(3,9) と原点 O を頂点とする三角形

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  ylim は curve_ylim() で実データ範囲から安全に計算する。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_gl3.py
出力:
    figures/quadratic-graph-line-area-combined.png
    assets/images/quadratic-graph-line-area-combined.png
    ../figures/quadratic-graph-line-area-combined.png  （PDF用）
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
Y_YLABEL_OFFSET = 0.45
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
    # x 範囲: -2.2 〜 4.2。共有点 x=-1, x=3
    x = np.linspace(-2.2, 4.2, 500)
    y_para = x**2       # np.clip() 不使用
    y_line = 2*x + 3    # np.clip() 不使用

    # 三角形の頂点
    Ox, Oy = 0, 0
    Ax, Ay = -1, 1
    Bx, By = 3, 9

    y_lo, y_hi = curve_ylim(y_para, extra_y=[Oy, Ay, By, y_line[0], y_line[-1]], margin=0.15)
    y_lo = min(y_lo, -1.0)

    X_LO, X_HI = -2.5, 4.5

    fig, ax = plt.subplots(1, 1, figsize=(7.0, 4.5))
    fig.patch.set_facecolor("white")
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(y_lo - 0.5, y_hi + 0.9)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.45, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.50, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi + 0.55), xytext=(0, y_lo - 0.28),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, y_hi + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)

    # 三角形の塗りつぶし
    ax.fill([Ox, Ax, Bx], [Oy, Ay, By],
            alpha=0.25, color="#2563eb", zorder=1, label="三角形")
    # 三角形の辺（破線）
    ax.plot([Ox, Ax, Bx, Ox], [Oy, Ay, By, Oy],
            color="#1d4ed8", linewidth=1.2, linestyle="--", zorder=3)

    # 放物線（実線）
    ax.plot(x, y_para, color="black", linewidth=2.0, zorder=2)
    # 直線（点線・グレー系）
    ax.plot(x, y_line, color="#2563eb", linewidth=1.5, zorder=2, linestyle="--", alpha=0.6)

    # 3頂点のマーカー
    ax.plot(Ax, Ay, "o", color="#dc2626", markersize=7, zorder=6)
    ax.plot(Bx, By, "o", color="#dc2626", markersize=7, zorder=6)
    ax.plot(Ox, Oy, "o", color="#dc2626", markersize=7, zorder=6)

    # 座標ラベル
    ax.text(Ax - 0.15, Ay + 0.5, r"$A(-1,\ 1)$", ha="right", va="bottom",
            fontsize=9, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(Bx + 0.15, By - 0.3, r"$B(3,\ 9)$", ha="left", va="top",
            fontsize=9, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(Ox + 0.15, Oy - 0.5, r"$O(0,\ 0)$", ha="left", va="top",
            fontsize=9, color="#dc2626", bbox=_lbl_bbox, zorder=7)

    # x 軸刻み
    tick = 0.12
    for xv in [-1, 3]:
        ax.plot([xv, xv], [-tick, tick], "k-", linewidth=0.9, zorder=3)

    # 面積の値（重心付近: ((0-1+3)/3, (0+1+9)/3) ≈ (0.67, 3.33)）
    ax.text(0.8, 3.5, r"$S = 6$", ha="center", va="center",
            fontsize=11, color="#1d4ed8",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="#93c5fd", linewidth=1.0),
            zorder=7)

    # 方程式ラベル
    ax.text(-2.0, 8.0, r"$y = x^2$", ha="left", va="center",
            fontsize=9.5, bbox=_lbl_bbox, zorder=7)
    ax.text(2.2, 6.5, r"$y = 2x + 3$", ha="left", va="center",
            fontsize=9.5, color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text((X_LO + X_HI) / 2, y_hi + 0.20,
            r"$O$, $A(-1,1)$, $B(3,9)$ を頂点とする三角形",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold")

    fig.tight_layout(pad=0.5)

    fname = "quadratic-graph-line-area-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
