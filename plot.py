import matplotlib.pyplot as plt
from datetime import datetime
import os
from config import PLOTS_DIR


def plot_throughput(throughputs: list[int], intervals: list[datetime]):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(intervals, throughputs, label="Throughput", linewidth=1)

    ax.set_title("Throughput Plot")
    ax.set_xlabel("Interval Timestamps")
    ax.set_ylabel("Throughput")

    ax.grid(True, linestyle="--", alpha=0.6)

    output_path = os.path.join(PLOTS_DIR, "throughput.png")
    plt.savefig(output_path, dpi=300)
