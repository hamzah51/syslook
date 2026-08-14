import psutil


def check_disk_usage(path: str = "/", in_gb: bool = True) -> dict:
    """Retrieves total, used, and free disk space for a given path.

    Args:
        path: The directory path to check ('/' for Unix, 'C:\\' for Windows).
        in_gb: If True, converts the returned values from bytes to gigabytes.

    Returns:
        dict: A dictionary containing total, used, free, percent, and unit metrics.
    """
    try:
        usage = psutil.disk_usage(path)
        divisor = 1024 ** 3 if in_gb else 1
        unit = "GB" if in_gb else "bytes"

        return {
            "total": round(usage.total / divisor, 2),
            "used": round(usage.used / divisor, 2),
            "free": round(usage.free / divisor, 2),
            "percent": usage.percent,
            "unit": unit,
        }
    except FileNotFoundError:
        return {"error": f"The path '{path}' was not found."}
    except PermissionError:
        return {"error": f"Permission denied for path '{path}'."}
    except OSError:
        return {"error": f"Could not access path '{path}'."}
