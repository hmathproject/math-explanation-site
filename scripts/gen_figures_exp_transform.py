"""
gen_figures_exp_transform.py — 指数関数 平行移動・対称移動 図生成

左パネル: 平行移動 — y=2^x, y=2^{x-1}, y=2^x+1
右パネル: 対称移動 — y=2^x, y=2^{-x} = (1/2)^x（y軸対称）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_exp_transform.py
出力: site/figures/exp-function-transform.png
      site/assets/images/exp-function-transform.png
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
X_LO, X_HI = -2.5, 2.5
Y_LO, Y_HI = -0.3, 6.0


def draw_axes(ax):
    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)
    ax.set_xlim(X_LO - 0.4, X_HI + 0.7)
    ax.set_ylim(Y_LO, Y_HI + 0.8)
    ax.axis("off")

    # x 軸
    ax.annotate("", xy=(X_HI + 0.6, 0), xytext=(X_LO - 0.35, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.64, 0.0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.5), xytext=(0, Y_LO - 0.05),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, Y_HI + 0.52, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点
    ax.text(-0.18, -0.18, "O", ha="right", va="top", fontsize=9)

    # x 軸目盛り 1
    ax.plot([1, 1], [-0.06, 0.06], "k-", linewidth=0.8)
    ax.text(1.0, -0.25, "1", ha="center", va="top", fontsize=9)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")

    x = np.linspace(X_LO, X_HI, 600)

    # ── 左パネル: 平行移動 ─────────────────────────────────────────
    ax = axes[0]
    draw_axes(ax)

    # 漸近線 y=0
    ax.axhline(0, color="#aaaaaa", lw=0.7, ls="--", zorder=0)
    ax.text(X_HI + 0.48, 0.10, r"$y=0$", ha="left", va="bottom",
            fontsize=8, color="#888888")

    # 漸近線 y=1（y=2^x+1 用）
    ax.axhline(1, color="#cc8888", lw=0.7, ls=":", zorder=0)
    ax.text(X_HI + 0.48, 1.08, r"$y=1$", ha="left", va="bottom",
            fontsize=8, color="#cc8888")

    # y = 2^x（基準）
    y0 = 2.0 ** x
    mask = y0 <= Y_HI + 0.8
    ax.plot(x[mask], y0[mask], color="#1a1a1a", lw=1.8, ls="solid",
            label=r"$y = 2^x$（基準）", zorder=2)

    # y = 2^{x-1}（右に1移動）
    y1 = 2.0 ** (x - 1)
    ax.plot(x, np.clip(y1, Y_LO, Y_HI + 0.5), color="#555555", lw=1.8, ls="dashed",
            label=r"$y = 2^{x-1}$（右に1）", zorder=2)

    # y = 2^x + 1（上に1移動）
    y2 = 2.0 ** x + 1
    mask2 = y2 <= Y_HI + 0.5
    ax.plot(x[mask2], y2[mask2], color="#888888", lw=1.8, ls="dotted",
            label=r"$y = 2^x + 1$（上に1）", zorder=2)

    # (0, 1) 通過点 on y=2^x
    ax.plot(0, 1, "ko", markersize=5, zorder=5)

    ax.legend(loc="upper left", fontsize=8.5, framealpha=0.9,
              edgecolor="#cccccc", handlelength=2.0)
    ax.text((X_LO + X_HI) / 2, Y_HI + 0.72, "平行移動",
            ha="center", va="top", fontsize=11, fontweight="bold")

    # ── 右パネル: 対称移動（y軸対称）─────────────────────────────
    ax = axes[1]
    draw_axes(ax)

    # 漸近線 y=0
    ax.axhline(0, color="#aaaaaa", lw=0.7, ls="--", zorder=0)
    ax.text(X_HI + 0.48, 0.10, r"$y=0$", ha="left", va="bottom",
            fontsize=8, color="#888888")

    # y 軸（対称軸）を強調
    ax.axvline(0, color="#4466cc", lw=1.2, ls="--", zorder=1, alpha=0.6)
    ax.text(0.08, Y_HI + 0.05, "対称軸", ha="left", va="top",
            fontsize=8, color="#4466cc")

    # y = 2^x（基準）
    y0 = 2.0 ** x
    mask = y0 <= Y_HI + 0.5
    ax.plot(x[mask], y0[mask], color="#1a1a1a", lw=1.8, ls="solid",
            label=r"$y = 2^x$", zorder=2)

    # y = 2^{-x} = (1/2)^x（y軸対称）
    y_sym = 2.0 ** (-x)
    combined_label = "$y = 2^{-x}$\n$= \\left(\\frac{1}{2}\\right)^x$"
    ax.plot(x, np.clip(y_sym, Y_LO, Y_HI + 0.5), color="#cc4444", lw=2.0, ls="solid",
            label=combined_label, zorder=2)

    # (0, 1) 共通通過点
    ax.plot(0, 1, "ko", markersize=6, zorder=5)
    ax.text(0.12, 1.05, r"$(0,\ 1)$", ha="left", va="bottom", fontsize=9)

    ax.legend(loc="upper right", fontsize=8.5, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.8)
    ax.text((X_LO + X_HI) / 2, Y_HI + 0.72, "対称移動（y 軸対称）",
            ha="center", va="top", fontsize=11, fontweight="bold")

    fig.tight_layout(pad=0.4, w_pad=1.2)

    fname = "exp-function-transform.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
