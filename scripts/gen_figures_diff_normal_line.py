"""
gen_figures_diff_normal_line.py — 法線の方程式 概念図生成

Panel 1: y = x² での接線と法線の対比（f'(a) ≠ 0 の通常ケース）
Panel 2: y = x³ の x = 0 での水平接線と鉛直な法線（f'(a) = 0 の特殊ケース）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_normal_line.py
出力: site/figures/diff-normal-line-combined.png
      site/assets/images/diff-normal-line-combined.png
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


def draw_normal_panel(ax):
    """
    Panel 1: y = x² の x=1 での接線と法線。
    f'(1) = 2 → 接線傾き 2、法線傾き -1/2
    """
    a = 1.0

    def f(x):
        return x ** 2

    def df(x):
        return 2 * x

    fa = f(a)
    slope_t = df(a)
    slope_n = -1.0 / slope_t  # 法線の傾き

    x_arr = np.linspace(-0.5, 2.8, 400)
    y_arr = f(x_arr)

    y_tang = slope_t * (x_arr - a) + fa
    y_norm = slope_n * (x_arr - a) + fa

    y_lo, y_hi = -1.5, 5.5

    ax.set_xlim(-0.5, 3.0)
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.9, 0), xytext=(-0.4, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.95, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi - 0.2), xytext=(0, y_lo + 0.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, y_hi - 0.2, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.1, -0.2, "O", ha="right", va="top", fontsize=9)

    # 曲線
    ax.plot(x_arr, np.clip(y_arr, y_lo, y_hi), color=DARK_BLUE, linewidth=2.2,
            zorder=3, label=r"$y = x^2$")

    # 接線（赤破線）
    ax.plot(x_arr, np.clip(y_tang, y_lo, y_hi), color=RED, linewidth=1.8,
            linestyle="--", zorder=4, label=f"接線（傾き {slope_t}）")

    # 法線（緑破線）
    ax.plot(x_arr, np.clip(y_norm, y_lo, y_hi), color=GREEN, linewidth=1.8,
            linestyle="-.", zorder=4, label=f"法線（傾き {slope_n}）")

    # 接点
    ax.plot(a, fa, "o", color=ORANGE, markersize=9, zorder=6)
    ax.plot([a, a], [y_lo, fa], ":", color=GRAY, linewidth=0.9)
    ax.text(a, y_lo - 0.2, f"$x={int(a)}$", ha="center", va="top", fontsize=9)
    ax.text(a + 0.12, fa + 0.2,
            f"接点 $({int(a)},{int(fa)})$",
            ha="left", va="bottom", fontsize=8.5, color=ORANGE)

    # 直交を示す小さな四角
    sq = 0.1
    sq_pts = np.array([
        [a, fa],
        [a + sq * slope_n / abs(slope_n), fa + sq],
        [a + sq * slope_n / abs(slope_n) + sq / abs(slope_t), fa + sq - sq * slope_t / abs(slope_t)],
        [a + sq / abs(slope_t), fa - sq * slope_t / abs(slope_t)],
    ])
    from matplotlib.patches import Polygon
    poly = Polygon(sq_pts, closed=True, fill=False,
                   edgecolor=ORANGE, linewidth=1.0, zorder=5)
    ax.add_patch(poly)

    ax.legend(loc="upper left", fontsize=8, framealpha=0.85)
    ax.set_title(r"$y = x^2$、$x=1$ での接線と法線", fontsize=9.5, pad=4)
    ax.text(1.5, y_lo + 0.3,
            "接線の傾き $m$ と法線の傾き $-1/m$ の積 $= -1$（直交）",
            ha="center", va="bottom", fontsize=7.5, color=GRAY, style="italic")


def draw_horizontal_tangent_panel(ax):
    """
    Panel 2: y = x³ の x=0 での水平接線と鉛直な法線（f'(0) = 0 の特殊ケース）。
    f'(0) = 0 → 接線は水平（y = 0）、法線は鉛直（x = 0）
    """
    def f(x):
        return x ** 3

    x_arr = np.linspace(-1.5, 1.5, 400)
    y_arr = f(x_arr)

    y_lo, y_hi = -2.5, 2.5

    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(1.7, 0), xytext=(-1.7, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(1.75, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi - 0.2), xytext=(0, y_lo + 0.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, y_hi - 0.2, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.12, -0.2, "O", ha="right", va="top", fontsize=9)

    # 曲線
    ax.plot(x_arr, np.clip(y_arr, y_lo, y_hi), color=DARK_BLUE, linewidth=2.2,
            zorder=3, label=r"$y = x^3$")

    # 水平接線 y = 0（x 軸と重なる）
    ax.axhline(y=0, color=RED, linewidth=1.8, linestyle="--", zorder=4,
               label="接線 $y=0$（水平）")

    # 鉛直な法線 x = 0（y 軸と重なる）
    ax.axvline(x=0, color=GREEN, linewidth=1.8, linestyle="-.", zorder=4,
               label="法線 $x=0$（鉛直）")

    # 接点 (0, 0)
    ax.plot(0, 0, "o", color=ORANGE, markersize=9, zorder=6)
    ax.text(0.15, 0.4, "接点 $(0,\\ 0)$\n$f'(0)=0$",
            ha="left", va="bottom", fontsize=8.5, color=ORANGE)

    # 注記
    ax.text(0.8, y_hi - 0.3,
            r"$f'(0)=0$ のとき法線は鉛直 $(x=a)$",
            ha="center", va="top", fontsize=8.0, color=GREEN, fontweight="bold")

    ax.legend(loc="lower right", fontsize=8, framealpha=0.85)
    ax.set_title(r"$y = x^3$、$x=0$ での接線と法線（特殊ケース）", fontsize=9.5, pad=4)
    ax.text(0, y_lo + 0.2,
            r"$f'(a)=0$ → 接線は水平 → 法線は鉛直 (傾きは定義されない)",
            ha="center", va="bottom", fontsize=7.5, color=GRAY, style="italic")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_normal_panel(axes[0])
    draw_horizontal_tangent_panel(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-normal-line-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
