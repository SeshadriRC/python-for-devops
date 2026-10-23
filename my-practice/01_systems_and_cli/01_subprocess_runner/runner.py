"""
Production-grade subprocess execution utility for DevOps automation.
Enforces timeouts, safe argument parsing, execution metrics, and defensive error handling.
"""

from __future__ import annotations

import logging
import os
import shlex
import subprocess
import time
from dataclasses import dataclass, field
from typing import Mapping, Sequence

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class CommandResult:
    """Immutable result container for command execution."""
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    duration_seconds: float
    timed_out: bool = False

    @property
    def is_success(self) -> bool:
        """Returns True if the process exited with code 0 and did not time out."""
        return self.returncode == 0 and not self.timed_out


def execute_command(
    command: str | Sequence[str],
    *,
    timeout: float = 30.0,
    cwd: str | None = None,
    env: Mapping[str, str] | None = None,
    check: bool = False,
) -> CommandResult:
    """
    Safely executes a system command with strict timeout and execution metrics.

    Args:
        command: Command string (tokenized via shlex) or list of argument tokens.
        timeout: Maximum execution time in seconds before terminating.
        cwd: Directory path to set as current working directory.
        env: Environment variables dictionary. Merged with os.environ if provided.
        check: If True, raises subprocess.CalledProcessError when returncode != 0.

    Returns:
        CommandResult with captured stdout, stderr, return code, and elapsed time.

    Raises:
        FileNotFoundError: If the binary is not found in PATH.
        subprocess.CalledProcessError: If check=True and process returns non-zero.
    """
    if isinstance(command, str):
        cmd_args = shlex.split(command)
    else:
        cmd_args = list(command)

    if not cmd_args:
        raise ValueError("Cannot execute an empty command.")

    merged_env = None
    if env is not None:
        merged_env = {**os.environ, **env}

    start_time = time.perf_counter()
    logger.debug("Executing command: %s (cwd=%s, timeout=%ss)", cmd_args, cwd, timeout)

    try:
        proc = subprocess.run(
            cmd_args,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=cwd,
            env=merged_env,
            check=False,  # We handle check manually to populate duration
        )
        duration = time.perf_counter() - start_time

        result = CommandResult(
            command=cmd_args,
            returncode=proc.returncode,
            stdout=proc.stdout.strip(),
            stderr=proc.stderr.strip(),
            duration_seconds=round(duration, 3),
            timed_out=False,
        )

        if check and result.returncode != 0:
            raise subprocess.CalledProcessError(
                result.returncode,
                cmd_args,
                output=result.stdout,
                stderr=result.stderr,
            )

        return result

    except subprocess.TimeoutExpired as exc:
        duration = time.perf_counter() - start_time
        logger.warning("Command '%s' timed out after %.2fs", cmd_args[0], timeout)
        stdout = exc.stdout.decode("utf-8", errors="replace").strip() if exc.stdout else ""
        stderr = exc.stderr.decode("utf-8", errors="replace").strip() if exc.stderr else ""

        result = CommandResult(
            command=cmd_args,
            returncode=-1,
            stdout=stdout,
            stderr=stderr,
            duration_seconds=round(duration, 3),
            timed_out=True,
        )

        if check:
            raise exc

        return result

    except FileNotFoundError:
        logger.error("Binary '%s' not found on system PATH", cmd_args[0])
        raise


if __name__ == "__main__":
    # Quick self-test demonstration
    import sys

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    test_cmd = sys.argv[1:] if len(sys.argv) > 1 else ["uname", "-a"]

    print(f"Running: {' '.join(test_cmd)}")
    res = execute_command(test_cmd, timeout=5.0)
    print(f"Status: {'SUCCESS' if res.is_success else 'FAILED'} (exit code: {res.returncode})")
    print(f"Duration: {res.duration_seconds}s")
    print(f"Stdout:\n{res.stdout}")
    if res.stderr:
        print(f"Stderr:\n{res.stderr}")
