"""
gen_figures_vec_component_ops.py — 成分による演算

Panel 1: 成分ごとの加法が幾何の頭尾連結と一致することを座標系で示す
Panel 2: 実数倍が成分のk倍になる理由を座標系で示す

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_component_ops.py
出力: figures/vec-component-ops-combined.png
      assets/images/vec-component-ops-combined.png
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


def draw_component_addition(ax):
    """Panel 1: a+b の成分計算が幾何の頭尾連結と一致"""
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 5.5)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel("x", loc="right", fontsize=10)
    ax.set_ylabel("y", loc="top", rotation=0, fontsize=10)
    ax.set_title(r"$\vec{a}+\vec{b}$ の成分計算", fontsize=10, pad=4)
    ax.set_xticks(range(1, 7))
    ax.set_yticks(range(1, 6))
    ax.tick_params(labelsize=8)

    # a = (2, 1), b = (1, 2.5), a+b = (3, 3.5)
    a = np.array([2.0, 1.0])
    b = np.array([1.5, 2.5])
    ab = a + b

    # a: O → A
    draw_vector(ax, (0, 0), a, DARK_BLUE, lw=2.2)
    ax.text(a[0]/2 - 0.2, a[1]/2 - 0.3, r"$\vec{a}=(2,1)$",
            ha="right", va="top", fontsize=9.5, color=DARK_BLUE)

    # b: A → A+B (頭尾連結)
    draw_vector(ax, a, ab, RED, lw=2.2)
    ax.text(a[0] + b[0]/2 + 0.15, a[1] + b[1]/2,
            r"$\vec{b}=(1.5,2.5)$", ha="left", va="center",
            fontsize=9.5, color=RED)

    # a+b: O → A+B
    draw_vector(ax, (0, 0), ab, GREEN, lw=2.5, mutation_scale=22)
    ax.text(ab[0]/2 - 0.15, ab[1]/2 + 0.1,
            r"$\vec{a}+\vec{b}=(3.5,3.5)$", ha="right", va="bottom",
            fontsize=9.5, color=GREEN)

    # 成分の対応（点線補助線）
    ax.plot([0, ab[0]], [ab[1], ab[1]], color=GREEN, lw=0.8, linestyle=":")
    ax.plot([ab[0], ab[0]], [0, ab[1]], color=GREEN, lw=0.8, linestyle=":")
    ax.text(ab[0]+0.08, 0, f"{ab[0]:.1f}", ha="left", va="top",
            fontsize=8, color=GREEN)
    ax.text(0, ab[1]+0.1, f"{ab[1]:.1f}", ha="right", va="bottom",
            fontsize=8, color=GREEN)


def draw_scalar_multiple(ax):
    """Panel 2: k倍すると各成分もk倍になる"""
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 5.5)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel("x", loc="right", fontsize=10)
    ax.set_ylabel("y", loc="top", rotation=0, fontsize=10)
    ax.set_title(r"$k\vec{a}$ の成分計算", fontsize=10, pad=4)
    ax.set_xticks(range(1, 7))
    ax.set_yticks(range(1, 6))
    ax.tick_params(labelsize=8)

    # a = (1.5, 1)
    a = np.array([1.5, 1.0])
    k = 2.5

    # a 自身
    draw_vector(ax, (0, 0), a, DARK_BLUE, lw=2.2)
    ax.text(a[0]/2 - 0.2, a[1]/2 + 0.15,
            r"$\vec{a}=(1.5,1)$", ha="right", va="bottom",
            fontsize=9.5, color=DARK_BLUE)

    # k*a
    draw_vector(ax, (0, 0), k*a, GREEN, lw=2.5, mutation_scale=22)
    ax.text((k*a)[0]/2 + 0.1, (k*a)[1]/2 + 0.15,
            r"$2.5\vec{a}=(3.75,2.5)$", ha="left", va="bottom",
            fontsize=9.5, color=GREEN)

    # 点線で成分確認
    ax.plot([0, a[0]], [a[1], a[1]], color=DARK_BLUE, lw=0.8, linestyle=":")
    ax.plot([a[0], a[0]], [0, a[1]], color=DARK_BLUE, lw=0.8, linestyle=":")
    ax.plot([0, k*a[0]], [k*a[1], k*a[1]], color=GREEN, lw=0.8, linestyle=":")
    ax.plot([k*a[0], k*a[0]], [0, k*a[1]], color=GREEN, lw=0.8, linestyle=":")

    # 公式ボックス
    ax.text(3.0, 1.2,
            r"$k\vec{a} = k(a_1, a_2) = (ka_1, ka_2)$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_component_addition(axes[0])
    draw_scalar_multiple(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-component-ops-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
