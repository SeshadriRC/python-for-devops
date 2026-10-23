# Lab 1.1: Production-Grade Subprocess Execution

## 🎯 Objective
As a DevOps engineer, executing OS binaries (e.g., `git`, `docker`, `kubectl`, `aws`, `terraform`) from Python is common. However, naive implementations (`os.system`, `subprocess.Popen(..., shell=True)`) introduce:
1. **Shell Injection vulnerabilities**.
2. **Zombie processes / unhandled timeouts** hanging CI/CD pipelines indefinitely.
3. **Lost stderr/stdout** and silent failures.
4. **Platform-dependent path failures**.

In this lab, you learn how to build an enterprise-ready, defensive command runner function using Python's `subprocess` standard library and type hints.

---

## 🧠 Mental Model: Bash vs. Python

| Feature | Bash Pattern | Idiomatic Python |
| :--- | :--- | :--- |
| **Fail on error** | `set -e` | `subprocess.run(..., check=True)` or explicit check on `result.returncode != 0` |
| **Pipeline errors**| `set -o pipefail` | Chain commands via `Popen(stdout=PIPE)` or pass stdout to stdin |
| **Timeout protection** | `timeout 10s my_cmd` | `subprocess.run(cmd, timeout=10)` -> catch `TimeoutExpired` |
| **Safe arguments** | `"$@"` / quote escaping | Pass list of args: `["kubectl", "get", "pods"]` (`shell=False`) |
| **Missing binary** | `command -v my_cmd` | Catch `FileNotFoundError` or check `shutil.which("my_cmd")` |
| **Signal handling** | `trap cleanup EXIT INT` | `signal.signal(signal.SIGINT, handler)` / `try...finally` |

---

## 🛠️ Files in this Lab
- [`runner.py`](file:///mnt/c/Myfolder/MyProjects/python-for-devops/my-practice/01_systems_and_cli/01_subprocess_runner/runner.py): The core execution engine.
- [`test_runner.py`](file:///mnt/c/Myfolder/MyProjects/python-for-devops/my-practice/01_systems_and_cli/01_subprocess_runner/test_runner.py): Verification tests using `pytest`.

---

## 🚀 Hands-On Practice
Run the tests:
```bash
source .venv/bin/activate
pytest 01_systems_and_cli/01_subprocess_runner/test_runner.py -v
```
