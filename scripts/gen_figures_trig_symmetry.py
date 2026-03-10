"""
gen_figures_trig_symmetry.py — 対称性変換公式 概念図生成

Panel 1: π−θ → y軸対称 (x座標が逆符号)
Panel 2: π+θ → 原点対称 (x, y ともに逆符号)
Panel 3: −θ  → x軸対称 (y座標が逆符号)

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_trig_symmetry.py
出力: site/figures/trig-symmetry-combined.png
      site/assets/images/trig-symmetry-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
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
FIGURES_DIR.mkdir(exist_ok=True)
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#cc6600"


def draw_unit_circle_panel(ax, theta, theta2, title, label1, label2, sym_axis):
    """単位円上の2点の対称関係を示すパネルを描く。"""
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-1.55, 1.65)

    # 単位円
    circle = plt.Circle((0, 0), 1.0, color=DARK_BLUE, fill=False, linewidth=1.5)
    ax.add_patch(circle)

    # 軸
    arrow_kw = dict(color="black", lw=0.8, mutation_scale=7, shrinkA=0, shrinkB=0)
    ax.annotate("", xy=(1.45, 0), xytext=(-1.45, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.annotate("", xy=(0, 1.5), xytext=(0, -1.45),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(1.47, 0, r"$x$", ha="left", va="center", fontsize=9)
    ax.text(0.03, 1.52, r"$y$", ha="left", va="bottom", fontsize=9)
    ax.text(-0.07, -0.07, "O", ha="right", va="top", fontsize=9)

    # 対称軸
    if sym_axis == "y":
        ax.axvline(0, color="#aaaaaa", lw=1.0, linestyle=":", zorder=1)
    elif sym_axis == "x":
        ax.axhline(0, color="#aaaaaa", lw=1.0, linestyle=":", zorder=1)
    elif sym_axis == "origin":
        pass  # 原点対称は軸なし

    # 点 P(θ)
    cx1, cy1 = np.cos(theta), np.sin(theta)
    ax.plot([0, cx1], [0, cy1], color=DARK_BLUE, lw=1.3, zorder=3)
    ax.plot(cx1, cy1, "o", color=RED, markersize=7, zorder=6)
    # ラベル位置
    lbl_r = 1.22
    angle_mid1 = theta / 2
    ax.text(lbl_r * np.cos(angle_mid1), lbl_r * np.sin(angle_mid1),
            label1, ha="center", va="center", fontsize=9, color=RED)

    # 点 P(θ₂)
    cx2, cy2 = np.cos(theta2), np.sin(theta2)
    ax.plot([0, cx2], [0, cy2], color=GREEN, lw=1.3, linestyle="--", zorder=3)
    ax.plot(cx2, cy2, "s", color=GREEN, markersize=7, zorder=6)
    # ラベル
    angle_mid2 = theta2 / 2 if theta2 > 0 else theta2
    lbl_offset_x = -0.1 if cx2 < 0 else 0.1
    lbl_offset_y = 0.1 if cy2 > 0 else -0.12
    ax.text(lbl_r * np.cos(theta2) + lbl_offset_x,
            lbl_r * np.sin(theta2) + lbl_offset_y,
            label2, ha="center", va="center", fontsize=9, color=GREEN)

    # 座標ラベル (P)
    off_x = 0.12 if cx1 > 0 else -0.12
    off_y = 0.10 if cy1 > 0 else -0.12
    ax.text(cx1 + off_x, cy1 + off_y,
            r"$(\cos\theta,\,\sin\theta)$",
            ha="center" if abs(cx1) < 0.3 else ("left" if cx1 > 0 else "right"),
            va="bottom" if cy1 > 0 else "top",
            fontsize=7.5, color=RED)

    # タイトル
    ax.text(0, 1.58, title,
            ha="center", va="bottom", fontsize=10, fontweight="bold")


def main() -> None:
    theta = np.pi / 4  # 基準角

    fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
    fig.patch.set_facecolor("white")

    # Panel 1: π−θ (y軸対称)
    draw_unit_circle_panel(
        axes[0],
        theta=theta,
        theta2=np.pi - theta,
        title=r"$\pi - \theta$：y 軸対称",
        label1=r"$\theta$",
        label2=r"$\pi-\theta$",
        sym_axis="y",
    )
    # 符号変化ラベル
    axes[0].text(0, -1.45,
                 r"$\sin(\pi-\theta)=+\sin\theta$" + "\n" + r"$\cos(\pi-\theta)=-\cos\theta$",
                 ha="center", va="top", fontsize=8.5, color="#333333")

    # Panel 2: π+θ (原点対称)
    draw_unit_circle_panel(
        axes[1],
        theta=theta,
        theta2=np.pi + theta,
        title=r"$\pi + \theta$：原点対称",
        label1=r"$\theta$",
        label2=r"$\pi+\theta$",
        sym_axis="origin",
    )
    axes[1].text(0, -1.45,
                 r"$\sin(\pi+\theta)=-\sin\theta$" + "\n" + r"$\cos(\pi+\theta)=-\cos\theta$",
                 ha="center", va="top", fontsize=8.5, color="#333333")

    # Panel 3: −θ (x軸対称)
    draw_unit_circle_panel(
        axes[2],
        theta=theta,
        theta2=-theta,
        title=r"$-\theta$：x 軸対称",
        label1=r"$\theta$",
        label2=r"$-\theta$",
        sym_axis="x",
    )
    axes[2].text(0, -1.45,
                 r"$\sin(-\theta)=-\sin\theta$" + "\n" + r"$\cos(-\theta)=+\cos\theta$",
                 ha="center", va="top", fontsize=8.5, color="#333333")

    fig.tight_layout(pad=0.4, w_pad=0.8)

    fname = "trig-symmetry-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
