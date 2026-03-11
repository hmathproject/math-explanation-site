"""
gen_figures_seq_partial_fraction.py — 部分分数分解と階差Σ

Panel 1: 数値表（k=1..5 で 1/(k(k+1)) = 1/k - 1/(k+1)）
Panel 2: 消去棒グラフ（先頭と末尾だけ残る）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_partial_fraction.py
出力: figures/seq-partial-fraction-combined.png
      assets/images/seq-partial-fraction-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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


def draw_fraction_table(ax):
    """Panel 1: 部分分数の数値表"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title(r"$\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$", fontsize=10, pad=4)

    headers = [r"$k$", r"$\frac{1}{k(k+1)}$", r"$\frac{1}{k}$",
               r"$-\frac{1}{k+1}$", "確認"]
    x_pos = [0.7, 2.5, 4.5, 6.5, 8.7]

    ax.add_patch(plt.Rectangle((0.1, 6.9), 9.6, 0.65,
                                facecolor="#ddeeff", edgecolor=DARK_BLUE,
                                linewidth=0.8))
    for hdr, xp in zip(headers, x_pos):
        ax.text(xp, 7.2, hdr, ha="center", va="center",
                fontsize=9, color=DARK_BLUE, fontweight="bold")

    rows = [
        ("1", r"$\frac{1}{2}$",  r"$\frac{1}{1}$",  r"$-\frac{1}{2}$", r"$= \frac{1}{2}$"),
        ("2", r"$\frac{1}{6}$",  r"$\frac{1}{2}$",  r"$-\frac{1}{3}$", r"$= \frac{1}{6}$"),
        ("3", r"$\frac{1}{12}$", r"$\frac{1}{3}$",  r"$-\frac{1}{4}$", r"$= \frac{1}{12}$"),
        ("4", r"$\frac{1}{20}$", r"$\frac{1}{4}$",  r"$-\frac{1}{5}$", r"$= \frac{1}{20}$"),
        ("5", r"$\frac{1}{30}$", r"$\frac{1}{5}$",  r"$-\frac{1}{6}$", r"$= \frac{1}{30}$"),
    ]

    for row_idx, row in enumerate(rows):
        y = 6.3 - row_idx * 1.0
        bg = "#f7fbff" if row_idx % 2 == 0 else "white"
        ax.add_patch(plt.Rectangle((0.1, y - 0.4), 9.6, 0.75,
                                    facecolor=bg, edgecolor="#cccccc",
                                    linewidth=0.5))
        for val, xp in zip(row, x_pos):
            ax.text(xp, y, val, ha="center", va="center",
                    fontsize=9, color="#333333")

    ax.text(5.0, 0.6,
            r"分解の根拠: $1 = k+1 - k$ を分子に利用",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.8))


def draw_cancellation(ax):
    """Panel 2: 消去の様子 — 先頭と末尾だけ残る"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title(r"$\Sigma$ の残存: 先頭と末尾だけ残る", fontsize=10, pad=4)

    # 各行の 1/k と -1/(k+1) を表示
    n = 5
    rows_pos  = [f"$+\\frac{{1}}{{{k}}}$" for k in range(1, n + 1)]
    rows_neg  = [f"$-\\frac{{1}}{{{k+1}}}$" for k in range(1, n + 1)]
    y_start = 7.3

    for i, (pos, neg) in enumerate(zip(rows_pos, rows_neg)):
        y = y_start - i * 0.88
        surviving_pos = (i == 0)      # 1/1 は消えない
        surviving_neg = (i == n - 1)  # -1/(n+1) は消えない
        cancel = not surviving_pos and not surviving_neg

        col_pos = GREEN if surviving_pos else "#aaaaaa"
        col_neg = RED   if surviving_neg else "#aaaaaa"

        ax.text(2.0, y, pos, ha="center", va="center",
                fontsize=9.5, color=col_pos)
        ax.text(5.5, y, neg, ha="center", va="center",
                fontsize=9.5, color=col_neg)

        # 消える組み合わせに取り消し線的な薄背景
        if not surviving_neg and i > 0:
            ax.add_patch(plt.Rectangle((4.6, y - 0.3), 2.0, 0.55,
                                       facecolor="#eeeeee", edgecolor="#bbbbbb",
                                       linewidth=0.5, zorder=1))
        if not surviving_pos and i > 0:
            ax.add_patch(plt.Rectangle((1.2, y - 0.3), 1.6, 0.55,
                                       facecolor="#eeeeee", edgecolor="#bbbbbb",
                                       linewidth=0.5, zorder=1))

    # 結論
    ax.hlines(2.7, 0.2, 9.8, colors="#555555", linewidth=1.2)
    ax.text(0.4, 2.7, "合計", ha="left", va="center", fontsize=9, color="#555555")

    ax.text(5.0, 2.0,
            r"$\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n+1} = \frac{n}{n+1}$",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))

    ax.text(5.0, 0.8,
            "残存: 先頭 $+\\frac{1}{1}$（緑）と末尾 $-\\frac{1}{n+1}$（赤）",
            ha="center", va="center", fontsize=9, color=DARK_BLUE)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_fraction_table(axes[0])
    draw_cancellation(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-partial-fraction-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
