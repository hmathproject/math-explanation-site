"""
gen_figures_vec_perpendicular.py — 垂直条件

Panel 1: 垂直の矢印図（a⊥b → a·b=0, cos90°=0）
Panel 2: 余弦定理から成分公式 a·b=a1b1+a2b2 を導く図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_perpendicular.py
出力: figures/vec-perpendicular-combined.png
      assets/images/vec-perpendicular-combined.png
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


def draw_perpendicular(ax):
    """Panel 1: θ=90° → cos90°=0 → a·b=0"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"垂直 $\Leftrightarrow$ $\vec{a} \cdot \vec{b} = 0$", fontsize=10, pad=4)

    O = np.array([3.5, 3.0])

    # a (右向き)
    a = np.array([3.5, 0.0])
    draw_vector(ax, O, O + a, DARK_BLUE, lw=2.5, mutation_scale=22)
    ax.text(O[0]+a[0]+0.15, O[1], r"$\vec{a}$",
            ha="left", va="center", fontsize=12, color=DARK_BLUE)

    # b (上向き)
    b = np.array([0.0, 3.0])
    draw_vector(ax, O, O + b, RED, lw=2.5, mutation_scale=22)
    ax.text(O[0], O[1]+b[1]+0.15, r"$\vec{b}$",
            ha="center", va="bottom", fontsize=12, color=RED)

    # 直角マーク
    sq = 0.25
    ax.plot([O[0]+sq, O[0]+sq, O[0]], [O[1], O[1]+sq, O[1]+sq],
            color="#333333", lw=1.2)
    ax.text(O[0]+sq+0.05, O[1]+sq+0.05, "90°",
            ha="left", va="bottom", fontsize=9, color=ORANGE)

    # 説明ボックス
    ax.text(5.0, 0.9,
            r"$\cos 90° = 0$" + " なので\n"
            r"$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos 90° = 0$",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))

    ax.text(5.0, 6.4,
            "垂直のとき内積が 0 になるのは" + "\n"
            r"$\cos 90° = 0$ だから（定義に代入すると必然）",
            ha="center", va="center", fontsize=9, color="#555555")


def draw_component_formula(ax):
    """Panel 2: 余弦定理 → 成分公式の導出の補助図"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"余弦定理から成分公式を導く", fontsize=10, pad=4)

    O = np.array([1.5, 1.5])
    # a = (a1, a2), b = (b1, b2), a-b の三角形
    a_pt = np.array([5.5, 4.5])
    b_pt = np.array([6.5, 1.5])

    # a, b の矢印
    draw_vector(ax, O, a_pt, DARK_BLUE, lw=2.2, mutation_scale=20)
    ax.text((O[0]+a_pt[0])/2-0.3, (O[1]+a_pt[1])/2+0.1, r"$\vec{a}$",
            ha="right", va="bottom", fontsize=11, color=DARK_BLUE)

    draw_vector(ax, O, b_pt, RED, lw=2.2, mutation_scale=20)
    ax.text((O[0]+b_pt[0])/2, (O[1]+b_pt[1])/2-0.35, r"$\vec{b}$",
            ha="center", va="top", fontsize=11, color=RED)

    # a-b の辺（a の先端から b の先端）
    ax.plot([a_pt[0], b_pt[0]], [a_pt[1], b_pt[1]],
            color=GREEN, lw=2.0, linestyle="-")
    ax.text((a_pt[0]+b_pt[0])/2+0.15, (a_pt[1]+b_pt[1])/2,
            r"$|\vec{a}-\vec{b}|$", ha="left", va="center",
            fontsize=10, color=GREEN)

    # 角度 θ
    vec_a = a_pt - O
    vec_b = b_pt - O
    theta = np.arccos(np.dot(vec_a, vec_b) /
                      (np.linalg.norm(vec_a) * np.linalg.norm(vec_b)))
    arc_r = 0.9
    theta_a = np.arctan2(vec_a[1], vec_a[0])
    theta_b = np.arctan2(vec_b[1], vec_b[0])
    arc_ts = np.linspace(theta_b, theta_a, 40)
    ax.plot(O[0] + arc_r*np.cos(arc_ts),
            O[1] + arc_r*np.sin(arc_ts),
            color=ORANGE, lw=1.5)
    theta_mid = (theta_a + theta_b) / 2
    ax.text(O[0] + (arc_r+0.2)*np.cos(theta_mid),
            O[1] + (arc_r+0.2)*np.sin(theta_mid),
            r"$\theta$", ha="center", va="center",
            fontsize=11, color=ORANGE)

    # 導出の流れ（テキスト）
    steps = [
        r"余弦定理: $|\vec{a}-\vec{b}|^2 = |\vec{a}|^2 + |\vec{b}|^2 - 2|\vec{a}||\vec{b}|\cos\theta$",
        r"左辺を成分で展開: $(a_1-b_1)^2 + (a_2-b_2)^2$",
        r"整理すると: $\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2$",
    ]
    y0 = 2.8
    for i, s in enumerate(steps):
        ax.text(0.3, y0 - i*0.85, s, ha="left", va="center",
                fontsize=8.5, color=DARK_BLUE if i == 2 else "#444444")

    # 結果ボックス
    ax.text(5.0, 0.55,
            r"$\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2$",
            ha="center", va="center", fontsize=11, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_perpendicular(axes[0])
    draw_component_formula(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-perpendicular-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
