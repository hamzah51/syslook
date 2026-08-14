import psutil as ps


def get_memory_usage() -> dict:
    """Return current memory usage information in a readable format.

    Returns:
        dict: Total, used, available, free memory values in gigabytes,
        along with the usage percentage and unit label.
    """
    memory = ps.virtual_memory()
    gb = 1024 ** 3

    return {
        "total": round(memory.total / gb, 2),
        "used": round(memory.used / gb, 2),
        "available": round(memory.available / gb, 2),
        "free": round(memory.free / gb, 2),
        "percent": memory.percent,
        "unit": "GB",
    }