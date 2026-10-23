# Python for DevOps & SRE — Practical Lab Series

Hands-on, production-grade Python practice designed specifically for Senior DevOps / SRE engineers transitioning from Bash/Shell and declarative IaC to building robust internal tooling, controllers, CLI utilities, and automation agents.

---

## 🛠️ Environment Setup
- Python: `3.12+`
- Package & Environment Manager: [`uv`](https://github.com/astral-sh/uv) (installed at `~/.local/bin/uv`)
- Virtual Environment: `.venv`

```bash
# Add uv to PATH (if not already in ~/.bashrc)
export PATH="$HOME/.local/bin:$PATH"

# Activate environment
source .venv/bin/activate
```

---

## 🗺️ Practical Roadmap

### Phase 1: Systems Automation & CLI Tooling (Standard Library & Core)
*Goal: Replace fragile bash one-liners with resilient, typed, testable Python scripts.*
- **Lab 1.1**: Safe Process Execution & Signal Handling (`subprocess`, `signal`, `shlex`, exit codes)
- **Lab 1.2**: File Systems & Log Parsing (`pathlib`, `re`, streaming large log files without OOM)
- **Lab 1.3**: Production CLI Tooling (`argparse` vs `click`, structured JSON output, exit codes)
- **Lab 1.4**: Structured Logging & Configuration (`logging`, `json`, `os.environ`, `.env`)

### Phase 2: Networking, APIs & Secrets
*Goal: Interact with infrastructure APIs, webhooks, and secret managers.*
- **Lab 2.1**: REST APIs & Resilient HTTP Clients (`requests`/`httpx`, retry logic, exponential backoff)
- **Lab 2.2**: HashiCorp Vault / Secret Engine Integration (AppRole auth, dynamic secret rotation)
- **Lab 2.3**: Data Modeling & Validation (`pydantic` schemas for configs and API payloads)

### Phase 3: Cloud & Orchestration Automation
*Goal: Write custom operators, audit scripts, and lifecycle hooks.*
- **Lab 3.1**: AWS SDK (`boto3`) — Untagged/Orphaned resource cleaner, S3 lifecycle manager
- **Lab 3.2**: Docker Engine API (`docker-py`) — Container health inspector & image prune daemon
- **Lab 3.3**: Kubernetes API (`kubernetes`) — Pod crash-loop detector, automated restart/eviction policy

### Phase 4: Observability, GitOps & Production Tooling
*Goal: Synthetic monitoring, metrics scraping, drift detection, and CI/CD automation.*
- **Lab 4.1**: Prometheus Metric Exporter (Custom Prometheus client publishing cluster/app metrics)
- **Lab 4.2**: GitOps & IaC Drift Detection (Parsing Terraform plan JSON / Helm manifests)
- **Lab 4.3**: Unit & Integration Testing (`pytest`, mocking external HTTP & subprocess calls)

---

## 📁 Repository Structure
```text
my-practice/
├── 01_systems_and_cli/
├── 02_apis_and_secrets/
├── 03_cloud_and_k8s/
├── 04_observability_and_gitops/
├── .venv/
├── .gitignore
└── README.md
```
