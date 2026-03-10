"""
gen_figures_diff_cubic.py — 3次関数のグラフ概形 概念図生成

Panel 1: f(x) = x³ - 3x のグラフと増減表を対応させた完成図
Panel 2: f(x) = x³ - 3x² （a>0 で異なる形）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_cubic.py
出力: site/figures/diff-cubic-graph-combined.png
      site/assets/images/diff-cubic-graph-combined.png
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
GRAY = "#888888"
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_cubic_with_table(ax, f, fp, title, x_lo, x_hi,
                          extrema, x_ticks, y_lim, table_y):
    """
    3次関数グラフと増減の対応図。
    extrema: [(x, y, label, color), ...] 極値点リスト
    x_ticks: [(x, label), ...] 増減表の key points
    table_y: 増減表を描画する y 座標（ax 座標系）
    """
    x_range = np.linspace(x_lo, x_hi, 500)
    y_range = f(x_range)

    ax.set_xlim(x_lo - 0.5, x_hi + 0.6)
    ax.set_ylim(y_lim[0] - 0.5, y_lim[1] + 1.2)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(x_hi + 0.5, 0), xytext=(x_lo - 0.4, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_hi + 0.53, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_lim[1] + 1.0), xytext=(0, y_lim[0] - 0.4),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, y_lim[1] + 1.02, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.1, -0.2, "O", ha="right", va="top", fontsize=9)

    # 曲線
    ax.plot(x_range, y_range, color=DARK_BLUE, linewidth=2.2, zorder=3)

    # 極値点と垂線
    for xp, yp, label, color in extrema:
        ax.plot(xp, yp, "o", color=color, markersize=7, zorder=6)
        ax.plot([xp, xp], [y_lim[0] - 0.3, yp], ":", color=GRAY, linewidth=0.9)
        ax.plot([x_lo - 0.3, xp], [yp, yp], ":", color=GRAY, linewidth=0.9)
        ax.text(xp, y_lim[0] - 0.45, f"${xp}$", ha="center", va="top", fontsize=8.5)
        ax.text(x_lo - 0.35, yp, f"${int(yp)}$", ha="right", va="center", fontsize=8.5)
        ax.text(xp + 0.12, yp + 0.15, label, ha="left", va="bottom",
                fontsize=8.5, color=color, fontweight="bold")

    # ── 増減表（簡易版）──
    # 表の位置: x_lo..x_hi 全体を等分して x 値を表示
    tw_x0 = x_lo - 0.1
    tw_x1 = x_hi + 0.1
    tw_y = table_y
    cell_h = 0.6

    header = ["$x$"] + [lbl for _, lbl in x_ticks] + [""]
    cell_w = (tw_x1 - tw_x0) / (len(header) - 1)

    # ヘッダー行
    ax.plot([tw_x0, tw_x1], [tw_y, tw_y], "k-", linewidth=0.8)
    ax.plot([tw_x0, tw_x1], [tw_y - cell_h, tw_y - cell_h], "k-", linewidth=0.8)
    ax.plot([tw_x0, tw_x1], [tw_y - 2 * cell_h, tw_y - 2 * cell_h], "k-", linewidth=0.8)

    for i, h in enumerate(header):
        xc = tw_x0 + i * cell_w
        ax.text(xc, tw_y - cell_h / 2, h, ha="center", va="center", fontsize=8.5)

    # f'(x) 行
    fp_label = r"$f'(x)$"
    ax.text(tw_x0 - 0.0, tw_y - cell_h - cell_h / 2, fp_label,
            ha="center", va="center", fontsize=8.5)

    # f(x) 行
    fx_label = r"$f(x)$"
    ax.text(tw_x0 - 0.0, tw_y - 2 * cell_h - cell_h / 2, fx_label,
            ha="center", va="center", fontsize=8.5)

    # x 値
    for i, (xv, xlbl) in enumerate(x_ticks):
        xc = tw_x0 + (i + 0.5) * cell_w + cell_w * 0.5
        # f' の符号（間隔）
        fp_mid = fp((xv + (x_ticks[i - 1][0] if i > 0 else x_lo)) / 2 if i > 0
                    else (x_lo + xv) / 2)
        # 簡易的に区間を決める
    # 区間ごとに f' の符号と f の矢印を描く
    intervals = []
    xs = [x_lo] + [xv for xv, _ in x_ticks] + [x_hi]
    for i in range(len(xs) - 1):
        xm = (xs[i] + xs[i + 1]) / 2
        sign = "+" if fp(xm) > 0 else "-"
        arrow = "↗" if fp(xm) > 0 else "↘"
        intervals.append((sign, arrow))

    for i, (sign, arrow) in enumerate(intervals):
        xc = tw_x0 + (i + 0.5) * (tw_x1 - tw_x0) / len(intervals)
        color = GREEN if sign == "+" else RED
        ax.text(xc, tw_y - cell_h - cell_h / 2, sign,
                ha="center", va="center", fontsize=10, color=color)
        ax.text(xc, tw_y - 2 * cell_h - cell_h / 2, arrow,
                ha="center", va="center", fontsize=12, color=color)

    # 極値の値を表に埋め込む
    for xp, yp, label, color in extrema:
        idx = next(i for i, (xv, _) in enumerate(x_ticks) if abs(xv - xp) < 0.1)
        xc = tw_x0 + (idx + 1) * (tw_x1 - tw_x0) / len(header)
        ax.text(xc, tw_y - 2 * cell_h - cell_h / 2, f"${int(yp)}$",
                ha="center", va="center", fontsize=8.5, color=color)
        # f'=0 マーク
        ax.text(xc, tw_y - cell_h - cell_h / 2, "0",
                ha="center", va="center", fontsize=9, color=color)

    ax.set_title(title, fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.0, 5.5))
    fig.patch.set_facecolor("white")

    # Panel 1: f(x) = x³ - 3x
    def f1(x): return x ** 3 - 3 * x
    def fp1(x): return 3 * x ** 2 - 3

    draw_cubic_with_table(
        axes[0], f1, fp1,
        title=r"$f(x) = x^3 - 3x$",
        x_lo=-2.2, x_hi=2.2,
        extrema=[(-1, f1(-1), "極大", GREEN), (1, f1(1), "極小", RED)],
        x_ticks=[(-1, r"$-1$"), (1, r"$1$")],
        y_lim=(-2.5, 2.5),
        table_y=4.0,
    )

    # Panel 2: f(x) = x³ - 3x²
    def f2(x): return x ** 3 - 3 * x ** 2
    def fp2(x): return 3 * x ** 2 - 6 * x

    draw_cubic_with_table(
        axes[1], f2, fp2,
        title=r"$f(x) = x^3 - 3x^2$",
        x_lo=-0.8, x_hi=3.5,
        extrema=[(0, f2(0), "極大", GREEN), (2, f2(2), "極小", RED)],
        x_ticks=[(0, r"$0$"), (2, r"$2$")],
        y_lim=(-5.0, 1.5),
        table_y=3.5,
    )

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-cubic-graph-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
