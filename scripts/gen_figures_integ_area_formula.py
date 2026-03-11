"""
gen_figures_integ_area_formula.py — 1/6 公式と α-β 公式

Panel 1: 1/6 公式の可視化 — f(x)=(x-1)(x-3) の根 α=1, β=3
Panel 2: α-β 公式の応用 — y=x² と y=x+2 の面積

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_area_formula.py
出力: site/figures/integ-area-formula-combined.png
      site/assets/images/integ-area-formula-combined.png
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
    ax.text(0.06, ylim[1] - 0.1, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.12, -0.1, "O", ha="right", va="top", fontsize=9)


def draw_one_sixth_formula(ax):
    """Panel 1: 1/6 公式  ∫_α^β (x-α)(x-β)dx = -(β-α)³/6"""
    _draw_axes(ax, xlim=(-0.3, 4.2), ylim=(-1.4, 2.8))

    alpha, beta = 1.0, 3.0

    def f(x):
        return (x - alpha) * (x - beta)

    x_full = np.linspace(-0.1, 4.0, 500)

    # 根の間 [1, 3] は f < 0 → 赤塗り
    x_fill = np.linspace(alpha, beta, 400)
    ax.fill_between(x_fill, f(x_fill), 0,
                    color="#ffaaaa", alpha=0.70, zorder=2)

    ax.plot(x_full, f(x_full), color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 根点
    for xv in [alpha, beta]:
        ax.plot(xv, 0, "o", color=DARK_BLUE, markersize=6, zorder=5)
        ax.text(xv, 0.08, rf"$\alpha={int(xv)}$" if xv == alpha else rf"$\beta={int(xv)}$",
                ha="center", va="bottom", fontsize=9)
        ax.text(xv, -0.12, f"${int(xv)}$", ha="center", va="top", fontsize=8.5)

    # 頂点 (頂点 x = (α+β)/2 = 2)
    xv_top = (alpha + beta) / 2
    ax.plot(xv_top, f(xv_top), "o", color=RED, markersize=5, zorder=5)
    ax.plot([xv_top, xv_top], [0, f(xv_top)], ":", color=RED, linewidth=0.9, alpha=0.7)

    # 面積の値ラベル
    ax.text(2.0, -0.55,
            r"$\int_1^3 (x-1)(x-3)\,dx$" + "\n"
            r"$= -\dfrac{(3-1)^3}{6}$" + "\n"
            r"$= -\dfrac{8}{6} = -\dfrac{4}{3}$",
            ha="center", va="center", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, alpha=0.9))

    # 公式ボックス（上部）
    ax.text(2.0, 2.5,
            r"$\mathbf{1/6}$ 公式:" + "\n"
            r"$\int_\alpha^\beta (x-\alpha)(x-\beta)\,dx = -\dfrac{(\beta-\alpha)^3}{6}$",
            ha="center", va="top", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ddeeff",
                      edgecolor=DARK_BLUE, linewidth=1.5))

    # 面積（絶対値）
    ax.text(3.8, -0.9,
            r"面積 $= \dfrac{4}{3}$",
            ha="right", va="center", fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f0fff0",
                      edgecolor=GREEN, alpha=0.85))

    ax.set_title(r"$1/6$ 公式: $\int_\alpha^\beta (x-\alpha)(x-\beta)\,dx = -\dfrac{(\beta-\alpha)^3}{6}$",
                 fontsize=9.5, pad=4)


def draw_alpha_beta_application(ax):
    """Panel 2: y=x² と y=x+2 の面積 → α-β 公式で 9/2"""
    _draw_axes(ax, xlim=(-2.0, 3.0), ylim=(-0.8, 5.5))

    f = lambda t: t + 2    # 直線（上）
    g = lambda t: t ** 2   # 放物線（下）
    diff = lambda t: f(t) - g(t)   # = -t²+t+2 = -(t-2)(t+1)

    x = np.linspace(-1.8, 2.6, 500)

    # 塗りつぶし [-1, 2]
    x_fill = np.linspace(-1, 2, 400)
    ax.fill_between(x_fill, f(x_fill), g(x_fill),
                    color="#aaccff", alpha=0.70, zorder=2)

    ax.plot(x, f(x), color=RED, linewidth=2.0, zorder=3, label=r"$y=x+2$")
    ax.plot(x, g(x), color=DARK_BLUE, linewidth=2.0, zorder=3, label=r"$y=x^2$")

    # 交点
    for xv in [-1, 2]:
        yv = f(xv)
        ax.plot(xv, yv, "o", color=ORANGE, markersize=6, zorder=6)
        ax.plot([xv, xv], [0, yv], ":", color=GRAY, linewidth=0.9, alpha=0.7)
        ax.text(xv, -0.15, f"${xv}$", ha="center", va="top", fontsize=9)

    # α-β 公式の説明
    ax.text(0.5, 4.8,
            r"$f(x)-g(x) = x+2-x^2$" + "\n"
            r"$= -(x^2-x-2)$" + "\n"
            r"$= -(x-2)(x+1)$",
            ha="center", va="top", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    # 公式適用ボックス
    ax.text(0.5, 2.3,
            r"$\alpha=-1,\;\beta=2$" + "\n"
            r"面積 $= \dfrac{(\beta-\alpha)^3}{6}$" + "\n"
            r"$= \dfrac{(2-(-1))^3}{6} = \dfrac{27}{6} = \dfrac{9}{2}$",
            ha="center", va="center", fontsize=9.5, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f0fff0",
                      edgecolor=GREEN, linewidth=1.5))

    ax.legend(loc="upper left", fontsize=8)
    ax.set_title(r"$\alpha\text{-}\beta$ 公式: $y=x^2$ と $y=x+2$ の面積 $= \dfrac{9}{2}$",
                 fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_one_sixth_formula(axes[0])
    draw_alpha_beta_application(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-area-formula-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
