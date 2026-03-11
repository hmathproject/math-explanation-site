"""
gen_figures_seq_recur_basic.py — 基本型漸化式

Panel 1: 等差型フロー図（a_1 →+d→ a_2 →+d→ ...）
Panel 2: 等比型フロー図（a_1 →×r→ a_2 →×r→ ...）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_recur_basic.py
出力: figures/seq-recur-basic-combined.png
      assets/images/seq-recur-basic-combined.png
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
BOX_W = 1.1
BOX_H = 0.7


def draw_flow(ax, node_labels, arrow_labels, colors, title, result_text):
    """汎用フロー図ヘルパー"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.5)
    ax.set_title(title, fontsize=10, pad=4)

    n_nodes = len(node_labels)
    spacing = 9.0 / (n_nodes + 0.5)
    x_starts = [0.5 + i * spacing for i in range(n_nodes)]
    y_center = 3.5

    for i, (lbl, col) in enumerate(zip(node_labels, colors)):
        xc = x_starts[i]
        ax.add_patch(mpatches.FancyBboxPatch((xc - BOX_W / 2, y_center - BOX_H / 2),
                                         BOX_W, BOX_H,
                                         boxstyle="round,pad=0.1",
                                         facecolor=col, edgecolor=DARK_BLUE,
                                         linewidth=1.2, zorder=3))
        ax.text(xc, y_center, lbl, ha="center", va="center",
                fontsize=10, color="white", fontweight="bold", zorder=4)

    for i, (albl, col_pair) in enumerate(zip(arrow_labels, zip(colors, colors[1:]))):
        x_from = x_starts[i] + BOX_W / 2
        x_to   = x_starts[i + 1] - BOX_W / 2
        ax.annotate(
            "",
            xy=(x_to, y_center),
            xytext=(x_from, y_center),
            arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.5,
                            mutation_scale=10, shrinkA=3, shrinkB=3),
            zorder=2,
        )
        ax.text((x_from + x_to) / 2, y_center + 0.55,
                albl, ha="center", va="bottom", fontsize=10, color=RED,
                fontweight="bold")

    # 結論ボックス
    ax.text(5.0, 1.5, result_text,
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    # Panel 1: 等差型
    node_labels_arith = [r"$a_1$", r"$a_2$", r"$a_3$", r"$\cdots$", r"$a_n$"]
    arrow_labels_arith = [r"$+d$", r"$+d$", r"$+d$", r"$+d$"]
    colors_arith = [DARK_BLUE, DARK_BLUE, DARK_BLUE, "#888888", GREEN]
    draw_flow(
        axes[0], node_labels_arith, arrow_labels_arith, colors_arith,
        title=r"等差型: $a_{n+1} = a_n + d$",
        result_text=r"$a_n = a_1 + (n-1)d$" + "（差が一定 → 等差数列）"
    )

    # Panel 2: 等比型
    node_labels_geom = [r"$a_1$", r"$a_2$", r"$a_3$", r"$\cdots$", r"$a_n$"]
    arrow_labels_geom = [r"$\times r$", r"$\times r$", r"$\times r$", r"$\times r$"]
    colors_geom = [DARK_BLUE, DARK_BLUE, DARK_BLUE, "#888888", RED]
    draw_flow(
        axes[1], node_labels_geom, arrow_labels_geom, colors_geom,
        title=r"等比型: $a_{n+1} = r \cdot a_n$",
        result_text=r"$a_n = a_1 \cdot r^{n-1}$" + "（比が一定 → 等比数列）"
    )

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-recur-basic-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
