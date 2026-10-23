#!/usr/bin/env python3
"""
opsctl: Production DevOps & SRE CLI Toolkit.
Demonstrates Click subcommands, exit code enforcement, and dual human/JSON outputs.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table

console = Console()
err_console = Console(stderr=True)


@click.group()
@click.version_option(version="1.0.0", prog_name="opsctl")
def cli() -> None:
    """opsctl: Automated SRE & DevOps Operations CLI."""
    pass


@cli.group(name="sys")
def sys_group() -> None:
    """Host & system diagnostic commands."""
    pass


@sys_group.command(name="health")
@click.option("--path", default="/", help="Filesystem mount path to inspect.")
@click.option(
    "--disk-threshold",
    default=85.0,
    type=float,
    show_default=True,
    help="Alert threshold percentage for disk utilization.",
)
@click.option("--json", "json_output", is_flag=True, help="Output machine-readable JSON.")
def sys_health(path: str, disk_threshold: float, json_output: bool) -> None:
    """Checks filesystem capacity and CPU load metrics."""
    try:
        usage = shutil.disk_usage(path)
    except FileNotFoundError:
        err_console.print(f"[bold red]Error:[/] Path '{path}' does not exist.")
        sys.exit(2)

    total_gb = usage.total / (1024**3)
    used_gb = usage.used / (1024**3)
    free_gb = usage.free / (1024**3)
    used_pct = round((usage.used / usage.total) * 100, 2)

    # CPU load average (1m, 5m, 15m) on POSIX systems
    load_1, load_5, load_15 = os.getloadavg() if hasattr(os, "getloadavg") else (0.0, 0.0, 0.0)
    cpu_count = os.cpu_count() or 1

    is_unhealthy = used_pct >= disk_threshold

    payload = {
        "status": "CRITICAL" if is_unhealthy else "HEALTHY",
        "filesystem": {
            "path": path,
            "total_gb": round(total_gb, 2),
            "used_gb": round(used_gb, 2),
            "free_gb": round(free_gb, 2),
            "used_percent": used_pct,
            "threshold_percent": disk_threshold,
        },
        "load_average": {
            "1m": round(load_1, 2),
            "5m": round(load_5, 2),
            "15m": round(load_15, 2),
            "cpu_count": cpu_count,
        },
    }

    if json_output:
        click.echo(json.dumps(payload, indent=2))
    else:
        table = Table(title=f"System Health Triage ({path})")
        table.add_column("Metric", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        table.add_column("Status", style="bold")

        disk_status = f"[red]BREACHED (>= {disk_threshold}%)[/]" if is_unhealthy else "[green]OK[/]"
        table.add_row("Disk Usage", f"{used_pct}% ({used_gb:.1f}GB / {total_gb:.1f}GB)", disk_status)
        table.add_row("Load Avg (1m, 5m, 15m)", f"{load_1:.2f}, {load_5:.2f}, {load_15:.2f} ({cpu_count} CPUs)", "[green]OK[/]")

        console.print(table)

    # Production pattern: Exit code 1 indicates threshold violation
    if is_unhealthy:
        sys.exit(1)


if __name__ == "__main__":
    cli()
