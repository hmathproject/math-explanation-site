"""
gen_figures_wp2.py — 文章題・応用・記事2用図
2パネル横並び
  左: 道幅問題の模式図（30×40mの土地に幅xmの道）
  右: 方程式 x(x+4)=45 のグラフ（交点で解を読む）

【clipping 防止方針】
  np.clip() を曲線データに適用してはならない。
  ylim は curve_ylim() で実データ範囲から安全に計算する。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_wp2.py
出力:
    figures/quadratic-word-problems-geometry-combined.png
    assets/images/quadratic-word-problems-geometry-combined.png
    ../figures/quadratic-word-problems-geometry-combined.png  （PDF用）
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
TIGHT_LAYOUT_PAD = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")


def curve_ylim(y_arr, extra_y=(), margin=0.15):
    """
    曲線データと注釈 y 座標から安全な ylim を計算する。
    np.clip() の代わりにこの関数で ylim を決め、ax.set_ylim() に渡す。
    """
    y_all = list(y_arr) + list(extra_y)
    y_min, y_max = min(y_all), max(y_all)
    span = max(y_max - y_min, 1.0)
    return y_min - margin * span, y_max + margin * span


def draw_road_diagram(ax):
    """左パネル: 道幅問題の模式図"""
    ax.set_xlim(-6, 46)
    ax.set_ylim(-5, 36)
    ax.set_aspect("equal")
    ax.axis("off")

    W, H = 40, 30  # 横40m、縦30m

    # 道路の位置（中央付近）
    rx = 17.5   # 縦道の左端 x 座標
    ry = 12.5   # 横道の下端 y 座標
    rw = 5.0    # 道幅（x=5 の例）

    # 土地全体（グレー）
    outer = mpatches.Rectangle((0, 0), W, H,
                                facecolor="#f3f4f6", edgecolor="black", linewidth=1.5)
    ax.add_patch(outer)

    # 縦道（グレー濃）
    v_road = mpatches.Rectangle((rx, 0), rw, H,
                                 facecolor="#9ca3af", edgecolor="none")
    ax.add_patch(v_road)
    # 横道（グレー濃）
    h_road = mpatches.Rectangle((0, ry), W, rw,
                                 facecolor="#9ca3af", edgecolor="none")
    ax.add_patch(h_road)

    # 境界線を再描画（道路は土地の内部なので上から描く）
    for rect_args in [
        ((0, 0), W, H),
        ((rx, 0), rw, H),
        ((0, ry), W, rw),
    ]:
        pos, w, h = rect_args
        r = mpatches.Rectangle(pos, w, h,
                                facecolor="none", edgecolor="black", linewidth=0.7)
        ax.add_patch(r)

    # 寸法ラベル
    ax.text(W / 2, -3.5, "40 m", ha="center", va="top", fontsize=9)
    ax.text(-4, H / 2, "30 m", ha="right", va="center", fontsize=9, rotation=90)

    # 道幅の矢印
    ax.annotate("", xy=(rx + rw, 20), xytext=(rx, 20),
                arrowprops=dict(arrowstyle="<->", color="#dc2626", lw=1.2))
    ax.text(rx + rw / 2, 21, "x m", ha="center", va="bottom",
            fontsize=9, color="#dc2626", fontweight="bold")

    # 残り面積のラベル（右下の長方形）
    ax.text(rx + rw + (W - rx - rw) / 2, ry / 2,
            r"$(30-x)(40-x)$", ha="center", va="center",
            fontsize=7.5, color="#1d4ed8")

    ax.text(W / 2, H + 2.5,
            "縦横に幅 x m の道を1本ずつ作る",
            ha="center", va="bottom", fontsize=9.5, fontweight="bold")


def draw_panel_quadratic(ax):
    """右パネル: g(x) = x(x+4) と y=45 のグラフ（解 x=5 を視覚化）"""
    x = np.linspace(-1, 8, 500)
    y_func = x * (x + 4)   # np.clip() 不使用

    y_lo, y_hi = curve_ylim(y_func, extra_y=[0, 45], margin=0.15)
    y_lo = min(y_lo, -3)

    XL, XH = -1.2, 8.5
    ax.set_xlim(XL - 0.1, XH + 0.6)
    ax.set_ylim(y_lo - 2, y_hi + 5)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(XH + 0.45, 0), xytext=(XL - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(XH + 0.5, 0, r"$x$（cm）", ha="left", va="center", fontsize=8.5)
    ax.annotate("", xy=(0, y_hi + 3.5), xytext=(0, y_lo - 1.5),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.15, y_hi + 1.0, r"$y$（cm²）", ha="left", va="bottom", fontsize=8.5)

    ax.plot(x, y_func, color="black", linewidth=2.0, zorder=2)

    # y = 45 の水平線
    ax.axhline(y=45, color="#2563eb", linewidth=1.5, linestyle="--", zorder=1)
    ax.text(XH + 0.1, 45, r"$y = 45$", ha="left", va="center",
            fontsize=8.5, color="#2563eb", bbox=_lbl_bbox, zorder=7)

    # 交点 x=5 (y=45)
    ax.plot(5, 45, "o", color="#dc2626", markersize=7, zorder=6)
    ax.plot([5, 5], [0, 45], "r--", linewidth=0.9, zorder=1)

    tick = 1.5
    for xv, lbl in [(0, "O"), (5, "5")]:
        ax.plot([xv, xv], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(xv, -tick * 2, lbl, ha="center", va="top", fontsize=8.5, bbox=_lbl_bbox)

    ax.text(5 + 0.2, 45 + 1, r"$x = 5$（解）", ha="left", va="bottom",
            fontsize=8.5, color="#dc2626", bbox=_lbl_bbox, zorder=7)
    ax.text(0.3, y_lo - 1.5, r"$y = x(x+4)$",
            ha="left", va="top", fontsize=8.5, bbox=_lbl_bbox, zorder=7)

    cx = (XL + XH) / 2
    ax.text(cx, y_hi + 3, "方程式 $x(x+4)=45$ の解",
            ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax.text(cx, y_hi + 0.5, r"グラフとの交点が解（$x > 0$）",
            ha="center", va="bottom", fontsize=8, color="#6b7280")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")
    draw_road_diagram(axes[0])
    draw_panel_quadratic(axes[1])
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.5)

    fname = "quadratic-word-problems-geometry-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
