"""
gen_figures_vec_linear_combo.py — 1次結合と分解

Panel 1: 基本ベクトル e1=(1,0), e2=(0,1) の図
Panel 2: 任意ベクトルを sa+tb で分解する図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_linear_combo.py
出力: figures/vec-linear-combo-combined.png
      assets/images/vec-linear-combo-combined.png
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


def draw_basis_vectors(ax):
    """Panel 1: 基本ベクトル e1, e2 と任意ベクトルの分解"""
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 4.5)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel("x", loc="right", fontsize=10)
    ax.set_ylabel("y", loc="top", rotation=0, fontsize=10)
    ax.set_title(r"基本ベクトル $\vec{e}_1=(1,0),\ \vec{e}_2=(0,1)$",
                 fontsize=10, pad=4)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 5))
    ax.tick_params(labelsize=8)

    # e1 = (1,0)
    draw_vector(ax, (0, 0), (1, 0), RED, lw=2.5, mutation_scale=22)
    ax.text(0.5, -0.3, r"$\vec{e}_1=(1,0)$", ha="center", va="top",
            fontsize=10, color=RED)

    # e2 = (0,1)
    draw_vector(ax, (0, 0), (0, 1), GREEN, lw=2.5, mutation_scale=22)
    ax.text(-0.15, 0.5, r"$\vec{e}_2=(0,1)$", ha="right", va="center",
            fontsize=10, color=GREEN)

    # 例: a = (3, 2) = 3e1 + 2e2
    a = np.array([3.0, 2.5])
    draw_vector(ax, (0, 0), a, DARK_BLUE, lw=2.2)
    ax.text(a[0]/2 + 0.1, a[1]/2 + 0.15, r"$\vec{a}=(3,2.5)$",
            ha="left", va="bottom", fontsize=10, color=DARK_BLUE)

    # 3e1 成分
    draw_vector(ax, (0, 0), (a[0], 0), RED, lw=1.5, mutation_scale=14)
    ax.text(a[0]/2, -0.6, r"$3\vec{e}_1$", ha="center", va="top",
            fontsize=9.5, color=RED)

    # 2e2 成分
    draw_vector(ax, (a[0], 0), (a[0], a[1]), GREEN, lw=1.5, mutation_scale=14)
    ax.text(a[0]+0.15, a[1]/2, r"$2.5\vec{e}_2$", ha="left", va="center",
            fontsize=9.5, color=GREEN)

    ax.text(2.5, 0.8,
            r"$\vec{a} = 3\vec{e}_1 + 2.5\vec{e}_2$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.8))


def draw_general_decomp(ax):
    """Panel 2: 非平行な a,b で平面上の任意ベクトルを表す"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$\vec{p} = s\vec{a} + t\vec{b}$（1次結合）", fontsize=10, pad=4)

    O = np.array([1.5, 1.5])
    a = np.array([2.5, 0.5])
    b = np.array([0.8, 2.2])

    # s=2, t=1.5
    s, t = 2.0, 1.5
    sa = s * a
    tb = t * b
    p = sa + tb

    # a, b
    draw_vector(ax, O, O + a, DARK_BLUE, lw=2.2)
    ax.text(O[0]+a[0]/2, O[1]+a[1]/2-0.3, r"$\vec{a}$",
            ha="center", va="top", fontsize=11, color=DARK_BLUE)

    draw_vector(ax, O, O + b, RED, lw=2.2)
    ax.text(O[0]+b[0]/2-0.2, O[1]+b[1]/2, r"$\vec{b}$",
            ha="right", va="center", fontsize=11, color=RED)

    # sa: O → O+sa
    draw_vector(ax, O, O+sa, DARK_BLUE, lw=1.8, mutation_scale=16)
    ax.text(O[0]+sa[0]/2, O[1]+sa[1]/2-0.3, r"$s\vec{a}$",
            ha="center", va="top", fontsize=10, color=DARK_BLUE)

    # tb: O+sa → O+sa+tb = p
    draw_vector(ax, O+sa, O+p, RED, lw=1.8, mutation_scale=16)
    ax.text(O[0]+sa[0]+tb[0]/2+0.1, O[1]+sa[1]+tb[1]/2,
            r"$t\vec{b}$", ha="left", va="center", fontsize=10, color=RED)

    # p: O → p
    draw_vector(ax, O, O+p, GREEN, lw=2.5, mutation_scale=22)
    ax.text(O[0]+p[0]/2-0.2, O[1]+p[1]/2+0.15, r"$\vec{p}$",
            ha="right", va="bottom", fontsize=12, color=GREEN)

    # 点
    for pt, lbl, off in [(O, "O", (-0.2, -0.2)), (O+p, "P", (0.1, 0.1))]:
        ax.scatter([pt[0]], [pt[1]], s=35, color="#333333", zorder=5)
        ax.text(pt[0]+off[0], pt[1]+off[1], lbl,
                ha="center", va="center", fontsize=11, color="#333333",
                fontweight="bold")

    ax.text(5.5, 0.7,
            r"$\vec{a}, \vec{b}$ が非平行なら" + "\n"
            r"平面上のすべての $\vec{p}$ を $s\vec{a}+t\vec{b}$ で表せる",
            ha="center", va="center", fontsize=9, color="#555555",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#aaaaaa", linewidth=0.8))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_basis_vectors(axes[0])
    draw_general_decomp(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-linear-combo-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
