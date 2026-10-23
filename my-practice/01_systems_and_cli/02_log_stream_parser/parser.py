"""
High-performance streaming log parser and metrics aggregator for web server / ingress logs.
Processes logs line-by-line using generators to maintain O(1) memory footprint.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Generator, Iterator

# Standard combined log format with response time:
# $remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent $request_time
LOG_REGEX = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+'
    r'"(?P<method>\S+)\s+(?P<path>\S+)\s+(?P<protocol>[^"]+)"\s+'
    r'(?P<status>\d{3})\s+(?P<bytes>\d+)\s+(?P<duration>[\d\.]+)'
)


@dataclass(frozen=True)
class LogEntry:
    ip: str
    timestamp: str
    method: str
    path: str
    protocol: str
    status: int
    bytes_sent: int
    duration_seconds: float

    @property
    def is_server_error(self) -> bool:
        return 500 <= self.status <= 599

    @property
    def is_client_error(self) -> bool:
        return 400 <= self.status <= 499


def stream_log_entries(file_path: Path | str) -> Generator[LogEntry, None, None]:
    """
    Streams and parses log entries one line at a time.
    Keeps memory usage constant even for multi-gigabyte log files.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Log file not found: {path}")

    with path.open("r", encoding="utf-8", errors="replace") as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue

            match = LOG_REGEX.match(line)
            if not match:
                continue

            data = match.groupdict()
            yield LogEntry(
                ip=data["ip"],
                timestamp=data["timestamp"],
                method=data["method"],
                path=data["path"],
                protocol=data["protocol"],
                status=int(data["status"]),
                bytes_sent=int(data["bytes"]),
                duration_seconds=float(data["duration"]),
            )


def aggregate_log_stats(entries: Iterator[LogEntry]) -> dict:
    """
    Aggregates metrics from an iterator of LogEntry objects.
    """
    total_requests = 0
    status_counts: Counter[int] = Counter()
    server_error_paths: Counter[str] = Counter()
    total_latency = 0.0
    slow_requests: list[dict] = []

    for entry in entries:
        total_requests += 1
        status_counts[entry.status] += 1
        total_latency += entry.duration_seconds

        if entry.is_server_error:
            server_error_paths[entry.path] += 1

        if entry.duration_seconds > 1.0:
            slow_requests.append({
                "path": entry.path,
                "status": entry.status,
                "duration": entry.duration_seconds,
                "timestamp": entry.timestamp,
            })

    avg_latency = round(total_latency / total_requests, 4) if total_requests else 0.0

    return {
        "total_requests": total_requests,
        "status_distribution": dict(status_counts),
        "total_5xx_errors": sum(count for status, count in status_counts.items() if 500 <= status <= 599),
        "top_5xx_failing_endpoints": server_error_paths.most_common(5),
        "avg_latency_seconds": avg_latency,
        "slow_requests_count": len(slow_requests),
        "slow_requests": slow_requests,
    }


if __name__ == "__main__":
    target_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "sample.log"
    stats = aggregate_log_stats(stream_log_entries(target_file))
    print(json.dumps(stats, indent=2))
