"""
gen_figures_integ_antiderivative_basics.py — 不定積分・原始関数の基本

Panel 1: 微分と積分の逆演算サイクル図
Panel 2: ∫x² dx = x³/3 + C の族（C の値で決まる曲線群）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_antiderivative_basics.py
出力: site/figures/integ-antiderivative-basics-combined.png
      site/assets/images/integ-antiderivative-basics-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.patches as mpatches
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


def draw_cycle_diagram(ax):
    """Panel 1: 微分と積分の逆演算サイクル"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # ── ボックス定義 (cx, cy, label_top, label_bot) ──
    boxes = [
        (2.0, 6.0, r"$F(x)$",        r"$\dfrac{x^3}{3}$"),
        (8.0, 6.0, r"$f(x)$",         r"$x^2$"),
        (8.0, 2.0, r"$f(x)$",         r"$x^2$"),
        (2.0, 2.0, r"$F(x)+C$",       r"$\dfrac{x^3}{3}+C$"),
    ]

    box_w, box_h = 2.2, 1.4
    box_style = dict(boxstyle="round,pad=0.4", facecolor="#eef4ff", edgecolor=DARK_BLUE, linewidth=1.5)

    centers = []
    for (cx, cy, top, bot) in boxes:
        ax.text(cx, cy, top + "\n" + bot,
                ha="center", va="center", fontsize=10,
                bbox=box_style, linespacing=1.8)
        centers.append((cx, cy))

    # ── 矢印: 右上（微分 F→f） ──
    ax.annotate("", xy=(centers[1][0] - box_w / 2 - 0.05, centers[1][1]),
                xytext=(centers[0][0] + box_w / 2 + 0.05, centers[0][1]),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.8, mutation_scale=12,
                                shrinkA=0, shrinkB=0))
    ax.text(5.0, 6.35, "微分（d/dx）", ha="center", va="bottom", fontsize=9.5, color=RED)

    # ── 矢印: 下右（=、同じ関数） ──
    ax.annotate("", xy=(centers[2][0], centers[2][1] + box_h / 2 + 0.05),
                xytext=(centers[1][0], centers[1][1] - box_h / 2 - 0.05),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4, mutation_scale=10,
                                shrinkA=0, shrinkB=0))
    ax.text(8.45, 4.0, "（同じ関数）", ha="left", va="center", fontsize=8.5, color=GRAY)

    # ── 矢印: 左下（積分 f→F+C） ──
    ax.annotate("", xy=(centers[3][0] + box_w / 2 + 0.05, centers[3][1]),
                xytext=(centers[2][0] - box_w / 2 - 0.05, centers[2][1]),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.8, mutation_scale=12,
                                shrinkA=0, shrinkB=0))
    ax.text(5.0, 1.65, "積分（∫dx）", ha="center", va="top", fontsize=9.5, color=GREEN)

    # ── 矢印: 上左（F+C→F、左辺に C を加えた原始関数） ──
    ax.annotate("", xy=(centers[0][0], centers[0][1] - box_h / 2 - 0.05),
                xytext=(centers[3][0], centers[3][1] + box_h / 2 + 0.05),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4, mutation_scale=10,
                                shrinkA=0, shrinkB=0))
    ax.text(-0.3, 4.0, "（C を確定）", ha="left", va="center", fontsize=8.5, color=GRAY)

    # ── 中央の説明 ──
    ax.text(5.0, 4.0,
            "微分と積分は\n逆演算の関係",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fffbe6", edgecolor=ORANGE, linewidth=1.2))

    ax.set_title("微分 ⇄ 積分（逆演算サイクル）", fontsize=9.5, pad=4)


def draw_family_of_curves(ax):
    """Panel 2: ∫x² dx = x³/3 + C の族"""
    x = np.linspace(-2.0, 2.0, 400)

    ax.set_xlim(-2.4, 2.8)
    ax.set_ylim(-5.5, 5.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.35, 0), xytext=(-2.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.38, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 5.3), xytext=(0, -5.3),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, 5.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.12, -0.18, "O", ha="right", va="top", fontsize=9)

    C_values = [-2, -1, 0, 1, 2]
    colors = ["#5555cc", "#3399cc", DARK_BLUE, GREEN, RED]
    labels = [r"$C=-2$", r"$C=-1$", r"$C=0$", r"$C=1$", r"$C=2$"]

    for C, col, lab in zip(C_values, colors, labels):
        y = x ** 3 / 3 + C
        ax.plot(x, y, color=col, linewidth=1.8, label=lab)
        # ラベルを右端に付ける
        ax.text(2.02, 2.0 ** 3 / 3 + C, lab,
                ha="left", va="center", fontsize=8, color=col)

    # 傾きが x² であることを示すアノテーション
    ax.text(0.05, 4.8,
            r"すべての曲線で" + "\n" + r"$\dfrac{dy}{dx}=x^2$",
            ha="left", va="top", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, alpha=0.85))

    ax.set_title(r"$\int x^2\,dx = \dfrac{x^3}{3}+C$（$C$ の値で族が決まる）",
                 fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_cycle_diagram(axes[0])
    draw_family_of_curves(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-antiderivative-basics-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
