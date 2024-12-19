from metrics import (
    measure_throughput,
    get_protocol_distribution,
    get_packet_size_distribution,
    measure_jitter,
    measure_cumulative_traffic,
    measure_tcp_latency,
    measure_dns_resolution_times,
)
from typer import Typer, Argument, Option
import time
from scapy.all import rdpcap
import pyshark
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

app = Typer()


@app.command()
def gather(
    output: str = Argument(..., help="Path to save the captured .pcap file"),
    interface: str = Argument(..., help="Network interface to capture packets"),
    duration: int = Option(10, help="Duration in seconds for the packet capture"),
):
    """
    Gather network packets using PyShark and save them to a .pcap file.
    """
    logger.info(
        f"Starting packet capture on interface '{interface}' for {duration} seconds."
    )
    try:
        capture = pyshark.LiveCapture(interface=interface, output_file=output)

        start_time = time.time()
        for packet in capture.sniff_continuously():
            if time.time() - start_time >= duration:
                logger.info("Reached capture duration. Stopping capture.")
                break
        capture.close()
        logger.info(f"Packet capture completed. File saved as: {output}")
    except Exception as e:
        logger.error(f"Error during packet capture: {e}")


@app.command()
def analyze(pcap_file: str = Argument(..., help="Path to the .pcap file to analyze")):
    """
    Analyze a .pcap file and generate plots.
    """
    logger.info("Starting analysis...")
    os.makedirs(PLOTS_DIR, exist_ok=True)
    logger.info(f"Created 'plots' directory at {PLOTS_DIR}.")

    try:
        packets = rdpcap(pcap_file)
        logger.info(f"Read {len(packets)} packets from {pcap_file}.")

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

        logger.info("Analysis and plotting completed successfully.")
    except FileNotFoundError:
        logger.error(f"The file {pcap_file} does not exist.")
    except Exception as e:
        logger.error(f"An error occurred during analysis: {e}")


if __name__ == "__main__":
    app()
