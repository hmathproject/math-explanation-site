"""
gen_figures_qi2.py — 記事2用概念図
判別式 D の符号による3ケース（a>0 固定）
3パネル: D>0 / D=0 / D<0 それぞれで f(x)>0 の解の構造を示す

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qi2.py
出力: site/assets/images/quadratic-inequality-discriminant-combined.png
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
SOL_COLOR = "#d97706"
X_LO, X_HI = -4.2, 5.2


def f_dpos(x: np.ndarray) -> np.ndarray:
    """D>0: f(x) = x²-x-6 = (x+2)(x-3)"""
    return x**2 - x - 6


def f_dzero(x: np.ndarray) -> np.ndarray:
    """D=0: f(x) = (x-1)²"""
    return (x - 1.0)**2


def f_dneg(x: np.ndarray) -> np.ndarray:
    """D<0: f(x) = x²+x+1"""
    return x**2 + x + 1.0


# 3ケース定義
# sol_intervals: 図で強調する解の区間（放物線ハイライト + バー）
# is_strict: 端点が開区間か（True=open circle, False=closed）
# roots: x軸上にマークする根（D=0は接点、D<0は空リスト）
CASES = [
    {
        "title": r"D > 0: $f(x) > 0$ の解",
        "f": f_dpos,
        "roots": [-2.0, 3.0],
        "root_labels": [r"$-2$", r"$3$"],
        "sol_intervals": [(-np.inf, -2.0), (3.0, np.inf)],
        "is_strict": True,
        "Y_LO": -8.5, "Y_HI": 16.0, "SOL_Y": -6.8,
    },
    {
        # D=0: f(x)=(x-1)² ≥ 0 は全実数。接点 x=1 のみ f=0。
        # f(x)>0 の解を示す（x≠1 = 全実数から x=1 を除く）
        "title": r"D = 0: $f(x) \geq 0$ の解（全実数）",
        "f": f_dzero,
        "roots": [1.0],
        "root_labels": [r"$1$"],
        "sol_intervals": [(-np.inf, np.inf)],  # 全実数
        "is_strict": False,  # 端点なし（全実数）
        "Y_LO": -2.5, "Y_HI": 9.0, "SOL_Y": -1.8,
    },
    {
        # D<0, a>0: f(x)=x²+x+1 は常に正。
        "title": r"D < 0: $f(x) > 0$ の解（全実数）",
        "f": f_dneg,
        "roots": [],
        "root_labels": [],
        "sol_intervals": [(-np.inf, np.inf)],
        "is_strict": True,
        "Y_LO": -2.5, "Y_HI": 9.0, "SOL_Y": -1.8,
    },
]


def draw_case(ax: matplotlib.axes.Axes, case: dict) -> None:
    Y_LO = case["Y_LO"]
    Y_HI = case["Y_HI"]
    SOL_Y = case["SOL_Y"]
    f = case["f"]

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
    y_all = f(x_all)
    # Y範囲でクリップして描画
    ax.plot(x_all, np.clip(y_all, Y_LO - 0.3, Y_HI + 0.3),
            color="#cccccc", linewidth=1.2, zorder=1)

    # 解に対応する放物線部分（太い黒）
    for (lo, hi) in case["sol_intervals"]:
        lo_c = max(lo if lo != -np.inf else X_LO, X_LO)
        hi_c = min(hi if hi != np.inf else X_HI, X_HI)
        if lo_c < hi_c:
            x_seg = np.linspace(lo_c, hi_c, 300)
            y_seg = np.clip(f(x_seg), Y_LO - 0.3, Y_HI + 0.3)
            ax.plot(x_seg, y_seg, color="black", linewidth=2.3, zorder=2)

    # 根・接点の目盛りとラベル
    tick = 0.28
    lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")
    for r, lbl in zip(case["roots"], case["root_labels"]):
        ax.plot([r, r], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(r, -1.0 if Y_LO < -2 else -0.5, lbl,
                ha="center", va="top", fontsize=9, bbox=lbl_bbox, zorder=7)
        # D=0: 接点は closed circle（等号成立）、D>0: open circle
        fc = "black" if len(case["roots"]) == 1 else "white"
        ax.plot(r, 0.0, "o", color=fc, markeredgecolor="black",
                markersize=5, markeredgewidth=1.2, zorder=5)

    # 解区間バー（橙）
    for (lo, hi) in case["sol_intervals"]:
        lo_d = X_LO if lo == -np.inf else lo
        hi_d = X_HI if hi == np.inf else hi

        ax.plot([lo_d, hi_d], [SOL_Y, SOL_Y],
                color=SOL_COLOR, linewidth=4.0, solid_capstyle="butt", zorder=4)

        ak = dict(arrowstyle="-|>", color=SOL_COLOR,
                  lw=1.5, mutation_scale=8, shrinkA=0, shrinkB=0)
        if lo == -np.inf:
            ax.annotate("", xy=(X_LO - 0.08, SOL_Y),
                        xytext=(X_LO + 0.3, SOL_Y), arrowprops=ak)
        if hi == np.inf:
            ax.annotate("", xy=(X_HI + 0.18, SOL_Y),
                        xytext=(X_HI - 0.3, SOL_Y), arrowprops=ak)

        # 端点マーカー（全実数なので端点なし）
        if lo != -np.inf:
            fc = "white" if case["is_strict"] else SOL_COLOR
            ax.plot(lo, SOL_Y, "o", color=fc, markeredgecolor=SOL_COLOR,
                    markersize=6, markeredgewidth=1.8, zorder=5)
        if hi != np.inf:
            fc = "white" if case["is_strict"] else SOL_COLOR
            ax.plot(hi, SOL_Y, "o", color=fc, markeredgecolor=SOL_COLOR,
                    markersize=6, markeredgewidth=1.8, zorder=5)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + 0.15, case["title"],
            ha="center", va="bottom", fontsize=10, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.5))
    fig.patch.set_facecolor("white")
    for ax, case in zip(axes, CASES):
        draw_case(ax, case)
    fig.tight_layout(pad=0.2, w_pad=0.8)

    fname = "quadratic-inequality-discriminant-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    out_site = SITE_IMAGES_DIR / fname
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
