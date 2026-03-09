"""
gen_figures_rl3.py — 解の配置・記事3用概念図
2解がともに区間 (0,3) 内: 正解パターン + NGパターン3種 の4パネル

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_rl3.py
出力:
    figures/quadratic-root-location-both-in-interval-combined.png
    assets/images/quadratic-root-location-both-in-interval-combined.png
    ../figures/quadratic-root-location-both-in-interval-combined.png  （PDF用）
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
EXP_FIGURES_DIR = BASE_DIR.parent / "figures"
FIGURES_DIR.mkdir(exist_ok=True)
EXP_FIGURES_DIR.mkdir(exist_ok=True)

DPI = 150

Y_TITLE_OFFSET      = 0.20
Y_YLABEL_OFFSET     = 0.27
CASE_TITLE_FONTSIZE = 9.5
TIGHT_LAYOUT_PAD    = 0.5
_lbl_bbox = dict(boxstyle="square,pad=0.05", facecolor="white", edgecolor="none")

# 共通 x 範囲（NG4 で根が負になるため左を広げる）
X_LO, X_HI = -3.2, 5.2
Y_LO, Y_HI = -1.5, 6.0

# 区間端
ALPHA, BETA = 0.0, 3.0


def f_ok(x):
    """正解: f(x)=(x-1)(x-2), 根 1,2 ∈ (0,3)"""
    return (x - 1.0) * (x - 2.0)


def f_ng1(x):
    """NG1 (D<0): f(x)=(x-1.5)²+0.5, 実数解なし"""
    return (x - 1.5) ** 2 + 0.5


def f_ng2(x):
    """NG2 (f(β)≤0): f(x)=(x-0.8)(x-3.5), 根0.8,3.5 → f(3)<0"""
    return (x - 0.8) * (x - 3.5)


def f_ng3(x):
    """NG3 (軸が区間外): f(x)=(x+2)(x+1), 根-2,-1 → 軸-1.5<0"""
    return (x + 2.0) * (x + 1.0)


CASES = [
    {
        "title": "正解：2解が (0, 3) 内",
        "f": f_ok,
        "roots": [1.0, 2.0],
        "root_labels": [r"$1$", r"$2$"],
        "note": r"$D\geq0,\ f(0)>0,\ f(3)>0,\ 0<$ 軸 $<3$",
        "note_color": "#16a34a",
        "ng_mark": False,
    },
    {
        "title": r"NG: $D<0$（実数解なし）",
        "f": f_ng1,
        "roots": [],
        "root_labels": [],
        "note": r"$D<0$ → x軸と交わらない",
        "note_color": "#dc2626",
        "ng_mark": True,
    },
    {
        "title": r"NG: $f(3)\leq 0$（端点が内側）",
        "f": f_ng2,
        "roots": [0.8, 3.5],
        "root_labels": [r"$0.8$", r"$3.5$"],
        "note": r"$f(3)<0$ → 解の一方が区間外",
        "note_color": "#dc2626",
        "ng_mark": True,
    },
    {
        "title": "NG: 軸が区間外",
        "f": f_ng3,
        "roots": [-2.0, -1.0],
        "root_labels": [r"$-2$", r"$-1$"],
        "note": r"軸$=-1.5<0$ → 2解ともに区間外",
        "note_color": "#dc2626",
        "ng_mark": True,
    },
]


def draw_case(ax, case):
    f = case["f"]
    ax.set_xlim(X_LO - 0.1, X_HI + 0.45)
    ax.set_ylim(Y_LO - 0.5, Y_HI + 0.6)
    ax.axis("off")

    # 区間 (0,3) の薄い網掛け
    ax.axvspan(ALPHA, BETA, ymin=0.0, ymax=1.0,
               color="#bfdbfe", alpha=0.35, zorder=0)

    arrow_kw = dict(color="black", lw=0.9, mutation_scale=8, shrinkA=0, shrinkB=0)

    # x 軸
    ax.annotate("", xy=(X_HI + 0.32, 0), xytext=(X_LO - 0.05, 0),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(X_HI + 0.36, 0, r"$x$", ha="left", va="center", fontsize=9)

    # y 軸
    ax.annotate("", xy=(0, Y_HI + 0.48), xytext=(0, Y_LO - 0.28),
                arrowprops=dict(arrowstyle="-|>", **arrow_kw))
    ax.text(0.1, Y_HI + Y_YLABEL_OFFSET, r"$y$", ha="left", va="bottom", fontsize=9)

    # 区間端点の破線と α, β ラベル
    for xb, lbl in [(ALPHA, r"$0$"), (BETA, r"$3$")]:
        ax.plot([xb, xb], [Y_LO - 0.3, Y_HI + 0.2], "--",
                color="#9ca3af", linewidth=0.8, zorder=1)
        ax.text(xb, Y_LO - 0.35, lbl, ha="center", va="top", fontsize=8,
                bbox=_lbl_bbox, zorder=7)

    # 放物線
    x_all = np.linspace(X_LO, X_HI, 600)
    y_all = np.clip(f(x_all), Y_LO - 0.3, Y_HI + 0.3)
    color = "black" if not case["ng_mark"] else "#374151"
    ax.plot(x_all, y_all, color=color, linewidth=1.8, zorder=2)

    # 解の目盛りと open circle
    tick = 0.12
    for r, lbl in zip(case["roots"], case["root_labels"]):
        ax.plot([r, r], [-tick, tick], "k-", linewidth=0.9, zorder=3)
        ax.text(r, -0.32, lbl, ha="center", va="top", fontsize=8,
                bbox=_lbl_bbox, zorder=7)
        ax.plot(r, 0.0, "o", color="white", markeredgecolor="black",
                markersize=4.5, markeredgewidth=1.1, zorder=5)

    # NG マーク（破線赤枠）
    if case["ng_mark"]:
        from matplotlib.patches import FancyBboxPatch
        rect = FancyBboxPatch(
            (X_LO + 0.1, Y_LO - 0.1),
            (X_HI - X_LO - 0.2), (Y_HI - Y_LO + 0.1),
            boxstyle="round,pad=0.0", linewidth=1.5,
            edgecolor="#fca5a5", facecolor="none", linestyle="--", zorder=8,
            transform=ax.transData
        )
        ax.add_patch(rect)

    # ノート（条件説明）
    ax.text((X_LO + X_HI) / 2, Y_LO - 0.0,
            case["note"], ha="center", va="top",
            fontsize=7.5, color=case["note_color"],
            bbox=_lbl_bbox)

    # パネルタイトル
    cx = (X_LO + X_HI) / 2
    ax.text(cx, Y_HI + Y_TITLE_OFFSET, case["title"],
            ha="center", va="bottom",
            fontsize=CASE_TITLE_FONTSIZE, fontweight="bold")


def main():
    fig, axes = plt.subplots(1, 4, figsize=(18.0, 4.5))
    fig.patch.set_facecolor("white")
    for ax, case in zip(axes, CASES):
        draw_case(ax, case)
    fig.tight_layout(pad=TIGHT_LAYOUT_PAD, w_pad=0.8)

    fname = "quadratic-root-location-both-in-interval-combined.png"
    out_fig = FIGURES_DIR / fname
    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    for dest in [SITE_IMAGES_DIR, EXP_FIGURES_DIR]:
        shutil.copy2(out_fig, dest / fname)
        print(f"コピー: {dest / fname}")


if __name__ == "__main__":
    main()
