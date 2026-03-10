"""
gen_figures_diff_maxmin_param.py — 文字係数を含む最大値・最小値 概念図生成

f(x) = x³ - 3ax (a は文字係数) の区間 [-2, 2] での最大・最小

Panel 1: a > 0 のケース（例: a=1）— 極大と極小が区間内に存在
Panel 2: a < 0 のケース（例: a=-1）— 単調増加

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_maxmin_param.py
出力: site/figures/diff-max-min-param-combined.png
      site/assets/images/diff-max-min-param-combined.png
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


def draw_param_panel(ax, a_val, title, note):
    """
    f(x) = x³ - 3a·x の区間 [-2, 2] での最大・最小を描画。
    f'(x) = 3x² - 3a = 3(x² - a)
    """
    def f(x):
        return x ** 3 - 3 * a_val * x

    def fp(x):
        return 3 * x ** 2 - 3 * a_val

    a_range = (-2.0, 2.0)

    # 区間端点
    candidates = {-2.0: f(-2.0), 2.0: f(2.0)}

    # 極値（f'(x)=0 の解で区間内のもの）
    if a_val > 0:
        sqrt_a = np.sqrt(a_val)
        for xp in [-sqrt_a, sqrt_a]:
            if a_range[0] < xp < a_range[1]:
                candidates[xp] = f(xp)

    x_max = max(candidates, key=candidates.get)
    x_min = min(candidates, key=candidates.get)

    x_range = np.linspace(-2.0, 2.0, 400)
    y_range = f(x_range)

    y_lo = min(y_range) - 0.8
    y_hi = max(y_range) + 1.0

    ax.set_xlim(-2.7, 2.7)
    ax.set_ylim(y_lo, y_hi + 0.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(2.6, 0), xytext=(-2.6, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(2.63, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi + 0.4), xytext=(0, y_lo - 0.1),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, y_hi + 0.42, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.1, -0.3, "O", ha="right", va="top", fontsize=9)

    # 区間の境界を示す垂線
    for xp in [-2.0, 2.0]:
        ax.plot([xp, xp], [y_lo, f(xp)], ":", color=GRAY, linewidth=0.9)
        ax.text(xp, y_lo - 0.15, f"${int(xp)}$", ha="center", va="top", fontsize=8.5)

    # 区間外を薄く
    x_before = np.linspace(-2.5, -2.0, 80)
    x_after = np.linspace(2.0, 2.5, 80)
    for xr in [x_before, x_after]:
        yr = f(xr)
        ax.plot(xr, np.clip(yr, y_lo, y_hi), color=DARK_BLUE,
                linewidth=1.0, alpha=0.2, zorder=1)

    # 曲線
    ax.plot(x_range, y_range, color=DARK_BLUE, linewidth=2.2, zorder=3)

    # 候補点プロット
    for xp, yp in candidates.items():
        if abs(xp - x_max) < 1e-6:
            color = GREEN
            label_name = "最大"
        elif abs(xp - x_min) < 1e-6:
            color = RED
            label_name = "最小"
        else:
            color = ORANGE
            label_name = "極値"

        ax.plot(xp, yp, "o", color=color, markersize=8, zorder=6)
        xp_str = f"{xp:.0f}" if abs(xp - round(xp)) < 0.01 else f"{xp:.2f}"
        yp_str = f"{yp:.0f}" if abs(yp - round(yp)) < 0.01 else f"{yp:.2f}"
        ax.text(xp, yp + 0.35,
                f"{label_name}: $f({xp_str})={yp_str}$",
                ha="center", va="bottom", fontsize=7.5, color=color, fontweight="bold")

    # f の a 値に応じた増減表テキスト
    ax.text(-2.5, y_hi,
            f"$a = {a_val}$ のとき",
            ha="left", va="top", fontsize=9.5, fontweight="bold", color=DARK_BLUE)

    ax.text((a_range[0] + a_range[1]) / 2, y_lo - 0.5, note,
            ha="center", va="top", fontsize=8.0, color=GRAY, style="italic")

    ax.set_title(title, fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.2))
    fig.patch.set_facecolor("white")

    # Panel 1: a=1 (a>0, sqrt(a)=1, 極値が区間内)
    draw_param_panel(
        axes[0], a_val=1,
        title=r"$f(x)=x^3-3x$、区間 $[-2,\,2]$（$a=1>0$）",
        note=r"$f'(x)=3(x^2-1)$ → 極値 $x=\pm 1$ が区間内",
    )

    # Panel 2: a=-1 (a<0, f'(x)=3x²+3>0 なので単調増加)
    draw_param_panel(
        axes[1], a_val=-1,
        title=r"$f(x)=x^3+3x$、区間 $[-2,\,2]$（$a=-1<0$）",
        note=r"$f'(x)=3(x^2+1)>0$ → 単調増加、端点が最大・最小",
    )

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-max-min-param-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
