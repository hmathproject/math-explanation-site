"""
gen_figures_diff_tangent_line.py — 接線の方程式 概念図生成

Panel 1: y = x³ - 3x の x = 2 での接線
Panel 2: y = x² - 2x の x = -1 での接線

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_tangent_line.py
出力: site/figures/diff-tangent-line-combined.png
      site/assets/images/diff-tangent-line-combined.png
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


def draw_tangent_panel(ax, f, df, a, x_range, title, note, func_label):
    """
    関数 f(x) の x=a での接線を描画する。
    """
    fa = f(a)
    slope = df(a)

    x_arr = np.linspace(x_range[0], x_range[1], 400)
    y_arr = f(x_arr)

    # 接線: y - f(a) = slope * (x - a)
    y_tangent = slope * (x_arr - a) + fa

    y_lo = min(y_arr.min(), y_tangent.min()) - 0.8
    y_hi = max(y_arr.max(), y_tangent.max()) + 0.8

    ax.set_xlim(x_range[0] - 0.3, x_range[1] + 0.3)
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(x_range[1] + 0.2, 0), xytext=(x_range[0] - 0.2, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_range[1] + 0.25, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi - 0.1), xytext=(0, y_lo + 0.1),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, y_hi - 0.1, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.3, "O", ha="right", va="top", fontsize=9)

    # 曲線
    ax.plot(x_arr, y_arr, color=DARK_BLUE, linewidth=2.2, zorder=3, label=func_label)

    # 接線（破線）
    ax.plot(x_arr, y_tangent, color=RED, linewidth=1.8, linestyle="--", zorder=4,
            label=f"接線（傾き {slope}）")

    # 接点
    ax.plot(a, fa, "o", color=RED, markersize=9, zorder=6)
    ax.plot([a, a], [y_lo, fa], ":", color=GRAY, linewidth=0.9)
    ax.text(a, y_lo - 0.3, f"$x={a}$", ha="center", va="top", fontsize=9)
    ax.text(a + 0.15, fa + 0.3,
            f"接点 $({a},\\ {fa})$\n傾き $f'({a})={slope}$",
            ha="left", va="bottom", fontsize=8.5, color=RED)

    # 凡例
    ax.legend(loc="upper left", fontsize=8, framealpha=0.85)

    # 注記
    ax.text((x_range[0] + x_range[1]) / 2, y_hi - 0.2, note,
            ha="center", va="top", fontsize=8.0, color=GRAY, style="italic")
    ax.set_title(title, fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    # Panel 1: f(x) = x³ - 3x, x = 2
    def f1(x):
        return x ** 3 - 3 * x

    def df1(x):
        return 3 * x ** 2 - 3

    draw_tangent_panel(
        axes[0], f1, df1, a=2, x_range=(-1.5, 2.8),
        title=r"$f(x) = x^3 - 3x$、$x=2$ での接線",
        note=r"$f'(2) = 3\cdot4 - 3 = 9$　→　接線: $y = 9(x-2) + 2 = 9x - 16$",
        func_label=r"$y=x^3-3x$",
    )

    # Panel 2: f(x) = x² - 2x, x = -1
    def f2(x):
        return x ** 2 - 2 * x

    def df2(x):
        return 2 * x - 2

    draw_tangent_panel(
        axes[1], f2, df2, a=-1, x_range=(-2.5, 3.5),
        title=r"$f(x) = x^2 - 2x$、$x=-1$ での接線",
        note=r"$f'(-1) = 2(-1) - 2 = -4$　→　接線: $y = -4(x+1) + 3 = -4x - 1$",
        func_label=r"$y=x^2-2x$",
    )

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-tangent-line-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
