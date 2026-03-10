"""
gen_figures_trig_graph.py — 三角関数グラフ 基本形状 概念図生成

Panel 1: y = sin θ、θ ∈ [-2π, 2π]
Panel 2: y = cos θ、θ ∈ [-2π, 2π]
Panel 3: y = tan θ、θ ∈ [-3π/2, 3π/2]（y を [-3, 3] にクリップ、漸近線 θ = ±π/2）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_graph.py
出力: site/figures/trig-graph-shape-combined.png
      site/assets/images/trig-graph-shape-combined.png
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
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_sincos(ax, func, title, x_lo, x_hi, y_lo, y_hi):
    """sin / cos パネルを描画する。"""
    pad_x = 0.5
    pad_y = 0.3
    ax.set_xlim(x_lo - pad_x, x_hi + pad_x)
    ax.set_ylim(y_lo - pad_y, y_hi + pad_y)
    ax.axis("off")

    # x 軸
    ax.annotate("", xy=(x_hi + pad_x - 0.05, 0), xytext=(x_lo - pad_x + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_hi + pad_x - 0.02, 0.0, r"$\theta$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, y_hi + pad_y - 0.05), xytext=(0, y_lo - pad_y + 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, y_hi + pad_y - 0.02, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点
    ax.text(-0.15, -0.18, "O", ha="right", va="top", fontsize=9)

    # x 軸目盛りラベル
    x_ticks = [
        (-2 * np.pi, r"$-2\pi$"),
        (-np.pi,     r"$-\pi$"),
        (np.pi,      r"$\pi$"),
        (2 * np.pi,  r"$2\pi$"),
    ]
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", linewidth=0.8)
        ax.text(xv, -0.22, lbl, ha="center", va="top", fontsize=8)

    # y 軸目盛り ±1
    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", linewidth=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)

    # 曲線
    theta = np.linspace(x_lo, x_hi, 1200)
    y = func(theta)
    ax.plot(theta, y, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # タイトル
    ax.text((x_lo + x_hi) / 2, y_hi + pad_y - 0.02, title,
            ha="center", va="top", fontsize=11, fontweight="bold")


def draw_tan(ax, x_lo, x_hi, y_lo, y_hi):
    """tan パネルを描画する。漸近線・クリッピング込み。"""
    pad_x = 0.5
    pad_y = 0.4
    ax.set_xlim(x_lo - pad_x, x_hi + pad_x)
    ax.set_ylim(y_lo - pad_y, y_hi + pad_y)
    ax.axis("off")

    # x 軸
    ax.annotate("", xy=(x_hi + pad_x - 0.05, 0), xytext=(x_lo - pad_x + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(x_hi + pad_x - 0.02, 0.0, r"$\theta$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, y_hi + pad_y - 0.05), xytext=(0, y_lo - pad_y + 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, y_hi + pad_y - 0.02, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点
    ax.text(-0.18, -0.22, "O", ha="right", va="top", fontsize=9)

    # x 軸目盛り: -π, π のみ（ゼロ付近を避ける）
    for xv, lbl in [(-np.pi, r"$-\pi$"), (np.pi, r"$\pi$")]:
        ax.plot([xv, xv], [-0.1, 0.1], "k-", linewidth=0.8)
        ax.text(xv, -0.35, lbl, ha="center", va="top", fontsize=8)

    # y 軸目盛り ±1
    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([-0.1, 0.1], [yv, yv], "k-", linewidth=0.8)
        ax.text(-0.15, yv, lbl, ha="right", va="center", fontsize=8)

    # 漸近線 θ = ±π/2（描画範囲内）
    for asym in [-np.pi / 2, np.pi / 2]:
        ax.axvline(asym, color="#cc2222", linewidth=1.0, linestyle="--",
                   ymin=0.02, ymax=0.98, zorder=1)
    # ラベルは右側の漸近線にのみ付ける
    ax.text(np.pi / 2 + 0.08, y_hi - 0.4,
            r"$\theta=\frac{\pi}{2}$", ha="left", va="top", fontsize=8, color="#cc2222")

    # tan 曲線（区間ごとに分割してクリップ）
    # ブランチ1: (-3π/2, -π/2)
    for lo, hi in [(-3 * np.pi / 2, -np.pi / 2),
                   (-np.pi / 2,      np.pi / 2),
                   (np.pi / 2,       3 * np.pi / 2)]:
        eps = 0.04
        t = np.linspace(lo + eps, hi - eps, 600)
        y = np.tan(t)
        mask = (y >= y_lo - 0.1) & (y <= y_hi + 0.1)
        y_clipped = np.clip(y, y_lo - 0.1, y_hi + 0.1)
        # 不連続点で途切れるよう mask を利用
        ax.plot(t[mask], y_clipped[mask], color=DARK_BLUE, linewidth=2.0, zorder=3)

    # タイトル
    ax.text((x_lo + x_hi) / 2, y_hi + pad_y - 0.02, r"$y = \tan\theta$",
            ha="center", va="top", fontsize=11, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.0))
    fig.patch.set_facecolor("white")

    # Panel 1: sin
    draw_sincos(axes[0], np.sin, r"$y = \sin\theta$",
                x_lo=-2 * np.pi, x_hi=2 * np.pi, y_lo=-1.5, y_hi=1.5)

    # Panel 2: cos
    draw_sincos(axes[1], np.cos, r"$y = \cos\theta$",
                x_lo=-2 * np.pi, x_hi=2 * np.pi, y_lo=-1.5, y_hi=1.5)

    # Panel 3: tan
    draw_tan(axes[2],
             x_lo=-3 * np.pi / 2, x_hi=3 * np.pi / 2, y_lo=-3.0, y_hi=3.0)

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "trig-graph-shape-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
