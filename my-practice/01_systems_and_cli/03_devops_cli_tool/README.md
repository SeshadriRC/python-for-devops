# Lab 1.3: Production DevOps CLI Tool (`opsctl`)

## 🎯 Objective
In enterprise platform engineering, internal developer platforms (IDPs) and SRE runbooks rely on customized CLI tools (like `kubectl`, `helm`, `aws`).
Writing custom Python CLIs with [`click`](https://click.palletsprojects.com/) allows you to:
1. Support subcommands (`opsctl sys health`, `opsctl logs parse`).
2. Implement **Dual Output Modes**: Rich terminal tables for human engineers, and strict JSON (`--json`) for CI/CD pipelines.
3. Enforce **Exit Codes**: Exit 0 on success, Exit 1 on operational thresholds breached (e.g., disk > 90%), Exit 2 on syntax/usage errors.
4. Enable robust automated CLI testing via `click.testing.CliRunner`.

---

## 🛠️ Files in this Lab
- [`opsctl.py`](file:///mnt/c/Myfolder/MyProjects/python-for-devops/my-practice/01_systems_and_cli/03_devops_cli_tool/opsctl.py): The CLI application.
- [`test_opsctl.py`](file:///mnt/c/Myfolder/MyProjects/python-for-devops/my-practice/01_systems_and_cli/03_devops_cli_tool/test_opsctl.py): CLI automated tests.

---

## 🚀 Usage Examples
```bash
source .venv/bin/activate
cd 01_systems_and_cli/03_devops_cli_tool

# Human-readable system health check
python opsctl.py sys health --disk-threshold 85

# Machine-readable JSON output for CI/CD
python opsctl.py sys health --json

# Run unit tests
pytest test_opsctl.py -v
```
