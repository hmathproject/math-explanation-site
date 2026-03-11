"""
gen_figures_diff_equation_roots.py — 方程式への応用（実数解の個数）概念図生成

Panel 1: y = x³ - 3x に y = k (k = 3, 0, -3) を重ねた交点数の比較
Panel 2: k の値と実数解の個数の場合分け図（境界値 = 極値）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_equation_roots.py
出力: site/figures/diff-equation-roots-combined.png
      site/assets/images/diff-equation-roots-combined.png
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
PURPLE = "#7b2d8b"
GRAY = "#888888"
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_intersection_panel(ax):
    """
    Panel 1: y = x³ - 3x と y = k の交点数の変化。
    k = 3: 極大値を超える → 1交点
    k = 2（極大値）→ 2交点（極大点で接する）
    k = 0 → 3交点
    k = -2（極小値）→ 2交点
    k = -3: 極小値を下回る → 1交点
    実際の図では k = 3, 0, -3 を示す。
    """
    def f(x):
        return x ** 3 - 3 * x

    x_arr = np.linspace(-2.5, 2.5, 500)
    y_arr = f(x_arr)

    # f'(x) = 3x² - 3 = 0 → x = ±1
    # 極大値 f(-1) = 2, 極小値 f(1) = -2

    k_values = [
        (3, RED, "1交点"),
        (0, GREEN, "3交点"),
        (-3, PURPLE, "1交点"),
    ]
    k_boundary = [
        (2, "#ff9900", "2交点（k=極大値）"),
        (-2, "#0099aa", "2交点（k=極小値）"),
    ]

    y_lo, y_hi = -4.5, 4.5

    ax.set_xlim(-2.8, 3.5)
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.7, 0), xytext=(-2.7, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.75, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi - 0.2), xytext=(0, y_lo + 0.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, y_hi - 0.2, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.25, "O", ha="right", va="top", fontsize=9)

    # 曲線
    ax.plot(x_arr, y_arr, color=DARK_BLUE, linewidth=2.5, zorder=4, label=r"$y=x^3-3x$")

    # 極大・極小点
    ax.plot(-1, 2, "o", color="#ff9900", markersize=8, zorder=7)
    ax.text(-1.15, 2 + 0.25, "極大\n$(-1,\\ 2)$", ha="right", va="bottom",
            fontsize=7.5, color="#ff9900", fontweight="bold")
    ax.plot(1, -2, "o", color="#0099aa", markersize=8, zorder=7)
    ax.text(1.15, -2 - 0.25, "極小\n$(1,\\ -2)$", ha="left", va="top",
            fontsize=7.5, color="#0099aa", fontweight="bold")

    # y = k の各直線
    for k, color, label in k_values:
        ax.axhline(y=k, color=color, linewidth=1.5, linestyle="--", zorder=3, alpha=0.85)
        ax.text(2.75, k + 0.15, f"$k={k}$\n（{label}）",
                ha="left", va="bottom", fontsize=7.5, color=color)

        # 交点をプロット
        # x³ - 3x = k → x³ - 3x - k = 0 の解
        roots = np.roots([1, 0, -3, -k])
        real_roots = [r.real for r in roots if abs(r.imag) < 1e-9]
        for r in real_roots:
            ax.plot(r, k, "o", color=color, markersize=7, zorder=8)

    # 境界値の直線（極値）
    for k, color, label in k_boundary:
        ax.axhline(y=k, color=color, linewidth=1.2, linestyle=":", zorder=3, alpha=0.7)
        ax.text(-2.7, k + 0.15, f"$y={k}$（{label}）",
                ha="left", va="bottom", fontsize=7.0, color=color)

    ax.legend(loc="upper right", fontsize=8, framealpha=0.85)
    ax.set_title(r"$x^3 - 3x = k$ の実数解の個数", fontsize=9.5, pad=4)
    ax.text(0, y_lo + 0.3,
            "y=k が極大値・極小値を境に交点数が変わる",
            ha="center", va="bottom", fontsize=7.5, color=GRAY, style="italic")


def draw_case_panel(ax):
    """
    Panel 2: k の値に応じた解の個数の場合分けを表で表示。
    """
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title(r"$x^3 - 3x = k$ の解の個数：場合分けまとめ", fontsize=9.5, pad=4)

    # 数直線風の図
    ax.annotate("", xy=(9.5, 5.5), xytext=(0.5, 5.5),
                arrowprops=dict(arrowstyle="-|>", color="black",
                                lw=1.0, mutation_scale=8))
    ax.text(9.6, 5.5, r"$k$", ha="left", va="center", fontsize=10)

    # 境界点
    ax.plot(3.5, 5.5, "|", color="#ff9900", markersize=14, linewidth=2)
    ax.text(3.5, 5.8, r"$k=-2$（極小値）", ha="center", va="bottom", fontsize=8,
            color="#0099aa")
    ax.plot(6.5, 5.5, "|", color="#0099aa", markersize=14, linewidth=2)
    ax.text(6.5, 5.8, r"$k=2$（極大値）", ha="center", va="bottom", fontsize=8,
            color="#ff9900")

    # 区間ラベル
    cases = [
        (2.0, 4.8, "1個", RED, r"$k < -2$"),
        (3.5, 4.3, "2個", "#0099aa", r"$k = -2$"),
        (5.0, 4.8, "3個", GREEN, r"$-2 < k < 2$"),
        (6.5, 4.3, "2個", "#ff9900", r"$k = 2$"),
        (8.0, 4.8, "1個", PURPLE, r"$k > 2$"),
    ]
    for x, y, n, color, condition in cases:
        ax.text(x, y, f"{n}", ha="center", va="center", fontsize=13,
                color=color, fontweight="bold")
        ax.text(x, y - 0.65, condition, ha="center", va="top", fontsize=8.0,
                color=color)

    # 説明文
    ax.text(5, 3.0,
            "境界値（$k$ = 極大値 or 極小値）では、曲線と水平線が接触するため",
            ha="center", va="center", fontsize=8.5, color="#333333")
    ax.text(5, 2.3, "1つの交点が「重複」→ 解の個数が1つ減る",
            ha="center", va="center", fontsize=8.5, color="#333333")

    ax.text(5, 1.3,
            "核心: 解の個数 = グラフ $y = f(x)$ と水平線 $y = k$ の交点数",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#e8f0fb", alpha=0.8))

    ax.text(5, 0.35,
            "極大値・極小値を求めれば、すべての k に対する解の個数がわかる",
            ha="center", va="center", fontsize=7.5, color=GRAY, style="italic")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_intersection_panel(axes[0])
    draw_case_panel(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-equation-roots-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
