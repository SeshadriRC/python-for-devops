from pathlib import Path
import pytest
from parser import aggregate_log_stats, stream_log_entries, LogEntry


SAMPLE_LOG_PATH = Path(__file__).parent / "sample.log"


def test_stream_log_entries():
    entries = list(stream_log_entries(SAMPLE_LOG_PATH))
    assert len(entries) == 10
    first = entries[0]
    assert first.ip == "192.168.1.10"
    assert first.method == "GET"
    assert first.path == "/api/v1/health"
    assert first.status == 200
    assert first.duration_seconds == 0.002


def test_aggregate_log_stats():
    entries = stream_log_entries(SAMPLE_LOG_PATH)
    stats = aggregate_log_stats(entries)

    assert stats["total_requests"] == 10
    assert stats["status_distribution"][200] == 4
    assert stats["status_distribution"][403] == 1
    assert stats["status_distribution"][404] == 2
    assert stats["status_distribution"][500] == 2
    assert stats["status_distribution"][502] == 1
    assert stats["total_5xx_errors"] == 3

    # Check top failing endpoint
    top_failing = stats["top_5xx_failing_endpoints"]
    assert len(top_failing) == 1
    assert top_failing[0] == ("/api/v1/checkout", 3)

    # Check slow requests (> 1.0s)
    assert stats["slow_requests_count"] == 2
