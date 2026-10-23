# DevOps Python Study Notes

Quick reference guide comparing Bash patterns to Python for DevOps & SRE tasks.

---

## 📌 Topic 1: Environment Variables (`os.getenv`)

### 🧠 The Bash vs Python Comparison
In Bash:
```bash
# Set a default value if ENVIRONMENT is not set
environment="${ENVIRONMENT:-development}"
```

In Python:
```python
import os

# Exactly the same behavior:
environment = os.getenv("ENVIRONMENT", "development")
```

---

### 🔍 Anatomy of `os.getenv("KEY", "default")`

| Code Component | Meaning |
| :--- | :--- |
| `import os` | Imports Python's built-in Operating System library. |
| `os.getenv(...)` | Function: **"Get Environment Variable"**. |
| `"ENVIRONMENT"` | The exact name of the OS environment variable (like `$ENVIRONMENT`). |
| `"development"` | The **fallback / default value** used if the variable does not exist. |
| `environment =` | Stores the resulting string in a Python variable named `environment`. |

---

### ⚙️ How It Behaves in Practice

#### Scenario A: Variable is NOT set in the shell
```bash
python3 01_variables_and_env.py
```
* Python checks the OS for `$ENVIRONMENT`.
* It does not find it.
* It uses the fallback: `"development"`.
* Value of `environment`: `"development"`.

#### Scenario B: Variable IS set in the shell / CI / Docker
```bash
ENVIRONMENT=production python3 01_variables_and_env.py
```
* Python checks the OS for `$ENVIRONMENT`.
* It finds `"production"`.
* It ignores the fallback.
* Value of `environment`: `"production"`.

---

### 🚢 Why DevOps Engineers Need This
In real-world Kubernetes, Docker, and CI/CD pipelines, configurations are injected via environment variables:

```yaml
# Kubernetes Pod Spec:
env:
  - name: ENVIRONMENT
    value: "production"
  - name: AWS_REGION
    value: "us-east-1"
```

In your Python automation script:
```python
import os

# Safe against missing variables:
env = os.getenv("ENVIRONMENT", "development")
region = os.getenv("AWS_REGION", "us-east-1")
db_port = int(os.getenv("DB_PORT", "5432"))
```
Using `os.getenv()` with defaults prevents scripts from crashing with `KeyError` if a variable is forgotten in a config map or `.env` file.

---

## 📌 Topic 2: Printing & Variables (f-strings vs `echo`)

| Task | Bash | Python |
| :--- | :--- | :--- |
| **Assign string** | `APP="auth-service"` | `app = "auth-service"` |
| **Assign integer** | `PORT=8080` | `port = 8080` |
| **Print with variables** | `echo "App: $APP on port: $PORT"` | `print(f"App: {app} on port: {port}")` |

> 💡 **Tip**: The `f` before the quote in `f"..."` stands for **formatted string**. It allows you to put any variable directly inside `{}`.

---

## 📌 Topic 3: Conditions (if / else)

In Bash:
```bash
if [ "$ENVIRONMENT" = "production" ]; then
    echo "Running in PROD"
else
    echo "Running in NON-PROD"
fi
```

In Python:
```python
if environment == "production":
    print("Running in PROD")
else:
    print("Running in NON-PROD")
```

> ⚠️ **Key Python Rule**: Python uses **4 spaces (indentation)** instead of `then...fi`. Everything indented under `if` belongs to that block.
