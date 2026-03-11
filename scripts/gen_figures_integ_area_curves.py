"""
gen_figures_integ_area_curves.py — 2曲線間の面積

Panel 1: f(x)≥g(x) の場合 — y=x+2 と y=x² の間の面積
Panel 2: 上下関係が区間で入れ替わる場合 — y=x³ と y=x

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_area_curves.py
出力: site/figures/integ-area-curves-combined.png
      site/assets/images/integ-area-curves-combined.png
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
    ax.text(-0.1, -0.15, "O", ha="right", va="top", fontsize=9)


def draw_curves_ordered(ax):
    """Panel 1: y=x+2 (上) と y=x² (下), 交点 x=-1, 2"""
    _draw_axes(ax, xlim=(-2.0, 3.0), ylim=(-0.8, 5.5))

    x = np.linspace(-1.8, 2.6, 500)
    f = lambda t: t + 2     # 直線（上）
    g = lambda t: t ** 2    # 放物線（下）

    # 塗りつぶし [-1, 2]
    x_fill = np.linspace(-1, 2, 400)
    ax.fill_between(x_fill, f(x_fill), g(x_fill),
                    color="#aaccff", alpha=0.70, zorder=2)

    ax.plot(x, f(x), color=RED, linewidth=2.0, zorder=3, label=r"$y=x+2$（直線）")
    ax.plot(x, g(x), color=DARK_BLUE, linewidth=2.0, zorder=3, label=r"$y=x^2$（放物線）")

    # 交点
    for xv in [-1, 2]:
        yv = f(xv)
        ax.plot(xv, yv, "o", color=ORANGE, markersize=6, zorder=6)
        ax.plot([xv, xv], [0, yv], ":", color=GRAY, linewidth=0.9, alpha=0.7)
        ax.text(xv, -0.15, f"${xv}$", ha="center", va="top", fontsize=9)

    # 面積ラベル
    ax.text(0.5, 2.0,
            r"$\int_{-1}^{2}(f-g)\,dx$" + "\n"
            r"$= \int_{-1}^{2}(x+2-x^2)\,dx$" + "\n"
            r"$= \dfrac{9}{2}$",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    # 矢印「f≥g」
    ax.annotate("", xy=(1.0, f(1.0)), xytext=(1.0, g(1.0) + 0.05),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.4,
                                mutation_scale=9, shrinkA=2, shrinkB=2))
    ax.text(1.15, (f(1.0) + g(1.0)) / 2, r"$f \geq g$",
            ha="left", va="center", fontsize=8.5, color=GREEN)

    ax.legend(loc="upper left", fontsize=8)
    ax.set_title(r"$\int_{-1}^{2}(x+2-x^2)\,dx$（$f\geq g$ の場合）",
                 fontsize=9.5, pad=4)


def draw_curves_crossing(ax):
    """Panel 2: y=x³ と y=x — 上下が x=0 で入れ替わる"""
    _draw_axes(ax, xlim=(-1.5, 1.8), ylim=(-1.4, 1.4))

    x = np.linspace(-1.2, 1.2, 500)
    f = lambda t: t ** 3
    g = lambda t: t

    # 区間 (-1, 0): f > g (x³ > x for -1<x<0)  → f-g > 0 → 青
    x_a = np.linspace(-1, 0, 300)
    ax.fill_between(x_a, f(x_a), g(x_a),
                    color="#aaccff", alpha=0.70, zorder=2,
                    label=r"$x^3>x$（$-1<x<0$）")

    # 区間 (0, 1): f < g (x³ < x for 0<x<1) → f-g < 0 → 赤
    x_b = np.linspace(0, 1, 300)
    ax.fill_between(x_b, f(x_b), g(x_b),
                    color="#ffaaaa", alpha=0.70, zorder=2,
                    label=r"$x^3<x$（$0<x<1$）")

    ax.plot(x, f(x), color=DARK_BLUE, linewidth=2.0, zorder=3, label=r"$y=x^3$")
    ax.plot(x, g(x), color=RED, linewidth=2.0, zorder=3, label=r"$y=x$")

    # 交点
    for xv in [-1, 0, 1]:
        ax.plot(xv, g(xv), "o", color=ORANGE, markersize=6, zorder=6)
        ax.plot([xv, xv], [min(0, g(xv)) - 0.05, max(0, g(xv)) + 0.05],
                ":", color=GRAY, linewidth=0.9, alpha=0.6)
        ax.text(xv, -0.12 if xv != 0 else -0.14,
                f"${xv}$", ha="center", va="top", fontsize=8.5)

    # 計算ボックス
    ax.text(0.9, 1.2,
            "面積 $=$\n"
            r"$\int_{-1}^{0}|x^3-x|\,dx$" + "\n"
            r"$+\int_{0}^{1}|x^3-x|\,dx$" + "\n"
            r"$= \dfrac{1}{4}+\dfrac{1}{4}=\dfrac{1}{2}$",
            ha="center", va="top", fontsize=8.0, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    # 注記
    ax.text(-1.4, 1.25,
            "交点 $x=0$ で\n上下が入れ替わる\n→ 区間を分割！",
            ha="left", va="top", fontsize=8, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0",
                      edgecolor=RED, alpha=0.9))

    ax.legend(loc="lower right", fontsize=7.5, ncol=2)
    ax.set_title(r"交点で上下が入れ替わる: 区間を分割して積分",
                 fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_curves_ordered(axes[0])
    draw_curves_crossing(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-area-curves-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
