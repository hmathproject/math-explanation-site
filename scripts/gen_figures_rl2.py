"""
gen_figures_rl2.py — 解の配置・記事2用概念図
2解が異符号: f(0)<0（異符号）vs f(0)>0（同符号）の対比 2パネル

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_rl2.py
出力:
    figures/quadratic-root-location-opposite-sign-combined.png
    assets/images/quadratic-root-location-opposite-sign-combined.png
    ../figures/quadratic-root-location-opposite-sign-combined.png  （PDF用）
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

X_LO, X_HI = -3.5, 4.5
Y_LO_CASE1, Y_HI_CASE1 = -4.0, 8.0   # f(0)<0: f(0)=-3 が見える範囲
Y_LO_CASE2, Y_HI_CASE2 = -1.5, 8.0   # f(0)>0: 全体が上側


def f_opp(x):
    """f(0)<0: f(x) = x²-3, 解 ±√3 ≈ ±1.73"""
    return x ** 2 - 3.0


def f_same(x):
    """f(0)>0: f(x) = (x-1)(x-3) = x²-4x+3, 解 1,3 ともに正"""
    return (x - 1.0) * (x - 3.0)


CASES = [
    {
        "title": r"$f(0) < 0$（2解が異符号）",
        "f": f_opp,
        "Y_LO": Y_LO_CASE1, "Y_HI": Y_HI_CASE1,
        "roots": [-3.0 ** 0.5, 3.0 ** 0.5],
        "root_labels": [r"$-\sqrt{3}$", r"$\sqrt{3}$"],
        "f0_color": "#dc2626",   # 赤: f(0)<0 を強調
        "f0_text": r"$f(0)=-3<0$",
        "f0_offset": (1.2, 0.5),
        "cond_text": "← 0 を挟んで異符号",
        "cond_y": -3.4,
    },
    {
        "title": r"$f(0) > 0$（2解が同符号）",
        "f": f_same,
        "Y_LO": Y_LO_CASE2, "Y_HI": Y_HI_CASE2,
        "roots": [1.0, 3.0],
        "root_labels": [r"$1$", r"$3$"],
        "f0_color": "#16a34a",   # 緑: f(0)>0 を強調
        "f0_text": r"$f(0)=3>0$",
        "f0_offset": (1.2, 0.5),
        "cond_text": None,
    },
]


def draw_case(ax, case):
    f = case["f"]
    Y_LO = case["Y_LO"]
    Y_HI = case["Y_HI"]
    ax.set_xlim(X_LO - 0.1, X_HI + 0.45)
    ax.set_ylim(Y_LO - 0.5, Y_HI + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI + 0.32, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.36, 0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.48), xytext=(0, Y_LO - 0.28),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)

    # 放物線（全体）
    x_all = np.linspace(X_LO, X_HI, 600)
    y_all = np.clip(f(x_all), Y_LO - 0.3, Y_HI + 0.3)
    ax.plot(x_all, y_all, color="black", linewidth=2.0, zorder=2)

    # 解の目盛り・ラベル・open circle
    tick = 0.15 if Y_LO < -2 else 0.10
    lbl_y = -0.6 if Y_LO < -2 else -0.25
    for r, lbl in zip(case["roots"], case["root_labels"]):
        ax.plot([r, r], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(r, lbl_y, lbl, ha="center", va="top", fontsize=9,
                bbox=_lbl_bbox, zorder=7)
        ax.plot(r, 0.0, "o", color="white", markeredgecolor="black",
                markersize=5, markeredgewidth=1.2, zorder=5)

    # 原点 O
    ax.plot([0, 0], [-tick, tick], "k-", linewidth=0.9, zorder=3)
    ax.text(0, lbl_y, "$O$", ha="center", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    # f(0) の点を強調 + x=0 から f(0) への縦線
    f0 = float(f(0.0))
    clr = case["f0_color"]
    # x=0 → f(0) の縦セグメント（f(0) の符号を視覚化）
    ax.plot([0, 0], [0, f0], "-", color=clr, linewidth=2.5, zorder=4, alpha=0.7)
    ax.plot(0, f0, "D", color=clr, markersize=6, zorder=6)

    dx, dy = case["f0_offset"]
    ax.annotate(case["f0_text"],
                xy=(0, f0), xytext=(dx, f0 + dy),
                fontsize=9, color=clr,
                arrowprops=dict(arrowstyle="-", color=clr, lw=0.8),
                bbox=dict(facecolor="white", edgecolor="none", pad=0.05))

    # 「0を挟んで異符号」テキスト（case1 のみ）
    if case.get("cond_text"):
        ax.text((case["roots"][0] + case["roots"][1]) / 2,
                case["cond_y"], case["cond_text"],
                ha="center", va="center", fontsize=8, color="#6b7280",
                bbox=_lbl_bbox)

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

    fname = "quadratic-root-location-opposite-sign-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
