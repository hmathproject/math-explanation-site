"""
gen_figures_vec_dot_product.py — 内積の意味

Panel 1: 射影の図（a を b に射影した長さが |a|cosθ）
Panel 2: cosθ の符号と内積の正負の対応図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_dot_product.py
出力: figures/vec-dot-product-combined.png
      assets/images/vec-dot-product-combined.png
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


def draw_projection(ax):
    """Panel 1: a の b への射影 = |a|cosθ"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$（射影から）",
                 fontsize=10, pad=4)

    O = np.array([1.5, 2.0])
    theta = np.radians(35)
    len_a = 4.0
    len_b = 3.5

    a = len_a * np.array([np.cos(np.radians(60)), np.sin(np.radians(60))])
    b = len_b * np.array([np.cos(np.radians(0)), np.sin(np.radians(0))])

    # b の延長（薄い補助線）
    b_unit = b / np.linalg.norm(b)
    ax.plot([O[0], O[0] + b_unit[0] * 5.5], [O[1], O[1] + b_unit[1] * 5.5],
            color="#cccccc", lw=1.0, linestyle="-")

    # a, b の矢印
    draw_vector(ax, O, O + a, DARK_BLUE, lw=2.5, mutation_scale=22)
    ax.text(O[0]+a[0]/2-0.2, O[1]+a[1]/2+0.1, r"$\vec{a}$",
            ha="right", va="bottom", fontsize=12, color=DARK_BLUE)

    draw_vector(ax, O, O + b, RED, lw=2.5, mutation_scale=22)
    ax.text(O[0]+b[0]+0.1, O[1]+b[1], r"$\vec{b}$",
            ha="left", va="center", fontsize=12, color=RED)

    # 射影の足（垂線の足）
    proj_len = np.dot(a, b_unit)
    proj_pt = O + proj_len * b_unit

    # 射影の矢印（緑）
    draw_vector(ax, O, proj_pt, GREEN, lw=2.2, mutation_scale=18)
    ax.text(O[0]+proj_len/2*b_unit[0], O[1]+proj_len/2*b_unit[1]-0.35,
            r"$|\vec{a}|\cos\theta$", ha="center", va="top",
            fontsize=10, color=GREEN)

    # 垂線
    ax.plot([O[0]+a[0], proj_pt[0]], [O[1]+a[1], proj_pt[1]],
            color="#888888", lw=1.2, linestyle="--")

    # 直角マーク
    perp_dir = a - proj_len * b_unit
    perp_unit = perp_dir / np.linalg.norm(perp_dir)
    sq_size = 0.2
    sq_pt = proj_pt + sq_size * b_unit + sq_size * perp_unit
    ax.plot([proj_pt[0]+sq_size*b_unit[0],
             sq_pt[0],
             proj_pt[0]+sq_size*perp_unit[0]],
            [proj_pt[1]+sq_size*b_unit[1],
             sq_pt[1],
             proj_pt[1]+sq_size*perp_unit[1]],
            color="#888888", lw=0.9)

    # 角度 θ の弧
    arc_r = 0.8
    arc_theta = np.linspace(0, np.radians(60), 40)
    ax.plot(O[0] + arc_r*np.cos(arc_theta),
            O[1] + arc_r*np.sin(arc_theta),
            color=ORANGE, lw=1.5)
    ax.text(O[0]+arc_r*np.cos(np.radians(30))+0.1,
            O[1]+arc_r*np.sin(np.radians(30))+0.05,
            r"$\theta$", ha="left", va="bottom", fontsize=11, color=ORANGE)

    ax.text(5.5, 0.7,
            r"$\vec{a} \cdot \vec{b}$" + " = （" + r"$\vec{b}$" + " 方向への射影）× " + r"$|\vec{b}|$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def draw_dot_product_sign(ax):
    """Panel 2: cosθ の符号と内積の正負"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$\theta$ の大きさと内積の符号", fontsize=10, pad=4)

    configs = [
        # (theta_deg, dot_sign, color, label, y_center)
        (45,  "> 0", GREEN,     r"$0 \leq \theta < 90°$: 同じ方向寄り", 5.8),
        (90,  "= 0", ORANGE,    r"$\theta = 90°$: 直交（垂直）",         4.0),
        (130, "< 0", RED,       r"$90° < \theta \leq 180°$: 逆方向寄り", 2.2),
    ]

    for deg, sign, col, lbl, yc in configs:
        theta = np.radians(deg)
        cx = 2.0
        b_tip = np.array([cx + 2.5, yc])
        a_tip = np.array([cx + 2.5*np.cos(theta), yc + 2.5*np.sin(theta)])

        draw_vector(ax, (cx, yc), b_tip, "#888888", lw=1.8, mutation_scale=16)
        draw_vector(ax, (cx, yc), a_tip, col, lw=2.2, mutation_scale=18)

        ax.text(b_tip[0]+0.1, yc, r"$\vec{b}$", ha="left", va="center",
                fontsize=10, color="#888888")
        ax.text(a_tip[0]+0.1, a_tip[1], r"$\vec{a}$", ha="left", va="center",
                fontsize=10, color=col)

        arc_r = 0.6
        arc_thetas = np.linspace(0, theta, 30)
        ax.plot(cx + arc_r*np.cos(arc_thetas),
                yc + arc_r*np.sin(arc_thetas),
                color=ORANGE, lw=1.2)

        ax.text(6.0, yc, r"$\vec{a}\cdot\vec{b}$" + f" {sign}",
                ha="left", va="center", fontsize=10.5, color=col,
                fontweight="bold")
        ax.text(6.0, yc - 0.6, lbl, ha="left", va="center",
                fontsize=8.5, color="#555555")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_projection(axes[0])
    draw_dot_product_sign(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-dot-product-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
