"""
gen_figures_exp_graph.py — 指数関数グラフ 概念図生成

ケース1: a > 1  — y = 2^x（実線）, y = 3^x（破線）  右上がり・漸近線 y = 0
ケース2: 0 < a < 1 — y = (1/2)^x（実線）, y = (1/3)^x（破線）  右下がり・漸近線 y = 0

どちらも (0, 1) を通ること、y > 0 であることを示す。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_exp_graph.py
出力: site/figures/exp-function-graph.png
      site/assets/images/exp-function-graph.png
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

# ── 共通設定 ──────────────────────────────────────────────────
X_LO, X_HI = -2.5, 2.5
Y_LO, Y_HI = -0.5, 6.0


def draw_case(ax, title: str, funcs: list[dict]) -> None:
    """
    funcs: [{"f": callable, "label": str, "ls": linestyle}, ...]
    """
    ax.set_xlim(X_LO - 0.4, X_HI + 0.7)
    ax.set_ylim(Y_LO, Y_HI + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI + 0.6, 0), xytext=(X_LO - 0.35, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.64, 0.0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.5), xytext=(0, Y_LO - 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, Y_HI + 0.52, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点ラベル
    ax.text(-0.18, -0.18, "O", ha="right", va="top", fontsize=9)

    # 漸近線 y = 0 （x 軸と重なるが視認のため薄く引く）
    ax.axhline(0, color="#aaaaaa", linewidth=0.7, linestyle="--", zorder=0)
    ax.text(X_HI + 0.45, 0.10, r"$y=0$", ha="left", va="bottom",
            fontsize=8, color="#888888")

    # x 軸目盛り 1
    ax.plot([1, 1], [-0.06, 0.06], "k-", linewidth=0.8)
    ax.text(1.0, -0.25, "1", ha="center", va="top", fontsize=9)

    # 放物線を描く
    x_arr = np.linspace(X_LO, X_HI, 600)
    colors = ["#1a1a1a", "#555555"]  # 実線・破線の色
    for i, fd in enumerate(funcs):
        y_arr = fd["f"](x_arr)
        # クリップ（y > 6.5 を除外して枠外へはみ出さないように）
        mask = y_arr <= Y_HI + 0.8
        ax.plot(x_arr[mask], y_arr[mask],
                color=colors[i], linewidth=1.8,
                linestyle=fd["ls"], zorder=2, clip_on=True,
                label=fd["label"])

    # (0, 1) の通過点
    ax.plot(0, 1, "ko", markersize=6, zorder=5)
    ax.text(0.12, 1.05, r"$(0,\ 1)$", ha="left", va="bottom", fontsize=9)

    # 凡例（右上）
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)

    # タイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + 0.55, title,
            ha="center", va="top", fontsize=11, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")

    # ── ケース1: a > 1 ──────────────────────────────────────────
    draw_case(axes[0], r"$a > 1$：右上がり（単調増加）", [
        {"f": lambda x: 2.0 ** x, "label": r"$y = 2^x$",          "ls": "solid"},
        {"f": lambda x: 3.0 ** x, "label": r"$y = 3^x$",          "ls": "dashed"},
    ])

    # ── ケース2: 0 < a < 1 ──────────────────────────────────────
    draw_case(axes[1], r"$0 < a < 1$：右下がり（単調減少）", [
        {"f": lambda x: (0.5) ** x, "label": r"$y = \left(\frac{1}{2}\right)^x$", "ls": "solid"},
        {"f": lambda x: (1/3) ** x, "label": r"$y = \left(\frac{1}{3}\right)^x$", "ls": "dashed"},
    ])

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname    = "exp-function-graph.png"
    out_fig  = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
