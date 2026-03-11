"""
gen_figures_seq_recur_fn.py — 差が f(n) 型漸化式

Panel 1: 差 f(k) の積み上げ棒グラフ（a_n = a_1 + Σ f(k)）
Panel 2: 分岐図（n=1 と n≥2 の2ルート）

使い方:
    cd experiments/graph-guided-lessons/site
    python scripts/gen_figures_seq_recur_fn.py
出力: figures/seq-recur-fn-combined.png
      assets/images/seq-recur-fn-combined.png
"""

import platform
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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


def draw_accumulation_bars(ax):
    """Panel 1: f(k)=3k の差を積み上げて a_n に到達"""
    a1 = 2
    ns = list(range(1, 7))
    fks = [3 * k for k in range(1, 7)]  # f(k) = 3k

    # a_n = a_1 + sum_{k=1}^{n-1} f(k)
    cumul = [a1]
    for k in range(1, len(ns)):
        cumul.append(cumul[-1] + fks[k - 1])

    # 初項（底）
    ax.bar(ns, [a1] * len(ns), color=DARK_BLUE, alpha=0.4, width=0.6,
           label=r"$a_1$（初項）", zorder=3)

    # 各差の積み上げ（色を徐々に変える）
    prev_vals = [a1] * len(ns)
    for i in range(len(ns) - 1):
        deltas = [0] * len(ns)
        for j in range(i + 1, len(ns)):
            deltas[j] = fks[i]
        bottom_vals = list(prev_vals)
        # 実際は cumulative なので簡略化
    # 代わりに個別差分をstackして描く
    ax.cla()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    prev = [a1] * len(ns)
    ax.bar(ns, prev, color=DARK_BLUE, alpha=0.4, width=0.6,
           label=r"$a_1$", zorder=3)

    for step in range(len(ns) - 1):
        additions = [0] * len(ns)
        for j in range(step + 1, len(ns)):
            additions[j] = fks[step]
        alpha_val = 0.3 + 0.12 * step
        color_val = RED if step % 2 == 0 else ORANGE
        ax.bar(ns, additions, bottom=prev, color=color_val,
               alpha=min(alpha_val, 0.7), width=0.6, zorder=3)
        prev = [p + a for p, a in zip(prev, additions)]

    # a_n の値ラベル
    for n_i, c in zip(ns, cumul):
        ax.text(n_i, c + 0.3, f"$a_{{{n_i}}}={c}$",
                ha="center", va="bottom", fontsize=8.5, color=DARK_BLUE)

    ax.set_xlim(0.2, len(ns) + 0.8)
    ax.set_xticks(ns)
    ax.set_xticklabels([f"$n={x}$" for x in ns], fontsize=8.5)
    ax.set_ylabel("$a_n$", fontsize=10)
    ax.set_title(r"差 $f(k)=3k$ の積み上げ", fontsize=10, pad=4)
    ax.text(3.5, max(cumul) * 0.4,
            r"$a_n = a_1 + \sum_{k=1}^{n-1} f(k)$" + "\n（$n \geq 2$）",
            ha="center", va="center", fontsize=9.5, color=DARK_BLUE,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#eef4ff",
                      edgecolor=DARK_BLUE, linewidth=0.8))


def draw_branch_diagram(ax):
    """Panel 2: n=1 と n≥2 の分岐図"""
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.5)
    ax.set_title(r"$n \geq 2$ の条件と $a_1$ の別確認", fontsize=10, pad=4)

    # 起点
    ax.add_patch(mpatches.FancyBboxPatch((3.5, 5.5), 3.0, 0.7,
                                     boxstyle="round,pad=0.15",
                                     facecolor=DARK_BLUE, edgecolor="#333333",
                                     linewidth=1.0, alpha=0.85))
    ax.text(5.0, 5.85, r"$a_{n+1} - a_n = f(n)$", ha="center", va="center",
            fontsize=9.5, color="white", fontweight="bold")

    # 分岐線
    ax.annotate("", xy=(2.5, 4.0), xytext=(5.0, 5.5),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.3,
                                mutation_scale=9))
    ax.annotate("", xy=(7.5, 4.0), xytext=(5.0, 5.5),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.3,
                                mutation_scale=9))

    ax.text(2.5, 4.75, "$n=1$ のとき", ha="center", va="center",
            fontsize=9, color=RED)
    ax.text(7.5, 4.75, r"$n \geq 2$ のとき", ha="center", va="center",
            fontsize=9, color=GREEN)

    # n=1 のブランチ
    ax.add_patch(mpatches.FancyBboxPatch((1.0, 3.0), 3.0, 0.7,
                                     boxstyle="round,pad=0.1",
                                     facecolor="#fff0f0", edgecolor=RED,
                                     linewidth=1.2))
    ax.text(2.5, 3.35, r"$a_1 = S_1$ を直接計算", ha="center", va="center",
            fontsize=9, color=RED)

    # n≥2 のブランチ
    ax.add_patch(mpatches.FancyBboxPatch((6.0, 3.0), 3.0, 0.7,
                                     boxstyle="round,pad=0.1",
                                     facecolor="#f0fff4", edgecolor=GREEN,
                                     linewidth=1.2))
    ax.text(7.5, 3.35, r"$a_n = a_1 + \sum_{k=1}^{n-1}f(k)$",
            ha="center", va="center", fontsize=9, color=GREEN)

    # 矢印で合流
    ax.annotate("", xy=(5.0, 1.8), xytext=(2.5, 3.0),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.3,
                                mutation_scale=9))
    ax.annotate("", xy=(5.0, 1.8), xytext=(7.5, 3.0),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.3,
                                mutation_scale=9))

    ax.add_patch(mpatches.FancyBboxPatch((2.8, 1.1), 4.4, 0.65,
                                     boxstyle="round,pad=0.1",
                                     facecolor="#eef4ff", edgecolor=DARK_BLUE,
                                     linewidth=1.2))
    ax.text(5.0, 1.43, "2ケースを確認して $a_n$ の公式を確定",
            ha="center", va="center", fontsize=9, color=DARK_BLUE,
            fontweight="bold")

    ax.text(5.0, 0.45,
            "$n=1$ の式が合わないときは定義域を $n \\geq 2$ と書く",
            ha="center", va="center", fontsize=8.5, color=DARK_BLUE)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.8))
    fig.patch.set_facecolor("white")

    draw_accumulation_bars(axes[0])
    draw_branch_diagram(axes[1])

    fig.tight_layout(pad=0.5, w_pad=1.5)

    fname = "seq-recur-fn-combined.png"
    out_fig = FIGURES_DIR / fname
    out_site = SITE_IMAGES_DIR / fname

    fig.savefig(out_fig, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"生成: {out_fig}")
    shutil.copy2(out_fig, out_site)
    print(f"コピー: {out_site}")


if __name__ == "__main__":
    main()
