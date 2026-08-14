import time

import psutil


def get_network_speed(interval: float = 1.0) -> dict:
    """Calculate upload and download speeds over the given interval.

    Args:
        interval: The time to measure in seconds.

    Returns:
        dict: A dictionary containing upload/download speeds in MB/s and Mbps.
    """
    start_io = psutil.net_io_counters()
    time.sleep(interval)
    end_io = psutil.net_io_counters()

    bytes_sent = end_io.bytes_sent - start_io.bytes_sent
    bytes_recv = end_io.bytes_recv - start_io.bytes_recv

    upload_mb_s = (bytes_sent / (1024 * 1024)) / interval
    download_mb_s = (bytes_recv / (1024 * 1024)) / interval

    return {
        "upload_mb_s": round(upload_mb_s, 2),
        "download_mb_s": round(download_mb_s, 2),
        "upload_mbps": round(upload_mb_s * 8, 2),
        "download_mbps": round(download_mb_s * 8, 2),
    }
#