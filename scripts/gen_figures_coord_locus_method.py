"""
gen_figures_coord_locus_method.py — 軌跡の求め方

Panel 1: 媒介変数消去プロセス
Panel 2: 逆の確認（十分条件の検証）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_coord_locus_method.py
出力: site/figures/coord-locus-method-combined.png
      site/assets/images/coord-locus-method-combined.png
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


def draw_parametric_elimination(ax):
    """Panel 1: 媒介変数消去プロセス"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    steps = [
        (r"$x = t+1,\quad y = t^2$",           "#eef4ff", DARK_BLUE,   "媒介変数表示"),
        (r"$t = x - 1$   （$x$ から消去）",       "#fff8f0", ORANGE,     "消去ステップ"),
        (r"$y = (x-1)^2$",                       "#f0fff4", GREEN,      "代入"),
        (r"放物線 $y = x^2 - 2x + 1$",           "#fff0f0", RED,        "軌跡の方程式"),
    ]

    box_style_base = dict(boxstyle="round,pad=0.5", linewidth=1.4)
    y_positions = [6.8, 5.2, 3.6, 2.0]
    note_offsets = [3.0, 3.0, 3.0, 3.0]

    prev_y = None
    for i, ((text, fc, ec, note), y_pos) in enumerate(zip(steps, y_positions)):
        bs = {**box_style_base, "facecolor": fc, "edgecolor": ec}
        ax.text(4.5, y_pos, text, ha="center", va="center",
                fontsize=11, color=ec, bbox=bs)

        # サイドノート
        ax.text(8.2, y_pos, note, ha="left", va="center",
                fontsize=8.5, color=GRAY)

        if prev_y is not None:
            ax.annotate("", xy=(4.5, y_pos + 0.52),
                        xytext=(4.5, prev_y - 0.52),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        lw=1.4, mutation_scale=9,
                                        shrinkA=0, shrinkB=0))
        prev_y = y_pos

    # タイトル行
    ax.text(4.5, 7.7, "媒介変数の消去",
            ha="center", va="center", fontsize=10.5, color=DARK_BLUE,
            fontweight="bold")

    # ポイントの囲み
    ax.text(4.5, 0.8,
            "手順: ① 一方から媒介変数を解く → ② もう一方に代入",
            ha="center", va="center", fontsize=8.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#f8f8f8",
                      edgecolor=GRAY, linewidth=0.8))

    ax.set_title("媒介変数消去プロセス", fontsize=10, pad=4)


def draw_reverse_check(ax):
    """Panel 2: 逆の確認（十分条件の検証）"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # 放物線の概念図（右側）
    # 小さい放物線を右下に描く
    x_p = np.linspace(-1.5, 3.5, 300)
    y_p = (x_p - 1) ** 2
    # スケールして右下に配置
    x_scaled = x_p * 1.1 + 5.5
    y_scaled = y_p * 0.55 + 0.4
    mask = (y_scaled >= 0.3) & (y_scaled <= 4.0)
    ax.plot(x_scaled[mask], y_scaled[mask], color=DARK_BLUE, linewidth=2.0, zorder=3)

    # 除外なし（t は全実数なので放物線全体が軌跡）
    # 矢印で「全体が対応」を示す
    ax.text(7.5, 4.3, r"$y=(x-1)^2$" + "\n（$t\in\mathbb{R}$）",
            ha="center", va="bottom", fontsize=9, color=DARK_BLUE)

    # 逆の確認フロー（左側）
    ax.text(0.4, 7.5,
            "逆の確認（十分条件の検証）",
            ha="left", va="top", fontsize=10.5, color=DARK_BLUE,
            fontweight="bold")

    flow_steps = [
        ("① 軌跡の方程式 $y=(x-1)^2$ を仮定",           "#eef4ff", DARK_BLUE),
        ("② $t = x-1$ とおくと $t\\in\\mathbb{R}$",      "#f0fff4", GREEN),
        ("③ $x=t+1,\\ y=t^2$ を満たす $t$ が存在",       "#fff8f0", ORANGE),
        ("④ 方程式の点はすべて軌跡 $\\Rightarrow$ 十分", "#f0fff4", GREEN),
    ]

    y_positions = [6.2, 5.0, 3.8, 2.6]
    prev_y = None
    for (text, fc, ec), yp in zip(flow_steps, y_positions):
        ax.text(2.5, yp, text, ha="left", va="center",
                fontsize=9, color=ec,
                bbox=dict(boxstyle="round,pad=0.35", facecolor=fc,
                          edgecolor=ec, linewidth=1.0))
        if prev_y is not None:
            ax.annotate("", xy=(2.6, yp + 0.38),
                        xytext=(2.6, prev_y - 0.38),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        lw=1.2, mutation_scale=8,
                                        shrinkA=0, shrinkB=0))
        prev_y = yp

    # 結論ボックス
    ax.text(2.5, 1.4,
            "軌跡は $y=(x-1)^2$（除外点なし）",
            ha="left", va="center", fontsize=9.5, color=RED,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fff0f0",
                      edgecolor=RED, linewidth=1.3))

    ax.set_title("逆の確認（十分条件の検証）", fontsize=10, pad=4)


def main() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_parametric_elimination(axes[0])
    draw_reverse_check(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "coord-locus-method-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")

    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
