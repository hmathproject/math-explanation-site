"""
gen_figures_vec_position.py — 位置ベクトルの考え方

Panel 1: OA, OB, OP の位置ベクトル（始点を O に統一）
Panel 2: AB = OB - OA を位置ベクトルで表す

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_position.py
出力: figures/vec-position-combined.png
      assets/images/vec-position-combined.png
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


def draw_position_vectors(ax):
    """Panel 1: 位置ベクトル OA, OB, OP の図"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title("位置ベクトル（始点を O に統一）", fontsize=10, pad=4)

    O = np.array([2.0, 1.5])

    # 3点の位置
    A = np.array([5.5, 5.5])
    B = np.array([8.5, 2.5])
    P = np.array([6.0, 3.0])

    # OA, OB, OP
    draw_vector(ax, O, A, DARK_BLUE, lw=2.2, mutation_scale=20)
    ax.text((O[0]+A[0])/2-0.3, (O[1]+A[1])/2+0.1,
            r"$\vec{a}=\overrightarrow{OA}$",
            ha="right", va="bottom", fontsize=10, color=DARK_BLUE)

    draw_vector(ax, O, B, RED, lw=2.2, mutation_scale=20)
    ax.text((O[0]+B[0])/2+0.1, (O[1]+B[1])/2-0.35,
            r"$\vec{b}=\overrightarrow{OB}$",
            ha="left", va="top", fontsize=10, color=RED)

    draw_vector(ax, O, P, GREEN, lw=2.2, mutation_scale=20)
    ax.text((O[0]+P[0])/2-0.15, (O[1]+P[1])/2-0.35,
            r"$\vec{p}=\overrightarrow{OP}$",
            ha="right", va="top", fontsize=10, color=GREEN)

    # 点のラベル
    for pt, lbl, off in [(O, "O", (-0.2, -0.2)), (A, "A", (-0.1, 0.2)),
                          (B, "B", (0.2, 0.0)), (P, "P", (0.2, 0.1))]:
        ax.scatter([pt[0]], [pt[1]], s=40, color="#333333", zorder=5)
        ax.text(pt[0]+off[0], pt[1]+off[1], lbl,
                ha="center", va="center", fontsize=11,
                color="#333333", fontweight="bold")

    ax.text(5.0, 0.5,
            "各点の位置は「O から its の矢印」で表す\n"
            r"点 $\text{P}$ ↔ 位置ベクトル $\vec{p}=\overrightarrow{OP}$",
            ha="center", va="center", fontsize=9, color="#555555",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#aaaaaa", linewidth=0.8))


def draw_ab_decomp(ax):
    """Panel 2: AB = OB - OA = b - a（位置ベクトルで書き換え）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$\overrightarrow{AB} = \vec{b} - \vec{a}$", fontsize=10, pad=4)

    O = np.array([1.5, 1.5])
    A = np.array([4.5, 5.0])
    B = np.array([8.5, 3.0])

    # OA
    draw_vector(ax, O, A, DARK_BLUE, lw=2.0, mutation_scale=18)
    ax.text((O[0]+A[0])/2-0.3, (O[1]+A[1])/2+0.05,
            r"$\vec{a}$", ha="right", va="center",
            fontsize=11, color=DARK_BLUE)

    # OB
    draw_vector(ax, O, B, RED, lw=2.0, mutation_scale=18)
    ax.text((O[0]+B[0])/2, (O[1]+B[1])/2-0.35,
            r"$\vec{b}$", ha="center", va="top",
            fontsize=11, color=RED)

    # AB = OB - OA
    draw_vector(ax, A, B, GREEN, lw=2.5, mutation_scale=22)
    ax.text((A[0]+B[0])/2, (A[1]+B[1])/2+0.25,
            r"$\overrightarrow{AB}=\vec{b}-\vec{a}$",
            ha="center", va="bottom", fontsize=11, color=GREEN)

    # 点ラベル
    for pt, lbl, off in [(O, "O", (-0.2, -0.2)), (A, "A", (-0.15, 0.2)),
                          (B, "B", (0.2, 0.05))]:
        ax.scatter([pt[0]], [pt[1]], s=40, color="#333333", zorder=5)
        ax.text(pt[0]+off[0], pt[1]+off[1], lbl,
                ha="center", va="center", fontsize=11,
                color="#333333", fontweight="bold")

    # 導出
    ax.text(5.0, 0.8,
            r"$\overrightarrow{OA}+\overrightarrow{AB}=\overrightarrow{OB}$" + " より\n"
            r"$\overrightarrow{AB} = \overrightarrow{OB}-\overrightarrow{OA} = \vec{b}-\vec{a}$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_position_vectors(axes[0])
    draw_ab_decomp(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-position-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
