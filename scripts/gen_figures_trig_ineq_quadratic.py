"""
gen_figures_trig_ineq_quadratic.py — 置換して二次不等式に帰着 概念図生成

2sin²θ − sinθ − 1 ≥ 0 → t = sinθ ≤ -1/2 または t = 1
解: θ = π/2 および [7π/6, 11π/6]

Panel 1: t 軸上での不等式の解（-1 ≤ t ≤ -1/2 と t = 1）を図示
Panel 2: sin グラフ上でθの解区間を塗りつぶし

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_ineq_quadratic.py
出力: site/figures/trig-ineq-quadratic.png
      site/assets/images/trig-ineq-quadratic.png
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
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#cc6600"

arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_panel1(ax):
    """t 軸上の不等式の解を示す数直線。"""
    ax.axis("off")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.2, 1.2)

    # t 軸
    ax.annotate("", xy=(1.45, 0), xytext=(-1.45, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(1.47, 0, r"$t$", ha="left", va="center", fontsize=11)

    # 目盛り: -1, -1/2, 0, 1
    ticks = [(-1, r"$-1$"), (-0.5, r"$-\frac{1}{2}$"), (0, r"$0$"), (1, r"$1$")]
    for tv, lbl in ticks:
        ax.plot([tv, tv], [-0.07, 0.07], "k-", lw=1.0)
        ax.text(tv, -0.18, lbl, ha="center", va="top", fontsize=9)

    # 解の区間: -1 ≤ t ≤ -1/2 (closed)
    ax.plot([-1.0, -0.5], [0, 0], color=RED, lw=5, solid_capstyle="butt",
            alpha=0.6, zorder=2)
    ax.plot(-1.0, 0, "o", color=RED, markersize=8, zorder=5)
    ax.plot(-0.5, 0, "o", color=RED, markersize=8, zorder=5)
    ax.text(-0.75, 0.25,
            r"$-1 \leq t \leq -\frac{1}{2}$",
            ha="center", va="bottom", fontsize=9.5, color=RED)

    # 解: t = 1 (single point)
    ax.plot(1.0, 0, "o", color=GREEN, markersize=10, zorder=5)
    ax.text(1.0, 0.25, r"$t = 1$",
            ha="center", va="bottom", fontsize=9.5, color=GREEN)

    # 定義域ラベル
    ax.annotate("", xy=(1.0, -0.5), xytext=(-1.0, -0.5),
                arrowprops=dict(arrowstyle="<->", color="#888888", lw=1.2))
    ax.text(0, -0.65, r"定義域 $-1 \leq t \leq 1$",
            ha="center", va="top", fontsize=8.5, color="#666666")

    ax.text(0, 0.95, r"t の不等式の解（定義域 $-1 \leq t \leq 1$ との共通部分）",
            ha="center", va="top", fontsize=8.5, fontweight="bold")


def draw_panel2(ax):
    """sin グラフ上で解の θ 区間を塗りつぶす。"""
    x_lo, x_hi = 0, 2 * np.pi
    px, py = 0.5, 0.45
    ax.axis("off")
    ax.set_xlim(x_lo - px, x_hi + px)
    ax.set_ylim(-1.6 - py, 1.6 + py)

    ax.annotate("", xy=(x_hi + px - 0.05, 0), xytext=(x_lo - px + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_hi + px - 0.02, 0, r"$\theta$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(x_lo, 1.6 + py - 0.05), xytext=(x_lo, -1.6 - py + 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_lo + 0.05, 1.6 + py - 0.02, r"$y$", ha="left", va="bottom", fontsize=10)

    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([x_lo - 0.06, x_lo + 0.06], [yv, yv], "k-", lw=0.8)
        ax.text(x_lo - 0.12, yv, lbl, ha="right", va="center", fontsize=8)
    ax.text(x_lo - 0.12, -0.12, "O", ha="right", va="top", fontsize=9)

    theta = np.linspace(0, 2 * np.pi, 2000)
    y_sin = np.sin(theta)

    # 解区間1: [7π/6, 11π/6] → sinθ ≤ -1/2
    y_lower = -0.5
    ax.fill_between(theta, y_sin, y_lower,
                    where=(y_sin <= y_lower),
                    alpha=0.3, color="lightcoral", zorder=1)

    ax.plot(theta, y_sin, color=DARK_BLUE, lw=2.0, zorder=3)

    # y = -1/2 ライン
    ax.axhline(-0.5, color=RED, lw=1.3, linestyle="--", zorder=2)
    ax.text(x_hi + 0.15, -0.5 - 0.1, r"$t = -\frac{1}{2}$",
            ha="left", va="top", fontsize=8.5, color=RED)

    # y = 1 の点
    ax.axhline(1.0, color=GREEN, lw=1.0, linestyle=":", zorder=2, alpha=0.7)
    ax.text(x_hi + 0.15, 1.0 + 0.07, r"$t = 1$",
            ha="left", va="bottom", fontsize=8.5, color=GREEN)

    # 解の端点
    sol_a, sol_b = 7 * np.pi / 6, 11 * np.pi / 6
    for xv in [sol_a, sol_b]:
        ax.plot(xv, -0.5, "o", color=RED, markersize=7, zorder=5)

    # θ = π/2 (t=1)
    ax.plot(np.pi / 2, 1.0, "o", color=GREEN, markersize=8, zorder=5)

    # x 目盛り
    x_ticks = [
        (np.pi / 2,       r"$\frac{\pi}{2}$"),
        (np.pi,           r"$\pi$"),
        (7 * np.pi / 6,   r"$\frac{7\pi}{6}$"),
        (3 * np.pi / 2,   r"$\frac{3\pi}{2}$"),
        (11 * np.pi / 6,  r"$\frac{11\pi}{6}$"),
        (2 * np.pi,       r"$2\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.20, lbl, ha="center", va="top", fontsize=7.5)

    ax.text((x_lo + x_hi) / 2, -2.05,
            r"$\theta = \frac{\pi}{2}$ または $\frac{7\pi}{6} \leq \theta \leq \frac{11\pi}{6}$",
            ha="center", va="top", fontsize=9, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    fig.patch.set_facecolor("white")

    draw_panel1(axes[0])
    draw_panel2(axes[1])

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "trig-ineq-quadratic.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
