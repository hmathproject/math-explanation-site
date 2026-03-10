"""
gen_figures_exp_equation.py — 指数不等式 図生成

左パネル: a > 1 — y=2^x、2^x > 8（x > 3）の解の範囲
右パネル: 0 < a < 1 — y=(1/2)^x、(1/2)^x ≤ (1/2)^2（x ≥ 2）の解の範囲
         単調減少のため不等号の向きが逆になることを可視化する

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_exp_equation.py
出力: site/figures/exp-function-equation.png
      site/assets/images/exp-function-equation.png
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

# ── 共通設定 ──────────────────────────────────────────────────
X_LO, X_HI = -2.5, 3.5
Y_LO, Y_HI = -0.3, 9.5


def draw_axes(ax):
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.set_xlim(X_LO - 0.4, X_HI + 0.8)
    ax.set_ylim(Y_LO, Y_HI + 0.9)
    ax.axis("off")

    # x 軸
    ax.annotate("", xy=(X_HI + 0.7, 0), xytext=(X_LO - 0.35, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.74, 0.0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.6), xytext=(0, Y_LO - 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, Y_HI + 0.62, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点
    ax.text(-0.18, -0.18, "O", ha="right", va="top", fontsize=9)

    # 漸近線 y=0
    ax.axhline(0, color="#aaaaaa", lw=0.7, ls="--", zorder=0)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")

    x = np.linspace(X_LO, X_HI, 600)

    # ── 左パネル: a > 1（y = 2^x、2^x > 8 ⟺ x > 3） ─────────────
    ax = axes[0]
    draw_axes(ax)

    # y = 2^x
    y = 2.0 ** x
    mask = y <= Y_HI + 0.5
    ax.plot(x[mask], y[mask], color="#1a1a1a", lw=1.8, zorder=2,
            label=r"$y = 2^x$")

    # 水平線 y=8（=2^3）
    ax.axhline(8, color="#cc4444", lw=1.0, ls="--", zorder=1)
    ax.text(X_HI + 0.55, 8.15, r"$y = 8$", ha="left", va="bottom",
            fontsize=9, color="#cc4444")

    # x=3 目盛り
    ax.plot([3, 3], [-0.1, 0.1], "k-", lw=0.8)
    ax.text(3.0, -0.28, "3", ha="center", va="top", fontsize=9)

    # 交点 (3, 8)
    ax.plot(3, 8, "o", color="#cc4444", markersize=5, zorder=5)
    ax.text(3.08, 8.2, r"$(3,\ 8)$", ha="left", va="bottom", fontsize=8)

    # 塗りつぶし: x > 3（2^x > 8 の解の範囲）
    x_shade = np.linspace(3.0, X_HI, 200)
    y_shade = np.minimum(2.0 ** x_shade, Y_HI + 0.3)
    ax.fill_between(x_shade, 8, y_shade,
                    color="#ff9999", alpha=0.30, zorder=0)

    # 不等号方向の注記
    ax.annotate("",
                xy=(3.6, 9.0), xytext=(2.3, 9.0),
                arrowprops=dict(arrowstyle="-|>", color="#cc4444",
                                lw=1.2, mutation_scale=10))
    ax.text(2.9, 9.3, r"$x > 3$", ha="center", va="bottom",
            fontsize=9, color="#cc4444")

    ax.legend(loc="upper left", fontsize=9, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)
    ax.text((X_LO + X_HI) / 2, Y_HI + 0.80,
            r"$a > 1$（単調増加）— 不等号そのまま",
            ha="center", va="top", fontsize=10, fontweight="bold")

    # ── 右パネル: 0 < a < 1（y=(1/2)^x、(1/2)^x ≤ 1/4 ⟺ x ≥ 2） ─
    ax = axes[1]
    draw_axes(ax)

    # y = (1/2)^x
    y_dec = 0.5 ** x
    ax.plot(x, np.clip(y_dec, Y_LO, Y_HI + 0.5), color="#1a1a1a", lw=1.8, zorder=2,
            label=r"$y = \left(\frac{1}{2}\right)^x$")

    # 水平線 y=1/4（=(1/2)^2）
    ax.axhline(0.25, color="#cc4444", lw=1.0, ls="--", zorder=1)
    ax.text(X_HI + 0.55, 0.30, r"$y = \frac{1}{4}$", ha="left", va="bottom",
            fontsize=9, color="#cc4444")

    # x=2 目盛り
    ax.plot([2, 2], [-0.1, 0.1], "k-", lw=0.8)
    ax.text(2.0, -0.28, "2", ha="center", va="top", fontsize=9)

    # 交点 (2, 1/4)
    ax.plot(2, 0.25, "o", color="#cc4444", markersize=5, zorder=5)
    ax.text(2.1, 0.33, r"$\left(2,\ \frac{1}{4}\right)$",
            ha="left", va="bottom", fontsize=8)

    # 塗りつぶし: x ≥ 2（(1/2)^x ≤ 1/4 の解の範囲）
    x_shade2 = np.linspace(2.0, X_HI, 200)
    y_shade2 = 0.5 ** x_shade2
    ax.fill_between(x_shade2, y_shade2, 0.25,
                    color="#ff9999", alpha=0.30, zorder=0)

    # 不等号逆転の注記（ボックス）
    ax.text(X_HI - 0.2, 4.5,
            "単調減少\n→ 不等号逆転",
            ha="right", va="center", fontsize=8.5, color="#555555",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff8e8",
                      edgecolor="#cccccc", lw=0.8))

    # 不等号方向の注記
    ax.annotate("",
                xy=(2.6, 9.0), xytext=(1.3, 9.0),
                arrowprops=dict(arrowstyle="-|>", color="#cc4444",
                                lw=1.2, mutation_scale=10))
    ax.text(1.9, 9.3, r"$x \geq 2$", ha="center", va="bottom",
            fontsize=9, color="#cc4444")

    ax.legend(loc="upper right", fontsize=9, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)
    ax.text((X_LO + X_HI) / 2, Y_HI + 0.80,
            r"$0 < a < 1$（単調減少）— 不等号逆転",
            ha="center", va="top", fontsize=10, fontweight="bold")

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "exp-function-equation.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
