from metrics import (
    measure_throughput,
    get_protocol_distribution,
    get_packet_size_distribution,
    measure_jitter,
    measure_cumulative_traffic,
)
from scapy.all import rdpcap
from plot import (
    plot_throughput,
    plot_protocol_distribution,
    plot_packet_size_distribution,
    plot_jitter,
    plot_cum_traffic,
)
from config import PLOTS_DIR
import os
from config import logger

if __name__ == "__main__":
    os.makedirs(PLOTS_DIR, exist_ok=True)
    logger.info("Created 'plots' directory.")
    packets = rdpcap("packet_captures/personal.pcapng")
    logger.info("Read .pcap file.")

    sizes = get_packet_size_distribution(packets)
    throughputs, intervals = measure_throughput(packets)
    dist = get_protocol_distribution(packets)
    jitter_values = measure_jitter(packets)
    timestamps, cumulative_traffic = measure_cumulative_traffic(packets)

    plot_throughput(throughputs, intervals)
    plot_protocol_distribution(dist)
    plot_packet_size_distribution(sizes)
    plot_jitter(jitter_values)
    plot_cum_traffic(timestamps, cumulative_traffic)
