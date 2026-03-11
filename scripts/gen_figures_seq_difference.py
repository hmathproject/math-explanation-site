"""
gen_figures_seq_difference.py — 階差数列

Panel 1: 4列テーブル（n / a_n / b_n = a_{n+1}-a_n / 2階差）+ 差の矢印
Panel 2: n≥2 の制約と a_1 の別確認（並列比較）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_difference.py
出力: figures/seq-difference-combined.png
      assets/images/seq-difference-combined.png
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


def draw_difference_table(ax):
    """Panel 1: 階差数列の表（a_n = n^2 + n の例）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.set_title(r"階差数列の表（$a_n = n^2 + n$ の例）", fontsize=10, pad=4)

    ns = [1, 2, 3, 4, 5, 6]
    ans = [n * n + n for n in ns]            # a_n = n^2 + n
    bns = [ans[i + 1] - ans[i] for i in range(len(ans) - 1)]  # b_n = a_{n+1} - a_n
    # b_n = (n+1)^2+(n+1) - n^2-n = 2n+2
    d2 = [bns[i + 1] - bns[i] for i in range(len(bns) - 1)]  # 2階差 = 2

    headers = [r"$n$", r"$a_n$", r"$b_n = a_{n+1}-a_n$", r"$\Delta^2 a_n$"]
    x_pos = [0.7, 2.5, 5.5, 8.5]

    ax.add_patch(plt.Rectangle((0.1, 6.85), 9.6, 0.6,
                                facecolor="#ddeeff", edgecolor=DARK_BLUE,
                                linewidth=0.8))
    for hdr, xp in zip(headers, x_pos):
        ax.text(xp, 7.15, hdr, ha="center", va="center",
                fontsize=9, color=DARK_BLUE, fontweight="bold")

    for row_idx, n_i in enumerate(ns):
        y = 6.3 - row_idx * 0.88
        a = ans[row_idx]
        b = bns[row_idx] if row_idx < len(bns) else "—"
        d = d2[row_idx] if row_idx < len(d2) else "—"
        bg = "#f7fbff" if row_idx % 2 == 0 else "white"
        ax.add_patch(plt.Rectangle((0.1, y - 0.35), 9.6, 0.65,
                                    facecolor=bg, edgecolor="#cccccc",
                                    linewidth=0.5))
        vals = [str(n_i), str(a),
                str(b) if b != "—" else "—",
                str(d) if d != "—" else "—"]
        cols = [DARK_BLUE, DARK_BLUE, RED, ORANGE]
        for v, xp, c in zip(vals, x_pos, cols):
            ax.text(xp, y, v, ha="center", va="center", fontsize=9.5, color=c)

    ax.text(5.0, 0.6,
            r"$b_n = 2n+2$（等差）、$\Delta^2 a_n = 2$（定数）",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.8))


def draw_n1_check(ax):
    """Panel 2: n=1 の別確認"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.set_title(r"$n \geq 2$ の制約: $a_1$ は別確認が必要", fontsize=10, pad=4)

    ax.text(5.0, 7.1,
            r"$a_n = a_1 + \sum_{k=1}^{n-1} b_k$（$n \geq 2$）",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))

    # 左: n=2 で公式を使う
    ax.text(2.5, 6.0, r"$n=2$（公式）", ha="center", va="center",
            fontsize=9.5, color=GREEN, fontweight="bold")
    ax.text(2.5, 5.3, r"$a_2 = a_1 + b_1$", ha="center", va="center",
            fontsize=9.5, color=GREEN)
    ax.text(2.5, 4.6, r"$= 2 + 4 = 6$ ✓", ha="center", va="center",
            fontsize=9.5, color=GREEN)

    # 右: n=1 は公式外
    ax.text(7.5, 6.0, r"$n=1$（公式 外！）", ha="center", va="center",
            fontsize=9.5, color=RED, fontweight="bold")
    ax.text(7.5, 5.3, r"$a_1 + \sum_{k=1}^{0} b_k$", ha="center", va="center",
            fontsize=9.5, color=RED)
    ax.text(7.5, 4.6, r"$= a_1 + 0 = a_1$（空和）", ha="center", va="center",
            fontsize=9.5, color=RED)

    ax.hlines(4.0, 0.5, 9.5, colors="#aaaaaa", linewidth=0.8)

    ax.text(5.0, 3.5,
            "▶ $n=1$ 代入: 公式が $a_1 = a_1$ となるのは偶然一致\n  （$b_k$ の添字が $1$ から始まっているため）",
            ha="center", va="center", fontsize=9, color="#555555")

    ax.text(5.0, 2.5,
            r"公式が $n=1$ で成立するか必ず確認する。" + "\n" +
            "成立しない場合は「$a_1 = ○○$、$n \\geq 2$ のとき …」と書く",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff8ee",
                      edgecolor=ORANGE, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_difference_table(axes[0])
    draw_n1_check(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-difference-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
