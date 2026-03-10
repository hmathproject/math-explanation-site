"""
gen_figures_cs.py — 平方完成 概念図生成

ケース1: y = x²-4x+5 = (x-2)²+1  （a>0: 下に凸、頂点が最小点）
ケース2: y = -x²+4x-3 = -(x-2)²+1 （a<0: 上に凸、頂点が最高点）

どちらも軸 x=2、頂点 (2,1) を示し、a の符号による違いを横並びで対比する。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_cs.py
出力: site/figures/quadratic-completing-square.png
      site/assets/images/quadratic-completing-square.png
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

# ── ケース定義 ──────────────────────────────────────────────────
CASES = [
    {
        "f":        lambda x: x**2 - 4*x + 5,
        "title":    r"$a > 0$：下に凸",
        "formula":  r"$y = (x-2)^2 + 1$",
        "vertex":   (2.0, 1.0),
        "vx_note":  "最小点",
        "vx_note_dy": 0.4,   # 頂点ラベルを上にずらす量
        "vx_note_va": "bottom",
        "y_lo": -0.6, "y_hi": 6.8,
    },
    {
        "f":        lambda x: -x**2 + 4*x - 3,
        "title":    r"$a < 0$：上に凸",
        "formula":  r"$y = -(x-2)^2 + 1$",
        "vertex":   (2.0, 1.0),
        "vx_note":  "最高点",
        "vx_note_dy": -0.5,  # 頂点ラベルを下にずらす量
        "vx_note_va": "top",
        "y_lo": -4.2, "y_hi": 2.6,
    },
]

X_LO, X_HI = -0.3, 4.3   # 両ケース共通の x 表示範囲


def draw_case(ax, case: dict) -> None:
    f      = case["f"]
    vx, vy = case["vertex"]
    y_lo   = case["y_lo"]
    y_hi   = case["y_hi"]

    ax.set_xlim(X_LO - 0.3, X_HI + 0.6)
    ax.set_ylim(y_lo, y_hi + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸（矢印付き）
    ax.annotate("", xy=(X_HI + 0.5, 0), xytext=(X_LO - 0.25, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.54, 0.0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸（矢印付き）
    ax.annotate("", xy=(0, y_hi + 0.5), xytext=(0, y_lo - 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, y_hi + 0.52, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点ラベル
    ax.text(-0.18, -0.18, "O", ha="right", va="top", fontsize=9)

    # 放物線
    x_arr = np.linspace(X_LO, X_HI, 600)
    y_arr = f(x_arr)
    ax.plot(x_arr, y_arr, color="black", linewidth=2.0, zorder=2, clip_on=True)

    # 軸の破線 x = vx（y_lo から y_hi まで）
    ax.plot([vx, vx], [y_lo, y_hi], color="#888888",
            linewidth=0.9, linestyle="--", zorder=1, clip_on=True)

    # 軸ラベル「軸 x = 2」— x 軸の少し下
    ax.text(vx, y_lo - 0.05, r"軸 $x=2$",
            ha="center", va="top", fontsize=9, color="#555555")

    # x 軸の目盛り（x = 2）
    tick = 0.07
    ax.plot([vx, vx], [-tick, tick], "k-", linewidth=0.9, zorder=3)
    ax.text(vx - 0.18, -0.22, "2", ha="center", va="top", fontsize=9)

    # 頂点から x 軸への点線
    ax.plot([vx, vx], [0.0, vy], color="black",
            linewidth=0.7, linestyle=":", zorder=1)

    # 頂点（黒塗り丸）
    ax.plot(vx, vy, "ko", markersize=7, zorder=6)

    # 頂点ラベル「頂点 (2, 1) / 最小点 or 最高点」
    dy  = case["vx_note_dy"]
    va  = case["vx_note_va"]
    lbl = f"頂点 $(2,\\ 1)$\n（{case['vx_note']}）"
    ax.text(vx + 0.25, vy + dy, lbl,
            ha="left", va=va, fontsize=9, linespacing=1.5,
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                      edgecolor="#cccccc", alpha=0.95))

    # 式ラベル（右端・上寄り）
    ax.text(X_HI + 0.3, y_hi + 0.3, case["formula"],
            ha="right", va="top", fontsize=10)

    # ケースタイトル（上部）
    cx = (X_LO + X_HI) / 2
    ax.text(cx, y_hi + 0.55, case["title"],
            ha="center", va="top", fontsize=11, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")

    for ax, case in zip(axes, CASES):
        draw_case(ax, case)

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname   = "quadratic-completing-square.png"
    out_fig  = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
