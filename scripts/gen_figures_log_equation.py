"""
gen_figures_log_equation.py
対数方程式・不等式の記事用図を生成する。
出力: site/figures/log-equation.png, site/assets/images/log-equation.png

2パネル横並び:
  左: y=log_2 x (a>1, 単調増加) — 不等号の向きがそのまま
  右: y=log_{1/2} x (0<a<1, 単調減少) — 不等号の向きが逆転
"""

import platform
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

# ── フォント設定 ──────────────────────────────────────────────────────────────
if platform.system() == "Darwin":
    plt.rcParams["font.family"] = "Hiragino Sans"
elif platform.system() == "Windows":
    plt.rcParams["font.family"] = "MS Gothic"
else:
    plt.rcParams["font.family"] = "Noto Sans CJK JP"

plt.rcParams["axes.unicode_minus"] = False

# ── 出力先 ────────────────────────────────────────────────────────────────────
SITE_DIR = Path(__file__).parents[1]
FIGURES_DIR = SITE_DIR / "figures"
SITE_IMAGES_DIR = SITE_DIR / "assets" / "images"
FIGURES_DIR.mkdir(exist_ok=True)
SITE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

FNAME = "log-equation.png"


def draw_axes(ax, xlim, ylim):
    """x軸・y軸を描画する。"""
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    # 軸ラベル
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8))
    ax.text(xlim[1] - 0.1, -0.25, "$x$", ha="right", va="top", fontsize=10)
    ax.text(0.1, ylim[1] - 0.1, "$y$", ha="left", va="top", fontsize=10)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.subplots_adjust(wspace=0.35)

    # ── 左パネル: y = log_2 x (a>1, 単調増加) ─────────────────────────────
    ax = axes[0]
    xlim = (-0.3, 5.5)
    ylim = (-3.0, 2.8)
    draw_axes(ax, xlim, ylim)

    x_vals = np.linspace(0.05, 5.2, 400)
    y_vals = np.log2(x_vals)
    ax.plot(x_vals, y_vals, color="#2563eb", linewidth=2.0, label=r"$y = \log_2 x$")

    # 不等式 log_2 x > log_2 2 すなわち x > 2 の解の範囲をシェーディング
    x_thresh = 2.0
    ax.axvline(x_thresh, color="#93c5fd", linewidth=1.2, linestyle="--")
    ax.fill_betweenx(ylim, x_thresh, xlim[1] * 0.95, alpha=0.18, color="#2563eb")

    # 通過点 (1, 0)
    ax.plot(1, 0, "o", color="#2563eb", markersize=5)
    ax.text(1.0, -0.4, "$(1,\\ 0)$", ha="center", va="top", fontsize=8.5,
            color="#1e3a5f")

    # x=2 の注記
    ax.text(x_thresh, ylim[0] + 0.2, "$x=2$", ha="center", va="bottom",
            fontsize=8.5, color="#2563eb")

    # 漸近線 x=0
    ax.text(0.15, ylim[1] - 0.2, "漸近線\n$x=0$", ha="left", va="top",
            fontsize=7.5, color="gray")

    ax.set_title(r"$a=2>1$（単調増加）" + "\n不等号の向きはそのまま",
                 fontsize=9.5, pad=6)
    ax.legend(loc="upper left", fontsize=9, frameon=False)

    # 解の範囲注記
    ax.annotate("$x > 2$ の範囲", xy=(3.5, 1.2), fontsize=8.5, color="#1d4ed8",
                ha="center")

    # ── 右パネル: y = log_{1/2} x (0<a<1, 単調減少) ───────────────────────
    ax = axes[1]
    xlim = (-0.3, 5.5)
    ylim = (-2.8, 3.0)
    draw_axes(ax, xlim, ylim)

    x_vals = np.linspace(0.05, 5.2, 400)
    y_vals = np.log(x_vals) / np.log(0.5)
    ax.plot(x_vals, y_vals, color="#dc2626", linewidth=2.0,
            label=r"$y = \log_{1/2} x$")

    # 不等式 log_{1/2} x > log_{1/2} 3 すなわち x < 3 の解の範囲
    x_thresh = 3.0
    ax.axvline(x_thresh, color="#fca5a5", linewidth=1.2, linestyle="--")
    ax.fill_betweenx(ylim, 0.05, x_thresh, alpha=0.18, color="#dc2626")

    # 通過点 (1, 0)
    ax.plot(1, 0, "o", color="#dc2626", markersize=5)
    ax.text(1.0, -0.4, "$(1,\\ 0)$", ha="center", va="top", fontsize=8.5,
            color="#7f1d1d")

    # x=3 の注記
    ax.text(x_thresh, ylim[0] + 0.2, "$x=3$", ha="center", va="bottom",
            fontsize=8.5, color="#dc2626")

    ax.set_title(r"$0<a=\frac{1}{2}<1$（単調減少）" + "\n不等号の向きが逆転",
                 fontsize=9.5, pad=6)
    ax.legend(loc="upper right", fontsize=9, frameon=False)

    # 解の範囲注記
    ax.annotate("$0 < x < 3$ の範囲", xy=(1.5, -1.8), fontsize=8.5,
                color="#991b1b", ha="center")

    # ── 保存 ─────────────────────────────────────────────────────────────────
    out_figures = FIGURES_DIR / FNAME
    out_images = SITE_IMAGES_DIR / FNAME
    fig.savefig(out_figures, dpi=150, bbox_inches="tight", facecolor="white")
    import shutil
    shutil.copy(out_figures, out_images)
    print(f"生成完了: {out_figures}")
    print(f"コピー完了: {out_images}")
    plt.close(fig)


if __name__ == "__main__":
    main()
