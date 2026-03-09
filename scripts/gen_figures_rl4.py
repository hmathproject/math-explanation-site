"""
gen_figures_rl4.py — 解の配置・記事4用概念図
解が区間を挟む: f(α)·f(β)<0 の2パターン

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_rl4.py
出力:
    figures/quadratic-root-location-one-in-interval-combined.png
    assets/images/quadratic-root-location-one-in-interval-combined.png
    ../figures/quadratic-root-location-one-in-interval-combined.png  （PDF用）
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

X_LO, X_HI = -2.5, 5.5
Y_LO, Y_HI = -3.0, 7.0

ALPHA, BETA = 0.0, 3.0


def f_c1(x):
    """f(0)>0, f(3)<0: f(x)=x²-4x+1, 解 2±√3 ≈ 0.27, 3.73"""
    return x ** 2 - 4.0 * x + 1.0


def f_c2(x):
    """f(0)<0, f(3)>0: f(x)=(x+1)(x-2)=x²-x-2, 解 -1, 2"""
    return (x + 1.0) * (x - 2.0)


SQRT3 = 3.0 ** 0.5

CASES = [
    {
        "title": r"$f(0)>0,\ f(3)<0$",
        "f": f_c1,
        "roots": [2.0 - SQRT3, 2.0 + SQRT3],
        "root_labels": [r"$2{-}\sqrt{3}$", r"$2{+}\sqrt{3}$"],
        "f0_color": "#16a34a",   # 緑: f(0)>0
        "f3_color": "#dc2626",   # 赤: f(3)<0
        "f0_val": 1.0,
        "f3_val": -2.0,
        "inside_root_idx": 0,   # 区間内の解のインデックス
        "outside_root_idx": 1,
    },
    {
        "title": r"$f(0)<0,\ f(3)>0$",
        "f": f_c2,
        "roots": [-1.0, 2.0],
        "root_labels": [r"$-1$", r"$2$"],
        "f0_color": "#dc2626",   # 赤: f(0)<0
        "f3_color": "#16a34a",   # 緑: f(3)>0
        "f0_val": -2.0,
        "f3_val": 4.0,
        "inside_root_idx": 1,
        "outside_root_idx": 0,
    },
]


def draw_case(ax, case):
    f = case["f"]
    ax.set_xlim(X_LO - 0.1, X_HI + 0.45)
    ax.set_ylim(Y_LO - 0.5, Y_HI + 0.6)
    ax.axis("off")

    # 区間 (0,3) の薄い網掛け
    ax.axvspan(ALPHA, BETA, ymin=0.0, ymax=1.0,
               color="#bfdbfe", alpha=0.35, zorder=0)

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI + 0.32, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.36, 0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.48), xytext=(0, Y_LO - 0.28),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)

    # 区間端点の破線とラベル
    for xb, lbl in [(ALPHA, r"$0$"), (BETA, r"$3$")]:
        ax.plot([xb, xb], [Y_LO - 0.3, Y_HI + 0.2], "--",
                color="#9ca3af", linewidth=0.8, zorder=1)
        ax.text(xb, Y_LO - 0.38, lbl, ha="center", va="top", fontsize=8.5,
                bbox=_lbl_bbox, zorder=7)

    # 放物線
    x_all = np.linspace(X_LO, X_HI, 600)
    y_all = np.clip(f(x_all), Y_LO - 0.3, Y_HI + 0.3)
    ax.plot(x_all, y_all, color="black", linewidth=2.0, zorder=2)

    # 解の目盛りと open circle
    tick = 0.15
    for i, (r, lbl) in enumerate(zip(case["roots"], case["root_labels"])):
        ax.plot([r, r], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(r, -0.42, lbl, ha="center", va="top", fontsize=8.5,
                bbox=_lbl_bbox, zorder=7)
        ax.plot(r, 0.0, "o", color="white", markeredgecolor="black",
                markersize=5, markeredgewidth=1.2, zorder=5)

    # 区間内・区間外ラベル
    r_in  = case["roots"][case["inside_root_idx"]]
    r_out = case["roots"][case["outside_root_idx"]]
    ax.text(r_in,  -1.0, "区間内", ha="center", va="top", fontsize=7.5,
            color="#1d4ed8", bbox=_lbl_bbox, zorder=7)
    ax.text(r_out, -1.0, "区間外", ha="center", va="top", fontsize=7.5,
            color="#6b7280", bbox=_lbl_bbox, zorder=7)

    # f(0) の点と縦線
    f0 = case["f0_val"]
    ax.plot([0, 0], [0, f0], "-", color=case["f0_color"], linewidth=2.5, zorder=4, alpha=0.8)
    ax.plot(0, f0, "D", color=case["f0_color"], markersize=6, zorder=6)
    sign0 = ">" if f0 > 0 else "<"
    ax.text(-0.3, f0, f"$f(0){sign0}0$", ha="right", va="center", fontsize=8,
            color=case["f0_color"], bbox=_lbl_bbox, zorder=7)

    # f(3) の点と縦線
    f3 = case["f3_val"]
    ax.plot([3, 3], [0, f3], "-", color=case["f3_color"], linewidth=2.5, zorder=4, alpha=0.8)
    ax.plot(3, f3, "D", color=case["f3_color"], markersize=6, zorder=6)
    sign3 = ">" if f3 > 0 else "<"
    ax.text(3.3, f3, f"$f(3){sign3}0$", ha="left", va="center", fontsize=8,
            color=case["f3_color"], bbox=_lbl_bbox, zorder=7)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, case["title"],
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.8))
    fig.patch.set_facecolor("white")
    for ax, case in zip(axes, CASES):
        draw_case(ax, case)
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.0)

    fname = "quadratic-root-location-one-in-interval-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
