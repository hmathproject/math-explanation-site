"""
gen_figures_seq_sigma.py — Σ記号と基本公式

Panel 1: 三角数の点配置（Σk = n(n+1)/2 の幾何的証明）
Panel 2: Σ の線形性（列 {a_k} と {b_k} を積み上げ）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_sigma.py
出力: figures/seq-sigma-combined.png
      assets/images/seq-sigma-combined.png
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
FIGURES_DIR.mkdir(exist_ok=True)
SITE_IMAGES_DIR.mkdir(exist_ok=True)
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#bb6600"


def draw_triangle_dots(ax):
    """Panel 1: 三角数の点配置 — n=5 の例"""
    n = 5
    ax.set_xlim(-0.5, n + 1.5)
    ax.set_ylim(-0.5, n + 0.8)
    ax.axis("off")
    ax.set_title(r"$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$: 三角数の2倍", fontsize=10, pad=4)

    # 元の三角形（下から k=1, 2, ..., n の行）
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            ax.scatter(col, n + 1 - row, s=100, color=DARK_BLUE, zorder=4)

    # 補完の三角形（180度回転してくっつける）
    for row in range(1, n + 1):
        for col in range(row + 1, n + 2):
            ax.scatter(col, n + 1 - row, s=100, color=ORANGE, alpha=0.6, zorder=3)

    # 矩形の外枠
    ax.add_patch(plt.Rectangle((0.5, 0.5), n, n, fill=False,
                                edgecolor=GREEN, linewidth=1.5, linestyle="--"))

    # ラベル
    ax.text(0.3, (n + 1) / 2, r"$\vdots$" + f"\n{n}行", ha="center", va="center",
            fontsize=9, color=DARK_BLUE)
    ax.text((n + 1) / 2, n + 0.6, r"$n+1$ 列", ha="center", va="bottom",
            fontsize=9, color=GREEN)

    ax.text(n + 1.2, 0.5,
            "青 = 元の三角数\n橙 = 補完分\n合計 = $n(n+1)$\n" +
            r"$\Rightarrow \sum k = \frac{n(n+1)}{2}$",
            ha="left", va="bottom", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def draw_linearity_bars(ax):
    """Panel 2: Σ の線形性 — {a_k} と {b_k} を別色で積み上げ"""
    n = 5
    ks = list(range(1, n + 1))
    aks = [k + 1 for k in ks]       # a_k = k+1
    bks = [2 * k for k in ks]       # b_k = 2k

    # a_k の棒（下部）
    ax.bar(ks, aks, color=DARK_BLUE, alpha=0.6, width=0.4,
           label=r"$a_k$", zorder=3)
    # b_k の棒（上に積み上げ）
    ax.bar(ks, bks, bottom=aks, color=RED, alpha=0.6, width=0.4,
           label=r"$b_k$", zorder=3)

    # 各棒にラベル
    for k, a, b in zip(ks, aks, bks):
        ax.text(k, a / 2, str(a), ha="center", va="center",
                fontsize=8.5, color="white", fontweight="bold")
        ax.text(k, a + b / 2, str(b), ha="center", va="center",
                fontsize=8.5, color="white", fontweight="bold")

    # 合計ラベル
    totals_a = sum(aks)
    totals_b = sum(bks)
    ax.text(3.0, max(a + b for a, b in zip(aks, bks)) + 1.2,
            r"$\sum a_k + \sum b_k = \sum (a_k + b_k)$",
            ha="center", va="bottom", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.8))

    ax.set_xlim(0.2, n + 0.8)
    ax.set_xticks(ks)
    ax.set_xticklabels([f"$k={k}$" for k in ks], fontsize=8.5)
    ax.set_ylabel("値", fontsize=10)
    ax.set_title(r"$\Sigma$ の線形性: $\Sigma(a_k + b_k) = \Sigma a_k + \Sigma b_k$",
                 fontsize=10, pad=4)
    ax.legend(fontsize=9, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_triangle_dots(axes[0])
    draw_linearity_bars(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-sigma-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
