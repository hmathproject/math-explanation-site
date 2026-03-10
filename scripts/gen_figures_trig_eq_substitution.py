"""
gen_figures_trig_eq_substitution.py — 置換を使う三角方程式 概念図生成

2cos²θ − cosθ − 1 = 0 の解を cos グラフで示す。
t = 1 → θ = 0, t = -1/2 → θ = 2π/3, 4π/3 の3点を可視化。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_eq_substitution.py
出力: site/figures/trig-eq-substitution.png
      site/assets/images/trig-eq-substitution.png
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


def main() -> None:
    fig, ax = plt.subplots(1, 1, figsize=(7.5, 4.2))
    fig.patch.set_facecolor("white")

    ax.axis("off")
    ax.set_xlim(-0.4, 2 * np.pi + 0.8)
    ax.set_ylim(-1.75, 1.75)

    # 軸
    ax.annotate("", xy=(2 * np.pi + 0.7, 0), xytext=(-0.35, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2 * np.pi + 0.72, 0, r"$\theta$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 1.65), xytext=(0, -1.65),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, 1.67, r"$y$", ha="left", va="bottom", fontsize=10)

    # y 目盛り
    for yv, lbl in [(1, "1"), (0.5, ""), (-0.5, r"$-\frac{1}{2}$"), (-1, "-1")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", lw=0.8)
        if lbl:
            ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)
    ax.text(-0.1, -0.12, "O", ha="right", va="top", fontsize=9)

    # x 目盛り
    x_ticks = [
        (0,               r"$0$"),
        (2 * np.pi / 3,   r"$\frac{2\pi}{3}$"),
        (np.pi,           r"$\pi$"),
        (4 * np.pi / 3,   r"$\frac{4\pi}{3}$"),
        (3 * np.pi / 2,   r"$\frac{3\pi}{2}$"),
        (2 * np.pi,       r"$2\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.20, lbl, ha="center", va="top", fontsize=8)

    theta = np.linspace(0, 2 * np.pi, 1000)

    # y = cos θ
    ax.plot(theta, np.cos(theta), color=DARK_BLUE, lw=2.2, zorder=4)

    # y = 1 の水平線（点線）
    ax.axhline(1.0, color=RED, lw=1.2, linestyle=":", zorder=2, alpha=0.7)
    ax.text(2 * np.pi + 0.15, 1.0 + 0.07, r"$t=1$",
            ha="left", va="bottom", fontsize=8.5, color=RED)

    # y = -1/2 の水平線
    ax.axhline(-0.5, color=GREEN, lw=1.4, linestyle="--", zorder=2)
    ax.text(2 * np.pi + 0.15, -0.5 - 0.08, r"$t=-\frac{1}{2}$",
            ha="left", va="top", fontsize=8.5, color=GREEN)

    # 解の点
    sols_t1 = [(0, 1.0)]
    sols_thalf = [(2 * np.pi / 3, -0.5), (4 * np.pi / 3, -0.5)]

    for xv, yv in sols_t1:
        ax.plot(xv, yv, "o", color=RED, markersize=9, zorder=5)
        ax.text(xv + 0.1, yv + 0.12, r"$\theta=0$",
                ha="left", va="bottom", fontsize=9, color=RED)

    for xv, yv in sols_thalf:
        ax.plot(xv, yv, "o", color=GREEN, markersize=8, zorder=5)
        ax.plot([xv, xv], [0, yv], ":", color=GREEN, lw=1.0)

    ax.text(2 * np.pi / 3 + 0.05, -0.5 - 0.15,
            r"$\theta=\frac{2\pi}{3}$",
            ha="center", va="top", fontsize=8.5, color=GREEN)
    ax.text(4 * np.pi / 3, -0.5 - 0.15,
            r"$\theta=\frac{4\pi}{3}$",
            ha="center", va="top", fontsize=8.5, color=GREEN)

    # 曲線ラベル
    ax.text(3 * np.pi / 2, -1.4, r"$y = \cos\theta$",
            ha="center", va="top", fontsize=10, color=DARK_BLUE)

    ax.text(np.pi, 1.65,
            r"$t=\cos\theta$ の解を cos グラフで読む：$\theta=0,\,\frac{2\pi}{3},\,\frac{4\pi}{3}$",
            ha="center", va="top", fontsize=8.5, fontweight="bold")

    fig.tight_layout(pad=0.4)

    fname = "trig-eq-substitution.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
