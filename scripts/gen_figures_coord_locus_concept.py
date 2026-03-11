"""
gen_figures_coord_locus_concept.py — 軌跡の概念

Panel 1: 動点 P の軌跡
Panel 2: 除外点が生じる場合

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_locus_concept.py
出力: site/figures/coord-locus-concept-combined.png
      site/assets/images/coord-locus-concept-combined.png
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
SITE_IMAGES_DIR.mkdir(exist_ok=True)
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#bb6600"
GRAY = "#888888"
arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)


def draw_locus_concept(ax):
    """Panel 1: 動点 P の軌跡（PA=PB の垂直二等分線）"""
    ax.set_xlim(-4.0, 4.0)
    ax.set_ylim(-4.0, 4.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(3.8, 0), xytext=(-3.8, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(3.85, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 4.3), xytext=(0, -3.8),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, 4.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)

    # 固定点 A=(-2, 0), B=(2, 0)
    Ax, Ay = -2.0, 0.0
    Bx, By = 2.0, 0.0
    ax.plot(Ax, Ay, "s", color=DARK_BLUE, markersize=9, zorder=5)
    ax.plot(Bx, By, "s", color=DARK_BLUE, markersize=9, zorder=5)
    ax.text(Ax - 0.1, Ay - 0.35, r"$A(-2,0)$", ha="center", va="top",
            fontsize=9, color=DARK_BLUE)
    ax.text(Bx + 0.1, By - 0.35, r"$B(2,0)$", ha="center", va="top",
            fontsize=9, color=DARK_BLUE)

    # PA=PB を満たす点 P の例（x=0 上の5点）
    p_y_vals = [-3.0, -1.5, 0.5, 1.5, 3.0]
    for py in p_y_vals:
        px = 0.0
        ax.plot(px, py, "o", color=RED, markersize=6, zorder=4, alpha=0.8)
        # PA, PB を示す破線
        pa = np.sqrt((px - Ax) ** 2 + (py - Ay) ** 2)
        pb = np.sqrt((px - Bx) ** 2 + (py - By) ** 2)
        ax.plot([px, Ax], [py, Ay], color=GRAY, linewidth=0.9,
                linestyle=":", zorder=3, alpha=0.7)
        ax.plot([px, Bx], [py, By], color=GRAY, linewidth=0.9,
                linestyle=":", zorder=3, alpha=0.7)

    # 軌跡: x=0 （垂直二等分線）
    ax.plot([0, 0], [-3.8, 4.0], color=DARK_BLUE, linewidth=2.2,
            linestyle="--", zorder=4, label="軌跡")

    # 「P が動く」矢印
    ax.annotate("", xy=(0, 2.8), xytext=(0, 0.9),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.3,
                                mutation_scale=9, shrinkA=0, shrinkB=0))

    # 軌跡ラベル
    ax.text(0.25, 3.5, "軌跡: $x=0$\n（垂直二等分線）",
            ha="left", va="center", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))

    # 条件ラベル
    ax.text(-3.8, 4.2,
            "条件: $PA = PB$",
            ha="left", va="top", fontsize=9.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.9))

    ax.set_title("動点 $P$ の軌跡", fontsize=10, pad=4)


def draw_excluded_point(ax):
    """Panel 2: 除外点が生じる場合"""
    ax.set_xlim(-1.5, 4.5)
    ax.set_ylim(-3.5, 3.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(4.3, 0), xytext=(-1.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(4.35, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 3.3), xytext=(0, -3.3),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, 3.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)

    # 固定点 A=(0,0), B=(2,0)
    Ax, Ay = 0.0, 0.0
    Bx, By = 2.0, 0.0
    ax.plot(Ax, Ay, "s", color=DARK_BLUE, markersize=8, zorder=5)
    ax.plot(Bx, By, "s", color=DARK_BLUE, markersize=8, zorder=5)
    ax.text(Ax - 0.1, Ay - 0.35, r"$A(0,0)$", ha="center", va="top",
            fontsize=8.5, color=DARK_BLUE)
    ax.text(Bx + 0.1, By - 0.35, r"$B(2,0)$", ha="center", va="top",
            fontsize=8.5, color=DARK_BLUE)

    # 軌跡 x=1（PA=PB の垂直二等分線、ただし A,B 間の中点は x=1）
    # 実際は PA/PB=1 → PA=PB → 垂直二等分線 x=1
    # 除外点: P が A または B と一致するとき（距離 = 0 になるが AB の中点は常に x=1 上）
    # ここでは直観的に「除外点がある軌跡」として y=0 上の x=1 は条件を満たすが
    # 「P=A または P=B は除外」という例を示す

    # 軌跡 x=1 の線（ただし1点を除く）
    ax.plot([1, 1], [-3.0, -0.22], color=DARK_BLUE, linewidth=2.2,
            linestyle="--", zorder=4)
    ax.plot([1, 1], [0.22, 3.0], color=DARK_BLUE, linewidth=2.2,
            linestyle="--", zorder=4)

    # 除外点 (1, 0) を open circle で表示
    circle_ex = plt.Circle((1.0, 0.0), 0.18, color=DARK_BLUE, fill=False,
                            linewidth=2.0, zorder=5)
    ax.add_patch(circle_ex)

    # 除外点のラベル
    ax.text(1.3, 0.0, "除外点 $(1,0)$",
            ha="left", va="center", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.9))

    # 条件の説明
    ax.text(-1.2, 3.0,
            "条件: $\\frac{PA}{PB}=1$\n$\\Rightarrow PA=PB$\n軌跡: $x=1$",
            ha="left", va="top", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))

    # 除外の理由
    ax.text(-1.2, -1.5,
            "除外点の理由:\n$P$ が $A$ に一致すると\n$PA=0$（距離が未定義）",
            ha="left", va="top", fontsize=8.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.9))

    ax.set_title("除外点が生じる場合", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_locus_concept(axes[0])
    draw_excluded_point(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-locus-concept-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
