"""
gen_figures_qi1.py — 記事1用概念図
f(x) = x²-x-6 = (x+2)(x-3)、根 x=-2, 3
2パネル: (1) f(x)>0 の解、(2) f(x)<0 の解

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qi1.py
出力: site/assets/images/quadratic-inequality-basics-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib
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
FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150

X_LO, X_HI = -4.2, 5.2
Y_LO, Y_HI = -8.5, 16.0
SOL_Y = -6.8   # 解区間バーのy座標（x軸より下）
SOL_COLOR = "#d97706"


def f(x: np.ndarray) -> np.ndarray:
    return x**2 - x - 6


ROOTS = [-2.0, 3.0]

CASES = [
    {
        "title": r"① $f(x) > 0$ の解",
        "sol_intervals": [(-np.inf, -2.0), (3.0, np.inf)],
        "is_strict": True,
    },
    {
        "title": r"② $f(x) < 0$ の解",
        "sol_intervals": [(-2.0, 3.0)],
        "is_strict": True,
    },
]


def draw_case(ax: matplotlib.axes.Axes, case: dict) -> None:
    ax.set_xlim(X_LO - 0.1, X_HI + 0.35)
    ax.set_ylim(Y_LO - 0.5, Y_HI + 0.65)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI + 0.28, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.32, 0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.5), xytext=(0, Y_LO - 0.25),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + 0.52, r"$y$", ha="left", va="bottom", fontsize=10)

    # 全体放物線（薄いグレー）
    x_all = np.linspace(X_LO, X_HI, 600)
    ax.plot(x_all, f(x_all), color="#cccccc", linewidth=1.2, zorder=1)

    # 解に対応する放物線部分（太い黒）
    for (lo, hi) in case["sol_intervals"]:
        lo_c = max(lo if lo != -np.inf else X_LO, X_LO)
        hi_c = min(hi if hi != np.inf else X_HI, X_HI)
        if lo_c < hi_c:
            x_seg = np.linspace(lo_c, hi_c, 300)
            ax.plot(x_seg, f(x_seg), color="black", linewidth=2.3, zorder=2)

    # 根の目盛り・ラベル・x軸上の open circle
    tick = 0.28
    lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")
    for r, lbl in zip(ROOTS, [r"$-2$", r"$3$"]):
        ax.plot([r, r], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(r, -1.0, lbl, ha="center", va="top", fontsize=9,
                bbox=lbl_bbox, zorder=7)
        ax.plot(r, 0.0, "o", color="white", markeredgecolor="black",
                markersize=5, markeredgewidth=1.2, zorder=5)

    # 解区間バー（橙）
    for (lo, hi) in case["sol_intervals"]:
        lo_d = X_LO if lo == -np.inf else lo
        hi_d = X_HI if hi == np.inf else hi

        ax.plot([lo_d, hi_d], [SOL_Y, SOL_Y],
                color=SOL_COLOR, linewidth=4.0, solid_capstyle="butt", zorder=4)

        # 無限大方向の矢印
        ak = dict(arrowstyle="-|>", color=SOL_COLOR,
                  lw=1.5, mutation_scale=8, shrinkA=0, shrinkB=0)
        if lo == -np.inf:
            ax.annotate("", xy=(X_LO - 0.08, SOL_Y),
                        xytext=(X_LO + 0.3, SOL_Y), arrowprops=ak)
        if hi == np.inf:
            ax.annotate("", xy=(X_HI + 0.18, SOL_Y),
                        xytext=(X_HI - 0.3, SOL_Y), arrowprops=ak)

        # 端点マーカー（strict → open circle）
        fc = "white" if case["is_strict"] else SOL_COLOR
        if lo != -np.inf:
            ax.plot(lo, SOL_Y, "o", color=fc, markeredgecolor=SOL_COLOR,
                    markersize=6, markeredgewidth=1.8, zorder=5)
        if hi != np.inf:
            ax.plot(hi, SOL_Y, "o", color=fc, markeredgecolor=SOL_COLOR,
                    markersize=6, markeredgewidth=1.8, zorder=5)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + 0.15, case["title"],
            ha="center", va="bottom", fontsize=10, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")
    for ax, case in zip(axes, CASES):
        draw_case(ax, case)
    fig.tight_layout(pad=0.2, w_pad=0.8)

    fname = "quadratic-inequality-basics-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    out_site = SITE_IMAGES_DIR / fname
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
