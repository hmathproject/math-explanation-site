"""
gen_figures_vec_figure_conditions.py — 図形条件のベクトル式化

Panel 1: 重心が3頂点の位置ベクトルの平均になる理由の図
Panel 2: 共線条件（P が直線 AB 上 ↔ OP = OA + t*AB）の図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_figure_conditions.py
出力: figures/vec-figure-conditions-combined.png
      assets/images/vec-figure-conditions-combined.png
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


def draw_centroid(ax):
    """Panel 1: 重心 G = (a+b+c)/3（中線の交点）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"重心 $\vec{g} = \dfrac{\vec{a}+\vec{b}+\vec{c}}{3}$", fontsize=10, pad=4)

    O = np.array([1.0, 1.0])
    A = np.array([4.0, 6.5])
    B = np.array([1.5, 2.5])
    C = np.array([7.5, 2.5])
    G = (A + B + C) / 3  # 重心（絶対座標）

    # 三角形 ABC
    triangle = plt.Polygon([A, B, C], facecolor="#e8f0ff", edgecolor=DARK_BLUE,
                            linewidth=1.5, alpha=0.5)
    ax.add_patch(triangle)

    # 中線 3本（薄い補助線）
    M_BC = (B + C) / 2
    M_AC = (A + C) / 2
    M_AB = (A + B) / 2
    for from_pt, to_pt in [(A, M_BC), (B, M_AC), (C, M_AB)]:
        ax.plot([from_pt[0], to_pt[0]], [from_pt[1], to_pt[1]],
                color="#aaaaaa", lw=1.0, linestyle="--")

    # OA, OB, OC, OG
    for pt, col, lbl in [(A, DARK_BLUE, r"$\vec{a}$"),
                           (B, RED, r"$\vec{b}$"),
                           (C, GREEN, r"$\vec{c}$")]:
        draw_vector(ax, O, pt, col, lw=1.6, mutation_scale=16)

    draw_vector(ax, O, G, ORANGE, lw=2.5, mutation_scale=22)
    ax.text((O[0]+G[0])/2+0.2, (O[1]+G[1])/2+0.1,
            r"$\vec{g}$", ha="left", va="center",
            fontsize=12, color=ORANGE)

    # 点ラベル
    for pt, lbl, off in [(O, "O", (-0.2, -0.2)), (A, "A", (0.0, 0.25)),
                          (B, "B", (-0.25, -0.15)), (C, "C", (0.2, -0.15)),
                          (G, "G", (0.2, 0.15))]:
        ax.scatter([pt[0]], [pt[1]], s=35, color="#333333", zorder=5)
        ax.text(pt[0]+off[0], pt[1]+off[1], lbl,
                ha="center", va="center", fontsize=11,
                color="#333333", fontweight="bold")

    ax.text(5.5, 0.5,
            "重心 G は 3頂点の「平均の位置」\n"
            r"各中線を $2:1$ に内分する点",
            ha="center", va="center", fontsize=9, color="#555555",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#aaaaaa", linewidth=0.8))


def draw_collinear(ax):
    """Panel 2: 共線条件 OP = OA + t*AB"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$P$ が直線 $AB$ 上 $\Leftrightarrow$ $\overrightarrow{OP} = \vec{a} + t\overrightarrow{AB}$",
                 fontsize=9.5, pad=4)

    O = np.array([1.0, 1.0])
    A = np.array([3.0, 5.0])
    B = np.array([6.5, 3.0])
    AB = B - A

    # t=0.6 の点（直線上）
    P = A + 0.6 * AB
    # t=1.4 の点（延長上）
    Q = A + 1.4 * AB

    # 直線の延長
    t_vals = np.array([-0.3, 1.8])
    line_pts = np.array([A + t*AB for t in t_vals])
    ax.plot(line_pts[:, 0], line_pts[:, 1],
            color="#aaaaaa", lw=1.0, linestyle="--")

    # OA, OB, OP, OQ
    draw_vector(ax, O, A, DARK_BLUE, lw=2.0, mutation_scale=18)
    ax.text((O[0]+A[0])/2-0.2, (O[1]+A[1])/2+0.1,
            r"$\vec{a}$", ha="right", va="bottom",
            fontsize=11, color=DARK_BLUE)

    draw_vector(ax, O, B, RED, lw=2.0, mutation_scale=18)
    ax.text((O[0]+B[0])/2+0.1, (O[1]+B[1])/2+0.1,
            r"$\vec{b}$", ha="left", va="bottom",
            fontsize=11, color=RED)

    draw_vector(ax, O, P, GREEN, lw=2.2, mutation_scale=20)
    ax.text((O[0]+P[0])/2-0.2, (O[1]+P[1])/2-0.35,
            r"$\overrightarrow{OP}$", ha="right", va="top",
            fontsize=10, color=GREEN)

    draw_vector(ax, O, Q, ORANGE, lw=2.0, mutation_scale=18)

    # AB 矢印
    draw_vector(ax, A, B, "#777777", lw=1.5, mutation_scale=15)
    ax.text((A[0]+B[0])/2, (A[1]+B[1])/2+0.25,
            r"$\overrightarrow{AB}$", ha="center", va="bottom",
            fontsize=10, color="#777777")

    # t ラベル
    ax.text(P[0]+0.15, P[1]+0.15, r"$t=0.6$",
            ha="left", va="bottom", fontsize=9, color=GREEN)
    ax.text(Q[0]+0.15, Q[1], r"$t=1.4$（延長上）",
            ha="left", va="center", fontsize=9, color=ORANGE)

    # 点ラベル
    for pt, lbl, off in [(O, "O", (-0.2, -0.2)), (A, "A", (-0.15, 0.2)),
                          (B, "B", (0.2, 0.1)), (P, "P", (0.0, -0.2)),
                          (Q, "Q", (0.2, 0.0))]:
        ax.scatter([pt[0]], [pt[1]], s=35, color="#333333", zorder=5)
        ax.text(pt[0]+off[0], pt[1]+off[1], lbl,
                ha="center", va="center", fontsize=10,
                color="#333333", fontweight="bold")

    ax.text(5.0, 0.5,
            r"$t$ が実数全体を動くとき $P$ は直線 $AB$ 上を動く",
            ha="center", va="center", fontsize=9, color="#555555",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f5f5f5",
                      edgecolor="#aaaaaa", linewidth=0.8))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_centroid(axes[0])
    draw_collinear(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-figure-conditions-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
