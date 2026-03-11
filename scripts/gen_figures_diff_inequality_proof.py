"""
gen_figures_diff_inequality_proof.py — 不等式への応用（微分で示す）概念図生成

Panel 1: h(x) = x³ - 3x + 2 のグラフで最小値 = 0 を確認
         （x ≥ 0 での x³ - 3x + 2 ≥ 0 の証明に対応）
Panel 2: f(x) = x³ と g(x) = 3x - 2 の大小関係（x ≥ 1 で f ≥ g）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_inequality_proof.py
出力: site/figures/diff-inequality-proof-combined.png
      site/assets/images/diff-inequality-proof-combined.png
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


def draw_h_graph_panel(ax):
    """
    Panel 1: h(x) = x³ - 3x + 2 の x ≥ 0 でのグラフ。
    h'(x) = 3x² - 3 = 0 → x = 1（x ≥ 0 の範囲）
    h(1) = 1 - 3 + 2 = 0 = 最小値
    x = 0 で h(0) = 2（端点）
    → 最小値 0 ≥ 0 なので h(x) ≥ 0 （x ≥ 0）が成立
    """
    def h(x):
        return x ** 3 - 3 * x + 2

    x_full = np.linspace(-0.5, 3.0, 500)
    y_full = h(x_full)

    x_pos = np.linspace(0, 3.0, 400)
    y_pos = h(x_pos)

    y_lo, y_hi = -1.5, 6.5

    ax.set_xlim(-0.5, 3.2)
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(3.1, 0), xytext=(-0.4, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(3.15, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi - 0.2), xytext=(0, y_lo + 0.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, y_hi - 0.2, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.12, -0.25, "O", ha="right", va="top", fontsize=9)

    # x < 0 の部分（薄い）
    ax.plot(x_full[x_full < 0], y_full[x_full < 0],
            color=DARK_BLUE, linewidth=1.2, alpha=0.3, zorder=2)

    # x ≥ 0 の部分（太い）
    ax.plot(x_pos, np.clip(y_pos, y_lo, y_hi), color=DARK_BLUE, linewidth=2.5,
            zorder=4, label=r"$h(x)=x^3-3x+2$（$x \geq 0$）")

    # y = 0 の参照線
    ax.axhline(y=0, color=RED, linewidth=1.0, linestyle="--", alpha=0.6, zorder=3)

    # 最小値点 (1, 0)
    ax.plot(1, 0, "o", color=RED, markersize=10, zorder=7)
    ax.text(1.15, 0 + 0.25, "最小値 $h(1)=0$\n（等号成立: $x=1$）",
            ha="left", va="bottom", fontsize=8.5, color=RED, fontweight="bold")
    ax.plot([1, 1], [y_lo, 0], ":", color=GRAY, linewidth=0.9)
    ax.text(1, y_lo - 0.15, "$1$", ha="center", va="top", fontsize=9)

    # 端点 (0, 2)
    ax.plot(0, 2, "s", color=ORANGE, markersize=8, zorder=6)
    ax.text(0.12, 2 + 0.2, "$h(0)=2$", ha="left", va="bottom",
            fontsize=8.5, color=ORANGE)

    # 塗り（h(x) ≥ 0 の領域を強調）
    ax.fill_between(x_pos, 0, np.clip(y_pos, 0, y_hi),
                    alpha=0.12, color=GREEN, zorder=1)

    ax.legend(loc="upper right", fontsize=8, framealpha=0.85)
    ax.set_title(r"$h(x) = x^3 - 3x + 2$ の最小値確認（$x \geq 0$）", fontsize=9.5, pad=4)
    ax.text(1.5, y_lo + 0.3,
            r"最小値 $h(1) = 0 \geq 0$ → $x \geq 0$ 全体で $h(x) \geq 0$ が成立",
            ha="center", va="bottom", fontsize=7.5, color=GRAY, style="italic")


def draw_fgx_panel(ax):
    """
    Panel 2: f(x) = x³ と g(x) = 3x - 2 の大小関係。
    h(x) = f(x) - g(x) = x³ - 3x + 2
    x ≥ 1 での h(x) ≥ 0 を示す（Panel 1 の証明の応用）
    """
    def f(x):
        return x ** 3

    def g(x):
        return 3 * x - 2

    x_arr = np.linspace(0.2, 2.5, 400)
    y_f = f(x_arr)
    y_g = g(x_arr)

    y_lo, y_hi = -2.5, 8.0

    ax.set_xlim(0.0, 2.7)
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.6, 0), xytext=(-0.1, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.65, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi - 0.2), xytext=(0, y_lo + 0.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, y_hi - 0.2, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.1, -0.25, "O", ha="right", va="top", fontsize=9)

    # f(x) = x³
    ax.plot(x_arr, np.clip(y_f, y_lo, y_hi), color=DARK_BLUE, linewidth=2.2,
            zorder=4, label=r"$f(x)=x^3$")

    # g(x) = 3x - 2
    ax.plot(x_arr, np.clip(y_g, y_lo, y_hi), color=RED, linewidth=2.0,
            linestyle="--", zorder=4, label=r"$g(x)=3x-2$")

    # 交点 x = 1（f(1) = g(1) = 1）
    ax.plot(1, 1, "o", color=ORANGE, markersize=10, zorder=7)
    ax.plot([1, 1], [y_lo, 1], ":", color=GRAY, linewidth=0.9)
    ax.text(1, y_lo - 0.15, "$1$", ha="center", va="top", fontsize=9)
    ax.text(1.1, 1.3, "等号成立\n$x=1$", ha="left", va="bottom",
            fontsize=8.0, color=ORANGE, fontweight="bold")

    # 塗り（x ≥ 1 で f ≥ g の領域）
    x_right = x_arr[x_arr >= 1]
    yf_right = f(x_right)
    yg_right = g(x_right)
    ax.fill_between(x_right, np.clip(yg_right, y_lo, y_hi),
                    np.clip(yf_right, y_lo, y_hi),
                    alpha=0.15, color=GREEN, zorder=1,
                    label=r"$f(x) \geq g(x)$（$x \geq 1$）")

    # 矢印で大小関係を示す
    ax.annotate("", xy=(1.8, f(1.8)), xytext=(1.8, g(1.8)),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.5,
                                mutation_scale=10))
    ax.text(1.85, (f(1.8) + g(1.8)) / 2, r"$f \geq g$",
            ha="left", va="center", fontsize=9, color=GREEN, fontweight="bold")

    ax.legend(loc="upper left", fontsize=8, framealpha=0.85)
    ax.set_title(r"$x^3 \geq 3x - 2$（$x \geq 1$）の視覚的確認", fontsize=9.5, pad=4)
    ax.text(1.3, y_lo + 0.3,
            r"$h(x)=f(x)-g(x) \geq 0$ を微分で示す",
            ha="center", va="bottom", fontsize=7.5, color=GRAY, style="italic")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_h_graph_panel(axes[0])
    draw_fgx_panel(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-inequality-proof-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
