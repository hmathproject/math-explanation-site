"""
gen_figures_diff_maxmin_closed.py — 閉区間での最大値・最小値 概念図生成

Panel 1: 端点が最大値になる例  f(x) = x³-3x, 区間 [0,3]
Panel 2: 極値が最小値になる例  f(x) = x³-3x, 区間 [-2,2]

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_maxmin_closed.py
出力: site/figures/diff-max-min-closed-combined.png
      site/assets/images/diff-max-min-closed-combined.png
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


def draw_closed_panel(ax, a, b, title, note):
    """
    f(x) = x³ - 3x の閉区間 [a, b] 上の最大・最小を可視化する。
    端点・極値のうちどれが最大・最小になるかを強調する。
    """
    def f(x):
        return x ** 3 - 3 * x

    # 候補点: 端点 + 極値（区間内のもの）
    candidates = [a, b]
    for xp in [-1.0, 1.0]:  # 極値 x=-1(極大2), x=1(極小-2)
        if a <= xp <= b:
            candidates.append(xp)
    candidates = sorted(set(candidates))
    vals = {xp: f(xp) for xp in candidates}

    x_max = max(vals, key=vals.get)
    x_min = min(vals, key=vals.get)

    x_range = np.linspace(a, b, 400)
    y_range = f(x_range)

    pad_x = 0.5
    y_lo = min(f(a), f(b), -2.2) - 0.5
    y_hi = max(f(a), f(b), 2.2) + 0.8

    ax.set_xlim(a - pad_x, b + pad_x + 0.2)
    ax.set_ylim(y_lo, y_hi + 0.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(b + pad_x + 0.1, 0), xytext=(a - pad_x + 0.1, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(b + pad_x + 0.13, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi + 0.4), xytext=(0, y_lo - 0.1),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, y_hi + 0.42, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.08, -0.2, "O", ha="right", va="top", fontsize=9)

    # 区間外を薄くする
    x_before = np.linspace(a - pad_x, a, 80)
    x_after = np.linspace(b, b + pad_x, 80)
    for xr in [x_before, x_after]:
        yr = f(xr)
        # clip to y_lo..y_hi
        ax.plot(xr, np.clip(yr, y_lo, y_hi), color=DARK_BLUE,
                linewidth=1.0, alpha=0.2, zorder=1)

    # 区間内の曲線（太い）
    ax.plot(x_range, y_range, color=DARK_BLUE, linewidth=2.2, zorder=3)

    # 区間端点の垂線（薄い）
    for xp in [a, b]:
        ax.plot([xp, xp], [y_lo, f(xp)], ":", color=GRAY, linewidth=0.9)

    # 候補点をプロット
    for xp, yp in vals.items():
        if xp == x_max:
            color = GREEN
            label = "最大"
        elif xp == x_min:
            color = RED
            label = "最小"
        else:
            color = ORANGE
            label = "極値"

        ax.plot(xp, yp, "o", color=color, markersize=8, zorder=6)
        ax.text(xp, yp + 0.25, f"{label}\n$f({int(xp) if xp == int(xp) else xp})={int(yp) if yp == int(yp) else yp:.1f}$",
                ha="center", va="bottom", fontsize=8.0, color=color, fontweight="bold")
        ax.plot([xp, xp], [y_lo, yp], ":", color=color, linewidth=0.7, alpha=0.5)
        ax.text(xp, y_lo - 0.15,
                f"${int(xp) if xp == int(xp) else xp}$",
                ha="center", va="top", fontsize=8.5)

    # 注記
    ax.text((a + b) / 2, y_hi + 0.1, note,
            ha="center", va="bottom", fontsize=8.0, color=GRAY, style="italic")

    ax.set_title(title, fontsize=9.5, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    # Panel 1: [0, 3] — 端点 x=3 が最大、極小 x=1 が最小
    draw_closed_panel(
        axes[0], a=0, b=3,
        title=r"$f(x)=x^3-3x$、区間 $[0,\,3]$",
        note="端点 x=3 が最大。極小 x=1 と端点を比較する。",
    )

    # Panel 2: [-2, 2] — 極大 x=-1 が最大、極小 x=1 が最小（端点は内側）
    draw_closed_panel(
        axes[1], a=-2, b=2,
        title=r"$f(x)=x^3-3x$、区間 $[-2,\,2]$",
        note="極大・極小・両端点の全候補を比較して最大・最小を決める。",
    )

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-max-min-closed-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
