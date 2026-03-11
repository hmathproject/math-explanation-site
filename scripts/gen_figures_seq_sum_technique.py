"""
gen_figures_seq_sum_technique.py — ずらし引きとテレスコーピング

Panel 1: ずらし引き法の対応表（S_n と rS_n の各項を縦に並べる）
Panel 2: テレスコーピング（b_k - b_{k-1} の連鎖消去）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_sum_technique.py
出力: figures/seq-sum-technique-combined.png
      assets/images/seq-sum-technique-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt

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


def draw_shift_subtract_table(ax):
    """Panel 1: ずらし引きの対応表"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title("ずらし引き法: $S_n$ と $rS_n$", fontsize=10, pad=4)

    # S_n 行
    ax.text(0.2, 7.3, r"$S_n$   $=$", ha="left", va="center",
            fontsize=9.5, color=DARK_BLUE, fontweight="bold")
    sn_terms = [r"$1\cdot2^0$", r"$+\;2\cdot2^1$", r"$+\;3\cdot2^2$",
                r"$+\;\cdots$", r"$+\;n\cdot2^{n-1}$"]
    x_pos_s = [2.0, 3.4, 5.0, 6.4, 7.8]
    for t, xp in zip(sn_terms, x_pos_s):
        ax.text(xp, 7.3, t, ha="left", va="center", fontsize=9, color=DARK_BLUE)

    # rS_n 行（1位ずれる）
    ax.text(0.2, 6.1, r"$2S_n$ $=$", ha="left", va="center",
            fontsize=9.5, color=RED, fontweight="bold")
    rsn_terms = [r"$1\cdot2^1$", r"$+\;2\cdot2^2$", r"$+\;\cdots$",
                 r"$+\;(n{-}1)\cdot2^{n-1}$", r"$+\;n\cdot2^n$"]
    x_pos_r = [3.4, 5.0, 6.4, 7.1, 7.8 + 1.2]
    for t, xp in zip(rsn_terms, x_pos_r):
        ax.text(xp, 6.1, t, ha="left", va="center", fontsize=9, color=RED)

    # 等しくて消える箇所をグレー背景
    cancel_xs = [3.4, 5.0, 7.1]
    for xc in cancel_xs:
        for yy in [7.3, 6.1]:
            ax.add_patch(plt.Rectangle((xc - 0.1, yy - 0.3), 2.0, 0.55,
                                       facecolor="#eeeeee", edgecolor="#aaaaaa",
                                       linewidth=0.5, zorder=1))

    # 引き算線
    ax.hlines(5.4, 0.1, 9.9, colors="#555555", linewidth=1.2)
    ax.text(0.05, 5.4, "−", ha="left", va="center", fontsize=12, color="#555555")

    # 差
    ax.text(0.2, 4.7, r"$(1-2)S_n$ $=$", ha="left", va="center",
            fontsize=9.5, color=GREEN, fontweight="bold")
    ax.text(2.8, 4.7, r"$1\cdot2^0\;-\;n\cdot2^n$", ha="left", va="center",
            fontsize=9.5, color=GREEN)

    # 結論
    ax.text(5.0, 3.6,
            r"$S_n = n\cdot2^n - (2^n - 1)$" + "\n" +
            r"$= (n-1)\cdot2^n + 1$",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))

    # ポイント
    ax.text(5.0, 2.4,
            "等比部 $2^k$ だけ残り、等差部 $k$ が消える",
            ha="center", va="center", fontsize=9, color=DARK_BLUE)


def draw_telescoping(ax):
    """Panel 2: テレスコーピングの連鎖消去"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title("テレスコーピング: 中間項が連鎖消去", fontsize=10, pad=4)

    # b_k = k(k+1)(k+2)/3
    ns = [1, 2, 3, 4, 5]
    rows = [
        (r"$(b_2 - b_1)$", r"$= 1\cdot2$"),
        (r"$(b_3 - b_2)$", r"$= 2\cdot3$"),
        (r"$(b_4 - b_3)$", r"$= 3\cdot4$"),
        (r"$(b_5 - b_4)$", r"$= 4\cdot5$"),
        (r"$(b_6 - b_5)$", r"$= 5\cdot6$"),
    ]
    y_start = 7.2
    for i, (lhs, rhs) in enumerate(rows):
        y = y_start - i * 0.8
        ax.text(0.3, y, lhs, ha="left", va="center", fontsize=9.5,
                color=DARK_BLUE)
        ax.text(4.5, y, rhs, ha="left", va="center", fontsize=9.5,
                color=DARK_BLUE)
        if i < len(rows) - 1:
            # b_2 in row 0 cancels with b_2 in row 1, etc.
            cancel_term = f"$b_{{{i+2}}}$"
            ax.add_patch(plt.Rectangle((1.5, y - 0.28), 1.4, 0.5,
                                       facecolor="#eeeeee", edgecolor="#999999",
                                       linewidth=0.5, zorder=1))

    # 引き算線
    ax.hlines(2.75, 0.1, 9.9, colors="#555555", linewidth=1.2)
    ax.text(0.05, 2.75, "合計", ha="left", va="center", fontsize=9, color="#555555")

    # 合計式
    ax.text(0.3, 2.1, r"$\sum_{k=1}^{5} k(k+1)$", ha="left", va="center",
            fontsize=9.5, color=GREEN)
    ax.text(4.5, 2.1, r"$= b_6 - b_1$", ha="left", va="center",
            fontsize=9.5, color=GREEN)

    ax.text(0.3, 1.2,
            r"$b_k = \frac{k(k+1)(k+2)}{3}$ なので",
            ha="left", va="center", fontsize=9, color=DARK_BLUE)
    ax.text(0.3, 0.5,
            r"$\sum_{k=1}^{n} k(k+1) = \frac{n(n+1)(n+2)}{3}$",
            ha="left", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_shift_subtract_table(axes[0])
    draw_telescoping(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-sum-technique-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
