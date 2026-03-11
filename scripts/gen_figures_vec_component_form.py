"""
gen_figures_vec_component_form.py — 成分表示と大きさ

Panel 1: 成分分解の座標図（x成分・y成分への射影）
Panel 2: ピタゴラスの定理で大きさを導出する直角三角形図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_component_form.py
出力: figures/vec-component-form-combined.png
      assets/images/vec-component-form-combined.png
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


def draw_component_decomp(ax):
    """Panel 1: 成分分解の座標図"""
    # 座標系あり
    ax.set_xlim(-0.8, 5.5)
    ax.set_ylim(-0.8, 5.0)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel("x", loc="right", fontsize=10)
    ax.set_ylabel("y", loc="top", rotation=0, fontsize=10)
    ax.set_title("成分 = x軸・y軸への射影", fontsize=10, pad=4)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([1, 2, 3, 4])
    ax.tick_params(labelsize=8)

    # ベクトル a = (3, 4)
    a = np.array([3.0, 3.5])
    draw_vector(ax, (0, 0), a, DARK_BLUE, lw=2.5, mutation_scale=22)
    ax.text(a[0]/2 - 0.3, a[1]/2 + 0.1, r"$\vec{a}$",
            ha="right", va="bottom", fontsize=12, color=DARK_BLUE)

    # x 成分（水平の赤い線）
    ax.annotate("", xy=(a[0], 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", mutation_scale=16,
                                lw=1.8, color=RED))
    ax.text(a[0]/2, -0.35, r"$a_1$（x 成分）",
            ha="center", va="top", fontsize=9.5, color=RED)

    # y 成分（垂直の緑の線）
    ax.annotate("", xy=(a[0], a[1]), xytext=(a[0], 0),
                arrowprops=dict(arrowstyle="-|>", mutation_scale=16,
                                lw=1.8, color=GREEN))
    ax.text(a[0] + 0.15, a[1]/2, r"$a_2$（y 成分）",
            ha="left", va="center", fontsize=9.5, color=GREEN)

    # 点線（射影補助線）
    ax.plot([0, a[0]], [a[1], a[1]], color=DARK_BLUE, lw=1.0, linestyle=":")
    ax.plot([a[0], a[0]], [0, a[1]], color=DARK_BLUE, lw=1.0, linestyle=":")

    # 終点のラベル
    ax.scatter([a[0]], [a[1]], s=40, color=DARK_BLUE, zorder=5)
    ax.text(a[0]+0.1, a[1]+0.15, r"$(a_1,\ a_2)$",
            ha="left", va="bottom", fontsize=9.5, color=DARK_BLUE)

    # 直角マーク
    sq = 0.12
    ax.plot([a[0]-sq, a[0]-sq, a[0]], [0, sq, sq],
            color="#888888", lw=0.8)


def draw_magnitude_pythagorean(ax):
    """Panel 2: 大きさ = sqrt(a1^2 + a2^2)（ピタゴラスの定理）"""
    ax.set_xlim(-0.8, 5.5)
    ax.set_ylim(-0.8, 5.0)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlabel("x", loc="right", fontsize=10)
    ax.set_ylabel("y", loc="top", rotation=0, fontsize=10)
    ax.set_title(r"$|\vec{a}| = \sqrt{a_1^2 + a_2^2}$（ピタゴラスの定理）",
                 fontsize=10, pad=4)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([1, 2, 3, 4])
    ax.tick_params(labelsize=8)

    a = np.array([3.0, 3.5])

    # 直角三角形の塗りつぶし
    triangle = plt.Polygon([(0, 0), (a[0], 0), (a[0], a[1])],
                            facecolor="#e8f0ff", edgecolor=DARK_BLUE,
                            linewidth=1.0, alpha=0.6)
    ax.add_patch(triangle)

    # 斜辺 = |a|
    draw_vector(ax, (0, 0), a, DARK_BLUE, lw=2.5, mutation_scale=22)
    ax.text(a[0]/2 - 0.5, a[1]/2 + 0.1,
            r"$|\vec{a}|$", ha="right", va="bottom",
            fontsize=12, color=DARK_BLUE)

    # 底辺 a1
    ax.text(a[0]/2, -0.4, r"$a_1$", ha="center", va="top",
            fontsize=10.5, color=RED)

    # 高さ a2
    ax.text(a[0] + 0.15, a[1]/2, r"$a_2$", ha="left", va="center",
            fontsize=10.5, color=GREEN)

    # 直角マーク
    sq = 0.12
    ax.plot([a[0]-sq, a[0]-sq, a[0]], [0, sq, sq],
            color="#888888", lw=0.8)

    # 公式ボックス
    ax.text(1.5, 1.0,
            r"$|\vec{a}|^2 = a_1^2 + a_2^2$" + "\n"
            r"$|\vec{a}| = \sqrt{a_1^2 + a_2^2}$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_component_decomp(axes[0])
    draw_magnitude_pythagorean(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-component-form-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
