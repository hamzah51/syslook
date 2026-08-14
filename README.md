# SysMonitor

A small system monitoring dashboard built with Python and Textual.

It shows live CPU, memory, disk, and network usage in a terminal UI and keeps running until you quit with:

- `q`
- then `Enter`

## Features

- CPU usage percentage and per-core values
- Memory usage statistics
- Disk usage for the current system drive
- Network upload and download speeds


## Requirements

- Python 3.12+
- `psutil`
- `textual`

## Install

From the project root:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

If you are using the project environment already configured by the workspace, you can also run:

```bash
.venv\Scripts\python.exe -m sysmonitor.app
```

## Run

```bash
python -m sysmonitor.app
```

or:

```bash
.venv\Scripts\python.exe -m sysmonitor.app
```

## Project structure

```text
src/
  sysmonitor/
    app.py
    cpu.py
    memory.py
    disk.py
    network.py
```
