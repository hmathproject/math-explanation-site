"""
gen_figures_seq_sum_general.py — 一般項と和の関係

Panel 1: テーブル図（n / a_n / S_n / S_n - S_{n-1} の4列）
Panel 2: 積み上げ棒グラフ（今回追加分 a_n を強調）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_sum_general.py
出力: figures/seq-sum-general-combined.png
      assets/images/seq-sum-general-combined.png
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


def draw_table(ax):
    """Panel 1: テーブル a_n=2n+1 → S_n=n^2+2n"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    ax.set_title("$a_n$ と $S_n$ の関係表", fontsize=10, pad=4)

    ns = [1, 2, 3, 4, 5]
    ans = [2 * n + 1 for n in ns]           # a_n = 2n+1
    sns = [n * n + 2 * n for n in ns]       # S_n = n^2 + 2n
    diffs = ["–"] + [str(sns[i] - sns[i - 1]) for i in range(1, len(ns))]

    headers = ["$n$", "$a_n$", "$S_n$", r"$S_n - S_{n-1}$"]
    x_pos = [1.0, 3.0, 5.5, 8.0]
    y_header = 6.3

    # ヘッダー背景
    ax.add_patch(plt.Rectangle((0.1, y_header - 0.3), 9.6, 0.55,
                                facecolor="#ddeeff", edgecolor=DARK_BLUE,
                                linewidth=0.8))
    for hdr, xp in zip(headers, x_pos):
        ax.text(xp, y_header, hdr, ha="center", va="center",
                fontsize=9.5, color=DARK_BLUE, fontweight="bold")

    # データ行
    row_data = list(zip(ns, ans, sns, diffs))
    for row_idx, (n, a, s, d) in enumerate(row_data):
        y = y_header - 0.85 * (row_idx + 1)
        bg = "#f7fbff" if row_idx % 2 == 0 else "white"
        ax.add_patch(plt.Rectangle((0.1, y - 0.3), 9.6, 0.55,
                                    facecolor=bg, edgecolor="#cccccc",
                                    linewidth=0.5))
        for val, xp in zip([str(n), str(a), str(s), d], x_pos):
            col = RED if val == d and d != "–" else "#333333"
            ax.text(xp, y, val, ha="center", va="center",
                    fontsize=9.5, color=col)

    # 注記
    ax.text(5.0, 0.5,
            r"$n \geq 2$ のとき $S_n - S_{n-1} = a_n$" + "\n" +
            r"$n=1$ のとき $a_1 = S_1$ を別確認",
            ha="center", va="center", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.9))


def draw_stacked_bars(ax):
    """Panel 2: 積み上げ棒グラフ — a_n = 今回の追加分"""
    ns = [1, 2, 3, 4, 5]
    ans = [2 * n + 1 for n in ns]
    sns = [n * n + 2 * n for n in ns]

    # 累積部分（前の S_{n-1}）と追加分（a_n）
    prev_s = [0] + sns[:-1]

    ax.bar(ns, prev_s, color=DARK_BLUE, alpha=0.45, width=0.6,
           label=r"$S_{n-1}$（前の累積）", zorder=3)
    ax.bar(ns, ans, bottom=prev_s, color=RED, alpha=0.75, width=0.6,
           label=r"$a_n$（今回の追加）", zorder=3)

    # S_n ラベル
    for n, s in zip(ns, sns):
        ax.text(n, s + 0.3, f"$S_{{{n}}}={s}$",
                ha="center", va="bottom", fontsize=8.5, color=DARK_BLUE)

    # a_n ラベル（赤い部分の中央）
    for n, a, ps in zip(ns, ans, prev_s):
        ax.text(n, ps + a / 2, f"$a_{{{n}}}={a}$",
                ha="center", va="center", fontsize=8, color="white",
                fontweight="bold")

    ax.set_xlim(0.2, 5.8)
    ax.set_xticks(ns)
    ax.set_xticklabels([f"$n={x}$" for x in ns], fontsize=8.5)
    ax.set_ylabel("値", fontsize=10)
    ax.set_title(r"$a_n = S_n$ に今回加わった量", fontsize=10, pad=4)
    ax.legend(fontsize=8.5, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_table(axes[0])
    draw_stacked_bars(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-sum-general-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
