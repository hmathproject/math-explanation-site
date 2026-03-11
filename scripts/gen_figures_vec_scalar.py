"""
gen_figures_vec_scalar.py — 実数倍と平行

Panel 1: k=2, k=-1, k=1/2 の矢印で実数倍の意味を示す
Panel 2: 平行ベクトルの条件（向きの一致・逆）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_scalar.py
出力: figures/vec-scalar-combined.png
      assets/images/vec-scalar-combined.png
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


def draw_scalar_mult(ax):
    """Panel 1: k=1(基準), k=2, k=-1, k=1/2 の矢印"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.set_title("実数倍の効果", fontsize=10, pad=4)

    # 基準ベクトル a（右向き、長さ 2.0 に対応）
    ax.text(0.4, 6.8, r"$\vec{a}$（基準）", ha="left", va="center",
            fontsize=9.5, color="#333333")

    # 各行: tail_x = 0.5, 長さは k × 2.0 (unit pixels)
    unit = 2.2  # ピクセル単位の「1倍」の長さ
    configs = [
        # (k, label, color, tail_y)
        (1.0,  r"$\vec{a}$（$k=1$）",          DARK_BLUE, 5.8),
        (2.0,  r"$2\vec{a}$（$k=2$, 2倍）",    GREEN,     4.4),
        (0.5,  r"$\frac{1}{2}\vec{a}$（$k=\frac{1}{2}$, 半分）", ORANGE, 3.0),
        (-1.0, r"$-\vec{a}$（$k=-1$, 逆向き）", RED,      1.6),
    ]

    tail_x = 1.0
    for k, lbl, col, ty in configs:
        length = k * unit
        draw_vector(ax, (tail_x, ty), (tail_x + length, ty), col,
                    lw=2.2, mutation_scale=18)
        ax.text(tail_x + length + 0.2 if k >= 0 else tail_x + length - 0.2,
                ty, lbl, ha="left" if k >= 0 else "right",
                va="center", fontsize=9.5, color=col)

    ax.text(5.5, 0.7,
            "k > 0: 同じ向きに k 倍   k < 0: 逆向きに |k| 倍\n"
            "k = 0: 零ベクトル",
            ha="center", va="center", fontsize=9, color="#555555",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#aaaaaa", linewidth=0.8))


def draw_parallel_condition(ax):
    """Panel 2: 平行ベクトルの条件を図で示す"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.set_title("平行ベクトルの条件", fontsize=10, pad=4)

    # ケース1: 同じ向きの平行（k>0）
    ax.text(5.0, 7.1, "非零ベクトル同士が平行 = 一方が他方の実数倍",
            ha="center", va="center", fontsize=9, color="#333333")

    # a と b=2a（同じ方向）
    O1 = np.array([1.0, 5.7])
    a_dir = np.array([2.5, 1.0])
    draw_vector(ax, O1, O1 + a_dir, DARK_BLUE, lw=2.2)
    ax.text(O1[0] + a_dir[0]/2 - 0.1, O1[1] + a_dir[1]/2 + 0.25,
            r"$\vec{a}$", ha="center", va="bottom", fontsize=11, color=DARK_BLUE)

    O2 = np.array([1.0, 4.0])
    draw_vector(ax, O2, O2 + 1.8*a_dir, GREEN, lw=2.2)
    ax.text(O2[0] + 0.9*a_dir[0], O2[1] + 0.9*a_dir[1] + 0.25,
            r"$\vec{b}=1.8\vec{a}$", ha="center", va="bottom",
            fontsize=10, color=GREEN)

    # ケース2: 逆向きの平行（k<0）
    O3 = np.array([1.0, 2.6])
    draw_vector(ax, O3, O3 + a_dir, DARK_BLUE, lw=2.2)
    ax.text(O3[0] + a_dir[0]/2, O3[1] + a_dir[1]/2 + 0.25,
            r"$\vec{a}$", ha="center", va="bottom", fontsize=11, color=DARK_BLUE)

    O4 = np.array([1.0, 1.5])
    draw_vector(ax, O4 + a_dir, O4, RED, lw=2.2)
    ax.text(O4[0] + a_dir[0]/2, O4[1] + a_dir[1]/2 + 0.25,
            r"$\vec{c}=-\vec{a}$", ha="center", va="bottom",
            fontsize=10, color=RED)

    ax.text(5.0, 0.7,
            "零ベクトル " + r"$\vec{0}$" + " は向きが定義されないため\n"
            "平行条件 " + r"$\vec{b}=k\vec{a}$" + " から除外して考える",
            ha="center", va="center", fontsize=9, color="#555555",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff8ee",
                      edgecolor=ORANGE, linewidth=0.8))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_scalar_mult(axes[0])
    draw_parallel_condition(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-scalar-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
