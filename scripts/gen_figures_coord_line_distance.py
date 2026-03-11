"""
gen_figures_coord_line_distance.py — 点と直線の距離

Panel 1: 点 P から直線 l への距離
Panel 2: 距離公式の構造

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_line_distance.py
出力: site/figures/coord-line-distance-combined.png
      site/assets/images/coord-line-distance-combined.png
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


def draw_point_line_distance(ax):
    """Panel 1: 点 P から直線 l への距離"""
    ax.set_xlim(-1.5, 4.5)
    ax.set_ylim(-1.0, 5.5)
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(4.3, 0), xytext=(-1.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(4.35, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 5.3), xytext=(0, -0.8),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.08, 5.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.15, -0.18, "O", ha="right", va="top", fontsize=9)

    # 直線 3x - 4y + 5 = 0  ⟺  y = (3x+5)/4
    x_line = np.linspace(-1.0, 4.0, 300)
    y_line = (3 * x_line + 5) / 4
    ax.plot(x_line, y_line, color=DARK_BLUE, linewidth=2.0, zorder=3)
    ax.text(3.7, 3.55, r"$\ell$", ha="left", va="bottom",
            fontsize=11, color=DARK_BLUE)
    ax.text(-1.0, 0.7, r"$3x-4y+5=0$", ha="left", va="center",
            fontsize=8.5, color=DARK_BLUE)

    # 点 P = (1, 4)
    Px, Py = 1.0, 4.0
    ax.plot(Px, Py, "o", color=RED, markersize=8, zorder=5)
    ax.text(Px + 0.12, Py + 0.15, r"$P(1,\ 4)$", ha="left", va="bottom",
            fontsize=9.5, color=RED)

    # 垂線の足 H の計算
    # 直線 3x-4y+5=0, 法線方向 n=(3,-4)
    # H = P - [(3*1 - 4*4 + 5)/25] * (3,-4)
    #   = (1,4) - [(-8)/25]*(3,-4)
    #   = (1,4) - (-24/25, 32/25)
    #   = (1 + 24/25, 4 - 32/25) = (49/25, 68/25)
    Hx = 49 / 25
    Hy = 68 / 25

    ax.plot(Hx, Hy, "s", color=GREEN, markersize=7, zorder=5)
    ax.text(Hx + 0.12, Hy - 0.25, r"$H$", ha="left", va="top",
            fontsize=9, color=GREEN)

    # 垂線 PH（GREEN dashed）
    ax.plot([Px, Hx], [Py, Hy], color=GREEN, linewidth=1.8,
            linestyle="--", zorder=4)

    # 直角マーク（小さい正方形）
    # PH 方向: (Hx-Px, Hy-Py) = (24/25, -32/25)
    ph = np.array([Hx - Px, Hy - Py])
    ph_norm = ph / np.linalg.norm(ph)
    # 直線方向 (4, 3)/5
    ld = np.array([4, 3]) / 5
    sq_s = 0.18
    corner = np.array([Hx, Hy])
    sq_pts = np.array([
        corner,
        corner + sq_s * ph_norm,
        corner + sq_s * ph_norm + sq_s * ld,
        corner + sq_s * ld,
        corner
    ])
    ax.plot(sq_pts[:, 0], sq_pts[:, 1], color=GREEN, linewidth=1.2, zorder=5)

    # 距離の注釈
    mx, my = (Px + Hx) / 2, (Py + Hy) / 2
    ax.text(mx + 0.1, my + 0.3,
            r"$d = \dfrac{|3\cdot1-4\cdot4+5|}{\sqrt{3^2+4^2}} = \dfrac{8}{5}$",
            ha="left", va="bottom", fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=1.0))

    ax.set_title("点 $P$ から直線 $\\ell$ への距離", fontsize=10, pad=4)


def draw_formula_structure(ax):
    """Panel 2: 距離公式の構造"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # 中央に公式を大きく表示
    ax.text(5.0, 6.5,
            r"$d = \dfrac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$",
            ha="center", va="center", fontsize=16, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=2.0))

    # 各部位の説明
    label_style = dict(fontsize=9.5, va="center",
                       bbox=dict(boxstyle="round,pad=0.3",
                                 facecolor="#fffbe6",
                                 edgecolor=ORANGE, linewidth=1.0))

    # 分子の説明
    ax.annotate("直線 $ax+by+c=0$ に\n点 $(x_0,y_0)$ を代入\nした値の絶対値",
                xy=(4.85, 7.05), xytext=(1.2, 7.5),
                ha="center", va="center", fontsize=9,
                bbox=dict(boxstyle="round,pad=0.35", facecolor="#fffbe6",
                          edgecolor=ORANGE, linewidth=1.0),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.2,
                                mutation_scale=8, shrinkA=4, shrinkB=4))

    # 分母の説明
    ax.annotate("直線の法線ベクトル\n$(a, b)$ の大きさ",
                xy=(5.5, 5.9), xytext=(8.5, 5.2),
                ha="center", va="center", fontsize=9,
                bbox=dict(boxstyle="round,pad=0.35", facecolor="#f0fff4",
                          edgecolor=GREEN, linewidth=1.0),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.2,
                                mutation_scale=8, shrinkA=4, shrinkB=4))

    # 条件の説明
    ax.text(5.0, 4.5,
            "直線: $ax + by + c = 0$\n点:   $P(x_0, y_0)$",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#f8f8f8",
                      edgecolor=GRAY, linewidth=1.2))

    # 具体例
    ax.text(5.0, 2.8,
            "具体例: 直線 $3x-4y+5=0$, 点 $P(1,4)$",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE)
    ax.text(5.0, 2.0,
            r"$d = \dfrac{|3\cdot1-4\cdot4+5|}{\sqrt{9+16}} = \dfrac{|-8|}{5} = \dfrac{8}{5}$",
            ha="center", va="center", fontsize=11, color=RED,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=1.2))

    # 注意事項
    ax.text(5.0, 0.8,
            "※ $a=b=0$ のとき直線は存在しない（除外）",
            ha="center", va="center", fontsize=8.5, color=GRAY)

    ax.set_title("距離公式の構造", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_point_line_distance(axes[0])
    draw_formula_structure(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-line-distance-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
