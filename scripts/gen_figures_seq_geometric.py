"""
gen_figures_seq_geometric.py — 等比数列

Panel 1: 比率バー図（棒が等比的に伸びる）
Panel 2: ずらし引き — S_n と rS_n を並べて差を可視化

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_geometric.py
出力: figures/seq-geometric-combined.png
      assets/images/seq-geometric-combined.png
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


def draw_geometric_bars(ax):
    """Panel 1: 等比数列の棒グラフ（a_1=2, r=2, n=1..6）"""
    a1, r, n = 2, 2, 6
    xs = list(range(1, n + 1))
    ys = [a1 * (r ** (k - 1)) for k in xs]

    bars = ax.bar(xs, ys, color=DARK_BLUE, alpha=0.55, width=0.6, zorder=3)

    labels = [r"$a_1$", r"$a_1 r$", r"$a_1 r^2$",
              r"$a_1 r^3$", r"$a_1 r^4$", r"$a_1 r^5$"]
    vals   = ["2", "4", "8", "16", "32", "64"]

    for x, y, lbl, val in zip(xs, ys, labels, vals):
        ax.text(x, y + 0.8, lbl, ha="center", va="bottom", fontsize=8.5,
                color=DARK_BLUE)
        ax.text(x, y / 2, val, ha="center", va="center", fontsize=8,
                color="white", fontweight="bold")

    # ×r 矢印
    for i in range(len(xs) - 1):
        ax.annotate(
            "",
            xy=(xs[i + 1] - 0.3, ys[i] * 1.05),
            xytext=(xs[i] + 0.3, ys[i] * 1.05),
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2,
                            mutation_scale=8, shrinkA=0, shrinkB=0),
        )
        ax.text((xs[i] + xs[i + 1]) / 2, ys[i] * 1.18,
                r"$\times r$", ha="center", va="bottom", fontsize=8, color=RED)

    ax.set_xlim(0.2, n + 0.8)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"$n={x}$" for x in xs], fontsize=8.5)
    ax.set_ylabel("$a_n$", fontsize=10)
    ax.set_title(r"等比数列: 各項が $r$ 倍", fontsize=10, pad=4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def draw_shift_subtract(ax):
    """Panel 2: ずらし引き — S_n と rS_n を対応づける"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)

    ax.set_title("ずらし引き: $S_n - rS_n$", fontsize=10, pad=4)

    # ヘッダー
    ax.text(0.5, 7.2, "$S_n$ =", ha="left", va="center", fontsize=9.5,
            color=DARK_BLUE, fontweight="bold")
    ax.text(0.5, 6.2, "$rS_n$ =", ha="left", va="center", fontsize=9.5,
            color=RED, fontweight="bold")

    terms_s  = [r"$a_1$",    r"$a_1 r$",   r"$a_1 r^2$", r"$a_1 r^3$", r"$\cdots$", r"$a_1 r^{n-1}$"]
    terms_rs = [r"$a_1 r$",  r"$a_1 r^2$", r"$a_1 r^3$", r"$\cdots$",  r"$a_1 r^{n-1}$", r"$a_1 r^n$"]

    x_starts = [1.8, 3.0, 4.2, 5.4, 6.4, 7.6]
    x_labels = [r"$+$"] * 5

    for i, (ts, xp) in enumerate(zip(terms_s, x_starts)):
        ax.text(xp, 7.2, ts, ha="center", va="center", fontsize=8.5,
                color=DARK_BLUE)
    for i, (tr, xp) in enumerate(zip(terms_rs, x_starts)):
        ax.text(xp, 6.2, tr, ha="center", va="center", fontsize=8.5,
                color=RED)

    # 対応する等しい項をグレーで囲む
    cancel_pairs = [(3.0, 7.2, 3.0, 6.2), (4.2, 7.2, 4.2, 6.2),
                    (5.4, 7.2, 5.4, 6.2), (7.6, 7.2, 7.6, 6.2)]
    for xc, yc, _, _ in cancel_pairs:
        for yy in [7.2, 6.2]:
            ax.add_patch(plt.Rectangle((xc - 0.5, yy - 0.3), 1.0, 0.55,
                                       facecolor="#f0f0f0", edgecolor="#888888",
                                       linewidth=0.8, zorder=1))

    # 引き算の横線
    ax.hlines(5.6, 0.3, 9.5, colors="#555555", linewidth=1.2)
    ax.text(0.1, 5.6, "−", ha="left", va="center", fontsize=12, color="#555555")

    # 残存
    ax.text(0.5, 5.0, "$(1-r)S_n$ =", ha="left", va="center", fontsize=9.5,
            color=GREEN, fontweight="bold")
    ax.text(1.8, 5.0, r"$a_1$", ha="center", va="center", fontsize=9,
            color=GREEN)
    ax.text(3.3, 5.0, r"$-$", ha="center", va="center", fontsize=9,
            color=GREEN)
    ax.text(7.6, 5.0, r"$a_1 r^n$", ha="center", va="center", fontsize=9,
            color=GREEN)

    # 結論
    ax.text(4.5, 4.0,
            r"$S_n = \dfrac{a_1(1-r^n)}{1-r}$ （$r \neq 1$ のとき）",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))
    ax.text(4.5, 3.0,
            r"$r = 1$ のとき $S_n = na_1$（全項が $a_1$ で等しい）",
            ha="center", va="center", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_geometric_bars(axes[0])
    draw_shift_subtract(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-geometric-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
