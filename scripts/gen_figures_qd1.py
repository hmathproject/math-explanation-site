"""
gen_figures_qd1.py — 式の決定・記事1用概念図
3点を通る放物線 y=2x²-5x+3 と3つの与えられた点を1パネルで表示

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qd1.py
出力:
    figures/quadratic-determine-3points-combined.png
    assets/images/quadratic-determine-3points-combined.png
    ../figures/quadratic-determine-3points-combined.png  （PDF用）
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
Y_YLABEL_OFFSET = 0.27
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")

X_LO, X_HI = -0.8, 3.2
Y_LO, Y_HI = -0.8, 6.5


def main():
    fig, ax = plt.subplots(1, 1, figsize=(7.0, 4.5))
    fig.patch.set_facecolor("white")
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.42, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.46, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, Y_HI + 0.48), xytext=(0, Y_LO - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)

    # 放物線 y=2x²-5x+3
    x = np.linspace(-0.5, 3.1, 500)
    y = np.clip(2*x**2 - 5*x + 3, Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    # 式ラベル
    ax.text(3.0, 5.8, r"$y = 2x^2 - 5x + 3$", ha="right", va="center", fontsize=9.5,
            bbox=_lbl_bbox, zorder=7)

    # 3点
    pts = [(0, 3), (1, 0), (2, 1)]
    pt_labels = [r"$(0,\ 3)$", r"$(1,\ 0)$", r"$(2,\ 1)$"]
    pt_offsets = [(0.12, 0.25), (0.12, 0.3), (0.12, 0.25)]
    for (px, py), lbl, (dx, dy) in zip(pts, pt_labels, pt_offsets):
        ax.plot(px, py, "o", color="#2563eb", markersize=7, zorder=6)
        ax.text(px + dx, py + dy, lbl, ha="left", va="bottom", fontsize=9,
                color="#2563eb", bbox=_lbl_bbox, zorder=7)

    # 原点
    tick = 0.10
    ax.plot([0, 0], [-tick, tick], "k-", linewidth=0.9, zorder=3)
    ax.text(0, -0.28, "$O$", ha="center", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    # タイトル
    ax.text((X_LO + X_HI) / 2, Y_HI + 0.20,
            "3点を通る放物線（一般形で連立方程式を立てる）",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold")

    fig.tight_layout(pad=0.5)

    fname = "quadratic-determine-3points-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
