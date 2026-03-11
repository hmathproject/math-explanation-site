"""
gen_figures_coord_circle_tangent.py — 円の接線

Panel 1: 接点 T での接線: OT⊥接線
Panel 2: 外点 P からの2本の接線

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_circle_tangent.py
出力: site/figures/coord-circle-tangent-combined.png
      site/assets/images/coord-circle-tangent-combined.png
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


def draw_tangent_at_point(ax):
    """Panel 1: 接点 T での接線: OT⊥接線"""
    ax.set_xlim(-4.2, 4.8)
    ax.set_ylim(-4.2, 4.2)
    ax.set_aspect("equal")
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(4.5, 0), xytext=(-4.0, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(4.55, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 4.0), xytext=(0, -4.0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, 4.05, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)

    # 円: 中心O=(0,0), r=3
    r = 3.0
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(r * np.cos(theta), r * np.sin(theta),
            color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 接点 T = (3, 0)
    Tx, Ty = 3.0, 0.0
    ax.plot(Tx, Ty, "o", color=RED, markersize=8, zorder=5)
    ax.text(Tx + 0.15, Ty + 0.25, r"$T(3,\ 0)$", ha="left", va="bottom",
            fontsize=9.5, color=RED)

    # 接線 x = 3（垂直線）
    ax.plot([3, 3], [-3.8, 3.8], color=RED, linewidth=2.2, zorder=4)
    ax.text(3.15, 3.5, "接線 $x=3$", ha="left", va="center",
            fontsize=9, color=RED)

    # 半径 OT の矢印
    ax.annotate("", xy=(Tx - 0.08, Ty), xytext=(0.08, 0),
                arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.8,
                                mutation_scale=10, shrinkA=0, shrinkB=0))
    ax.text(1.5, 0.25, r"$OT$", ha="center", va="bottom",
            fontsize=9, color=GREEN)

    # 直角マーク
    sq_s = 0.25
    sq_pts = np.array([[Tx, 0], [Tx, sq_s], [Tx - sq_s, sq_s], [Tx - sq_s, 0], [Tx, 0]])
    ax.plot(sq_pts[:, 0], sq_pts[:, 1], color=GREEN, linewidth=1.4, zorder=6)

    # 注釈
    ax.text(-3.8, -3.0,
            "$OT \\perp$ 接線\n$\\Rightarrow$ OT は法線",
            ha="left", va="center", fontsize=9.5, color=GREEN,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#f0fff4",
                      edgecolor=GREEN, linewidth=1.2))

    # 方程式の導出
    ax.text(-3.8, 3.5,
            r"$x\cdot3 + y\cdot0 = 9$" + "\n" + r"$\Rightarrow x = 3$",
            ha="left", va="top", fontsize=9, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=1.0))

    ax.set_title("接点 $T$ での接線: $OT \\perp$ 接線", fontsize=10, pad=4)


def draw_tangent_from_external(ax):
    """Panel 2: 外点 P からの2本の接線"""
    ax.set_xlim(-3.5, 5.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # 座標軸
    ax.annotate("", xy=(5.2, 0), xytext=(-3.3, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(5.25, 0, r"$x$", ha="left", va="center", fontsize=10)
    ax.annotate("", xy=(0, 3.3), xytext=(0, -3.3),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, 3.35, r"$y$", ha="left", va="bottom", fontsize=10)
    ax.text(-0.2, -0.2, "O", ha="right", va="top", fontsize=9.5)

    # 円: 中心O=(0,0), r=2
    r = 2.0
    theta_all = np.linspace(0, 2 * np.pi, 400)
    ax.plot(r * np.cos(theta_all), r * np.sin(theta_all),
            color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 外点 P = (4, 0)
    Px, Py = 4.0, 0.0
    ax.plot(Px, Py, "o", color=ORANGE, markersize=8, zorder=5)
    ax.text(Px + 0.15, Py + 0.15, r"$P(4,\ 0)$", ha="left", va="bottom",
            fontsize=9.5, color=ORANGE)

    # 接点の計算
    # |OP| = 4, r = 2
    # 接点の角度 θ: cos θ = r/|OP| ではなく
    # 接点は円上の点 (2cosφ, 2sinφ) s.t. OP·OT = r²
    # 4·2cosφ + 0·2sinφ = 4 → cosφ = 1/2 → φ = ±60°
    phi1 = np.pi / 3   # 60°
    phi2 = -np.pi / 3  # -60°
    T1x, T1y = r * np.cos(phi1), r * np.sin(phi1)
    T2x, T2y = r * np.cos(phi2), r * np.sin(phi2)

    # 接点マーク
    ax.plot(T1x, T1y, "o", color=RED, markersize=7, zorder=5)
    ax.plot(T2x, T2y, "o", color=RED, markersize=7, zorder=5)
    ax.text(T1x - 0.15, T1y + 0.25, r"$T_1$", ha="right", va="bottom",
            fontsize=9.5, color=RED)
    ax.text(T2x - 0.15, T2y - 0.25, r"$T_2$", ha="right", va="top",
            fontsize=9.5, color=RED)

    # 接線 PT1, PT2
    ax.plot([Px, T1x], [Py, T1y], color=RED, linewidth=1.8, zorder=4)
    ax.plot([Px, T2x], [Py, T2y], color=RED, linewidth=1.8, zorder=4)

    # 接線長 PT1 = PT2 の表示
    m1x, m1y = (Px + T1x) / 2, (Py + T1y) / 2
    m2x, m2y = (Px + T2x) / 2, (Py + T2y) / 2
    pt_len = np.sqrt((Px - T1x) ** 2 + (Py - T1y) ** 2)
    ax.text(m1x + 0.2, m1y + 0.1, f"$PT_1={pt_len:.2f}$",
            ha="left", va="center", fontsize=8.5, color=RED)
    ax.text(m2x + 0.2, m2y - 0.1, f"$PT_2={pt_len:.2f}$",
            ha="left", va="center", fontsize=8.5, color=RED)

    # OT1 の半径（直角確認）
    ax.plot([0, T1x], [0, T1y], color=GRAY, linewidth=1.2,
            linestyle="--", zorder=3)
    ax.plot([0, T2x], [0, T2y], color=GRAY, linewidth=1.2,
            linestyle="--", zorder=3)

    # 等長注釈
    ax.text(-3.0, -2.8,
            "$PT_1 = PT_2$\n（外点からの接線長は等しい）",
            ha="left", va="bottom", fontsize=9, color=ORANGE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fffbe6",
                      edgecolor=ORANGE, linewidth=1.1))

    ax.set_title("外点 $P$ からの2本の接線", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_tangent_at_point(axes[0])
    draw_tangent_from_external(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-circle-tangent-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
