"""
gen_figures_seq_arithmetic.py — 等差数列

Panel 1: 点の並び（隣接差 d を矢印で明示）
Panel 2: 和 S_n の台形面積ビジュアル

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_arithmetic.py
出力: figures/seq-arithmetic-combined.png
      assets/images/seq-arithmetic-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
SITE_IMAGES_DIR.mkdir(exist_ok=True)
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#bb6600"


def draw_sequence_dots(ax):
    """Panel 1: 点の並び — 等差数列の各項と差 d の矢印"""
    a1, d, n = 3, 2, 7
    xs = list(range(1, n + 1))
    ys = [a1 + (k - 1) * d for k in xs]

    ax.scatter(xs, ys, color=DARK_BLUE, s=60, zorder=5)

    # 隣接矢印 "+d"
    for i in range(len(xs) - 1):
        ax.annotate(
            "",
            xy=(xs[i + 1], ys[i + 1] - 0.15),
            xytext=(xs[i], ys[i] + 0.15),
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2,
                            mutation_scale=8, shrinkA=3, shrinkB=3),
        )
        mid_x = (xs[i] + xs[i + 1]) / 2 + 0.12
        mid_y = (ys[i] + ys[i + 1]) / 2
        ax.text(mid_x, mid_y, f"+{d}", fontsize=8.5, color=RED,
                ha="left", va="center")

    # n ラベル
    for x, y in zip(xs, ys):
        ax.text(x, y - 0.5, f"$a_{{{x}}}$", ha="center", va="top",
                fontsize=8, color=DARK_BLUE)

    # a_1 と a_n のラベル強調
    ax.text(xs[0] - 0.3, ys[0], f"$a_1={a1}$", ha="right", va="center",
            fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=0.8))
    ax.text(xs[-1] + 0.3, ys[-1], f"$a_n={ys[-1]}$", ha="left", va="center",
            fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=0.8))

    ax.set_xlim(0.2, n + 0.8)
    ax.set_ylim(ys[0] - 1.5, ys[-1] + 1.5)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"$n={x}$" for x in xs], fontsize=8)
    ax.set_ylabel("$a_n$", fontsize=10)
    ax.set_title("等差数列: 隣接差 $d$ が一定", fontsize=10, pad=4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_trapezoid_sum(ax):
    """Panel 2: 和 S_n の台形面積 — 棒グラフ + 台形ライン"""
    a1, d, n = 3, 2, 7
    xs = list(range(1, n + 1))
    ys = [a1 + (k - 1) * d for k in xs]

    bars = ax.bar(xs, ys, color=DARK_BLUE, alpha=0.45, width=0.7, zorder=3)

    # 台形の上辺（a_1 と a_n を結ぶ斜線）
    ax.plot([xs[0] - 0.35, xs[-1] + 0.35],
            [ys[0], ys[-1]], color=ORANGE, lw=2.0, zorder=4, label="台形の斜辺")

    # a_1, a_n の水平破線
    ax.hlines(ys[0], xs[0] - 0.35, xs[-1] + 0.35,
              color=GREEN, lw=1.2, linestyle="--")
    ax.hlines(ys[-1], xs[0] - 0.35, xs[-1] + 0.35,
              color=RED, lw=1.2, linestyle="--")
    ax.text(xs[-1] + 0.5, ys[0], f"$a_1={ys[0]}$",
            ha="left", va="center", fontsize=9, color=GREEN)
    ax.text(xs[-1] + 0.5, ys[-1], f"$a_n={ys[-1]}$",
            ha="left", va="center", fontsize=9, color=RED)

    # S_n の式ラベル
    ax.text(4.0, 10.5,
            r"$S_n = \frac{n}{2}(a_1 + a_n)$" + "\n（台形面積と同じ形）",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))

    ax.set_xlim(0.2, n + 1.5)
    ax.set_ylim(0, ys[-1] + 3)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"$n={x}$" for x in xs], fontsize=8)
    ax.set_ylabel("$a_n$", fontsize=10)
    ax.set_title(r"和 $S_n$ は台形面積", fontsize=10, pad=4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_sequence_dots(axes[0])
    draw_trapezoid_sum(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-arithmetic-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
