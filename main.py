from metrics import measure_throughput
from scapy.all import rdpcap
from plot import plot_throughput
from config import PLOTS_DIR
import os

if __name__ == "__main__":
    os.makedirs(PLOTS_DIR, exist_ok=True)
    packets = rdpcap("packet_captures/telnet.pcap")
    throughputs, intervals = measure_throughput(packets)
    plot_throughput(throughputs, intervals)
