import psutil as ps


def get_cpu_usage() -> dict:
    """Return current CPU usage statistics.

    Returns:
        dict: A dictionary containing the overall CPU usage percentage,
        the logical CPU count, and per-core percentages.
    """
    return {
        "percent": ps.cpu_percent(interval=0.5),
        "count": ps.cpu_count(),
        "per_core": ps.cpu_percent(interval=0.5, percpu=True),
    }