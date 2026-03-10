"""
gen_figures_diff_derivative.py — 導関数の概念図生成

Panel 1: 差商（割線）→ 接線の極限イメージ
Panel 2: f'(x)>0 なら増加、f'(x)<0 なら減少 の概念図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_derivative.py
出力: site/figures/diff-derivative-intro-combined.png
      site/assets/images/diff-derivative-intro-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.patches as mpatches
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
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_secant_to_tangent(ax):
    """Panel 1: 差商（割線）から接線へのイメージ"""
    def f(x):
        return x ** 3 - 2 * x ** 2 + 1.5

    x0 = 0.5  # 接点

    x_range = np.linspace(-0.3, 2.2, 400)
    y_range = f(x_range)

    ax.set_xlim(-0.4, 2.5)
    ax.set_ylim(-0.5, 2.8)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.4, 0), xytext=(-0.35, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.43, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 2.7), xytext=(0, -0.45),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, 2.72, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.07, -0.08, "O", ha="right", va="top", fontsize=9)

    # f(x) の曲線
    ax.plot(x_range, y_range, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 接点
    x0_y = f(x0)
    ax.plot(x0, x0_y, "o", color=RED, markersize=6, zorder=6)
    ax.text(x0 - 0.08, x0_y + 0.15, r"$P(a,\,f(a))$",
            ha="right", va="bottom", fontsize=8.5, color=RED)

    # 割線（遠い点 Q）
    xq_far = 1.9
    slope_far = (f(xq_far) - x0_y) / (xq_far - x0)
    xq_line = np.linspace(0.1, 2.1, 100)
    yq_far = x0_y + slope_far * (xq_line - x0)
    ax.plot(xq_line, yq_far, color=ORANGE, linewidth=1.2, linestyle="--",
            label=r"割線（$h$ が大きい）", zorder=2)

    # 割線（近い点 Q'）
    xq_near = 1.1
    slope_near = (f(xq_near) - x0_y) / (xq_near - x0)
    yq_near = x0_y + slope_near * (xq_line - x0)
    ax.plot(xq_line, yq_near, color="#aa44aa", linewidth=1.2, linestyle="--",
            label=r"割線（$h$ が小さい）", zorder=2)

    # 接線（実際の微分係数）
    f_prime_x0 = 3 * x0 ** 2 - 4 * x0
    xtan_line = np.linspace(0.0, 1.8, 100)
    ytan = x0_y + f_prime_x0 * (xtan_line - x0)
    ax.plot(xtan_line, ytan, color=RED, linewidth=2.0, zorder=4,
            label=r"接線（$h \to 0$ の極限）")

    # Q 点
    ax.plot(xq_far, f(xq_far), "o", color=ORANGE, markersize=5, zorder=5)
    ax.text(xq_far + 0.05, f(xq_far), r"$Q$",
            ha="left", va="center", fontsize=8.5, color=ORANGE)

    # 差商の説明テキスト
    ax.text(1.5, 0.2,
            r"$\frac{f(a+h)-f(a)}{h}$" + "\n" + r"$\to f'(a)$（$h\to 0$）",
            ha="center", va="bottom", fontsize=8.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0", edgecolor=RED, alpha=0.8))

    ax.set_title("差商の極限 = 接線の傾き = f'(a)", fontsize=9.5, pad=4)


def draw_sign_of_derivative(ax):
    """Panel 2: f'(x)>0 なら増加、f'(x)<0 なら減少"""
    def f(x):
        return x ** 3 - 3 * x + 0.5

    def fp(x):
        return 3 * x ** 2 - 3

    x_range = np.linspace(-2.0, 2.0, 400)
    y_range = f(x_range)

    ax.set_xlim(-2.3, 2.5)
    ax.set_ylim(-3.0, 3.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.4, 0), xytext=(-2.2, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.43, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 3.4), xytext=(0, -2.9),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, 3.42, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.1, -0.18, "O", ha="right", va="top", fontsize=9)

    # 増加領域（f'>0）を緑でハイライト
    x_inc1 = np.linspace(-2.0, -1.0, 200)
    ax.fill_between(x_inc1, f(x_inc1), -3.2, alpha=0.12, color=GREEN)
    x_inc2 = np.linspace(1.0, 2.0, 200)
    ax.fill_between(x_inc2, f(x_inc2), -3.2, alpha=0.12, color=GREEN)

    # 減少領域（f'<0）を赤でハイライト
    x_dec = np.linspace(-1.0, 1.0, 200)
    ax.fill_between(x_dec, f(x_dec), -3.2, alpha=0.10, color=RED)

    # f(x) の曲線
    ax.plot(x_range, y_range, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 極値点
    for xp, label, va in [(-1, r"$x=-1$", "bottom"), (1, r"$x=1$", "bottom")]:
        ax.plot(xp, f(xp), "o", color=RED, markersize=6, zorder=6)
        ax.plot([xp, xp], [-3.0, f(xp)], ":", color="gray", linewidth=0.8)
        ax.text(xp, -3.15, label, ha="center", va="top", fontsize=8)

    # 矢印ラベル（増加・減少方向）
    ax.annotate("", xy=(-1.5, f(-1.5) + 0.5), xytext=(-1.5, f(-1.5) - 0.1),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5))
    ax.text(-1.55, f(-1.5) + 0.6, r"$f'>0$" + "\n増加",
            ha="right", va="bottom", fontsize=8, color=GREEN)

    ax.annotate("", xy=(0, f(0) - 0.5), xytext=(0, f(0) + 0.1),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5))
    ax.text(0.1, f(0) - 0.6, r"$f'<0$" + "\n減少",
            ha="left", va="top", fontsize=8, color=RED)

    ax.annotate("", xy=(1.5, f(1.5) + 0.5), xytext=(1.5, f(1.5) - 0.1),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5))
    ax.text(1.55, f(1.5) + 0.6, r"$f'>0$" + "\n増加",
            ha="left", va="bottom", fontsize=8, color=GREEN)

    ax.set_title(r"$f'(x)$ の符号 → 関数の増加・減少", fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_secant_to_tangent(axes[0])
    draw_sign_of_derivative(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "diff-derivative-intro-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
