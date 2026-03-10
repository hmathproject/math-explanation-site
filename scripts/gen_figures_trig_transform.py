"""
gen_figures_trig_transform.py — 三角関数グラフ 変換 概念図生成

Panel 1: 振幅の変化 — y = sin θ（薄灰）と y = 2 sin θ（濃色）
Panel 2: 周期の変化 — y = sin θ（薄灰）と y = sin 2θ（濃色）
Panel 3: 位相のずれ  — y = sin θ（薄灰）と y = sin(θ - π/3)（濃色）
Panel 4: 垂直移動   — y = sin θ（薄灰）と y = sin θ + 1（濃色）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_transform.py
出力: site/figures/trig-graph-transform-combined.png
      site/assets/images/trig-graph-transform-combined.png
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
GRAY = "#aaaaaa"
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

# x 範囲は全パネル共通 [0, 2π]
X_LO, X_HI = 0.0, 2 * np.pi
X_TICKS = [
    (np.pi / 2,      r"$\frac{\pi}{2}$"),
    (np.pi,          r"$\pi$"),
    (3 * np.pi / 2,  r"$\frac{3\pi}{2}$"),
    (2 * np.pi,      r"$2\pi$"),
]


def setup_axes(ax, y_lo, y_hi):
    """軸・目盛りの共通セットアップ。"""
    pad_x = 0.5
    pad_y = 0.35
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
    ax.text(-0.15, -0.18, "O", ha="right", va="top", fontsize=9)

    # x 軸目盛り
    for xv, lbl in X_TICKS:
        ax.plot([xv, xv], [-0.06, 0.06], "k-", linewidth=0.8)
        ax.text(xv, -0.22, lbl, ha="center", va="top", fontsize=8)

    return pad_y, y_hi


def draw_panel1(ax):
    """振幅の変化: y = sin θ と y = 2 sin θ。"""
    y_lo, y_hi = -2.5, 2.5
    pad_y, y_hi_eff = setup_axes(ax, y_lo, y_hi)

    # y 軸目盛り ±1, ±2
    for yv, lbl in [(1, "1"), (-1, "-1"), (2, "2"), (-2, "-2")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", linewidth=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)

    theta = np.linspace(X_LO, X_HI, 1000)

    # y = sin θ（薄灰）
    ax.plot(theta, np.sin(theta), color=GRAY, linewidth=1.2, linestyle="--",
            label=r"$y=\sin\theta$", zorder=2)

    # y = 2 sin θ（濃色）
    ax.plot(theta, 2 * np.sin(theta), color=DARK_BLUE, linewidth=2.0,
            label=r"$y=2\sin\theta$", zorder=3)

    # 最大値 2 の注記
    ax.annotate("", xy=(np.pi / 2, 2.0), xytext=(np.pi / 2, 1.0),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=0.9,
                                mutation_scale=7, shrinkA=0, shrinkB=3))
    ax.text(np.pi / 2 + 0.15, 1.5, "最大値 2", ha="left", va="center",
            fontsize=8, color="#333333")

    ax.legend(loc="upper right", fontsize=8, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)

    ax.text((X_LO + X_HI) / 2, y_hi + pad_y - 0.02, "振幅：A = 2",
            ha="center", va="top", fontsize=11, fontweight="bold")


def draw_panel2(ax):
    """周期の変化: y = sin θ と y = sin 2θ。"""
    y_lo, y_hi = -1.5, 1.5
    pad_y, y_hi_eff = setup_axes(ax, y_lo, y_hi)

    # y 軸目盛り ±1
    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", linewidth=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)

    theta = np.linspace(X_LO, X_HI, 1000)

    # y = sin θ（薄灰）
    ax.plot(theta, np.sin(theta), color=GRAY, linewidth=1.2, linestyle="--",
            label=r"$y=\sin\theta$", zorder=2)

    # y = sin 2θ（濃色）
    ax.plot(theta, np.sin(2 * theta), color=DARK_BLUE, linewidth=2.0,
            label=r"$y=\sin 2\theta$", zorder=3)

    # 1周期目が π で終わることを示す垂直補助線
    ax.plot([np.pi, np.pi], [-0.1, 0.1], "k-", linewidth=0.8)
    ax.text(np.pi, -0.28, r"$\pi$", ha="center", va="top", fontsize=8)

    ax.legend(loc="upper right", fontsize=8, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)

    ax.text((X_LO + X_HI) / 2, y_hi + pad_y - 0.02, r"周期：$T = \pi$",
            ha="center", va="top", fontsize=11, fontweight="bold")


def draw_panel3(ax):
    """位相のずれ: y = sin θ と y = sin(θ - π/3)。"""
    y_lo, y_hi = -1.5, 1.5
    pad_y, y_hi_eff = setup_axes(ax, y_lo, y_hi)

    # y 軸目盛り ±1
    for yv, lbl in [(1, "1"), (-1, "-1")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", linewidth=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)

    theta = np.linspace(X_LO, X_HI, 1000)

    # y = sin θ（薄灰）
    ax.plot(theta, np.sin(theta), color=GRAY, linewidth=1.2, linestyle="--",
            label=r"$y=\sin\theta$", zorder=2)

    # y = sin(θ - π/3)（濃色）
    ax.plot(theta, np.sin(theta - np.pi / 3), color=DARK_BLUE, linewidth=2.0,
            label=r"$y=\sin(\theta - \frac{\pi}{3})$", zorder=3)

    # π/3 でのずれを示す破線
    ax.axvline(np.pi / 3, color="#cc2222", linewidth=1.0, linestyle="--",
               ymin=0.1, ymax=0.9, zorder=1)
    ax.text(np.pi / 3 + 0.08, 1.1, r"$\theta = \frac{\pi}{3}$",
            ha="left", va="bottom", fontsize=8, color="#cc2222")

    ax.legend(loc="upper right", fontsize=8, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)

    ax.text((X_LO + X_HI) / 2, y_hi + pad_y - 0.02, r"位相のずれ：$\frac{\pi}{3}$",
            ha="center", va="top", fontsize=11, fontweight="bold")


def draw_panel4(ax):
    """垂直移動: y = sin θ と y = sin θ + 1。"""
    y_lo, y_hi = -1.5, 2.5
    pad_y, y_hi_eff = setup_axes(ax, y_lo, y_hi)

    # y 軸目盛り -1, 0, 1, 2
    for yv, lbl in [(2, "2"), (1, "1"), (-1, "-1")]:
        ax.plot([-0.06, 0.06], [yv, yv], "k-", linewidth=0.8)
        ax.text(-0.12, yv, lbl, ha="right", va="center", fontsize=8)

    theta = np.linspace(X_LO, X_HI, 1000)

    # y = sin θ（薄灰）
    ax.plot(theta, np.sin(theta), color=GRAY, linewidth=1.2, linestyle="--",
            label=r"$y=\sin\theta$", zorder=2)

    # y = sin θ + 1（濃色）
    ax.plot(theta, np.sin(theta) + 1, color=DARK_BLUE, linewidth=2.0,
            label=r"$y=\sin\theta + 1$", zorder=3)

    # 中心線 y = 1 の補助線
    ax.axhline(1.0, color="#cc2222", linewidth=0.9, linestyle=":", zorder=1, alpha=0.8)
    ax.text(X_HI + 0.15, 1.0 + 0.06, r"中心線 $y=1$",
            ha="left", va="bottom", fontsize=8, color="#cc2222")

    ax.legend(loc="upper right", fontsize=8, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)

    ax.text((X_LO + X_HI) / 2, y_hi + pad_y - 0.02, r"垂直移動：D = 1",
            ha="center", va="top", fontsize=11, fontweight="bold")


def main() -> None:
    fig, axes = plt.subplots(1, 4, figsize=(17.5, 4.0))
    fig.patch.set_facecolor("white")

    draw_panel1(axes[0])
    draw_panel2(axes[1])
    draw_panel3(axes[2])
    draw_panel4(axes[3])

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "trig-graph-transform-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
