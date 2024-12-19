from metrics import (
    measure_throughput,
    get_protocol_distribution,
    get_packet_size_distribution,
    measure_jitter,
    measure_cumulative_traffic,
    measure_tcp_latency,
    measure_dns_resolution_times,
)
from scapy.all import rdpcap
from plot import (
    plot_throughput,
    plot_protocol_distribution,
    plot_packet_size_distribution,
    plot_jitter,
    plot_cum_traffic,
    plot_tcp_latency,
    plot_dns_lookup_times,
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
    tcp_timestamps, tcp_rtts = measure_tcp_latency(packets)
    dns_res_times = measure_dns_resolution_times(packets)

    plot_throughput(throughputs, intervals)
    plot_protocol_distribution(dist)
    plot_packet_size_distribution(sizes)
    plot_jitter(jitter_values)
    plot_cum_traffic(timestamps, cumulative_traffic)
    plot_tcp_latency(tcp_timestamps, tcp_rtts)
    plot_dns_lookup_times(dns_res_times)
