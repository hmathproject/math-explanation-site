"""
gen_figures_integ_antiderivative_calc.py — 不定積分の計算手順

Panel 1: (2x+1)² の展開→積分フロー
Panel 2: ∫x(x-2)dx で展開が必要な理由（正誤比較）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_integ_antiderivative_calc.py
出力: site/figures/integ-antiderivative-calc-combined.png
      site/assets/images/integ-antiderivative-calc-combined.png
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


def draw_expand_then_integrate(ax):
    """Panel 1: (2x+1)² → 展開 → 積分フロー"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # ── タイトル帯 ──
    ax.text(5.0, 8.6, "展開してから積分する",
            ha="center", va="center", fontsize=11, fontweight="bold", color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ddeeff", edgecolor=DARK_BLUE, linewidth=1.5))

    step_box = dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor=DARK_BLUE, linewidth=1.3)
    arrow_kw_v = dict(arrowstyle="-|>", color=DARK_BLUE, lw=1.5, mutation_scale=12,
                      shrinkA=0, shrinkB=0)

    steps = [
        (5.0, 6.8, r"$\int (2x+1)^2\,dx$",           "#eef4ff"),
        (5.0, 4.9, r"$= \int (4x^2+4x+1)\,dx$",       "#eeffee"),
        (5.0, 3.0, r"$= \dfrac{4x^3}{3}+2x^2+x+C$",   "#fff8ee"),
    ]

    annots = [
        (7.8, 5.85, "① まず展開",   ORANGE),
        (7.8, 3.95, "② 各項を積分", GREEN),
    ]

    for (cx, cy, txt, fc) in steps:
        ax.text(cx, cy, txt,
                ha="center", va="center", fontsize=11,
                bbox=dict(boxstyle="round,pad=0.5", facecolor=fc, edgecolor=DARK_BLUE, linewidth=1.3))

    # 矢印
    for (y_from, y_to) in [(6.45, 5.25), (4.55, 3.55)]:
        ax.annotate("", xy=(5.0, y_to), xytext=(5.0, y_from),
                    arrowprops=dict(arrowstyle="-|>", color=DARK_BLUE, lw=1.5,
                                    mutation_scale=12, shrinkA=0, shrinkB=0))

    for (cx, cy, note, col) in annots:
        ax.text(cx, cy, note, ha="left", va="center", fontsize=9.5, color=col,
                bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor=col, alpha=0.8))

    # 重要メモ
    ax.text(5.0, 1.5,
            r"積分の線形性: $\int(f+g)\,dx = \int f\,dx + \int g\,dx$" + "\n"
            r"→ 展開すれば各項に $\int x^n\,dx = \dfrac{x^{n+1}}{n+1}+C$ が使える",
            ha="center", va="center", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f5f5ff", edgecolor=GRAY, alpha=0.9))

    ax.set_title(r"$(2x+1)^2$ の積分: 展開→各項積分", fontsize=9.5, pad=4)


def draw_correct_vs_wrong(ax):
    """Panel 2: ∫x(x-2)dx の正誤比較"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # ── タイトル ──
    ax.text(5.0, 8.6, r"$\int x(x-2)\,dx$ の計算",
            ha="center", va="center", fontsize=11, fontweight="bold", color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#ddeeff", edgecolor=DARK_BLUE, linewidth=1.5))

    # ── 誤った方法（左） ──
    ax.text(2.3, 7.4, "[誤]  誤った考え方", ha="center", va="center",
            fontsize=10, color=RED, fontweight="bold")
    wrong_box = dict(boxstyle="round,pad=0.45", facecolor="#fff0f0", edgecolor=RED, linewidth=1.3)
    wrong_lines = [
        r"「そのまま積分できる？」",
        r"$\int x(x-2)\,dx$",
        r"$\neq \dfrac{x^2}{2}\cdot\dfrac{(x-2)^2}{2}+C$",
    ]
    for i, line in enumerate(wrong_lines):
        ax.text(2.3, 6.55 - i * 1.05, line,
                ha="center", va="center", fontsize=9.5, color=RED,
                bbox=wrong_box, usetex=False)

    ax.text(2.3, 3.8,
            "積分は掛け算を\nそのまま分解できない！",
            ha="center", va="center", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0", edgecolor=RED, alpha=0.9))

    # 区切り線
    ax.plot([5.0, 5.0], [1.0, 8.2], color=GRAY, linewidth=1.0, linestyle="--")

    # ── 正しい方法（右） ──
    ax.text(7.7, 7.4, "[正]  正しい計算", ha="center", va="center",
            fontsize=10, color=GREEN, fontweight="bold")
    ok_box = dict(boxstyle="round,pad=0.45", facecolor="#f0fff0", edgecolor=GREEN, linewidth=1.3)
    ok_lines = [
        (r"① 展開: $x(x-2)=x^2-2x$",        7.7, 6.55),
        (r"② 積分: $\int(x^2-2x)\,dx$",       7.7, 5.50),
        (r"$= \dfrac{x^3}{3}-x^2+C$",          7.7, 4.35),
    ]
    for (line, cx, cy) in ok_lines:
        ax.text(cx, cy, line, ha="center", va="center", fontsize=9.5, color=GREEN,
                bbox=ok_box)

    # 矢印（正しい方）
    ax.annotate("", xy=(7.7, 5.85), xytext=(7.7, 6.15),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.4,
                                mutation_scale=10, shrinkA=0, shrinkB=0))
    ax.annotate("", xy=(7.7, 4.75), xytext=(7.7, 5.1),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.4,
                                mutation_scale=10, shrinkA=0, shrinkB=0))

    ax.text(7.7, 3.1,
            "展開すれば\n各項に公式が使える！",
            ha="center", va="center", fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f0fff0", edgecolor=GREEN, alpha=0.9))

    # ── まとめ ──
    ax.text(5.0, 1.5,
            "原則: 積分する前に必ず展開・整理する",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fffbe6", edgecolor=ORANGE, linewidth=1.3))

    ax.set_title(r"積分で積の形はそのまま使えない → 展開が必須", fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_expand_then_integrate(axes[0])
    draw_correct_vs_wrong(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "integ-antiderivative-calc-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
