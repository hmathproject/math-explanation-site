"""
gen_figures_integ_definite_param.py — 上端が文字のときの定積分

Panel 1: ∫₀ᵃ 2x dx = a² を三角形面積として確認（a=2 の例）
Panel 2: ∫₀ᵃ (3x²-2x) dx = a³-a² — 結果が a の式になる例

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_definite_param.py
出力: site/figures/integ-definite-param-combined.png
      site/assets/images/integ-definite-param-combined.png
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
    ax.text(-0.1, -0.12, "O", ha="right", va="top", fontsize=9)


def draw_triangle_area(ax):
    """Panel 1: ∫₀ᵃ 2x dx = a² （三角形）"""
    a = 2.0
    _draw_axes(ax, xlim=(-0.4, 3.0), ylim=(-0.6, 5.5))

    x_full = np.linspace(0, 2.6, 300)

    # 三角形領域 [0, a]
    x_fill = np.linspace(0, a, 300)
    ax.fill_between(x_fill, 2 * x_fill, 0,
                    color="#aaccff", alpha=0.7, zorder=2)

    ax.plot(x_full, 2 * x_full, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 境界
    ax.plot([a, a], [0, 2 * a], color=DARK_BLUE, linewidth=1.2,
            linestyle="--", alpha=0.8)
    ax.plot([0, a], [2 * a, 2 * a], color=DARK_BLUE, linewidth=1.2,
            linestyle="--", alpha=0.8)

    # ラベル
    ax.text(a, -0.2, r"$a=2$", ha="center", va="top", fontsize=9)
    ax.text(-0.15, 2 * a, r"$2a=4$", ha="right", va="center", fontsize=9)
    ax.text(0.0, -0.2, r"$0$", ha="center", va="top", fontsize=9)

    # 三角形寸法ラベル
    ax.annotate("", xy=(a, -0.4), xytext=(0, -0.4),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.3,
                                mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.text(a / 2, -0.5, r"底辺 $=a$", ha="center", va="top", fontsize=8.5, color=ORANGE)

    ax.annotate("", xy=(a + 0.15, 2 * a), xytext=(a + 0.15, 0),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3,
                                mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.text(a + 0.2, a, r"高さ $=2a$", ha="left", va="center", fontsize=8.5, color=GREEN)

    # 面積ラベル
    ax.text(0.65, 1.4,
            r"面積 $= \dfrac{1}{2}\cdot a\cdot 2a = a^2$",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.9))

    # 計算ボックス
    ax.text(1.55, 4.6,
            r"$\int_0^a 2x\,dx = \left[x^2\right]_0^a = a^2$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ddeeff",
                      edgecolor=DARK_BLUE, linewidth=1.3))

    ax.set_title(r"$\int_0^a 2x\,dx = a^2$（三角形の面積として確認）",
                 fontsize=9.5, pad=4)


def draw_param_integral(ax):
    """Panel 2: ∫₀ᵃ (3x²-2x) dx = a³-a²"""
    _draw_axes(ax, xlim=(-0.4, 2.6), ylim=(-1.5, 7.0))

    def f(x):
        return 3 * x ** 2 - 2 * x

    x_full = np.linspace(-0.2, 2.4, 500)

    # 例示: a=1 と a=2 の面積
    for a, col, lab in [(1, GREEN, r"$a=1$"), (2, ORANGE, r"$a=2$")]:
        x_fill = np.linspace(0, a, 300)
        y_fill = f(x_fill)
        # f は [0,1] で一部負になる（頂点は x=1/3）
        ax.fill_between(x_fill, y_fill, 0,
                        alpha=0.30, color=col, zorder=2)
        ax.plot([a, a], [0, f(a)], color=col, linewidth=1.2, linestyle="--", alpha=0.8)
        ax.text(a, -0.3, lab, ha="center", va="top", fontsize=8.5, color=col)

    ax.plot(x_full, f(x_full), color=DARK_BLUE, linewidth=2.0, zorder=3)

    # ゼロ点（f(x)=0 → x=0 または x=2/3）
    ax.plot(0, 0, "o", color=DARK_BLUE, markersize=4, zorder=5)
    ax.plot(2 / 3, 0, "o", color=DARK_BLUE, markersize=4, zorder=5)
    ax.text(2 / 3, 0.12, r"$\frac{2}{3}$", ha="center", va="bottom", fontsize=8)

    # 計算ボックス（中央上）
    ax.text(1.2, 6.2,
            r"$\int_0^a (3x^2-2x)\,dx$" + "\n"
            r"$= \left[x^3-x^2\right]_0^a$" + "\n"
            r"$= a^3-a^2$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ddeeff",
                      edgecolor=DARK_BLUE, linewidth=1.3))

    # a=1 の結果
    ax.text(0.5, -1.0,
            r"$a=1$: $1-1=0$",
            ha="center", va="center", fontsize=8.5, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#f0fff0",
                      edgecolor=GREEN, alpha=0.85))
    # a=2 の結果
    ax.text(1.8, -1.0,
            r"$a=2$: $8-4=4$",
            ha="center", va="center", fontsize=8.5, color=ORANGE,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#fffbe6",
                      edgecolor=ORANGE, alpha=0.85))

    ax.set_title(r"上端が文字 $a$: 結果も $a$ の式になる", fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_triangle_area(axes[0])
    draw_param_integral(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-definite-param-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
