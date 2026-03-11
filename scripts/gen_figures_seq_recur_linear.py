"""
gen_figures_seq_recur_linear.py — 1次変換型漸化式

Panel 1: a_n の推移と固定点 α（scatter + 水平破線）
Panel 2: 変換フロー図（a_n → b_n = a_n - α → 等比型）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_recur_linear.py
出力: figures/seq-recur-linear-combined.png
      assets/images/seq-recur-linear-combined.png
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


def draw_sequence_with_fixedpoint(ax):
    """Panel 1: a_{n+1} = 2a_n - 3, a_1=1, 固定点 α=3"""
    a1, p, q = 1, 2, -3    # a_{n+1} = 2a_n - 3  →  α=3
    alpha = q / (1 - p)    # α = pα + q  →  -3 = 2α - α  →  α = 3
    n = 7
    ns = list(range(1, n + 1))
    vals = [a1]
    for _ in range(n - 1):
        vals.append(p * vals[-1] + q)

    ax.scatter(ns, vals, color=DARK_BLUE, s=70, zorder=5)

    # 折れ線（連続グラフではなく視覚補助の細い線のみ、integers間）
    ax.plot(ns, vals, color=DARK_BLUE, linewidth=0.8, alpha=0.4,
            zorder=2, linestyle="--")

    # 各点ラベル
    for n_i, v in zip(ns, vals):
        offset = 2 if v < alpha else -2
        ax.text(n_i + 0.12, v + offset * 0.3, str(v),
                ha="left", va="center", fontsize=8.5, color=DARK_BLUE)

    # 固定点 α の水平線
    ax.axhline(y=alpha, color=RED, linewidth=1.5, linestyle="--", zorder=4)
    ax.text(n + 0.3, alpha, f"固定点 $\\alpha = {int(alpha)}$",
            ha="left", va="center", fontsize=9.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.8))

    ax.set_xlim(0.5, n + 1.5)
    ax.set_xticks(ns)
    ax.set_xticklabels([f"$n={x}$" for x in ns], fontsize=8)
    ax.set_ylabel("$a_n$", fontsize=10)
    ax.set_title(r"$a_{n+1} = 2a_n - 3$ の推移と固定点", fontsize=10, pad=4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.text(1.5, min(vals) - 3,
            r"$b_n = a_n - \alpha$ とおくと" + "\n" +
            r"$b_n$ は等比数列",
            ha="center", va="top", fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=0.8))


def draw_transformation_flow(ax):
    """Panel 2: 変換手順フロー"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.5)
    ax.set_title(r"変換 $b_n = a_n - \alpha$ で等比型へ", fontsize=10, pad=4)

    boxes = [
        (1.5, 5.2, r"$a_n$",                  DARK_BLUE),
        (5.0, 5.2, r"$b_n = a_n - \alpha$",    RED),
        (5.0, 3.0, r"$b_{n+1} = p \cdot b_n$", GREEN),
        (1.5, 3.0, r"$a_n = b_n + \alpha$",    DARK_BLUE),
    ]

    for xc, yc, lbl, col in boxes:
        ax.add_patch(mpatches.FancyBboxPatch((xc - 1.4, yc - 0.4), 2.8, 0.8,
                                         boxstyle="round,pad=0.1",
                                         facecolor=col, edgecolor="#333333",
                                         linewidth=1.0, alpha=0.85, zorder=3))
        ax.text(xc, yc, lbl, ha="center", va="center",
                fontsize=9.5, color="white", fontweight="bold", zorder=4)

    arrows = [
        (1.5, 5.2, 5.0, 5.2, r"$-\alpha$"),
        (5.0, 5.2, 5.0, 3.0, r"等比型"),
        (5.0, 3.0, 1.5, 3.0, r"$+\alpha$"),
    ]
    for x1, y1, x2, y2, lbl in arrows:
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.5,
                            mutation_scale=10, shrinkA=20, shrinkB=20),
        )
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        offset = (0.3, 0) if x1 != x2 else (0.5, 0)
        ax.text(mx + offset[0], my + offset[1], lbl,
                ha="center", va="center", fontsize=9, color=RED,
                fontweight="bold")

    ax.text(5.0, 1.8,
            r"$\alpha = p\alpha + q$ を解いて $\alpha$ を求める",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))
    ax.text(5.0, 0.9,
            r"$p = 1$ のとき $\alpha$ は定まらない → 等差型へ帰着",
            ha="center", va="center", fontsize=9, color=ORANGE)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_sequence_with_fixedpoint(axes[0])
    draw_transformation_flow(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-recur-linear-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
