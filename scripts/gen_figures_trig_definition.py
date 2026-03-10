"""
gen_figures_trig_definition.py — 単位円と三角関数の定義 概念図生成

単位円 x²+y²=1 上の点 P と cos/sin の関係、代表角の位置を示す。

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_definition.py
出力: site/figures/trig-unit-circle.png
      site/assets/images/trig-unit-circle.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.patches as mpatches
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


def main() -> None:
    fig, ax = plt.subplots(1, 1, figsize=(5.5, 5.5))
    fig.patch.set_facecolor("white")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.65, 1.85)
    ax.set_ylim(-1.55, 1.75)

    # 単位円
    circle = plt.Circle((0, 0), 1.0, color=DARK_BLUE, fill=False, linewidth=1.8)
    ax.add_patch(circle)

    # 軸
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(1.6, 0), xytext=(-1.55, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(1.63, 0, r"$x$", ha="left", va="center", fontsize=11)
    ax.annotate("", xy=(0, 1.65), xytext=(0, -1.5),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.04, 1.68, r"$y$", ha="left", va="bottom", fontsize=11)
    ax.text(-0.08, -0.07, "O", ha="right", va="top", fontsize=10)

    # 主要な角度: π/6, π/3, 2π/3, π の点
    angles_info = [
        (np.pi / 6,  r"$\frac{\pi}{6}$",   r"$\left(\frac{\sqrt{3}}{2},\,\frac{1}{2}\right)$",   "right"),
        (np.pi / 4,  r"$\frac{\pi}{4}$",   r"$\left(\frac{\sqrt{2}}{2},\,\frac{\sqrt{2}}{2}\right)$", "right"),
        (np.pi / 3,  r"$\frac{\pi}{3}$",   r"$\left(\frac{1}{2},\,\frac{\sqrt{3}}{2}\right)$",   "right"),
    ]

    for angle, ang_label, coord_label, ha in angles_info:
        cx, cy = np.cos(angle), np.sin(angle)
        ax.plot(cx, cy, "o", color=DARK_BLUE, markersize=5, zorder=5)
        r_lbl = 0.58
        ax.text(r_lbl * np.cos(angle), r_lbl * np.sin(angle),
                ang_label, ha="center", va="center", fontsize=8, color=DARK_BLUE)

    # 代表点: θ = π/3
    theta_demo = np.pi / 3
    cx, cy = np.cos(theta_demo), np.sin(theta_demo)

    # 半径
    ax.plot([0, cx], [0, cy], color=DARK_BLUE, linewidth=1.5, zorder=3)
    # 点 P
    ax.plot(cx, cy, "o", color=RED, markersize=8, zorder=6)
    ax.text(cx + 0.06, cy + 0.06, r"$\mathrm{P}(\cos\theta,\,\sin\theta)$",
            ha="left", va="bottom", fontsize=9, color=RED)

    # 垂線 (dashed)
    ax.plot([cx, cx], [0, cy], "--", color=GREEN, linewidth=1.2, zorder=2)
    ax.plot([0, cx], [cy, cy], "--", color="#bb6600", linewidth=1.2, zorder=2)

    # ラベル: cosθ, sinθ
    ax.text(cx / 2, -0.12, r"$\cos\theta$",
            ha="center", va="top", fontsize=10, color=GREEN)
    ax.text(cx + 0.08, cy / 2, r"$\sin\theta$",
            ha="left", va="center", fontsize=10, color="#bb6600")

    # 角度弧
    arc = mpatches.Arc((0, 0), 0.38, 0.38, angle=0,
                        theta1=0, theta2=np.degrees(theta_demo),
                        color=RED, linewidth=1.2)
    ax.add_patch(arc)
    ax.text(0.24, 0.08, r"$\theta$", ha="left", va="bottom", fontsize=10, color=RED)

    # タイトル
    ax.text(0, -1.45, "単位円：半径 = 1 なので P の座標がそのまま (cosθ, sinθ)",
            ha="center", va="top", fontsize=8.5, color="gray",
            style="italic")

    fig.tight_layout(pad=0.3)

    fname = "trig-unit-circle.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
