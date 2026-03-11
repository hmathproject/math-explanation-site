"""
gen_figures_seq_group.py — 群数列

Panel 1: 群の区切り図（数列を区切り線でグループ分け）
Panel 2: 座標型位置図（縦=群番号、横=群内位置）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_group.py
出力: figures/seq-group-combined.png
      assets/images/seq-group-combined.png
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
COLORS = [DARK_BLUE, RED, GREEN, ORANGE]


def draw_group_separation(ax):
    """Panel 1: 群の区切り図（|1|2,3|4,5,6|7,8,9,10|）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title("群数列の区切り", fontsize=10, pad=4)

    # 各群の要素
    groups = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10],
    ]
    group_labels = ["第1群", "第2群", "第3群", "第4群"]
    group_sizes  = [1, 2, 3, 4]
    first_terms  = [1, 2, 4, 7]

    # 数列全体を横一列に並べる（y=5.8）
    seq_y = 5.8
    all_items = [item for g in groups for item in g]
    x_positions = [(i + 1) * (9.0 / (len(all_items) + 1)) + 0.5
                   for i in range(len(all_items))]

    pos_idx = 0
    for g_idx, (group, col) in enumerate(zip(groups, COLORS)):
        # 囲み背景
        x_start = x_positions[pos_idx] - 0.35
        x_end   = x_positions[pos_idx + len(group) - 1] + 0.35
        ax.add_patch(plt.Rectangle((x_start, seq_y - 0.4),
                                    x_end - x_start, 0.8,
                                    facecolor=col, alpha=0.18,
                                    edgecolor=col, linewidth=1.5))
        for item in group:
            xp = x_positions[pos_idx]
            ax.text(xp, seq_y, str(item), ha="center", va="center",
                    fontsize=11, color=col, fontweight="bold")
            pos_idx += 1

        # 群ラベル（下）
        mid_x = (x_positions[sum(group_sizes[:g_idx])] +
                 x_positions[sum(group_sizes[:g_idx + 1]) - 1]) / 2
        ax.text(mid_x, seq_y - 0.85, group_labels[g_idx],
                ha="center", va="top", fontsize=9, color=col)

    # 区切り棒
    sep_positions = [0]
    cnt = 0
    for g in groups[:-1]:
        cnt += len(g)
        sep_x = (x_positions[cnt - 1] + x_positions[cnt]) / 2
        ax.vlines(sep_x, seq_y - 1.4, seq_y + 0.5,
                  colors="#666666", linewidth=1.5, linestyle="-")

    # 表で群の情報を示す
    y_tbl = 3.8
    table_data = [
        ("第 $n$ 群", "要素数", "最初の項番号", "最後の項番号"),
        ("1", "1", "1", "1"),
        ("2", "2", "2", "3"),
        ("3", "3", "4", "6"),
        ("4", "4", "7", "10"),
        (r"$n$", r"$n$", r"$\frac{n(n-1)}{2}+1$", r"$\frac{n(n+1)}{2}$"),
    ]
    x_cols = [1.0, 3.2, 5.8, 8.5]
    bg_colors = ["#ddeeff"] + ["#f7fbff" if i % 2 == 0 else "white"
                                for i in range(len(table_data) - 1)]

    for row_idx, row in enumerate(table_data):
        y = y_tbl - row_idx * 0.72
        bg = "#ddeeff" if row_idx == 0 else ("#f7fbff" if row_idx % 2 == 1 else "white")
        ax.add_patch(plt.Rectangle((0.2, y - 0.3), 9.4, 0.58,
                                    facecolor=bg, edgecolor="#cccccc",
                                    linewidth=0.5))
        for val, xp in zip(row, x_cols):
            fw = "bold" if row_idx == 0 else "normal"
            col = DARK_BLUE if row_idx in [0, len(table_data) - 1] else "#333333"
            ax.text(xp, y, val, ha="center", va="center",
                    fontsize=8.5, color=col, fontweight=fw)


def draw_position_grid(ax):
    """Panel 2: 座標型位置図（縦=群番号、横=群内位置）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.set_title("第 $n$ 群・第 $k$ 番目の位置", fontsize=10, pad=4)

    groups = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9, 10],
    ]

    # x軸: 群内位置 (k=1..4)
    # y軸: 群番号 (n=1..4, 上が1)
    x_scale = 1.8
    y_scale = 1.4
    x_offset = 1.0
    y_offset = 0.8

    # 軸ラベル
    ax.text(5.0, 7.2, "横軸: 群内の位置 $k$", ha="center", va="center",
            fontsize=9, color="#555555")
    ax.text(0.3, 4.0, "縦軸:\n群番号\n$n$", ha="center", va="center",
            fontsize=8.5, color="#555555")

    for k in range(1, 5):
        ax.text(x_offset + k * x_scale, y_offset + 4.8, f"$k={k}$",
                ha="center", va="center", fontsize=9, color="#666666")

    for g_idx, (group, col) in enumerate(zip(groups, COLORS)):
        n_num = g_idx + 1
        y_n = y_offset + (4 - n_num) * y_scale
        ax.text(0.7, y_n + 0.1, f"$n={n_num}$", ha="right", va="center",
                fontsize=9, color=col, fontweight="bold")

        for k_idx, item in enumerate(group):
            k_num = k_idx + 1
            xp = x_offset + k_num * x_scale
            ax.scatter([xp], [y_n], s=90, color=col, zorder=4)
            ax.text(xp + 0.12, y_n + 0.22, str(item),
                    ha="left", va="bottom", fontsize=9, color=col,
                    fontweight="bold")

    # 説明ボックス
    ax.text(5.5, 0.8,
            "第 $n$ 群の最初の項番号: $\\frac{n(n-1)}{2}+1$\n"
            "第 $n$ 群の第 $k$ 番目は全体の $\\frac{n(n-1)}{2}+k$ 番目",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_group_separation(axes[0])
    draw_position_grid(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-group-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
