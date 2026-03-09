"""
gen_figures_qd3.py — 式の決定・記事3用概念図
因数形: x=1,x=3が解, y=2(x-1)(x-3), 通る点(0,6)を1パネルで表示

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  clip() は範囲外の y 値を上限/下限に張り付かせ、水平な黒線に見える。
  旧コードは x=-0.3 で y=8.58 が Y_HI+0.2=7.7 を超えて左端に水平線が出ていた。
  curve_ylim() で実データ範囲から安全に ylim を計算して修正。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_qd3.py
出力:
    figures/quadratic-determine-roots-combined.png
    assets/images/quadratic-determine-roots-combined.png
    ../figures/quadratic-determine-roots-combined.png  （PDF用）
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
    # x=-0.3 で y=8.58 になるため、旧コードの Y_HI=7.5（clip上限7.7）では切れていた
    x = np.linspace(-0.3, 4.1, 500)
    y = 2*(x-1)*(x-3)  # np.clip() は使わない

    # マーカー y 値（解 y=0 × 2, 通過点 y=6, 頂点 y=-2）を含めて ylim を計算
    y_lo, y_hi = curve_ylim(y, extra_y=[0, 6, -2], margin=0.15)
    y_lo = min(y_lo, -1.5)

    X_LO, X_HI = -0.5, 4.2

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

    ax.text(4.0, y_hi * 0.75, r"$y = 2(x-1)(x-3)$", ha="right", va="center",
            fontsize=9.5, bbox=_lbl_bbox, zorder=7)

    tick = 0.12
    for xr, lbl in [(1, r"$x=1$（解）"), (3, r"$x=3$（解）")]:
        ax.plot([xr, xr], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.plot(xr, 0, "o", color="white", markeredgecolor="#dc2626",
                markersize=6, markeredgewidth=1.5, zorder=5)
        ax.text(xr, -0.38, lbl, ha="center", va="top", fontsize=8.5,
                color="#dc2626", bbox=_lbl_bbox, zorder=7)

    ax.plot(0, 6, "o", color="#2563eb", markersize=7, zorder=6)
    ax.text(0.12, 6.1, r"$(0,\ 6)$", ha="left", va="bottom", fontsize=9,
            color="#2563eb", bbox=_lbl_bbox, zorder=7)

    ax.text(0.12, -0.38, "$O$", ha="left", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    ax.plot(2, -2, "s", color="#9ca3af", markersize=5, zorder=5)
    ax.text(2.12, -2.0, "頂点$(2,\ -2)$", ha="left", va="center", fontsize=8,
            color="#9ca3af", bbox=_lbl_bbox, zorder=7)

    ax.text((X_LO + X_HI) / 2, y_hi + 0.20,
            "2つの解が既知 → 因数形で a だけを求める",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold")

    fig.tight_layout(pad=0.5)

    fname = "quadratic-determine-roots-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
