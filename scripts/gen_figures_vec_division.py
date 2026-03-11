"""
gen_figures_vec_division.py — 内分・外分

Panel 1: 内分点の比による位置（m:n で「引き寄せられる」図）
Panel 2: 外分点の位置図

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_vec_division.py
出力: figures/vec-division-combined.png
      assets/images/vec-division-combined.png
"""

import platform
import shutil
from pathlib import Path

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
SITE_IMAGES_DIR.mkdir(exist_ok=True)
DPI = 150

DARK_BLUE = "#1a3a6b"
RED = "#cc2222"
GREEN = "#1a6b3a"
ORANGE = "#bb6600"


def draw_vector(ax, tail, tip, color, lw=2.0, mutation_scale=20):
    ax.annotate("", xy=tip, xytext=tail,
                arrowprops=dict(arrowstyle="-|>", mutation_scale=mutation_scale,
                                lw=lw, color=color))


def draw_internal_division(ax):
    """Panel 1: 内分点 P（m:n で A と B を内分）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title("内分点の位置ベクトル", fontsize=10, pad=4)

    O = np.array([1.0, 1.5])
    A = np.array([2.5, 5.5])
    B = np.array([9.0, 3.5])

    # m:n = 2:1
    m, n = 2, 1
    P = (n * A + m * B) / (m + n)  # 内分点の公式

    # OA, OB
    draw_vector(ax, O, A, DARK_BLUE, lw=1.8, mutation_scale=18)
    ax.text((O[0]+A[0])/2-0.2, (O[1]+A[1])/2+0.05,
            r"$\vec{a}$", ha="right", va="center",
            fontsize=11, color=DARK_BLUE)

    draw_vector(ax, O, B, RED, lw=1.8, mutation_scale=18)
    ax.text((O[0]+B[0])/2, (O[1]+B[1])/2-0.35,
            r"$\vec{b}$", ha="center", va="top",
            fontsize=11, color=RED)

    # OP (内分点)
    draw_vector(ax, O, P, GREEN, lw=2.5, mutation_scale=22)
    ax.text((O[0]+P[0])/2+0.15, (O[1]+P[1])/2+0.2,
            r"$\vec{p}$", ha="left", va="bottom",
            fontsize=11, color=GREEN)

    # AB の線分
    ax.plot([A[0], B[0]], [A[1], B[1]], color="#aaaaaa", lw=1.2, linestyle="--")

    # P の位置とm:n の表示
    ax.scatter([A[0]], [A[1]], s=40, color=DARK_BLUE, zorder=5)
    ax.scatter([B[0]], [B[1]], s=40, color=RED, zorder=5)
    ax.scatter([P[0]], [P[1]], s=50, color=GREEN, zorder=6)

    for pt, lbl, off in [(O, "O", (-0.2, -0.2)), (A, "A", (-0.2, 0.2)),
                          (B, "B", (0.2, 0.1)), (P, "P", (0.0, 0.25))]:
        ax.text(pt[0]+off[0], pt[1]+off[1], lbl,
                ha="center", va="center", fontsize=11,
                color="#333333", fontweight="bold")

    # m:n の表示
    AP = P - A
    PB = B - P
    ax.text((A[0]+P[0])/2, (A[1]+P[1])/2 + 0.3, f"{m}",
            ha="center", va="bottom", fontsize=11, color=GREEN, fontweight="bold")
    ax.text((P[0]+B[0])/2, (P[1]+B[1])/2 + 0.3, f"{n}",
            ha="center", va="bottom", fontsize=11, color=GREEN, fontweight="bold")
    ax.text((A[0]+P[0]+P[0]+B[0])/4, (A[1]+P[1]+P[1]+B[1])/4 + 0.55,
            f"{m} : {n}", ha="center", va="bottom", fontsize=10, color=GREEN)

    ax.text(5.0, 0.5,
            r"$\vec{p} = \dfrac{n\vec{a}+m\vec{b}}{m+n}$" +
            f"（{m}:{n} の内分）",
            ha="center", va="center", fontsize=10, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))


def draw_external_division(ax):
    """Panel 2: 外分点 Q（m:n で A と B を外分）"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.set_title("外分点の位置ベクトル", fontsize=10, pad=4)

    O = np.array([1.0, 2.5])
    A = np.array([3.5, 5.0])
    B = np.array([6.5, 4.0])

    # m:n = 3:1 の外分
    m, n = 3, 1
    Q = (m * B - n * A) / (m - n)  # 外分点の公式（m≠n）

    # OA, OB
    draw_vector(ax, O, A, DARK_BLUE, lw=1.8, mutation_scale=18)
    ax.text((O[0]+A[0])/2-0.2, (O[1]+A[1])/2+0.1,
            r"$\vec{a}$", ha="right", va="bottom",
            fontsize=11, color=DARK_BLUE)

    draw_vector(ax, O, B, RED, lw=1.8, mutation_scale=18)
    ax.text((O[0]+B[0])/2+0.1, (O[1]+B[1])/2+0.1,
            r"$\vec{b}$", ha="left", va="bottom",
            fontsize=11, color=RED)

    # OQ (外分点)
    draw_vector(ax, O, Q, ORANGE, lw=2.5, mutation_scale=22)
    ax.text((O[0]+Q[0])/2, (O[1]+Q[1])/2-0.35,
            r"$\vec{q}$", ha="center", va="top",
            fontsize=11, color=ORANGE)

    # AB の延長線（外分点側）
    ax.plot([A[0], Q[0]+0.5], [A[1], Q[1]+0.1*(Q[1]-A[1])/(Q[0]-A[0]+0.001)],
            color="#aaaaaa", lw=1.0, linestyle="--")

    for pt, lbl, off in [(O, "O", (-0.2, -0.2)), (A, "A", (-0.2, 0.2)),
                          (B, "B", (0.0, 0.25)), (Q, "Q", (0.2, 0.1))]:
        ax.scatter([pt[0]], [pt[1]], s=40, color="#333333", zorder=5)
        ax.text(pt[0]+off[0], pt[1]+off[1], lbl,
                ha="center", va="center", fontsize=11,
                color="#333333", fontweight="bold")

    ax.text(5.0, 1.0,
            r"$\vec{q} = \dfrac{m\vec{b}-n\vec{a}}{m-n}$（$m \neq n$）" + "\n"
            f"（{m}:{n} の外分）",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.9))

    # 符号の説明
    ax.text(5.0, 6.3,
            "外分: 公式の分子の符号が内分と逆になる\n"
            "（Q は AB の延長上、A と B の外側にある）",
            ha="center", va="center", fontsize=8.5, color="#666666")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_internal_division(axes[0])
    draw_external_division(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "vec-division-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
