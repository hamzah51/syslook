from __future__ import annotations

import platform

try:
    from .cpu import get_cpu_usage
    from .disk import check_disk_usage
    from .memory import get_memory_usage
    from .network import get_network_speed
except ImportError:  # pragma: no cover
    from sysmonitor.cpu import get_cpu_usage
    from sysmonitor.disk import check_disk_usage
    from sysmonitor.memory import get_memory_usage
    from sysmonitor.network import get_network_speed

from textual.app import App, ComposeResult
from textual.widgets import Footer, Static


class SysMonitorApp(App):
    CSS = """
    Screen {
        background: #121a22;
        color: white;
    }

    #title {
        width: 100%;
        content-align: center middle;
        text-style: bold;
        color: #7dd3fc;
        padding: 1 0;
        margin-bottom: 1;
    }

    .panel {
        width: 100%;
        margin: 0 0 1 0;
        padding: 1 2;
        background: #1f2937;
        border: round #374151;
    }

    #status {
        color: #fbbf24;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.quit_pending = False

    def compose(self) -> ComposeResult:
        yield Static("System Monitor", id="title")
        yield Static("Press q, then Enter to quit.", id="status", classes="panel")
        yield Static("", id="cpu", classes="panel")
        yield Static("", id="memory", classes="panel")
        yield Static("", id="disk", classes="panel")
        yield Static("", id="network", classes="panel")
        yield Footer()

    def on_mount(self) -> None:
        self.refresh_metrics()
        self.set_interval(1.0, self.refresh_metrics)

    def refresh_metrics(self) -> None:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk_path = "C:\\" if platform.system() == "Windows" else "/"
        disk = check_disk_usage(path=disk_path)
        network = get_network_speed(interval=1.0)

        self.query_one("#cpu", Static).update(
            f"CPU: {cpu['percent']:.1f}% | Cores: {cpu['count']} | Per core: {cpu['per_core']}"
        )
        self.query_one("#memory", Static).update(
            f"Memory: {memory['percent']:.1f}% | Used: {memory['used']}{memory['unit']} / {memory['total']}{memory['unit']} | Available: {memory['available']}{memory['unit']}"
        )
        self.query_one("#disk", Static).update(
            f"Disk: {disk['percent']:.1f}% | Used: {disk['used']}{disk['unit']} / {disk['total']}{disk['unit']} | Free: {disk['free']}{disk['unit']}"
        )
        self.query_one("#network", Static).update(
            "Network: "
            f"Down: {network['download_mbps']} Mbps | "
            f"Up: {network['upload_mbps']} Mbps"
        )

        if self.quit_pending:
            self.query_one("#status", Static).update("Quit requested. Press Enter to confirm.")
        else:
            self.query_one("#status", Static).update("Press q, then Enter to quit.")

    def on_key(self, event) -> None:
        if event.key.lower() == "q":
            self.quit_pending = True
            self.query_one("#status", Static).update("Quit requested. Press Enter to confirm.")
            event.stop()
            return

        if event.key == "enter" and self.quit_pending:
            self.exit()
            return

        if event.key == "escape" and self.quit_pending:
            self.quit_pending = False
            self.query_one("#status", Static).update("Press q, then Enter to quit.")


def main() -> None:
    SysMonitorApp().run()


if __name__ == "__main__":
    main()