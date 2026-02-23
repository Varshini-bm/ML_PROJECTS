import matplotlib.pyplot as plt
import numpy as np

def init_plot():
    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    ax.set_title("⚡ HOLO PERFORMANCE MATRIX ⚡", color="cyan", fontsize=14, weight="bold")
    ax.set_ylim(0, 10)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylabel("Score", color="white")
    ax.set_xticks(range(4))
    ax.set_xticklabels(["Clarity", "Confidence", "Impact", "Overall"], color="magenta", fontsize=10)

    # Add neon-style grid
    ax.grid(True, color="cyan", alpha=0.3, linestyle="--")

    return fig, ax


def update_plot(ax, scores):
    ax.clear()
    metrics = list(scores.keys())
    values = list(scores.values())

    # neon-style scatter plot instead of boring bars
    x = np.arange(len(metrics))
    y = values

    ax.scatter(x, y, s=500, c="cyan", alpha=0.9, edgecolors="magenta", linewidths=2, marker="o")

    # glowing trails (lines)
    ax.plot(x, y, color="magenta", linestyle="--", linewidth=1.5, alpha=0.7)

    # re-apply sci-fi styling
    ax.set_facecolor("black")
    ax.set_ylim(0, 10)
    ax.set_xlim(-0.5, 3.5)
    ax.set_xticks(range(4))
    ax.set_xticklabels(metrics, color="magenta", fontsize=10)
    ax.set_ylabel("Score", color="white")
    ax.set_title("⚡ HOLO PERFORMANCE MATRIX ⚡", color="cyan", fontsize=14, weight="bold")
    ax.grid(True, color="cyan", alpha=0.3, linestyle="--")

    plt.pause(0.01)
