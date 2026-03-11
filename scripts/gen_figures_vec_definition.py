"""
gen_figures_vec_definition.py — ベクトルとは何か

Panel 1: 複数の矢印で「向きと大きさが同じなら同じベクトル」を示す図
Panel 2: 零ベクトルと逆ベクトルの図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_definition.py
出力: figures/vec-definition-combined.png
      assets/images/vec-definition-combined.png
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


def draw_vector(ax, tail, tip, color, lw=2.0, mutation_scale=20):
    ax.annotate("", xy=tip, xytext=tail,
                arrowprops=dict(arrowstyle="-|>", mutation_scale=mutation_scale,
                                lw=lw, color=color))


def draw_equal_vectors(ax):
    """Panel 1: 複数の始点から同じ向き・長さの矢印 — どれも同じベクトル"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title("始点が違っても同じベクトル", fontsize=10, pad=4)

    # 3 本の「同じ」ベクトル（向き=右上30°, 長さ=2.5）
    dx, dy = 2.5, 1.4
    starts = [(1.0, 4.5), (4.0, 5.5), (6.5, 2.5)]
    labels_tail = ["A", "C", "E"]
    labels_tip  = ["B", "D", "F"]

    for i, (sx, sy) in enumerate(starts):
        ex, ey = sx + dx, sy + dy
        col = [DARK_BLUE, RED, GREEN][i]
        draw_vector(ax, (sx, sy), (ex, ey), col)
        ax.scatter([sx, ex], [sy, ey], s=25, color=col, zorder=4)
        ax.text(sx - 0.25, sy, labels_tail[i], ha="right", va="center",
                fontsize=10, color=col)
        ax.text(ex + 0.1, ey + 0.1, labels_tip[i], ha="left", va="bottom",
                fontsize=10, color=col)

    # 説明ラベル
    ax.text(5.0, 0.8,
            r"$\overrightarrow{AB} = \overrightarrow{CD} = \overrightarrow{EF}$" + "\n"
            "（向きと大きさが同じ → 同じベクトル）",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))

    # 始点の違いを強調
    ax.text(2.8, 6.8, "始点は\n異なる", ha="center", va="top",
            fontsize=8.5, color="#666666")


def draw_zero_and_inverse(ax):
    """Panel 2: 零ベクトル・逆ベクトルの図"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title("零ベクトルと逆ベクトル", fontsize=10, pad=4)

    # --- 逆ベクトル a と -a ---
    ax.text(5.0, 6.6, "逆ベクトル", ha="center", va="center",
            fontsize=9.5, color="#333333", fontweight="bold")

    # a: 左から右
    draw_vector(ax, (1.5, 5.5), (5.0, 5.5), DARK_BLUE)
    ax.text(3.25, 5.75, r"$\vec{a}$", ha="center", va="bottom",
            fontsize=11, color=DARK_BLUE)

    # -a: 右から左（逆向き）
    draw_vector(ax, (8.5, 4.8), (5.0, 4.8), RED)
    ax.text(6.75, 4.55, r"$-\vec{a}$", ha="center", va="top",
            fontsize=11, color=RED)

    ax.text(5.0, 4.1,
            r"$\vec{a}$ と $-\vec{a}$ は大きさが同じで向きが逆",
            ha="center", va="center", fontsize=9, color="#555555")

    # --- 零ベクトル ---
    ax.text(5.0, 3.3, "零ベクトル", ha="center", va="center",
            fontsize=9.5, color="#333333", fontweight="bold")

    # 点 P と "矢印なし" の表現
    ax.scatter([5.0], [2.5], s=60, color=ORANGE, zorder=4)
    ax.text(5.0, 2.5, "P", ha="center", va="center", fontsize=1,
            color="white")  # invisible text for spacing
    ax.annotate("", xy=(5.05, 2.5), xytext=(5.0, 2.5),
                arrowprops=dict(arrowstyle="-|>", mutation_scale=12,
                                lw=1.5, color=ORANGE))
    ax.text(5.0, 2.5, "P", ha="center", va="top", fontsize=10,
            color=ORANGE, fontweight="bold")
    ax.text(5.0, 1.85, r"$\vec{0}$: 大きさ 0 のベクトル" + "\n（始点と終点が一致）",
            ha="center", va="center", fontsize=9, color=ORANGE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff8ee",
                      edgecolor=ORANGE, linewidth=0.8))

    # a + (-a) = 0
    ax.text(5.0, 0.55,
            r"$\vec{a} + (-\vec{a}) = \vec{0}$",
            ha="center", va="center", fontsize=10, color=DARK_BLUE)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_equal_vectors(axes[0])
    draw_zero_and_inverse(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-definition-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
