"""
gen_figures_rl1.py — 解の配置・記事1用概念図
2解が同符号（ともに正 / ともに負）2パネル横並び

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_rl1.py
出力:
    figures/quadratic-root-location-same-sign-combined.png
    assets/images/quadratic-root-location-same-sign-combined.png
    ../figures/quadratic-root-location-same-sign-combined.png  （PDF用）
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

BASE_DIR = Path(__file__).parent.parent        # = site/
FIGURES_DIR = BASE_DIR / "figures"
SITE_IMAGES_DIR = BASE_DIR / "assets" / "images"
EXP_FIGURES_DIR = BASE_DIR.parent / "figures"  # = graph-guided-lessons/figures/
FIGURES_DIR.mkdir(exist_ok=True)
EXP_FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150

# ── ラベル位置定数（PDF_QUALITY_CHECK.md 推奨値） ─────────────────
Y_TITLE_OFFSET      = 0.20
Y_YLABEL_OFFSET     = 0.27
CASE_TITLE_FONTSIZE = 10
TIGHT_LAYOUT_PAD    = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")

X_LO, X_HI = -3.5, 4.5
Y_LO, Y_HI = -0.7, 5.0

# ── 2ケース ───────────────────────────────────────────────────────
CASES = [
    {
        "title": "2解がともに正",
        "f":     lambda x: (x - 1.0) * (x - 2.0),
        "roots": [1.0, 2.0],
        "root_labels": [r"$1$", r"$2$"],
        "axis_x": 1.5,
        "axis_label": r"軸$=\frac{3}{2}>0$",
        "f0_text": r"$f(0)>0$",
        "f0_offset": (0.8, 1.0),
    },
    {
        "title": "2解がともに負",
        "f":     lambda x: (x + 2.0) * (x + 1.0),
        "roots": [-2.0, -1.0],
        "root_labels": [r"$-2$", r"$-1$"],
        "axis_x": -1.5,
        "axis_label": r"軸$=-\frac{3}{2}<0$",
        "f0_text": r"$f(0)>0$",
        "f0_offset": (0.8, 1.0),
    },
]


def draw_case(ax, case):
    f = case["f"]
    ax.set_xlim(X_LO - 0.1, X_HI + 0.45)
    ax.set_ylim(Y_LO - 0.4, Y_HI + 0.6)
    ax.axis("off")

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI + 0.32, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.36, 0, r"$x$", ha="left", va="center", fontsize=10)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.48), xytext=(0, Y_LO - 0.22),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=10)

    # 放物線
    x_all = np.linspace(X_LO, X_HI, 600)
    y_all = np.clip(f(x_all), Y_LO - 0.2, Y_HI + 0.2)
    ax.plot(x_all, y_all, color="black", linewidth=2.0, zorder=2)

    # 解の目盛り・ラベル・open circle
    tick = 0.13
    for r, lbl in zip(case["roots"], case["root_labels"]):
        ax.plot([r, r], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(r, -0.28, lbl, ha="center", va="top", fontsize=9,
                bbox=_lbl_bbox, zorder=7)
        ax.plot(r, 0.0, "o", color="white", markeredgecolor="black",
                markersize=5, markeredgewidth=1.2, zorder=5)

    # 原点 O
    ax.plot([0, 0], [-tick, tick], "k-", linewidth=0.9, zorder=3)
    ax.text(0, -0.28, "$O$", ha="center", va="top", fontsize=9,
            bbox=_lbl_bbox, zorder=7)

    # f(0) の点とアノテーション
    f0 = float(f(0.0))
    ax.plot(0, f0, "D", color="#2563eb", markersize=5.5, zorder=6)
    dx, dy = case["f0_offset"]
    ax.annotate(case["f0_text"],
                xy=(0, f0), xytext=(dx, f0 + dy),
                fontsize=9, color="#2563eb",
                arrowprops=dict(arrowstyle="-", color="#2563eb", lw=0.8),
                bbox=dict(facecolor="white", edgecolor="none", pad=0.05))

    # 軸の破線とラベル
    ax_x = case["axis_x"]
    ax.plot([ax_x, ax_x], [-0.22, Y_HI - 0.4], "--",
            color="#6b7280", linewidth=1.0, zorder=1)
    ax.text(ax_x, Y_HI - 0.45, case["axis_label"],
            ha="center", va="top", fontsize=8, color="#6b7280",
            bbox=_lbl_bbox, zorder=7)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, case["title"],
            ha="center", va="bottom", fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.5))
    fig.patch.set_facecolor("white")
    for ax, case in zip(axes, CASES):
        draw_case(ax, case)
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=1.0)

    fname = "quadratic-root-location-same-sign-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
