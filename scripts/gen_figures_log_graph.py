"""
gen_figures_log_graph.py — 対数関数 グラフ図生成

図1 (log-function-graph-inverse.png): 逆関数の対称性
  y=2^x、y=log_2 x、y=x を同一グラフに描く

図2 (log-function-graph-cases.png): a>1 と 0<a<1 の2ケース横並び
  左: y=log_2 x, y=log_3 x（a>1）
  右: y=log_{1/2} x, y=log_{1/3} x（0<a<1）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_log_graph.py
出力: site/figures/log-function-graph-inverse.png
      site/assets/images/log-function-graph-inverse.png
      site/figures/log-function-graph-cases.png
      site/assets/images/log-function-graph-cases.png
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


def log_b(x, base):
    """底 base の対数（numpy 配列対応）"""
    return np.log(x) / np.log(base)


# ── 図1: 逆関数の対称性 ──────────────────────────────────────────

def make_inverse_figure():
    """y=2^x、y=log_2 x、y=x を描き逆関数の対称性を示す"""
    fig, ax = plt.subplots(1, 1, figsize=(5.5, 5.5))
    fig.patch.set_facecolor("white")

    XLO, XHI = -2.8, 3.5
    YLO, YHI = -2.8, 3.5

    ax.set_xlim(XLO - 0.3, XHI + 0.6)
    ax.set_ylim(YLO - 0.3, YHI + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(XHI + 0.5, 0), xytext=(XLO - 0.25, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(XHI + 0.54, 0.0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, YHI + 0.40), xytext=(0, YLO - 0.25),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.06, YHI + 0.42, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点
    ax.text(-0.20, -0.20, "O", ha="right", va="top", fontsize=9)

    # 漸近線: y=0（水平）と x=0（垂直）— 薄い破線
    ax.axhline(0, color="#dddddd", lw=0.7, ls="--", zorder=0)
    ax.axvline(0, color="#dddddd", lw=0.7, ls="--", zorder=0)

    # y = x（対称軸の点線）
    x_diag = np.linspace(XLO, XHI, 300)
    ax.plot(x_diag, x_diag, color="#aaaaaa", lw=1.2, ls="dotted",
            label=r"$y = x$", zorder=1)

    # y = 2^x
    x1 = np.linspace(XLO, XHI, 600)
    y1 = 2.0 ** x1
    mask1 = (y1 >= YLO - 0.3) & (y1 <= YHI + 0.3)
    ax.plot(x1[mask1], y1[mask1], color="#1a1a1a", lw=1.8, ls="solid",
            label=r"$y = 2^x$", zorder=2)

    # y = log_2 x（x > 0 のみ）
    x2 = np.linspace(0.04, XHI, 600)
    y2 = log_b(x2, 2)
    mask2 = (y2 >= YLO - 0.3) & (y2 <= YHI + 0.3)
    ax.plot(x2[mask2], y2[mask2], color="#cc4444", lw=1.8, ls="solid",
            label=r"$y = \log_2 x$", zorder=2)

    # 特徴的な点: (0, 1) on y=2^x
    ax.plot(0, 1, "ko", markersize=5, zorder=5)
    ax.text(0.10, 1.06, r"$(0,\ 1)$", ha="left", va="bottom", fontsize=8.5)

    # 特徴的な点: (1, 0) on y=log_2 x
    ax.plot(1, 0, "o", color="#cc4444", markersize=5, zorder=5)
    ax.text(1.08, 0.08, r"$(1,\ 0)$", ha="left", va="bottom", fontsize=8.5)

    ax.legend(loc="upper left", fontsize=9, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.8)

    ax.text((XLO + XHI) / 2, YHI + 0.50, "指数関数と対数関数（逆関数）",
            ha="center", va="top", fontsize=11, fontweight="bold")

    fig.tight_layout(pad=0.4)
    return fig


# ── 図2: a>1 と 0<a<1 の2ケース横並び ────────────────────────────

X_LO_C, X_HI_C = 0.06, 7.0
Y_LO_C, Y_HI_C = -3.5, 3.0


def draw_log_case(ax, title: str, funcs: list[dict]) -> None:
    ax.set_xlim(-0.5, X_HI_C + 1.0)
    ax.set_ylim(Y_LO_C - 0.2, Y_HI_C + 1.0)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI_C + 0.9, 0), xytext=(-0.4, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI_C + 0.94, 0.0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI_C + 0.75), xytext=(0, Y_LO_C - 0.15),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.10, Y_HI_C + 0.78, r"$y$", ha="left", va="bottom", fontsize=10)

    # 原点
    ax.text(-0.22, -0.18, "O", ha="right", va="top", fontsize=9)

    # 漸近線 x = 0（垂直破線）
    ax.axvline(0, color="#aaaaaa", lw=0.8, ls="--", zorder=0)
    ax.text(0.10, Y_LO_C + 0.15, r"$x=0$", ha="left", va="bottom",
            fontsize=8, color="#888888")

    # x 軸目盛り 1
    ax.plot([1, 1], [-0.10, 0.10], "k-", linewidth=0.8)
    ax.text(1.0, -0.25, "1", ha="center", va="top", fontsize=9)

    # y = 0 の水平線（薄く）
    ax.axhline(0, color="#eeeeee", lw=0.6, zorder=0)

    # 曲線を描く
    x_arr = np.linspace(0.06, X_HI_C, 600)
    colors = ["#1a1a1a", "#555555"]
    for i, fd in enumerate(funcs):
        y_arr = fd["f"](x_arr)
        mask = (y_arr >= Y_LO_C - 0.2) & (y_arr <= Y_HI_C + 0.2)
        ax.plot(x_arr[mask], y_arr[mask],
                color=colors[i], lw=1.8, ls=fd["ls"], zorder=2,
                label=fd["label"])

    # 共通通過点 (1, 0)
    ax.plot(1, 0, "ko", markersize=6, zorder=5)
    ax.text(1.12, 0.10, r"$(1,\ 0)$", ha="left", va="bottom", fontsize=9)

    # 凡例
    legend_loc = "upper left" if "単調増加" in title else "upper right"
    ax.legend(loc=legend_loc, fontsize=9, framealpha=0.9,
              edgecolor="#cccccc", handlelength=1.6)

    # タイトル
    cx = (0 + X_HI_C) / 2
    ax.text(cx, Y_HI_C + 0.85, title,
            ha="center", va="top", fontsize=11, fontweight="bold")


def make_cases_figure():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")

    # 左: a > 1
    draw_log_case(axes[0], r"$a > 1$：右上がり（単調増加）", [
        {"f": lambda x: log_b(x, 2),    "label": r"$y = \log_2 x$",      "ls": "solid"},
        {"f": lambda x: log_b(x, 3),    "label": r"$y = \log_3 x$",      "ls": "dashed"},
    ])

    # 右: 0 < a < 1
    draw_log_case(axes[1], r"$0 < a < 1$：右下がり（単調減少）", [
        {"f": lambda x: log_b(x, 0.5),  "label": r"$y = \log_{1/2} x$",  "ls": "solid"},
        {"f": lambda x: log_b(x, 1/3),  "label": r"$y = \log_{1/3} x$",  "ls": "dashed"},
    ])

    fig.tight_layout(pad=0.4, w_pad=1.2)
    return fig


def main() -> None:
    # 図1: 逆関数の対称性
    fig1 = make_inverse_figure()
    fname1 = "log-function-graph-inverse.png"
    out1_fig  = FIGURES_DIR / fname1
    out1_site = SITE_IMAGES_DIR / fname1
    fig1.savefig(out1_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig1)
    shutil.copy2(out1_fig, out1_site)
    print(f"生成: {out1_fig}")
    print(f"コピー: {out1_site}")

    # 図2: 2ケース横並び
    fig2 = make_cases_figure()
    fname2 = "log-function-graph-cases.png"
    out2_fig  = FIGURES_DIR / fname2
    out2_site = SITE_IMAGES_DIR / fname2
    fig2.savefig(out2_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig2)
    shutil.copy2(out2_fig, out2_site)
    print(f"生成: {out2_fig}")
    print(f"コピー: {out2_site}")


if __name__ == "__main__":
    main()
