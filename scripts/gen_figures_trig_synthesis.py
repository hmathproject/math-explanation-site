"""
gen_figures_trig_synthesis.py — 三角関数の合成 概念図生成

Panel 1: R, φ を決める直角三角形（a=√3, b=1, R=2, φ=π/6）
Panel 2: y=√3sinθ+cosθ（合成前）と y=2sin(θ+π/6)（合成後）のグラフ比較

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_synthesis.py
出力: site/figures/trig-synthesis-combined.png
      site/assets/images/trig-synthesis-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.patches as mpatches
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
    """R と φ を決める直角三角形（ベクトル図）。"""
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.3, 2.6)
    ax.set_ylim(-0.5, 1.6)

    # a=√3 (水平), b=1 (垂直), R=2 (斜辺)
    a = np.sqrt(3)
    b = 1.0
    R = 2.0
    phi = np.pi / 6  # arctan(b/a)

    # 軸
    ax.annotate("", xy=(2.5, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.52, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 1.5), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.03, 1.52, r"$y$", ha="left", va="bottom", fontsize=10)

    # 三角形
    triangle_x = [0, a, a, 0]
    triangle_y = [0, 0, b, 0]
    ax.fill(triangle_x, triangle_y, color="lightyellow", alpha=0.7, zorder=1)
    ax.plot(triangle_x, triangle_y, color="#888888", lw=1.2, zorder=2)

    # ベクトル R
    ax.annotate("", xy=(a, b), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0,
                                mutation_scale=10, shrinkA=0, shrinkB=0))

    # 辺ラベル
    ax.text(a / 2, -0.12, r"$a = \sqrt{3}$",
            ha="center", va="top", fontsize=10, color=GREEN)
    ax.text(a + 0.08, b / 2, r"$b = 1$",
            ha="left", va="center", fontsize=10, color=ORANGE)
    ax.text(a / 2 - 0.15, b / 2 + 0.1, r"$R = \sqrt{a^2+b^2} = 2$",
            ha="center", va="bottom", fontsize=9.5, color=RED,
            rotation=np.degrees(phi))

    # 角度弧
    arc = mpatches.Arc((0, 0), 0.5, 0.5, angle=0,
                        theta1=0, theta2=np.degrees(phi),
                        color=DARK_BLUE, lw=1.2)
    ax.add_patch(arc)
    ax.text(0.32, 0.06, r"$\varphi = \frac{\pi}{6}$",
            ha="left", va="bottom", fontsize=9.5, color=DARK_BLUE)

    # タイトル
    ax.text(1.15, 1.55,
            r"$\cos\varphi = \frac{a}{R}$, $\sin\varphi = \frac{b}{R}$ から $\varphi$ を決定",
            ha="center", va="top", fontsize=8.5, color="#444444")

    ax.text(1.15, -0.48, r"$R = \sqrt{(\sqrt{3})^2 + 1^2} = 2$",
            ha="center", va="top", fontsize=9, fontweight="bold")


def draw_panel2(ax):
    """合成前後のグラフ比較。"""
    ax.axis("off")
    ax.set_xlim(-0.5, 2 * np.pi + 0.6)
    ax.set_ylim(-2.8, 2.8)

    # 軸
    ax.annotate("", xy=(2 * np.pi + 0.5, 0), xytext=(-0.45, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2 * np.pi + 0.52, 0, r"$\theta$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 2.6), xytext=(0, -2.65),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, 2.62, r"$y$", ha="left", va="bottom", fontsize=10)

    # y 目盛り
    for yv, lbl in [(2, "2"), (1, "1"), (-1, "-1"), (-2, "-2")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", lw=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)

    # x 目盛り
    x_ticks = [
        (np.pi / 3,      r"$\frac{\pi}{3}$"),
        (np.pi / 2,      r"$\frac{\pi}{2}$"),
        (np.pi,          r"$\pi$"),
        (4 * np.pi / 3,  r"$\frac{4\pi}{3}$"),
        (2 * np.pi,      r"$2\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", lw=0.8)
        ax.text(xv, -0.22, lbl, ha="center", va="top", fontsize=8)
    ax.text(-0.1, -0.12, "O", ha="right", va="top", fontsize=9)

    theta = np.linspace(0, 2 * np.pi, 1000)

    # 合成後: y = 2 sin(θ + π/6)
    y_synth = 2 * np.sin(theta + np.pi / 6)
    ax.plot(theta, y_synth, color=RED, lw=2.2, zorder=4,
            label=r"$2\sin\!\left(\theta+\frac{\pi}{6}\right)$")

    # 最大点マーク
    theta_max = np.pi / 3  # θ + π/6 = π/2 → θ = π/3
    ax.plot(theta_max, 2, "o", color=RED, markersize=7, zorder=5)
    ax.text(theta_max + 0.1, 2.1, r"最大 $2$ ($\theta=\frac{\pi}{3}$)",
            ha="left", va="bottom", fontsize=8, color=RED)

    theta_min = 4 * np.pi / 3
    ax.plot(theta_min, -2, "o", color=RED, markersize=7, zorder=5)
    ax.text(theta_min + 0.1, -2.1, r"最小 $-2$ ($\theta=\frac{4\pi}{3}$)",
            ha="left", va="top", fontsize=8, color=RED)

    # 式ラベル
    ax.text(2 * np.pi + 0.1, 1.8,
            r"$2\sin\!\left(\theta+\frac{\pi}{6}\right)$",
            ha="left", va="center", fontsize=9, color=RED)

    ax.text((0 + 2 * np.pi) / 2, -2.7,
            r"振幅 $R=2$、最大値 $=2$、最小値 $=-2$",
            ha="center", va="top", fontsize=9, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    fig.patch.set_facecolor("white")

    draw_panel1(axes[0])
    draw_panel2(axes[1])

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "trig-synthesis-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
