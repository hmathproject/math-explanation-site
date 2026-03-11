"""
gen_figures_diff_tangent_external.py — 曲線外の点からの接線 概念図生成

Panel 1: y = x³ から点 (0, -1) への2本の接線（グラフ主役型）
Panel 2: 接点パラメータ t の概念図（t の方程式で接線が確定する様子）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_diff_tangent_external.py
出力: site/figures/diff-tangent-external-combined.png
      site/assets/images/diff-tangent-external-combined.png
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


def draw_external_panel(ax):
    """
    Panel 1: y = x³ と外部点 P=(0,-1) から2本の接線を描画。
    接点 t を解いて t = 1（接線1）と t = -1（接線2）（実際はf(x)=x³の場合）
    実際の外部点 (0,-1) から y=x³への接線:
    接点(t, t³)、傾き 3t²、接線 y - t³ = 3t²(x - t) → y = 3t²x - 2t³
    通過条件: -1 = -2t³ → t³ = 1/2 → t = ∛(1/2) ≈ 0.794 (実根1つのみ)

    よりグラフが映えるように y=x³ から外部点 (2,0) への接線を使用:
    接点(t, t³)、傾き 3t²、接線 y = 3t²x - 2t³
    通過条件: 0 = 3t²·2 - 2t³ = 6t² - 2t³ = 2t²(3-t) → t=0 or t=3
    → 2本の接線: t=0(傾き0, y=0), t=3(傾き27, y=27x-54)
    """
    x_arr = np.linspace(-1.5, 3.5, 400)
    y_arr = x_arr ** 3

    # 外部点
    px, py = 2, 0

    # 接点 t=0: 接線 y=0
    t1 = 0
    slope1 = 3 * t1 ** 2
    intercept1 = t1 ** 3 - slope1 * t1
    y_tang1 = slope1 * x_arr + intercept1

    # 接点 t=3: 接線 y=27x-54
    t2 = 3
    slope2 = 3 * t2 ** 2
    intercept2 = t2 ** 3 - slope2 * t2
    y_tang2 = slope2 * x_arr + intercept2

    y_lo, y_hi = -3, 10

    ax.set_xlim(-1.5, 3.8)
    ax.set_ylim(y_lo, y_hi)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(3.7, 0), xytext=(-1.4, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(3.75, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, y_hi - 0.2), xytext=(0, y_lo + 0.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, y_hi - 0.2, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.4, "O", ha="right", va="top", fontsize=9)

    # y=x³ の曲線
    y_clip = np.clip(y_arr, y_lo, y_hi)
    ax.plot(x_arr, y_clip, color=DARK_BLUE, linewidth=2.2, zorder=3, label=r"$y=x^3$")

    # 接線1（t=0: 水平線 y=0）
    ax.plot(x_arr, np.clip(y_tang1, y_lo, y_hi), color=RED, linewidth=1.8,
            linestyle="--", zorder=4, label=f"接線1（傾き {slope1}）")

    # 接線2（t=3: y=27x-54）
    ax.plot(x_arr, np.clip(y_tang2, y_lo, y_hi), color=GREEN, linewidth=1.8,
            linestyle="--", zorder=4, label=f"接線2（傾き {slope2}）")

    # 外部点 P
    ax.plot(px, py, "s", color=ORANGE, markersize=9, zorder=7)
    ax.text(px + 0.1, py - 0.4, f"外部点 $P({px},{py})$",
            ha="left", va="top", fontsize=9, color=ORANGE, fontweight="bold")

    # 接点1 (0, 0)
    ax.plot(t1, t1 ** 3, "o", color=RED, markersize=8, zorder=6)
    ax.text(t1 - 0.15, t1 ** 3 + 0.3, f"接点1\n$(0,0)$",
            ha="right", va="bottom", fontsize=8, color=RED)

    # 接点2 (3, 27) — クリップ済み
    ax.plot(t2, min(t2 ** 3, y_hi - 0.3), "o", color=GREEN, markersize=8, zorder=6)
    ax.text(t2 - 0.15, min(t2 ** 3, y_hi - 0.3) - 0.3, "接点2\n$(3,27)$",
            ha="right", va="top", fontsize=8, color=GREEN)

    ax.legend(loc="upper left", fontsize=8, framealpha=0.85)
    ax.set_title(r"$y=x^3$ から外部点 $P(2,\,0)$ への接線", fontsize=9.5, pad=4)
    ax.text(0.0, y_lo + 0.3, "接点 $t$ を未知数に → $t$ の方程式が立つ → 解が接線の本数を決める",
            ha="left", va="bottom", fontsize=7.5, color=GRAY, style="italic")


def draw_concept_panel(ax):
    """
    Panel 2: 接点を未知数 t とする手順の概念図。
    接点 (t, f(t)) → 傾き f'(t) → 外部点通過条件 → t の方程式
    """
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)

    ax.set_title("外部点からの接線を求める手順", fontsize=9.5, pad=4)

    steps = [
        ("Step 1", "接点を $(t,\\ f(t))$ と設定する", "#1a3a6b", 6.8),
        ("Step 2", r"接線の傾き $= f'(t)$", "#cc2222", 5.2),
        ("Step 3", r"接線の方程式: $y - f(t) = f'(t)(x - t)$", "#1a6b3a", 3.6),
        ("Step 4", "外部点 $P(p,\\ q)$ を代入して $t$ の方程式", "#bb6600", 2.0),
        ("Step 5", "$t$ を解いて各接点に対応する接線を求める", "#555555", 0.5),
    ]

    for label, text, color, y in steps:
        ax.text(0.5, y, label, ha="left", va="center", fontsize=9,
                color=color, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", facecolor=color, alpha=0.15))
        ax.text(2.2, y, text, ha="left", va="center", fontsize=8.5, color="#333333")
        if y > 0.5:
            ax.annotate("", xy=(5, y - 0.8), xytext=(5, y - 0.3),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        lw=0.8, mutation_scale=7))

    ax.text(5, 7.6,
            r"$f(x)=x^3$ の例: $q = f'(t)(p-t)+f(t)$ に $p=2,\,q=0$ を代入",
            ha="center", va="top", fontsize=7.5, color=GRAY, style="italic")
    ax.text(5, 0.05, r"→ $2t^2(3-t) = 0$ → $t=0$ または $t=3$（2本の接線）",
            ha="center", va="bottom", fontsize=8, color="#333333")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_external_panel(axes[0])
    draw_concept_panel(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.2)

    fname = "diff-tangent-external-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
