import psutil as ps

def cpu_usage():
    """Returns CPU stats
    Args:
        time (int): The time object
        cpu (int): The cpu object
    Returns:
        cpu_times: 
            user: time spent by normal processes executing in user mode; on Linux this also includes guest time

            system: time spent by processes executing in kernel mode

            idle: time spent doing nothing
            cpu_percent: Time spent in total percentage.
        cpu_percent:
            Return a float representing the current system-wide CPU utilization as a percentage.
    """
    cpu_times = ps.cpu_times()
    cpu_percent = ps.cpu_percent(interval=1)
    return [
        {
            "user": cpu_times.user,
            "system": cpu_times.system,
            "idle": cpu_times.idle
        },
        {
            "percent": cpu_percent
        }
    ]
def memory_usage():
    """Returns Memory stats
    Returns:
        memory_stats: 
            total: total physical memory available
            available: the memory that can be given instantly to processes without the system going into swap
            used: memory used, calculated differently depending on the platform and designed for informational purposes only
            free: memory not being used at all (zeroed) that is readily available; note that this doesn't reflect the actual memory available (use available instead)
            percent: the percentage usage calculated as (total - available) / total * 100
    """
    memory_stats = ps.virtual_memory()
    return {
        "total": memory_stats.total,
        "available": memory_stats.available,
        "used": memory_stats.used,
        "free": memory_stats.free,
        "percent": memory_stats.percent
    }

        
try:
    while True:
        cpu_stats = cpu_usage()
        user = cpu_stats[0].get("user")
        system = cpu_stats[0].get("system")
        idle = cpu_stats[0].get("idle")
        percent = cpu_stats[1].get("percent")
        print(f"CPU Usage: {percent}% | User: {user} | System: {system} | Idle: {idle}")

        memory_stats = memory_usage()
        total = memory_stats.get("total")
        available = memory_stats.get("available")
        used = memory_stats.get("used")
        free = memory_stats.get("free")
        percent = memory_stats.get("percent")

        print(f"Memory Usage: {percent}% | Total: {total} | Available: {available} | Used: {used} | Free: {free}")
        print()
    
except KeyboardInterrupt:
    print("Exiting...")


