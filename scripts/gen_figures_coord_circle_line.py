"""
gen_figures_coord_circle_line.py — 円と直線の位置関係

Panel 1: 3ケース: d と r の比較
Panel 2: 弦の長さ = 2√(r²-d²)

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_circle_line.py
出力: site/figures/coord-circle-line-combined.png
      site/assets/images/coord-circle-line-combined.png
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


def draw_three_cases(ax):
    """Panel 1: 3ケース: d と r の比較"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    theta = np.linspace(0, 2 * np.pi, 300)
    r = 1.2
    centers_x = [1.5, 5.0, 8.5]
    cy = 4.2

    # ── ケース 1: d > r (交差なし) ──
    cx1 = centers_x[0]
    ax.plot(cx1 + r * np.cos(theta), cy + r * np.sin(theta),
            color=DARK_BLUE, linewidth=1.8)
    ax.plot([cx1 - 1.5, cx1 + 1.5], [cy + 2.0, cy + 2.0],
            color=RED, linewidth=1.8)
    # d の距離線
    ax.annotate("", xy=(cx1, cy + 2.0), xytext=(cx1, cy),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.2,
                                mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(cx1 + 0.12, cy + 1.0, r"$d$", ha="left", va="center",
            fontsize=9, color=ORANGE)
    ax.text(cx1, cy - 1.6, "$d > r$\n共有点なし",
            ha="center", va="top", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.8))

    # ── ケース 2: d = r (接する) ──
    cx2 = centers_x[1]
    ax.plot(cx2 + r * np.cos(theta), cy + r * np.sin(theta),
            color=DARK_BLUE, linewidth=1.8)
    ax.plot([cx2 - 1.5, cx2 + 1.5], [cy + r, cy + r],
            color=RED, linewidth=1.8)
    ax.plot(cx2, cy + r, "o", color=GREEN, markersize=7, zorder=5)
    ax.annotate("", xy=(cx2, cy + r), xytext=(cx2, cy),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.2,
                                mutation_scale=7, shrinkA=0, shrinkB=4))
    ax.text(cx2 + 0.12, cy + r / 2, r"$d=r$", ha="left", va="center",
            fontsize=9, color=ORANGE)
    ax.text(cx2, cy - 1.6, "$d = r$\n接する（1点）",
            ha="center", va="top", fontsize=9, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=0.8))

    # ── ケース 3: d < r (2点で交わる) ──
    cx3 = centers_x[2]
    ax.plot(cx3 + r * np.cos(theta), cy + r * np.sin(theta),
            color=DARK_BLUE, linewidth=1.8)
    line_y = cy + r * 0.4
    ax.plot([cx3 - 1.5, cx3 + 1.5], [line_y, line_y],
            color=RED, linewidth=1.8)
    # 交点を計算: x = ±√(r²-(line_y-cy)²) + cx3
    dy_val = line_y - cy
    dx_int = np.sqrt(r ** 2 - dy_val ** 2)
    ax.plot(cx3 - dx_int, line_y, "o", color=GREEN, markersize=6, zorder=5)
    ax.plot(cx3 + dx_int, line_y, "o", color=GREEN, markersize=6, zorder=5)
    ax.annotate("", xy=(cx3, line_y), xytext=(cx3, cy),
                arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.2,
                                mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(cx3 + 0.12, (line_y + cy) / 2, r"$d$", ha="left", va="center",
            fontsize=9, color=ORANGE)
    ax.text(cx3, cy - 1.6, "$d < r$\n2点で交わる",
            ha="center", va="top", fontsize=9, color=RED,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=0.8))

    # タイトル的な説明
    ax.text(5.0, 6.7,
            "判別条件: $d$ と $r$ の大小関係",
            ha="center", va="top", fontsize=10, color=DARK_BLUE)

    ax.set_title("3ケース: $d$ と $r$ の比較", fontsize=10, pad=4)


def draw_chord_length(ax):
    """Panel 2: 弦の長さ = 2√(r²-d²)"""
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-6.5, 6.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(6.2, 0), xytext=(-6.2, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(6.25, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 6.2), xytext=(0, -6.2),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, 6.25, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.25, "O", ha="right", va="top", fontsize=9.5)

    # 円: 中心O=(0,0), r=5
    r = 5.0
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(r * np.cos(theta), r * np.sin(theta),
            color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 弦: y = 3（d=3）
    d = 3.0
    half_chord = np.sqrt(r ** 2 - d ** 2)  # = 4
    Ax, Ay = -half_chord, d
    Bx, By = half_chord, d

    # 弦を描画
    ax.plot([Ax, Bx], [Ay, By], color=RED, linewidth=2.2, zorder=4)

    # 弦の端点
    ax.plot(Ax, Ay, "o", color=RED, markersize=6, zorder=5)
    ax.plot(Bx, By, "o", color=RED, markersize=6, zorder=5)

    # 中心から弦への垂線
    ax.plot([0, 0], [0, d], color=GREEN, linewidth=1.8,
            linestyle="--", zorder=4)

    # 直角マーク
    sq_s = 0.22
    sq_pts = np.array([[0, d], [sq_s, d], [sq_s, d - sq_s], [0, d - sq_s], [0, d]])
    ax.plot(sq_pts[:, 0], sq_pts[:, 1], color=GREEN, linewidth=1.2, zorder=5)

    # 半弦の長さ表示
    ax.annotate("", xy=(Bx, By), xytext=(0, d),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.2,
                                mutation_scale=7, shrinkA=0, shrinkB=0))
    ax.text(half_chord / 2, d + 0.4,
            r"$\sqrt{r^2-d^2}=4$",
            ha="center", va="bottom", fontsize=9, color=RED)

    # d の表示
    ax.text(-0.5, d / 2, r"$d=3$", ha="right", va="center",
            fontsize=9.5, color=GREEN)

    # 半径の表示
    angle_r = np.arctan2(d, half_chord)
    ax.annotate("", xy=(Bx, By), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=1.2,
                                linestyle="dashed", mutation_scale=7,
                                shrinkA=0, shrinkB=0))
    ax.text(Bx / 2 + 0.3, By / 2 - 0.5, r"$r=5$",
            ha="left", va="top", fontsize=9, color=GRAY)

    # 公式ラベル
    ax.text(0.0, -4.5,
            r"弦の長さ $= 2\sqrt{r^2-d^2} = 2\times4 = 8$",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.3))

    ax.set_title(r"弦の長さ $= 2\sqrt{r^2-d^2}$", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_three_cases(axes[0])
    draw_chord_length(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-circle-line-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
