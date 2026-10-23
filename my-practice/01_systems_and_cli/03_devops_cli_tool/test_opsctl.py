import json
from click.testing import CliRunner
from opsctl import cli


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "opsctl, version" in result.output


def test_sys_health_json():
    runner = CliRunner()
    result = runner.invoke(cli, ["sys", "health", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["status"] in ("HEALTHY", "CRITICAL")
    assert "filesystem" in data
    assert "load_average" in data


def test_sys_health_threshold_breach():
    runner = CliRunner()
    # Setting threshold to 0.0001% will trigger failure (exit code 1)
    result = runner.invoke(cli, ["sys", "health", "--disk-threshold", "0.0001", "--json"])
    assert result.exit_code == 1
    data = json.loads(result.output)
    assert data["status"] == "CRITICAL"


def test_sys_health_invalid_path():
    runner = CliRunner()
    result = runner.invoke(cli, ["sys", "health", "--path", "/non/existent/path/xyz"])
    assert result.exit_code == 2
