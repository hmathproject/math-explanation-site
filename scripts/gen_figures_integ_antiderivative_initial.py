"""
gen_figures_integ_antiderivative_initial.py — 初期条件による積分定数の確定

Panel 1: ∫2x dx = x² + C の族（すべての原始関数）
Panel 2: f(1)=3 という条件で C=2 が確定する

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_antiderivative_initial.py
出力: site/figures/integ-antiderivative-initial-combined.png
      site/assets/images/integ-antiderivative-initial-combined.png
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


def _draw_axes(ax, xlim=(-2.4, 2.8), ylim=(-3.5, 6.5)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    ax.annotate("", xy=(xlim[1] - 0.05, 0), xytext=(xlim[0] + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(xlim[1], 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, ylim[1] - 0.1), xytext=(0, ylim[0] + 0.1),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, ylim[1] - 0.05, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.12, -0.2, "O", ha="right", va="top", fontsize=9)


def draw_all_antiderivatives(ax):
    """Panel 1: ∫2x dx = x² + C の族"""
    _draw_axes(ax)

    x = np.linspace(-2.0, 2.0, 400)
    C_values = [-2, -1, 0, 1, 2]
    palette = ["#5555cc", "#3399cc", DARK_BLUE, GREEN, RED]
    labels  = [r"$C=-2$", r"$C=-1$", r"$C=0$", r"$C=1$", r"$C=2$"]

    for C, col, lab in zip(C_values, palette, labels):
        y = x ** 2 + C
        ax.plot(x, y, color=col, linewidth=1.8, label=lab)
        ax.text(2.04, 2.0 ** 2 + C, lab, ha="left", va="center", fontsize=8, color=col)

    ax.text(0.08, 5.8,
            r"全曲線: $\dfrac{dy}{dx}=2x$",
            ha="left", va="top", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.85))

    ax.set_title(r"$\int 2x\,dx = x^2+C$（すべての原始関数）", fontsize=9.5, pad=4)


def draw_initial_condition(ax):
    """Panel 2: f(1)=3 → C=2 が確定"""
    _draw_axes(ax)

    x = np.linspace(-2.0, 2.0, 400)
    C_values = [-2, -1, 0, 1, 2]

    # 全族をグレーで薄く描く
    for C in C_values:
        y = x ** 2 + C
        ax.plot(x, y, color=GRAY, linewidth=1.2, alpha=0.35, linestyle="--")

    # 確定した曲線 C=2 を強調
    C_sel = 2
    y_sel = x ** 2 + C_sel
    ax.plot(x, y_sel, color=RED, linewidth=2.4, zorder=5,
            label=r"$y=x^2+2$（$C=2$）")

    # 条件点 (1, 3)
    px, py = 1.0, 1.0 ** 2 + C_sel
    ax.plot(px, py, "o", color=RED, markersize=8, zorder=6)
    ax.annotate(r"$f(1)=3$: 点$(1,\,3)$を通る",
                xy=(px, py), xytext=(1.5, 4.5),
                fontsize=8.5, color=RED,
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2,
                                mutation_scale=9, shrinkA=0, shrinkB=4),
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0",
                          edgecolor=RED, alpha=0.9))

    # 垂線
    ax.plot([px, px], [0, py], ":", color=RED, linewidth=0.9, alpha=0.7)
    ax.plot([0, px], [py, py], ":", color=RED, linewidth=0.9, alpha=0.7)
    ax.text(px, -0.25, r"$1$", ha="center", va="top", fontsize=9)
    ax.text(-0.15, py, r"$3$", ha="right", va="center", fontsize=9)

    # 計算ボックス
    ax.text(-2.3, 5.8,
            r"$f(1)=1^2+C=3$" + "\n" + r"$\Rightarrow C=2$",
            ha="left", va="top", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=1.2))

    ax.legend(loc="upper right", fontsize=8)
    ax.set_title(r"$f(1)=3$ という条件で $C=2$ が確定する", fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_all_antiderivatives(axes[0])
    draw_initial_condition(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-antiderivative-initial-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
