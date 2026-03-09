"""
gen_figures_rl0.py — 解の配置・単元トップ用概念図（4種の配置パターン一覧）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_rl0.py
出力:
    figures/quadratic-root-location-overview.png
    assets/images/quadratic-root-location-overview.png
    ../figures/quadratic-root-location-overview.png  （PDF用）
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
CASE_TITLE_FONTSIZE = 9.5
TIGHT_LAYOUT_PAD    = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")

X_LO, X_HI = -3.5, 4.5
Y_LO, Y_HI = -1.5, 6.0

SQRT3 = 3.0 ** 0.5


def f1(x):
    return (x - 1.0) * (x - 2.0)     # ともに正（記事1用）


def f2(x):
    return x ** 2 - 3.0               # 異符号（記事2用）


def f3(x):
    return (x - 1.0) * (x - 2.0)     # 区間内（記事3, f1と同じ）


def f4(x):
    return x ** 2 - 4.0 * x + 1.0    # 区間挟む（記事4用）


CASES = [
    {
        "title": "① 2解が同符号（ともに正）",
        "subtitle": r"$f(0)>0,\ $ 軸 $>0$",
        "f": f1,
        "roots": [1.0, 2.0],
        "root_labels": [r"$1$", r"$2$"],
        "show_interval": False,
        "y_lo": -0.8, "y_hi": 5.0,
    },
    {
        "title": "② 2解が異符号",
        "subtitle": r"$f(0)<0$",
        "f": f2,
        "roots": [-SQRT3, SQRT3],
        "root_labels": [r"$-\sqrt{3}$", r"$\sqrt{3}$"],
        "show_interval": False,
        "y_lo": -3.5, "y_hi": 8.5,
    },
    {
        "title": "③ 2解がともに区間内",
        "subtitle": r"$D\geq0,\ f(0)>0,\ f(3)>0,\ 0<$ 軸 $<3$",
        "f": f3,
        "roots": [1.0, 2.0],
        "root_labels": [r"$1$", r"$2$"],
        "show_interval": True,
        "y_lo": -0.8, "y_hi": 5.0,
    },
    {
        "title": "④ 解が区間を挟む",
        "subtitle": r"$f(0)\cdot f(3)<0$",
        "f": f4,
        "roots": [2.0 - SQRT3, 2.0 + SQRT3],
        "root_labels": [r"$2{-}\sqrt{3}$", r"$2{+}\sqrt{3}$"],
        "show_interval": True,
        "y_lo": -3.0, "y_hi": 7.0,
    },
]


def draw_case(ax, case):
    f = case["f"]
    Y_LO = case["y_lo"]
    Y_HI = case["y_hi"]
    ax.set_xlim(X_LO - 0.1, X_HI + 0.45)
    ax.set_ylim(Y_LO - 0.5, Y_HI + 0.6)
    ax.axis("off")

    # 区間 (0,3) の薄い網掛け（③④のみ）
    if case["show_interval"]:
        ax.axvspan(0.0, 3.0, ymin=0.0, ymax=1.0,
                   color="#bfdbfe", alpha=0.35, zorder=0)
        for xb, lbl in [(0.0, r"$0$"), (3.0, r"$3$")]:
            ax.plot([xb, xb], [Y_LO - 0.3, Y_HI + 0.2], "--",
                    color="#9ca3af", linewidth=0.8, zorder=1)
            ax.text(xb, Y_LO - 0.38, lbl, ha="center", va="top", fontsize=8,
                    bbox=_lbl_bbox, zorder=7)

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI + 0.32, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.36, 0, r"$x$", ha="left", va="center", fontsize=9.5)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.48), xytext=(0, Y_LO - 0.28),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=9.5)

    # 放物線
    x_all = np.linspace(X_LO, X_HI, 600)
    y_all = np.clip(f(x_all), Y_LO - 0.3, Y_HI + 0.3)
    ax.plot(x_all, y_all, color="black", linewidth=2.0, zorder=2)

    # 解の目盛り・ラベル・open circle
    tick = 0.13 if Y_LO > -1 else 0.18
    lbl_y = -0.3 if Y_LO > -1 else -0.5
    for r, lbl in zip(case["roots"], case["root_labels"]):
        ax.plot([r, r], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(r, lbl_y, lbl, ha="center", va="top", fontsize=8.5,
                bbox=_lbl_bbox, zorder=7)
        ax.plot(r, 0.0, "o", color="white", markeredgecolor="black",
                markersize=5, markeredgewidth=1.2, zorder=5)

    # 原点 O（区間がないパネルのみ）
    if not case["show_interval"]:
        ax.plot([0, 0], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(0, lbl_y, "$O$", ha="center", va="top", fontsize=8.5,
                bbox=_lbl_bbox, zorder=7)

    # サブタイトル（条件要約）
    ax.text((X_LO + X_HI) / 2, Y_LO + 0.05,
            case["subtitle"], ha="center", va="bottom",
            fontsize=7.5, color="#374151", bbox=_lbl_bbox)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, case["title"],
            ha="center", va="bottom",
            fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 4, figsize=(18.0, 4.5))
    fig.patch.set_facecolor("white")
    for ax, case in zip(axes, CASES):
        draw_case(ax, case)
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=0.8)

    fname = "quadratic-root-location-overview.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
