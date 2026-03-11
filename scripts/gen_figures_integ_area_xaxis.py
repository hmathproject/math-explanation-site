"""
gen_figures_integ_area_xaxis.py — x 軸と曲線で囲まれた面積

Panel 1: f(x)≥0 の場合: 面積 = 定積分
Panel 2: f(x) が x 軸と交差する場合: 区間分割が必須

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_area_xaxis.py
出力: site/figures/integ-area-xaxis-combined.png
      site/assets/images/integ-area-xaxis-combined.png
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
    ax.text(-0.1, -0.1, "O", ha="right", va="top", fontsize=9)


def draw_positive_case(ax):
    """Panel 1: f(x) = x(2-x) = -x²+2x on [0,2]  (f≥0)"""
    _draw_axes(ax, xlim=(-0.4, 2.8), ylim=(-0.5, 1.8))

    def f(x):
        return -x ** 2 + 2 * x

    x_full = np.linspace(-0.2, 2.5, 400)

    x_fill = np.linspace(0, 2, 300)
    ax.fill_between(x_fill, f(x_fill), 0,
                    color="#aaccff", alpha=0.72, zorder=2)

    ax.plot(x_full, f(x_full), color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 境界
    for xv in [0, 2]:
        ax.plot(xv, 0, "o", color=DARK_BLUE, markersize=5, zorder=5)
        ax.text(xv, -0.1, f"${xv}$", ha="center", va="top", fontsize=9)

    # 頂点
    ax.plot(1.0, f(1.0), "o", color=RED, markersize=5, zorder=5)
    ax.text(1.0, f(1.0) + 0.07, r"頂点 $(1,\,1)$",
            ha="center", va="bottom", fontsize=8.5, color=RED)

    # 面積ラベル
    ax.text(1.0, 0.45,
            r"面積 $= \int_0^2 f(x)\,dx$" + "\n"
            r"$= \left[-\dfrac{x^3}{3}+x^2\right]_0^2$" + "\n"
            r"$= -\dfrac{8}{3}+4 = \dfrac{4}{3}$",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    ax.set_title(r"$f(x)\geq 0$ のとき: 面積 $= \int_0^2 f(x)\,dx$",
                 fontsize=9.5, pad=4)


def draw_split_intervals(ax):
    """Panel 2: f(x)=x²-1 on [-2,2] — 区間分割"""
    _draw_axes(ax, xlim=(-2.5, 2.8), ylim=(-1.7, 4.5))

    def f(x):
        return x ** 2 - 1

    x_full = np.linspace(-2.2, 2.2, 500)

    # 区間別塗りつぶし
    # [-2, -1]: f>0 → 青
    x_a = np.linspace(-2, -1, 200)
    ax.fill_between(x_a, f(x_a), 0, color="#aaccff", alpha=0.70, zorder=2,
                    label=r"$f>0$（$+$ 面積）")
    # [-1, 1]: f<0 → 赤
    x_b = np.linspace(-1, 1, 200)
    ax.fill_between(x_b, f(x_b), 0, color="#ffaaaa", alpha=0.70, zorder=2,
                    label=r"$f<0$（注意！）")
    # [1, 2]: f>0 → 青
    x_c = np.linspace(1, 2, 200)
    ax.fill_between(x_c, f(x_c), 0, color="#aaccff", alpha=0.70, zorder=2)

    ax.plot(x_full, f(x_full), color=DARK_BLUE, linewidth=2.0, zorder=3)

    # ゼロ点と境界
    for xv in [-2, -1, 1, 2]:
        ax.plot(xv, 0, "o", color=DARK_BLUE, markersize=5, zorder=5)
        ax.text(xv, -0.15, f"${xv}$", ha="center", va="top", fontsize=8.5)

    # 区間ラベル
    ax.text(-1.5, 1.4, r"$+$",
            ha="center", va="center", fontsize=14, color=DARK_BLUE, fontweight="bold")
    ax.text(0.0, -0.55, r"$-$",
            ha="center", va="center", fontsize=14, color=RED, fontweight="bold")
    ax.text(1.5, 1.4, r"$+$",
            ha="center", va="center", fontsize=14, color=DARK_BLUE, fontweight="bold")

    # 注意ボックス
    ax.text(0.1, 3.8,
            "面積 $=$ $|$各区間の定積分$|$ の合計\n"
            r"$= \left|\int_{-2}^{-1}\right|+\left|\int_{-1}^{1}\right|+\left|\int_{1}^{2}\right|$"
            "\n定積分をそのまま足すと符号に注意！",
            ha="left", va="top", fontsize=8, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, alpha=0.9))

    ax.legend(loc="lower right", fontsize=7.5)
    ax.set_title(r"$f(x)<0$ の区間があるとき: 区間分割が必須",
                 fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_positive_case(axes[0])
    draw_split_intervals(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-area-xaxis-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
