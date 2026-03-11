"""
gen_figures_vec_addition.py — ベクトルの加法・減法

Panel 1: 頭尾連結の矢印図（a+b）と平行四辺形則
Panel 2: AB = OB - OA の位置図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_addition.py
出力: figures/vec-addition-combined.png
      assets/images/vec-addition-combined.png
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


def draw_vector(ax, tail, tip, color, lw=2.0, mutation_scale=20, linestyle="solid"):
    ax.annotate("", xy=tip, xytext=tail,
                arrowprops=dict(arrowstyle="-|>", mutation_scale=mutation_scale,
                                lw=lw, color=color,
                                connectionstyle="arc3,rad=0"))


def draw_addition(ax):
    """Panel 1: 頭尾連結で a+b を作る（平行四辺形も併記）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$\vec{a}+\vec{b}$ の頭尾連結", fontsize=10, pad=4)

    # --- 頭尾連結 ---
    O = np.array([1.0, 2.0])
    A = np.array([4.2, 4.0])   # O + a
    B = np.array([7.0, 2.8])   # A + b = O + a + b

    # a: O → A
    draw_vector(ax, O, A, DARK_BLUE)
    ax.text((O[0]+A[0])/2 - 0.3, (O[1]+A[1])/2 + 0.2, r"$\vec{a}$",
            ha="right", va="bottom", fontsize=12, color=DARK_BLUE)

    # b: A → B
    draw_vector(ax, A, B, RED)
    ax.text((A[0]+B[0])/2 + 0.1, (A[1]+B[1])/2 + 0.15, r"$\vec{b}$",
            ha="left", va="bottom", fontsize=12, color=RED)

    # a+b: O → B
    draw_vector(ax, O, B, GREEN, lw=2.5)
    ax.text((O[0]+B[0])/2, (O[1]+B[1])/2 - 0.4, r"$\vec{a}+\vec{b}$",
            ha="center", va="top", fontsize=11, color=GREEN)

    # 平行四辺形（薄い補助線）
    C = B + (O - A)  # = O + b
    ax.plot([O[0], C[0]], [O[1], C[1]], color=RED, lw=1.2, linestyle="--", alpha=0.5)
    ax.plot([C[0], B[0]], [C[1], B[1]], color=DARK_BLUE, lw=1.2, linestyle="--", alpha=0.5)

    # 点のラベル
    for pt, lbl, offset in [(O, "O", (-0.15, -0.2)), (A, "P", (0.1, 0.1)),
                             (B, "Q", (0.1, 0.05)), (C, "", (0, 0))]:
        ax.scatter([pt[0]], [pt[1]], s=30, color="#333333", zorder=5)
        ax.text(pt[0]+offset[0], pt[1]+offset[1], lbl,
                ha="center", va="center", fontsize=10, color="#333333")

    ax.text(5.0, 0.6,
            "矢印の「頭と尾をつなぐ」ことで足し算\n"
            "（始点と終点を結ぶ矢印が和）",
            ha="center", va="center", fontsize=9, color="#555555",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#aaaaaa", linewidth=0.8))


def draw_subtraction(ax):
    """Panel 2: AB = OB - OA の位置図"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}$",
                 fontsize=10, pad=4)

    O = np.array([1.5, 1.5])
    A = np.array([4.0, 5.5])
    B = np.array([8.5, 3.5])

    # OA (位置ベクトル)
    draw_vector(ax, O, A, DARK_BLUE, lw=1.8)
    ax.text((O[0]+A[0])/2 - 0.4, (O[1]+A[1])/2, r"$\vec{a}=\overrightarrow{OA}$",
            ha="right", va="center", fontsize=10, color=DARK_BLUE)

    # OB (位置ベクトル)
    draw_vector(ax, O, B, RED, lw=1.8)
    ax.text((O[0]+B[0])/2, (O[1]+B[1])/2 - 0.4, r"$\vec{b}=\overrightarrow{OB}$",
            ha="center", va="top", fontsize=10, color=RED)

    # AB = OB - OA
    draw_vector(ax, A, B, GREEN, lw=2.5)
    ax.text((A[0]+B[0])/2, (A[1]+B[1])/2 + 0.3, r"$\overrightarrow{AB}$",
            ha="center", va="bottom", fontsize=11, color=GREEN)

    for pt, lbl, offset in [(O, "O", (-0.2, -0.2)), (A, "A", (-0.1, 0.2)),
                             (B, "B", (0.2, 0.1))]:
        ax.scatter([pt[0]], [pt[1]], s=35, color="#333333", zorder=5)
        ax.text(pt[0]+offset[0], pt[1]+offset[1], lbl,
                ha="center", va="center", fontsize=11, color="#333333",
                fontweight="bold")

    ax.text(5.0, 0.7,
            r"$\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \vec{b} - \vec{a}$",
            ha="center", va="center", fontsize=10.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_addition(axes[0])
    draw_subtraction(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-addition-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
