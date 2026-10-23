# Lab 1.2: Streaming Log Parser & Anomaly Aggregator

## 🎯 Objective
In DevOps and SRE, analyzing container or ingress logs (NGINX, Envoy, Kubernetes systemd) is routine.
While `awk` and `grep` work for one-off CLI triage, automation scripts need:
1. **Memory efficiency (Streaming)**: Never load a 5GB log into RAM with `.readlines()` or `.read()`. Use Python generators (`yield`).
2. **Regex Parsing with Named Groups**: Extract IP, Timestamp, HTTP Method, Path, Status Code, and Latency cleanly.
3. **Structured Aggregation**: Count error frequencies (4xx, 5xx), top offenders, and slow requests using `collections.Counter`.
4. **Structured JSON Output**: Ready to feed into Slack webhooks, Datadog metrics, or Alertmanager.

---

## 🧠 Mental Model: Bash vs. Python

| Task | Bash Pattern | Idiomatic Python |
| :--- | :--- | :--- |
| **Extract 5xx errors** | `grep 'HTTP/1.1" 5' access.log` | `re.compile(...)` filter with named group `(?P<status>5\d\d)` |
| **Count top endpoints** | `awk '{print $7}' \| sort \| uniq -c \| sort -nr \| head -5` | `collections.Counter(log.path for log in logs).most_common(5)` |
| **Handle huge files** | `while read -r line; do ... done < file` | `with open(path) as f: for line in f:` (O(1) memory streaming) |

---

## 🛠️ Files in this Lab
- [`parser.py`](file:///mnt/c/Myfolder/MyProjects/python-for-devops/my-practice/01_systems_and_cli/02_log_stream_parser/parser.py): The streaming parser and aggregator.
- [`sample.log`](file:///mnt/c/Myfolder/MyProjects/python-for-devops/my-practice/01_systems_and_cli/02_log_stream_parser/sample.log): Synthetic NGINX access log containing 200s, 404s, and 500s.
- [`test_parser.py`](file:///mnt/c/Myfolder/MyProjects/python-for-devops/my-practice/01_systems_and_cli/02_log_stream_parser/test_parser.py): Unit tests for the parser.
