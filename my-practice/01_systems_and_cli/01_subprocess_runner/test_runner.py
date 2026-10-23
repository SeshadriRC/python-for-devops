"""
Tests for production subprocess runner.
Verifies exit code capture, timeout handling, and environment isolation.
"""

import subprocess
import pytest
from runner import CommandResult, execute_command


def test_successful_command():
    result = execute_command(["echo", "hello devops"])
    assert result.is_success
    assert result.returncode == 0
    assert result.stdout == "hello devops"
    assert result.stderr == ""
    assert result.duration_seconds >= 0.0
    assert not result.timed_out


def test_command_string_shlex_split():
    result = execute_command("echo 'multi word argument' test")
    assert result.is_success
    assert result.stdout == "multi word argument test"
    assert result.command == ["echo", "multi word argument", "test"]


def test_failing_command():
    result = execute_command(["bash", "-c", "echo 'critical error' >&2; exit 2"])
    assert not result.is_success
    assert result.returncode == 2
    assert result.stderr == "critical error"


def test_failing_command_with_check():
    with pytest.raises(subprocess.CalledProcessError) as exc_info:
        execute_command(["bash", "-c", "exit 3"], check=True)
    assert exc_info.value.returncode == 3


def test_timeout_enforcement():
    result = execute_command(["sleep", "2"], timeout=0.2)
    assert not result.is_success
    assert result.timed_out
    assert result.returncode == -1
    assert result.duration_seconds >= 0.2


def test_binary_not_found():
    with pytest.raises(FileNotFoundError):
        execute_command(["non_existent_binary_xyz123"])


def test_custom_environment():
    result = execute_command(
        ["bash", "-c", "echo $DEPLOY_ENV"],
        env={"DEPLOY_ENV": "production"}
    )
    assert result.is_success
    assert result.stdout == "production"
