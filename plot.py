import matplotlib.pyplot as plt
from datetime import datetime
import os
from collections import Counter
from config import PLOTS_DIR
from config import logger


def plot_throughput(throughputs: list[int], intervals: list[datetime]):
    plt.figure(figsize=(10, 6))
    plt.plot(
        intervals,
        throughputs,
        label="Throughput",
        color="dodgerblue",
        linewidth=2,
        markersize=5,
    )
    plt.title(
        "Throughput Over Time", fontsize=16, fontweight="bold", fontname="monospace"
    )
    plt.xlabel("Time", fontsize=14, fontname="monospace")
    plt.ylabel("Throughput (bytes/sec)", fontsize=14, fontname="monospace")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    output_path = os.path.join(PLOTS_DIR, "throughput.png")
    logger.info("Plotted throughput.")
    plt.savefig(output_path, dpi=300)
    logger.info("Saved throughput plot.")


def plot_protocol_distribution(distribution: Counter):
    protocols = list(distribution.keys())
    counts = list(distribution.values())
    plt.figure(figsize=(10, 6))
    plt.barh(
        protocols,
        counts,
        color=plt.cm.Paired.colors[: len(protocols)],
        edgecolor="black",
    )
    plt.title(
        "Protocol Distribution", fontsize=16, fontweight="bold", fontname="monospace"
    )
    plt.xlabel("Packet Count", fontsize=14, fontname="monospace")
    plt.ylabel("Protocol", fontsize=14, fontname="monospace")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    output_path = os.path.join(PLOTS_DIR, "proto-dist.png")
    logger.info("Plotted protocol distribution.")
    plt.savefig(output_path, dpi=300)
    logger.info("Saved protocol distribution plot.")


def plot_packet_size_distribution(sizes: list[int]):
    plt.figure(figsize=(10, 6))
    plt.hist(sizes, bins=30, edgecolor="black")
    plt.title(
        "Packet Size Distribution", fontsize=16, fontweight="bold", fontname="monospace"
    )
    plt.xlabel("Packet Sizes", fontsize=14, fontname="monospace")
    plt.ylabel("Frequency", fontsize=14, fontname="monospace")
    plt.grid(True, axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    output_path = os.path.join(PLOTS_DIR, "pkt-sizes.png")
    logger.info("Plotted packet size distribution.")
    plt.savefig(output_path, dpi=300)
    logger.info("Saved packet size distribution plot.")


def plot_jitter(jitter_values: list[int]):
    plt.figure(figsize=(10, 6))
    plt.plot(
        jitter_values,
        label="Jitter",
        color="dodgerblue",
        linewidth=2,
        markersize=5,
    )
    plt.title("Jitter Over Time", fontsize=16, fontweight="bold", fontname="monospace")
    plt.xlabel("Packet Index", fontsize=14, fontname="monospace")
    plt.ylabel("Jitter (seconds)", fontsize=14, fontname="monospace")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    output_path = os.path.join(PLOTS_DIR, "jitter.png")
    logger.info("Plotted jitter.")
    plt.savefig(output_path, dpi=300)
    logger.info("Saved jitter plot.")


def plot_cum_traffic(timestamps: list[datetime], cumulative_traffic: list[int]):
    plt.figure(figsize=(10, 6))
    plt.plot(
        timestamps,
        cumulative_traffic,
        color="dodgerblue",
        linewidth=2,
        markersize=5,
    )
    plt.title(
        "Cumulative Traffic Volume Over Time",
        fontsize=16,
        fontweight="bold",
        fontname="monospace",
    )
    plt.xlabel("Time (seconds)", fontsize=14, fontname="monospace")
    plt.ylabel("Cumulative Traffic (bytes)", fontsize=14, fontname="monospace")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    output_path = os.path.join(PLOTS_DIR, "cum_traffic.png")
    logger.info("Plotted cumulative traffic.")
    plt.savefig(output_path, dpi=300)
    logger.info("Saved cumulative traffic plot.")
