from datetime import datetime
from scapy import packet


def measure_throughput(packets: list[packet.Packet], interval_duration: int = 1):
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

        throughputs.append(bytes_in_window)
        intervals.append(datetime.utcfromtimestamp(float(interval_start)))
        interval_start += interval_duration

    return throughputs, intervals
