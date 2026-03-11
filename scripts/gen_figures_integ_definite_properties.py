"""
gen_figures_integ_definite_properties.py — 定積分の性質

Panel 1: 区間加法性 ∫₀² = ∫₀¹ + ∫₁²
Panel 2: 奇関数の対称性 ∫₋ₐᵃ f(x)dx = 0

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_definite_properties.py
出力: site/figures/integ-definite-properties-combined.png
      site/assets/images/integ-definite-properties-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# ── フォント設定（CLAUDE.md 準拠）──────────────────────────────
if platform.system() == "Darwin":
    plt.rcParams["font.family"] = "Hiragino Sans"
elif platform.system() == "Windows":
    plt.rcParams["font.family"] = "MS Gothic"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["axes.unicode_minus"] = False

# ── 出力先 ──────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
FIGURES_DIR = BASE_DIR / "figures"
SITE_IMAGES_DIR = BASE_DIR / "assets" / "images"
FIGURES_DIR.mkdir(exist_ok=True)
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#bb6600"
GRAY = "#888888"
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def _draw_axes(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    ax.annotate("", xy=(xlim[1] - 0.05, 0), xytext=(xlim[0] + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xlim[1], 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, ylim[1] - 0.1), xytext=(0, ylim[0] + 0.1),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, ylim[1] - 0.08, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.1, -0.12, "O", ha="right", va="top", fontsize=9)


def draw_additivity(ax):
    """Panel 1: 区間加法性"""
    _draw_axes(ax, xlim=(-0.4, 2.7), ylim=(-0.6, 5.2))

    def f(x):
        return -x ** 2 + 4

    x_full = np.linspace(-0.2, 2.3, 400)

    # 塗りつぶし [0,1]: 青
    x1 = np.linspace(0, 1, 300)
    ax.fill_between(x1, f(x1), 0,
                    color="#aaccff", alpha=0.75, zorder=2,
                    label=r"$\int_0^1 f\,dx$")
    # 塗りつぶし [1,2]: 緑
    x2 = np.linspace(1, 2, 300)
    ax.fill_between(x2, f(x2), 0,
                    color="#aaffcc", alpha=0.75, zorder=2,
                    label=r"$\int_1^2 f\,dx$")

    ax.plot(x_full, f(x_full), color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 境界線
    for xv, lab in [(0, "a=0"), (1, "b=1"), (2, "c=2")]:
        ax.plot([xv, xv], [0, f(xv)], color=GRAY, linewidth=1.0,
                linestyle="--", alpha=0.8)
        ax.text(xv, -0.2, f"${lab.split('=')[0]}={lab.split('=')[1]}$",
                ha="center", va="top", fontsize=8.5)

    # 面積ラベル
    ax.text(0.5, 1.5, r"青: $\int_0^1$",
            ha="center", va="center", fontsize=8, color=DARK_BLUE)
    ax.text(1.5, 0.9, r"緑: $\int_1^2$",
            ha="center", va="center", fontsize=8, color=GREEN)

    ax.text(1.1, 4.5,
            r"$\int_0^2 f\,dx = \int_0^1 f\,dx + \int_1^2 f\,dx$",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    ax.legend(loc="upper right", fontsize=8)
    ax.set_title(r"区間加法性: $\int_0^2 = \int_0^1 + \int_1^2$", fontsize=9.5, pad=4)


def draw_odd_symmetry(ax):
    """Panel 2: 奇関数 f(x)=x³ の対称キャンセル"""
    _draw_axes(ax, xlim=(-2.4, 2.7), ylim=(-9.5, 9.5))

    x = np.linspace(-2.0, 2.0, 500)
    y = x ** 3

    # 正の部分 [0, 2]: 緑
    x_pos = np.linspace(0, 2, 300)
    ax.fill_between(x_pos, x_pos ** 3, 0,
                    color="#aaffcc", alpha=0.75, zorder=2,
                    label=r"$f>0$ の部分（$+$）")

    # 負の部分 [-2, 0]: 赤
    x_neg = np.linspace(-2, 0, 300)
    ax.fill_between(x_neg, x_neg ** 3, 0,
                    color="#ffaaaa", alpha=0.75, zorder=2,
                    label=r"$f<0$ の部分（$-$）")

    ax.plot(x, y, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 対称点ラベル
    ax.text(-2.0, -0.5, r"$-a$", ha="center", va="top", fontsize=9)
    ax.text(2.0, -0.5, r"$a$", ha="center", va="top", fontsize=9)
    for xv in [-2, 2]:
        ax.plot([xv, xv], [0, xv ** 3], color=GRAY, linewidth=1.0,
                linestyle="--", alpha=0.7)

    # ±ラベル
    ax.text(-1.0, -2.5, r"$-$", ha="center", va="center",
            fontsize=16, color=RED, fontweight="bold")
    ax.text(1.0, 2.5, r"$+$", ha="center", va="center",
            fontsize=16, color=GREEN, fontweight="bold")

    # 説明ボックス
    ax.text(0.1, 8.2,
            "奇関数: $f(-x)=-f(x)$\n"
            r"$\Rightarrow \int_{-a}^{a} f(x)\,dx = 0$"
            "\n（正と負が打ち消し合う）",
            ha="left", va="top", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    # 参考: 偶関数メモ
    ax.text(-2.3, -7.5,
            r"偶関数 $g(-x)=g(x)$ なら:" + "\n"
            r"$\int_{-a}^{a} g\,dx = 2\int_0^a g\,dx$",
            ha="left", va="bottom", fontsize=8, color=ORANGE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fffbe6",
                      edgecolor=ORANGE, alpha=0.85))

    ax.legend(loc="lower right", fontsize=7.5)
    ax.set_title(r"奇関数: $\int_{-a}^{a} x^3\,dx = 0$（正負が打ち消す）",
                 fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_additivity(axes[0])
    draw_odd_symmetry(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-definite-properties-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
