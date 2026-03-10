"""
gen_figures_diff_increasing.py — 増減表・極値・反例（x³）の概念図生成

Panel 1: f'(x) の符号変化（正→負）→ 極大の成立図  [f(x) = -x³+3x]
Panel 2: f'(c)=0 でも符号変化なし → 極値なし反例  [f(x) = x³]

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_increasing.py
出力: site/figures/diff-increasing-decreasing-combined.png
      site/assets/images/diff-increasing-decreasing-combined.png
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
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_extremum_panel(ax):
    """Panel 1: 符号変化あり → 極大が成立する例 f(x) = -x³+3x"""
    def f(x):
        return -x ** 3 + 3 * x

    x_range = np.linspace(-2.0, 2.0, 400)
    y_range = f(x_range)

    ax.set_xlim(-2.3, 2.5)
    ax.set_ylim(-2.8, 3.2)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.4, 0), xytext=(-2.2, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.43, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 3.1), xytext=(0, -2.7),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, 3.12, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.08, -0.15, "O", ha="right", va="top", fontsize=9)

    # 増加・減少の塗り分け
    x_inc = np.linspace(-2.0, -1.0, 200)
    ax.fill_between(x_inc, f(x_inc), -2.9, alpha=0.10, color=GREEN)
    x_dec = np.linspace(-1.0, 1.0, 200)
    ax.fill_between(x_dec, f(x_dec), -2.9, alpha=0.10, color=RED)
    x_inc2 = np.linspace(1.0, 2.0, 200)
    ax.fill_between(x_inc2, f(x_inc2), -2.9, alpha=0.10, color=GREEN)

    # 曲線
    ax.plot(x_range, y_range, color=DARK_BLUE, linewidth=2.2, zorder=3)

    # 極大点 x=-1, 極小点 x=1
    for xp, label, y_offset, color, name in [
        (-1, r"$x=-1$", 0.2, GREEN, "極大"),
        (1,  r"$x=1$",  0.2, RED,   "極小"),
    ]:
        ax.plot(xp, f(xp), "o", color=color, markersize=7, zorder=6)
        ax.plot([xp, xp], [-2.8, f(xp)], ":", color="gray", linewidth=0.9)
        ax.text(xp, -2.95, label, ha="center", va="top", fontsize=8)
        ax.text(xp, f(xp) + y_offset, name,
                ha="center", va="bottom", fontsize=9, color=color, fontweight="bold")

    # 増減の矢印
    for xm, dy in [(-1.6, 0.5), (1.5, -0.5)]:
        ax.annotate("", xy=(xm, f(xm) + dy), xytext=(xm, f(xm)),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5))
    ax.annotate("", xy=(0, f(0) - 0.5), xytext=(0, f(0) + 0.1),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5))

    # f' の符号ラベル
    ax.text(-1.6, 0.8, r"$f'>0$", ha="center", fontsize=8.5, color=GREEN)
    ax.text(0.0,  0.9, r"$f'<0$", ha="center", fontsize=8.5, color=RED)
    ax.text(1.6,  -0.8, r"$f'>0$", ha="center", fontsize=8.5, color=GREEN)

    ax.set_title(r"$f'(x)$ が正→負に変化 → 極大（負→正 → 極小）",
                 fontsize=9.0, pad=4)


def draw_no_extremum_panel(ax):
    """Panel 2: f'(0)=0 でも符号変化なし → 極値なし  f(x) = x³"""
    def f(x):
        return x ** 3

    x_range = np.linspace(-1.6, 1.6, 400)
    y_range = f(x_range)

    ax.set_xlim(-2.0, 2.2)
    ax.set_ylim(-2.5, 2.8)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.1, 0), xytext=(-1.9, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.13, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 2.7), xytext=(0, -2.4),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, 2.72, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.1, -0.13, "O", ha="right", va="top", fontsize=9)

    # 全体を薄い緑（増加のみ）
    ax.fill_between(x_range, y_range, -2.5, alpha=0.10, color=GREEN)

    # 曲線
    ax.plot(x_range, y_range, color=DARK_BLUE, linewidth=2.2, zorder=3)

    # x=0 の点
    ax.plot(0, 0, "o", color=RED, markersize=7, zorder=6)
    ax.plot([0, 0], [-2.5, 0], ":", color="gray", linewidth=0.9)
    ax.text(0.1, -0.3, r"$f'(0)=0$", ha="left", va="top", fontsize=8.5, color=RED)

    # 注記（極値なし）
    ax.text(0.0, 1.8,
            r"$f'(0)=0$ だが" + "\n" + "符号変化なし\n（ずっと $f'>0$）",
            ha="center", va="bottom", fontsize=8.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0", edgecolor=RED, alpha=0.85))

    # 増加矢印
    for xm, dy in [(-1.0, 0.5), (0.8, 0.5)]:
        ax.annotate("", xy=(xm, f(xm) + dy), xytext=(xm, f(xm)),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5))

    ax.set_title(r"$f'(0)=0$ でも符号変化なし → 極値なし（反例: $x^3$）",
                 fontsize=9.0, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_extremum_panel(axes[0])
    draw_no_extremum_panel(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "diff-increasing-decreasing-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
