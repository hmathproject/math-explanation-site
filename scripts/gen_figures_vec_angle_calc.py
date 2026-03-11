"""
gen_figures_vec_angle_calc.py — なす角と長さの計算

Panel 1: なす角 θ を内積から求める図
Panel 2: |a+b|² の展開を図で解釈（余弦定理との対応）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_angle_calc.py
出力: figures/vec-angle-calc-combined.png
      assets/images/vec-angle-calc-combined.png
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


def draw_angle_calc(ax):
    """Panel 1: cosθ = a·b / (|a||b|) でなす角を求める"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$\cos\theta = \dfrac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}$",
                 fontsize=10, pad=4)

    O = np.array([2.0, 2.0])
    theta_deg = 55
    len_a, len_b = 4.0, 3.5

    a = len_a * np.array([np.cos(np.radians(theta_deg)), np.sin(np.radians(theta_deg))])
    b = len_b * np.array([1.0, 0.0])

    # a, b
    draw_vector(ax, O, O + a, DARK_BLUE, lw=2.5, mutation_scale=22)
    ax.text(O[0]+a[0]/2-0.3, O[1]+a[1]/2+0.15, r"$\vec{a}$",
            ha="right", va="bottom", fontsize=12, color=DARK_BLUE)

    draw_vector(ax, O, O + b, RED, lw=2.5, mutation_scale=22)
    ax.text(O[0]+b[0]+0.15, O[1]+b[1], r"$\vec{b}$",
            ha="left", va="center", fontsize=12, color=RED)

    # θ の弧
    arc_r = 1.0
    arc_ts = np.linspace(0, np.radians(theta_deg), 40)
    ax.plot(O[0] + arc_r*np.cos(arc_ts),
            O[1] + arc_r*np.sin(arc_ts),
            color=ORANGE, lw=1.8)
    ax.text(O[0] + (arc_r+0.2)*np.cos(np.radians(theta_deg/2)),
            O[1] + (arc_r+0.2)*np.sin(np.radians(theta_deg/2)),
            r"$\theta$", ha="center", va="center",
            fontsize=11, color=ORANGE)

    # |a|, |b| のラベル
    ax.text(O[0]+a[0], O[1]+a[1]+0.2, r"$|\vec{a}|$",
            ha="center", va="bottom", fontsize=10, color=DARK_BLUE)
    ax.text(O[0]+b[0], O[1]-0.3, r"$|\vec{b}|$",
            ha="center", va="top", fontsize=10, color=RED)

    # 公式
    ax.text(5.5, 0.8,
            r"内積の定義: $\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta$" + "\n"
            r"両辺を $|\vec{a}||\vec{b}|$ で割る: $\cos\theta = \dfrac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}$",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def draw_norm_expansion(ax):
    """Panel 2: |a+b|² = |a|² + 2a·b + |b|² を三角形で表現"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title(r"$|\vec{a}+\vec{b}|^2 = |\vec{a}|^2 + 2\vec{a}\cdot\vec{b} + |\vec{b}|^2$",
                 fontsize=10, pad=4)

    O = np.array([1.5, 1.5])
    theta_deg = 50
    len_a, len_b = 3.5, 3.0

    a = len_a * np.array([np.cos(np.radians(theta_deg)), np.sin(np.radians(theta_deg))])
    b = len_b * np.array([1.0, 0.0])
    ab = a + b

    # a, b, a+b の矢印
    draw_vector(ax, O, O + a, DARK_BLUE, lw=2.2, mutation_scale=20)
    ax.text(O[0]+a[0]/2-0.3, O[1]+a[1]/2+0.1, r"$\vec{a}$",
            ha="right", va="bottom", fontsize=11, color=DARK_BLUE)

    draw_vector(ax, O + a, O + ab, RED, lw=2.2, mutation_scale=20)
    ax.text(O[0]+a[0]+b[0]/2, O[1]+a[1]+b[1]/2+0.2, r"$\vec{b}$",
            ha="center", va="bottom", fontsize=11, color=RED)

    draw_vector(ax, O, O + ab, GREEN, lw=2.5, mutation_scale=22)
    ax.text(O[0]+ab[0]/2+0.1, O[1]+ab[1]/2-0.3, r"$\vec{a}+\vec{b}$",
            ha="left", va="top", fontsize=11, color=GREEN)

    # θ の弧
    arc_r = 0.8
    arc_ts = np.linspace(0, np.radians(theta_deg), 40)
    ax.plot(O[0] + arc_r*np.cos(arc_ts),
            O[1] + arc_r*np.sin(arc_ts),
            color=ORANGE, lw=1.5)
    ax.text(O[0] + (arc_r+0.15)*np.cos(np.radians(theta_deg/2)),
            O[1] + (arc_r+0.15)*np.sin(np.radians(theta_deg/2)),
            r"$\theta$", ha="center", va="center",
            fontsize=10, color=ORANGE)

    # 余弦定理との比較テキスト
    ax.text(5.2, 2.2,
            "余弦定理（三角形）:\n"
            r"$c^2 = a^2 + b^2 - 2ab\cos\theta$" + "\n\n"
            "内積での展開:\n"
            r"$|\vec{a}+\vec{b}|^2 = |\vec{a}|^2 + 2\vec{a}\cdot\vec{b} + |\vec{b}|^2$",
            ha="left", va="center", fontsize=8.5, color="#444444",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f5f5",
                      edgecolor="#aaaaaa", linewidth=0.8))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_angle_calc(axes[0])
    draw_norm_expansion(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-angle-calc-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
