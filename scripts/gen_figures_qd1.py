"""
gen_figures_qd1.py — 式の決定・記事1用概念図
3点を通る放物線 y=2x²-5x+3 と3つの与えられた点を1パネルで表示

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  clip() は範囲外の y 値を上限/下限に張り付かせ、水平な黒線に見える。
  ylim を curve_ylim() で実データ範囲から計算して使う。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qd1.py
出力:
    figures/quadratic-determine-3points-combined.png
    assets/images/quadratic-determine-3points-combined.png
    ../figures/quadratic-determine-3points-combined.png  （PDF用）
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

if platform.system() == "Darwin":
    plt.rcParams["font.family"] = "Hiragino Sans"
elif platform.system() == "Windows":
    plt.rcParams["font.family"] = "MS Gothic"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["axes.unicode_minus"] = False

BASE_DIR = Path(__file__).parent.parent
FIGURES_DIR = BASE_DIR / "figures"
SITE_IMAGES_DIR = BASE_DIR / "assets" / "images"
EXP_FIGURES_DIR = BASE_DIR.parent / "figures"
FIGURES_DIR.mkdir(exist_ok=True)
EXP_FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150
Y_YLABEL_OFFSET = 0.27
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")


def curve_ylim(y_arr, extra_y=(), margin=0.15):
    """
    曲線データと注釈 y 座標から安全な ylim を計算する。

    np.clip() の代わりにこの関数で ylim を決め、ax.set_ylim() に渡す。
    - y_arr  : 曲線の y 値配列（np.ndarray）
    - extra_y: マーカー・ラベル等の追加 y 値リスト
    - margin : y スパンに対する上下余白の割合（デフォルト 15%）
    Returns : (y_lo, y_hi)
    """
    y_all = list(y_arr) + list(extra_y)
    y_min, y_max = min(y_all), max(y_all)
    span = max(y_max - y_min, 1.0)
    return y_min - margin * span, y_max + margin * span


def main():
    # x 範囲を -0.5〜3.0 に設定（3.0 では y=6.0, 3.1 では y=6.72 だったため -0.5〜3.0 に絞る）
    x = np.linspace(-0.5, 3.0, 500)
    y = 2*x**2 - 5*x + 3  # np.clip() は使わない

    # マーカー y 値も含めて ylim を計算
    marker_y = [3, 0, 1]
    y_lo, y_hi = curve_ylim(y, extra_y=marker_y, margin=0.15)
    y_lo = min(y_lo, -0.8)

    X_LO, X_HI = -0.7, 3.1

    fig, ax = plt.subplots(1, 1, figsize=(7.0, 4.5))
    fig.patch.set_facecolor("white")
    ax.set_xlim(X_LO - 0.1, X_HI + 0.5)
    ax.set_ylim(y_lo - 0.4, y_hi + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(X_HI + 0.42, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.46, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi + 0.48), xytext=(0, y_lo - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, y_hi + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)

    ax.plot(x, y, color="black", linewidth=2.0, zorder=2)

    ax.text(2.8, y_hi * 0.88, r"$y = 2x^2 - 5x + 3$", ha="right", va="center",
            fontsize=9.5, bbox=_lbl_bbox, zorder=7)

    pts = [(0, 3), (1, 0), (2, 1)]
    pt_labels = [r"$(0,\ 3)$", r"$(1,\ 0)$", r"$(2,\ 1)$"]
    pt_offsets = [(0.12, 0.2), (0.12, 0.25), (0.12, 0.2)]
    for (px, py), lbl, (dx, dy) in zip(pts, pt_labels, pt_offsets):
        ax.plot(px, py, "o", color="#2563eb", markersize=7, zorder=6)
        ax.text(px + dx, py + dy, lbl, ha="left", va="bottom", fontsize=9,
                color="#2563eb", bbox=_lbl_bbox, zorder=7)

    tick = 0.10
    ax.plot([0, 0], [-tick, tick], "k-", linewidth=0.9, zorder=3)
    ax.text(0, -0.28, "$O$", ha="center", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    ax.text((X_LO + X_HI) / 2, y_hi + 0.20,
            "3点を通る放物線（一般形で連立方程式を立てる）",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold")

    fig.tight_layout(pad=0.5)

    fname = "quadratic-determine-3points-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
