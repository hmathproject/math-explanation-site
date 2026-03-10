"""
gen_figures_trig_ineq_double.py — 合成を使う三角不等式 概念図生成

sinθ − cosθ ≥ 1 → √2 sin(θ − π/4) ≥ 1 → sin(θ − π/4) ≥ √2/2

Panel 1: y = sin(u) と y = √2/2 の不等式の解 (u の視点)
Panel 2: θ への変換後の解区間 π/2 ≤ θ ≤ π をグラフで示す

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_ineq_double.py
出力: site/figures/trig-ineq-double.png
      site/assets/images/trig-ineq-double.png
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

arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def setup_ax(ax, x_lo, x_hi, y_lo=-1.6, y_hi=1.6):
    px, py = 0.5, 0.45
    ax.axis("off")
    ax.set_xlim(x_lo - px, x_hi + px)
    ax.set_ylim(y_lo - py, y_hi + py)

    ax.annotate("", xy=(x_hi + px - 0.05, 0), xytext=(x_lo - px + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))

    ax.annotate("", xy=(x_lo, y_hi + py - 0.05), xytext=(x_lo, y_lo - py + 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_lo + 0.05, y_hi + py - 0.02, r"$y$", ha="left", va="bottom", fontsize=10)

    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([x_lo - 0.06, x_lo + 0.06], [yv, yv], "k-", lw=0.8)
        ax.text(x_lo - 0.12, yv, lbl, ha="right", va="center", fontsize=8)
    ax.text(x_lo - 0.12, -0.12, "O", ha="right", va="top", fontsize=9)


def draw_panel1(ax):
    """u = θ − π/4 を変数として sin(u) ≥ √2/2 の解区間を示す。"""
    x_lo, x_hi = -np.pi / 4, 7 * np.pi / 4
    setup_ax(ax, x_lo, x_hi)

    ax.text(x_hi + 0.2, 0, r"$u$", ha="left", va="center", fontsize=10)

    u = np.linspace(x_lo, x_hi, 1000)
    y_sin = np.sin(u)

    y_val = np.sqrt(2) / 2  # ≈ 0.707

    # 塗りつぶし: sin u ≥ √2/2
    ax.fill_between(u, y_sin, y_val,
                    where=(y_sin >= y_val),
                    alpha=0.3, color="lightblue", zorder=1)

    ax.plot(u, y_sin, color=DARK_BLUE, lw=2.0, zorder=3)

    ax.axhline(y_val, color=RED, lw=1.3, linestyle="--", zorder=2)
    ax.text(x_hi + 0.15, y_val + 0.07, r"$\frac{\sqrt{2}}{2}$",
            ha="left", va="bottom", fontsize=9, color=RED)

    # 解の端点 u = π/4, 3π/4
    sol_lo, sol_hi = np.pi / 4, 3 * np.pi / 4
    for xv in [sol_lo, sol_hi]:
        ax.plot(xv, y_val, "o", color=DARK_BLUE, markersize=6, zorder=5)

    # x 目盛り
    x_ticks = [
        (-np.pi / 4,  r"$-\frac{\pi}{4}$"),
        (np.pi / 4,   r"$\frac{\pi}{4}$"),
        (3 * np.pi / 4, r"$\frac{3\pi}{4}$"),
        (np.pi,       r"$\pi$"),
        (7 * np.pi / 4, r"$\frac{7\pi}{4}$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.22, lbl, ha="center", va="top", fontsize=8)

    ax.text((sol_lo + sol_hi) / 2, 1.5,
            r"$\frac{\pi}{4} \leq u \leq \frac{3\pi}{4}$",
            ha="center", va="top", fontsize=9, color=GREEN)

    ax.text((x_lo + x_hi) / 2, -2.0,
            r"$u = \theta - \frac{\pi}{4}$ の視点：$\frac{\pi}{4} \leq u \leq \frac{3\pi}{4}$",
            ha="center", va="top", fontsize=8.5, fontweight="bold")


def draw_panel2(ax):
    """θ の視点で y = √2 sin(θ − π/4) ≥ 1 の解区間 π/2 ≤ θ ≤ π を示す。"""
    x_lo, x_hi = 0, 2 * np.pi
    setup_ax(ax, x_lo, x_hi)

    ax.text(x_hi + 0.3, 0, r"$\theta$", ha="left", va="center", fontsize=10)

    theta = np.linspace(x_lo, x_hi, 1000)
    y_curve = np.sqrt(2) * np.sin(theta - np.pi / 4)

    y_val = 1.0  # √2 × (√2/2) = 1

    ax.fill_between(theta, y_curve, y_val,
                    where=(y_curve >= y_val),
                    alpha=0.3, color="lightblue", zorder=1)

    ax.plot(theta, y_curve, color=DARK_BLUE, lw=2.0, zorder=3)

    ax.axhline(y_val, color=RED, lw=1.3, linestyle="--", zorder=2)
    ax.text(x_hi + 0.15, y_val + 0.07, r"$y=1$",
            ha="left", va="bottom", fontsize=9, color=RED)

    sol_lo, sol_hi = np.pi / 2, np.pi
    for xv in [sol_lo, sol_hi]:
        ax.plot(xv, y_val, "o", color=DARK_BLUE, markersize=6, zorder=5)

    x_ticks = [
        (np.pi / 2,      r"$\frac{\pi}{2}$"),
        (np.pi,          r"$\pi$"),
        (3 * np.pi / 2,  r"$\frac{3\pi}{2}$"),
        (2 * np.pi,      r"$2\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.22, lbl, ha="center", va="top", fontsize=8)

    ax.text((sol_lo + sol_hi) / 2, 1.5,
            r"$\frac{\pi}{2} \leq \theta \leq \pi$",
            ha="center", va="top", fontsize=9, color=GREEN)

    ax.text((x_lo + x_hi) / 2, -2.0,
            r"θ に戻すと：$\frac{\pi}{2} \leq \theta \leq \pi$",
            ha="center", va="top", fontsize=8.5, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    fig.patch.set_facecolor("white")

    draw_panel1(axes[0])
    draw_panel2(axes[1])

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "trig-ineq-double.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
