"""
gen_figures_trig_period.py — 周期と一般角 概念図生成

Panel 1: sin θ = 1/2 の解が [0, 2π) に2つ (π/6, 5π/6) あることを示す
Panel 2: 同じ式の解が [0, 4π) に4つ (π/6, 5π/6, π/6+2π, 5π/6+2π) あること＝周期

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_period.py
出力: site/figures/trig-period-combined.png
      site/assets/images/trig-period-combined.png
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
    ax.axis("off")
    px, py = 0.4, 0.45
    ax.set_xlim(x_lo - px, x_hi + px)
    ax.set_ylim(y_lo - py, y_hi + py)

    ax.annotate("", xy=(x_hi + px - 0.05, 0), xytext=(x_lo - px + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_hi + px - 0.02, 0, r"$\theta$", ha="left", va="center", fontsize=10)

    ax.annotate("", xy=(x_lo, y_hi + py - 0.05), xytext=(x_lo, y_lo - py + 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_lo + 0.05, y_hi + py - 0.02, r"$y$", ha="left", va="bottom", fontsize=10)

    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([x_lo - 0.06, x_lo + 0.06], [yv, yv], "k-", linewidth=0.8)
        ax.text(x_lo - 0.12, yv, lbl, ha="right", va="center", fontsize=8)

    ax.text(x_lo - 0.12, -0.12, "O", ha="right", va="top", fontsize=9)


def draw_panel1(ax):
    """[0, 2π) で sin θ = 1/2 の解2つ (π/6, 5π/6)。"""
    x_lo, x_hi = 0, 2 * np.pi
    setup_ax(ax, x_lo, x_hi)

    theta = np.linspace(x_lo, x_hi, 1000)
    ax.plot(theta, np.sin(theta), color=DARK_BLUE, lw=2.0, zorder=3)

    # y = 1/2 ライン
    y_val = 0.5
    ax.axhline(y_val, color=RED, lw=1.2, linestyle="--", zorder=2)
    ax.text(x_hi + 0.1, y_val + 0.05, r"$y=\frac{1}{2}$",
            ha="left", va="bottom", fontsize=9, color=RED)

    # x 目盛り
    x_ticks = [
        (np.pi / 6,      r"$\frac{\pi}{6}$"),
        (np.pi / 2,      r"$\frac{\pi}{2}$"),
        (5 * np.pi / 6,  r"$\frac{5\pi}{6}$"),
        (np.pi,          r"$\pi$"),
        (3 * np.pi / 2,  r"$\frac{3\pi}{2}$"),
        (2 * np.pi,      r"$2\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.20, lbl, ha="center", va="top", fontsize=8)

    # 解の点
    for xv in [np.pi / 6, 5 * np.pi / 6]:
        ax.plot(xv, y_val, "o", color=RED, markersize=7, zorder=5)
        ax.plot([xv, xv], [0, y_val], ":", color=RED, lw=1.0)

    # 対称軸 θ=π/2
    ax.axvline(np.pi / 2, color=GREEN, lw=1.0, linestyle=":", alpha=0.7)
    ax.text(np.pi / 2 + 0.06, 1.4, r"軸 $\theta=\frac{\pi}{2}$",
            ha="left", va="top", fontsize=8, color=GREEN)

    ax.text((x_lo + x_hi) / 2, -2.0,
            r"$[0, 2\pi)$ の解：$\theta = \frac{\pi}{6}$ と $\theta = \frac{5\pi}{6}$",
            ha="center", va="top", fontsize=9, fontweight="bold")


def draw_panel2(ax):
    """[0, 4π) で4つの解が現れること（周期の可視化）。"""
    x_lo, x_hi = 0, 4 * np.pi
    setup_ax(ax, x_lo, x_hi)

    theta = np.linspace(x_lo, x_hi, 2000)
    ax.plot(theta, np.sin(theta), color=DARK_BLUE, lw=2.0, zorder=3)

    y_val = 0.5
    ax.axhline(y_val, color=RED, lw=1.2, linestyle="--", zorder=2)
    ax.text(x_hi + 0.1, y_val + 0.05, r"$y=\frac{1}{2}$",
            ha="left", va="bottom", fontsize=9, color=RED)

    # x 目盛り
    x_ticks = [
        (np.pi,          r"$\pi$"),
        (2 * np.pi,      r"$2\pi$"),
        (3 * np.pi,      r"$3\pi$"),
        (4 * np.pi,      r"$4\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.20, lbl, ha="center", va="top", fontsize=8)

    # 4つの解
    sols = [np.pi / 6, 5 * np.pi / 6,
            np.pi / 6 + 2 * np.pi, 5 * np.pi / 6 + 2 * np.pi]
    sol_labels = [
        r"$\frac{\pi}{6}$",
        r"$\frac{5\pi}{6}$",
        r"$\frac{\pi}{6}+2\pi$",
        r"$\frac{5\pi}{6}+2\pi$",
    ]
    colors_sol = [RED, GREEN, RED, GREEN]
    for xv, lbl, col in zip(sols, sol_labels, colors_sol):
        ax.plot(xv, y_val, "o", color=col, markersize=7, zorder=5)
        ax.plot([xv, xv], [-0.06, 0.06], "-", color=col, lw=0.8)
        ax.text(xv, -0.22, lbl, ha="center", va="top", fontsize=7.5, color=col)

    # 周期 2π の矢印
    y_arr = 1.45
    ax.annotate("", xy=(sols[2], y_arr), xytext=(sols[0], y_arr),
                arrowprops=dict(arrowstyle="<->", color="#555555", lw=1.2))
    ax.text((sols[0] + sols[2]) / 2, y_arr + 0.12,
            r"周期 $2\pi$", ha="center", va="bottom", fontsize=9, color="#555555")

    ax.text((x_lo + x_hi) / 2, -2.0,
            r"$+2n\pi$ で解が無限に続く（一般角）",
            ha="center", va="top", fontsize=9, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    fig.patch.set_facecolor("white")

    draw_panel1(axes[0])
    draw_panel2(axes[1])

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "trig-period-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
