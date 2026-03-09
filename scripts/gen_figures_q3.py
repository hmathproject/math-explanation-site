"""
gen_figures_q3.py — 問3用概念図生成
f(x) = x² - 2x + 2 = (x-1)² + 1、軸 x=1 固定、区間 [a, a+1] が動く
最小値の3ケース（軸が区間の右外・内部・左外）

使い方:
    cd experiments/graph-guided-lessons
    python scripts/gen_figures_q3.py
出力: site/assets/images/quadratic-min-moving-range-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# フォント設定（gen_figures.py と同じ）
if platform.system() == "Darwin":
    plt.rcParams["font.family"] = "Hiragino Sans"
elif platform.system() == "Windows":
    plt.rcParams["font.family"] = "MS Gothic"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["axes.unicode_minus"] = False

BASE_DIR = Path(__file__).parent.parent
FIGURES_DIR = BASE_DIR / "figures"
SITE_IMAGES_DIR = BASE_DIR / "site" / "assets" / "images"
FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150


def f(x: np.ndarray) -> np.ndarray:
    """f(x) = x² - 2x + 2 = (x-1)² + 1、軸 x=1"""
    return x**2 - 2 * x + 2


# 3ケース（代表値で区間を設定）
CASES = [
    {
        # ① a ≤ 0: 区間が軸の右外（右端 a+1 ≤ 1）
        # 代表値 a = -0.5 → 区間 [-0.5, 0.5]
        "min_x": 0.5,           # 最小点: 右端 x = a+1（軸 x=1 に最も近い）
        "axis_x": 1.0,
        "int_lo": -0.5,
        "int_hi": 0.5,
        "x_labels": {-0.5: r"$a$", 0.5: r"$a\!+\!1$", 1.0: r"$1$"},
        "title": r"① $a \leq 0$",
    },
    {
        # ② 0 < a < 1: 軸が区間の内部
        # 代表値 a = 0.5 → 区間 [0.5, 1.5]
        "min_x": 1.0,           # 最小点: 頂点 x=1（軸が区間内にある）
        "axis_x": 1.0,
        "int_lo": 0.5,
        "int_hi": 1.5,
        "x_labels": {0.5: r"$a$", 1.5: r"$a\!+\!1$", 1.0: r"$1$"},
        "title": r"② $0 < a < 1$",
    },
    {
        # ③ a ≥ 1: 区間が軸の左外（左端 a ≥ 1）
        # 代表値 a = 1.5 → 区間 [1.5, 2.5]
        "min_x": 1.5,           # 最小点: 左端 x = a（軸 x=1 に最も近い）
        "axis_x": 1.0,
        "int_lo": 1.5,
        "int_hi": 2.5,
        "x_labels": {1.5: r"$a$", 2.5: r"$a\!+\!1$", 1.0: r"$1$"},
        "title": r"③ $a \geq 1$",
    },
]

# 表示範囲（3ケース全体を収める）
X_LO, X_HI = -1.0, 3.2
Y_LO, Y_HI = -0.4, 5.5


def draw_concept(ax: matplotlib.axes.Axes, case: dict) -> None:
    """gen_figures.py の draw_concept と同構造。問3向けパラメータに対応。"""
    min_x  = case["min_x"]
    axis_x = case["axis_x"]
    int_lo = case["int_lo"]
    int_hi = case["int_hi"]

    min_y    = float(f(np.array([min_x]))[0])
    vertex_y = float(f(np.array([axis_x]))[0])

    ax.set_xlim(X_LO - 0.1, X_HI + 0.25)
    ax.set_ylim(Y_LO - 0.2, Y_HI + 0.35)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸（矢印付き）
    ax.annotate("", xy=(X_HI + 0.2, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.24, -0.02, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸（矢印付き）
    ax.annotate("", xy=(0, Y_HI + 0.25), xytext=(0, Y_LO - 0.1),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.04, Y_HI + 0.27, r"$y$", ha="left", va="bottom", fontsize=10)

    # 全体放物線（薄いグレー）
    x_all = np.linspace(X_LO, X_HI, 600)
    ax.plot(x_all, f(x_all), color="#cccccc", linewidth=1.0, zorder=1, clip_on=False)

    # 区間の放物線（太い黒）
    x_int = np.linspace(int_lo, int_hi, 300)
    ax.plot(x_int, f(x_int), color="black", linewidth=2.3, zorder=2, clip_on=False)

    # 軸の破線（頂点と x 軸を結ぶ）
    y_dash_bot = min(0.0, vertex_y) - 0.02
    y_dash_top = max(0.0, vertex_y) + 0.02
    y_dash_top = min(y_dash_top, Y_HI)
    ax.plot([axis_x, axis_x], [y_dash_bot, y_dash_top],
            color="#888888", linewidth=0.9, linestyle="--", zorder=1)

    # x 軸上の目盛り
    tick = 0.06
    for xv in {int_lo, int_hi, axis_x}:
        if X_LO <= xv <= X_HI:
            ax.plot([xv, xv], [-tick, tick], "k-", linewidth=0.9, zorder=3)

    # x 軸ラベル（白背景で重なり防止）
    _lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")
    lbl_y = -(abs(Y_LO) * 0.12 + 0.05)
    for xv, lbl in case["x_labels"].items():
        if X_LO <= xv <= X_HI:
            ax.text(xv, lbl_y, lbl, ha="center", va="top", fontsize=9,
                    bbox=_lbl_bbox, zorder=7)

    # 頂点（白丸）
    if Y_LO <= vertex_y <= Y_HI:
        ax.plot(axis_x, vertex_y, "o",
                color="white", markeredgecolor="black",
                markersize=5, markeredgewidth=1.2, zorder=5)

    # 最小点（黒塗り）
    ax.plot(min_x, min_y, "ko", markersize=6, zorder=6)

    # 最小点から x 軸への点線（最小点が頂点と異なるケースのみ）
    if abs(min_y) > 0.02 and min_x != axis_x:
        ax.plot([min_x, min_x], [0.0, min_y],
                color="black", linewidth=0.7, linestyle=":", zorder=1)

    # ケースタイトル（上部）
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + 0.12, case["title"],
            ha="center", va="bottom", fontsize=11, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.0))
    fig.patch.set_facecolor("white")
    for ax, case in zip(axes, CASES):
        draw_concept(ax, case)
    fig.tight_layout(pad=0.2, w_pad=0.8)

    fname = "quadratic-min-moving-range-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    out_site = SITE_IMAGES_DIR / fname
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
