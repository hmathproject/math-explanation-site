"""
gen_figures_trig_eq_synthesis.py — 合成を使う三角方程式 概念図生成

sinθ + √3 cosθ = 1 → 2sin(θ+π/3) = 1 の解をグラフで示す。
y = 2sin(θ+π/3) と y = 1 の交点 (θ=π/2, θ=11π/6) を可視化。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_eq_synthesis.py
出力: site/figures/trig-eq-synthesis.png
      site/assets/images/trig-eq-synthesis.png
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


def main() -> None:
    fig, ax = plt.subplots(1, 1, figsize=(7.0, 4.2))
    fig.patch.set_facecolor("white")

    ax.axis("off")
    ax.set_xlim(-0.4, 2 * np.pi + 0.6)
    ax.set_ylim(-2.7, 2.7)

    # 軸
    ax.annotate("", xy=(2 * np.pi + 0.5, 0), xytext=(-0.35, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2 * np.pi + 0.52, 0, r"$\theta$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 2.55), xytext=(0, -2.55),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, 2.57, r"$y$", ha="left", va="bottom", fontsize=10)

    # y 目盛り
    for yv, lbl in [(2, "2"), (1, "1"), (-1, "-1"), (-2, "-2")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", lw=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)
    ax.text(-0.1, -0.12, "O", ha="right", va="top", fontsize=9)

    # x 目盛り
    x_ticks = [
        (np.pi / 2,       r"$\frac{\pi}{2}$"),
        (np.pi,           r"$\pi$"),
        (3 * np.pi / 2,   r"$\frac{3\pi}{2}$"),
        (11 * np.pi / 6,  r"$\frac{11\pi}{6}$"),
        (2 * np.pi,       r"$2\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.22, lbl, ha="center", va="top", fontsize=8)

    theta = np.linspace(0, 2 * np.pi, 1000)

    # y = 2 sin(θ + π/3)
    y_curve = 2 * np.sin(theta + np.pi / 3)
    ax.plot(theta, y_curve, color=DARK_BLUE, lw=2.2, zorder=4,
            label=r"$y=2\sin(\theta+\frac{\pi}{3})$")

    # y = 1 ライン
    ax.axhline(1.0, color=RED, lw=1.4, linestyle="--", zorder=2)
    ax.text(2 * np.pi + 0.1, 1.0 + 0.08, r"$y=1$",
            ha="left", va="bottom", fontsize=9, color=RED)

    # 解の点: θ = π/2, θ = 11π/6
    sols = [np.pi / 2, 11 * np.pi / 6]
    sol_labels = [r"$\theta=\frac{\pi}{2}$", r"$\theta=\frac{11\pi}{6}$"]
    for xv, lbl in zip(sols, sol_labels):
        ax.plot(xv, 1.0, "o", color=RED, markersize=8, zorder=5)
        ax.plot([xv, xv], [0, 1.0], ":", color=RED, lw=1.0)
        ax.text(xv, 1.18, lbl, ha="center", va="bottom", fontsize=8.5, color=RED)

    # 曲線ラベル
    ax.text(np.pi / 6, 2.3,
            r"$y = 2\sin\!\left(\theta+\dfrac{\pi}{3}\right)$",
            ha="left", va="bottom", fontsize=9.5, color=DARK_BLUE)

    ax.text(np.pi, -2.55,
            r"$y = 2\sin(\theta+\frac{\pi}{3})$ と $y=1$ の交点から解が読める",
            ha="center", va="top", fontsize=9, fontweight="bold")

    fig.tight_layout(pad=0.4)

    fname = "trig-eq-synthesis.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
