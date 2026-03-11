"""
gen_figures_integ_definite_calc.py — 定積分の計算と符号付き面積

Panel 1: f(x)=x² on [0,2] — 定積分 = 面積（f≥0 の場合）
Panel 2: f(x)=x²-1 on [-2,2] — 符号付き面積（f<0 の区間では負）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_definite_calc.py
出力: site/figures/integ-definite-calc-combined.png
      site/assets/images/integ-definite-calc-combined.png
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
    ax.text(0.06, ylim[1] - 0.05, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.12, -0.12, "O", ha="right", va="top", fontsize=9)


def draw_positive_area(ax):
    """Panel 1: f(x)=x² on [0,2] — 定積分 = 面積"""
    _draw_axes(ax, xlim=(-0.4, 2.8), ylim=(-0.5, 5.2))

    x_full = np.linspace(-0.3, 2.6, 500)
    y_full = x_full ** 2

    # 塗りつぶし領域 [0, 2]
    x_fill = np.linspace(0, 2, 400)
    ax.fill_between(x_fill, x_fill ** 2, 0,
                    color="#aaccff", alpha=0.7, zorder=2)

    # 曲線
    ax.plot(x_full, y_full, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 境界の垂線
    for xv in [0, 2]:
        ax.plot([xv, xv], [0, xv ** 2], color=DARK_BLUE, linewidth=1.2,
                linestyle="--", alpha=0.7)
        ax.text(xv, -0.2, f"${xv}$", ha="center", va="top", fontsize=9)

    # 積分値ラベル
    ax.text(1.0, 1.4,
            r"$\int_0^2 x^2\,dx$" + "\n" + r"$=\left[\dfrac{x^3}{3}\right]_0^2$"
            + "\n" + r"$=\dfrac{8}{3}$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    # 面積ラベル
    ax.text(1.55, 0.55, r"面積 $=\dfrac{8}{3}$",
            ha="center", va="center", fontsize=8.5, color=DARK_BLUE)

    ax.set_title(r"$\int_0^2 x^2\,dx = \dfrac{8}{3}$（$f(x)\geq 0$: 面積 $=$ 定積分）",
                 fontsize=9.5, pad=4)


def draw_signed_area(ax):
    """Panel 2: f(x)=x²-1 on [-2,2] — 符号付き面積"""
    _draw_axes(ax, xlim=(-2.5, 2.8), ylim=(-1.8, 4.5))

    x_full = np.linspace(-2.2, 2.2, 500)
    y_full = x_full ** 2 - 1

    # 正の部分（f>0: x<-1 または x>1）
    x_pos1 = np.linspace(-2.2, -1.0, 300)
    x_pos2 = np.linspace(1.0, 2.2, 300)
    ax.fill_between(x_pos1, x_pos1 ** 2 - 1, 0,
                    color="#aaccff", alpha=0.65, zorder=2, label="正の面積（$f>0$）")
    ax.fill_between(x_pos2, x_pos2 ** 2 - 1, 0,
                    color="#aaccff", alpha=0.65, zorder=2)

    # 負の部分（f<0: -1 < x < 1）
    x_neg = np.linspace(-1.0, 1.0, 300)
    ax.fill_between(x_neg, x_neg ** 2 - 1, 0,
                    color="#ffaaaa", alpha=0.65, zorder=2, label="負の寄与（$f<0$）")

    # 曲線
    ax.plot(x_full, y_full, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # ゼロ交差点
    for xv in [-1, 1]:
        ax.plot(xv, 0, "o", color=DARK_BLUE, markersize=5, zorder=5)
        ax.text(xv, -0.15, f"${xv}$", ha="center", va="top", fontsize=9)

    ax.text(-2.0, -0.15, r"$-2$", ha="center", va="top", fontsize=9)
    ax.text(2.0, -0.15, r"$2$", ha="center", va="top", fontsize=9)

    # 正の値ラベル（左）
    ax.text(-1.6, 1.8, r"$+$", ha="center", va="center",
            fontsize=14, color="#1155cc", fontweight="bold")
    # 負の値ラベル（中央）
    ax.text(0.0, -0.6, r"$-$", ha="center", va="center",
            fontsize=14, color=RED, fontweight="bold")
    # 正の値ラベル（右）
    ax.text(1.6, 1.8, r"$+$", ha="center", va="center",
            fontsize=14, color="#1155cc", fontweight="bold")

    # 注記
    ax.text(0.15, 3.8,
            "定積分 $\\neq$ 面積\n"
            "（$f<0$ の区間では\n定積分の値が負になる）",
            ha="left", va="top", fontsize=8.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, alpha=0.9))

    ax.legend(loc="upper left", fontsize=7.5)
    ax.set_title(r"符号付き面積（$f(x)<0$ の区間では負）", fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_positive_area(axes[0])
    draw_signed_area(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-definite-calc-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
