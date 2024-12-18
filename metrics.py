from datetime import datetime
from scapy.all import Packet
from collections import Counter
from config import logger


def measure_throughput(packets: list[Packet], interval_duration: int = 1):
    logger.info("Processing .pcap for throughputs...")
    timestamps = [packet.time for packet in packets]
    sizes = [len(packet) for packet in packets]

    start_time = min(timestamps)
    end_time = max(timestamps)

    interval_start = start_time
    throughputs = []
    intervals = []

    while interval_start <= end_time:
        bytes_in_window = 0
        for i, timestamp in enumerate(timestamps):
            if interval_start <= timestamp < interval_start + 1:
                bytes_in_window += sizes[i]

        throughput_bps = (bytes_in_window * 8) / interval_duration
        throughputs.append(throughput_bps)
        intervals.append(datetime.fromtimestamp(float(interval_start)))

        interval_start += interval_duration
    logger.info(f"Computed throughputs for {interval_duration} second intervals.")
    return throughputs, intervals


def get_protocol_distribution(packets: list[Packet]):
    logger.info("Processing .pcap for protocol distribution...")
    protocols_count = Counter()

    protocol_names = {
        1: "ICMP",
        6: "TCP",
        17: "UDP",
        80: "HTTP",
        443: "HTTPS",
        53: "DNS",
        21: "FTP",
        22: "SSH",
        110: "POP3",
        143: "IMAP",
    }

    for pkt in packets:
        if pkt.haslayer("IP"):
            ip_layer = pkt["IP"]
            proto = ip_layer.proto

            protocol_name = protocol_names.get(proto, "Other")
            protocols_count[protocol_name] += 1
    logger.info("Computed protocol distribution.")
    return protocols_count


def get_packet_size_distribution(packets: list[Packet]):
    logger.info("Processing .pcap for packet sizes...")
    pkt_sizes = [len(pkt) for pkt in packets]
    logger.info("Computed packet size distribution.")
    return pkt_sizes


def measure_jitter(packets: list[Packet]):
    logger.info("Processing .pcap for inter-arrival times...")
    inter_arrival_times = [
        packets[i].time - packets[i - 1].time for i in range(1, len(packets))
    ]
    jitter_values = [
        abs(inter_arrival_times[i] - inter_arrival_times[i - 1])
        for i in range(1, len(inter_arrival_times))
    ]
    logger.info("Computed jitter values.")
    return jitter_values
