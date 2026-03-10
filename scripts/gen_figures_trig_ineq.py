"""
gen_figures_trig_ineq.py — 三角不等式 基本例 概念図生成

Panel 1: sin θ ≥ √3/2 の解  → θ ∈ [π/3, 2π/3] を水色で塗りつぶし
Panel 2: cos θ ≤ -1/2 の解  → θ ∈ [2π/3, 4π/3] を水色で塗りつぶし

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_ineq.py
出力: site/figures/trig-inequality-basic-combined.png
      site/assets/images/trig-inequality-basic-combined.png
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

X_LO, X_HI = 0.0, 2 * np.pi


def setup_axes(ax, y_lo, y_hi, x_ticks):
    """軸・目盛りの共通セットアップ。"""
    pad_x = 0.5
    pad_y = 0.45
    ax.set_xlim(X_LO - pad_x, X_HI + pad_x)
    ax.set_ylim(y_lo - pad_y, y_hi + pad_y)
    ax.axis("off")

    # x 軸
    ax.annotate("", xy=(X_HI + pad_x - 0.05, 0), xytext=(X_LO - pad_x + 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + pad_x - 0.02, 0.0, r"$\theta$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, y_hi + pad_y - 0.05), xytext=(0, y_lo - pad_y + 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.05, y_hi + pad_y - 0.02, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点
    ax.text(-0.15, -0.12, "O", ha="right", va="top", fontsize=9)

    # x 軸目盛り
    for xv, lbl in x_ticks:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", linewidth=0.8)
        ax.text(xv, -0.20, lbl, ha="center", va="top", fontsize=8)

    # y 軸目盛り ±1
    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", linewidth=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)

    return pad_y, y_hi


def draw_panel1(ax):
    """sin θ ≥ √3/2 の解パネル。"""
    y_lo, y_hi = -1.5, 1.5
    y_val = np.sqrt(3) / 2  # ≈ 0.866
    sol_lo, sol_hi = np.pi / 3, 2 * np.pi / 3

    x_ticks = [
        (np.pi / 3,      r"$\frac{\pi}{3}$"),
        (2 * np.pi / 3,  r"$\frac{2\pi}{3}$"),
        (np.pi,          r"$\pi$"),
        (3 * np.pi / 2,  r"$\frac{3\pi}{2}$"),
        (2 * np.pi,      r"$2\pi$"),
    ]
    pad_y, _ = setup_axes(ax, y_lo, y_hi, x_ticks)

    theta = np.linspace(X_LO, X_HI, 1000)
    y_sin = np.sin(theta)

    # 塗りつぶし: sin θ ≥ √3/2 の領域
    ax.fill_between(theta, y_sin, y_val,
                    where=(y_sin >= y_val),
                    alpha=0.3, color="lightblue", zorder=1)

    # sin 曲線
    ax.plot(theta, y_sin, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 水平ライン y = √3/2
    ax.axhline(y_val, color="#cc2222", linewidth=1.2, linestyle="--", zorder=2)
    ax.text(X_HI + 0.1, y_val + 0.05,
            r"$y = \frac{\sqrt{3}}{2}$",
            ha="left", va="bottom", fontsize=8, color="#cc2222")

    # 端点の黒丸（閉区間）
    for xv in [sol_lo, sol_hi]:
        ax.plot(xv, y_val, "o", color=DARK_BLUE, markersize=6, zorder=5)

    # 解の範囲ラベル
    ax.text((sol_lo + sol_hi) / 2, y_hi + pad_y - 0.02,
            r"$\frac{\pi}{3} \leq \theta \leq \frac{2\pi}{3}$",
            ha="center", va="top", fontsize=9, color="#1a6b3a")

    # パネルタイトル
    ax.text((X_LO + X_HI) / 2, y_lo - pad_y + 0.05,
            r"$\sin\theta \geq \frac{\sqrt{3}}{2}$",
            ha="center", va="bottom", fontsize=11, fontweight="bold")


def draw_panel2(ax):
    """cos θ ≤ -1/2 の解パネル。"""
    y_lo, y_hi = -1.5, 1.5
    y_val = -0.5
    sol_lo, sol_hi = 2 * np.pi / 3, 4 * np.pi / 3

    x_ticks = [
        (np.pi / 3,      r"$\frac{\pi}{3}$"),
        (2 * np.pi / 3,  r"$\frac{2\pi}{3}$"),
        (np.pi,          r"$\pi$"),
        (4 * np.pi / 3,  r"$\frac{4\pi}{3}$"),
        (3 * np.pi / 2,  r"$\frac{3\pi}{2}$"),
        (2 * np.pi,      r"$2\pi$"),
    ]
    pad_y, _ = setup_axes(ax, y_lo, y_hi, x_ticks)

    theta = np.linspace(X_LO, X_HI, 1000)
    y_cos = np.cos(theta)

    # 塗りつぶし: cos θ ≤ -1/2 の領域
    ax.fill_between(theta, y_cos, y_val,
                    where=(y_cos <= y_val),
                    alpha=0.3, color="lightblue", zorder=1)

    # cos 曲線
    ax.plot(theta, y_cos, color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 水平ライン y = -1/2
    ax.axhline(y_val, color="#cc2222", linewidth=1.2, linestyle="--", zorder=2)
    ax.text(X_HI + 0.1, y_val - 0.08,
            r"$y = -\frac{1}{2}$",
            ha="left", va="top", fontsize=8, color="#cc2222")

    # 端点の黒丸（閉区間）
    for xv in [sol_lo, sol_hi]:
        ax.plot(xv, y_val, "o", color=DARK_BLUE, markersize=6, zorder=5)

    # 解の範囲ラベル
    ax.text((sol_lo + sol_hi) / 2, y_hi + pad_y - 0.02,
            r"$\frac{2\pi}{3} \leq \theta \leq \frac{4\pi}{3}$",
            ha="center", va="top", fontsize=9, color="#1a6b3a")

    # パネルタイトル
    ax.text((X_LO + X_HI) / 2, y_lo - pad_y + 0.05,
            r"$\cos\theta \leq -\frac{1}{2}$",
            ha="center", va="bottom", fontsize=11, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.0))
    fig.patch.set_facecolor("white")

    draw_panel1(axes[0])
    draw_panel2(axes[1])

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "trig-inequality-basic-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
