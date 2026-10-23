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


---

## 📌 Topic 4: What is `{ }` (Curly Braces) in Python?

Curly braces `{}` have two main uses in Python:

### 1. Placeholder inside f-strings (Variable Substitution)
When you put an `f` before quotes, `{}` tells Python: *"Evaluate the variable inside me!"*

* **In Bash**:
  ```bash
  echo "Deploying to server: ${server_name}"
  ```
* **In Python**:
  ```python
  print(f"Deploying to server: {server_name}")
  ```
  If `server_name = "web-01"`, `{server_name}` is replaced with `"web-01"`. Without `{}`, Python would literally print the word `server_name`.

### 2. Dictionaries (Key-Value pairs like JSON or Bash `declare -A`)
Outside strings, `{}` defines a Dictionary (like a JSON object in Kubernetes manifests or Ansible):
```python
server_info = {
    "hostname": "web-01",
    "ip": "192.168.1.10",
    "port": 443
}

print(server_info["ip"])  # Prints: 192.168.1.10
```

---

## 📌 Topic 5: What is `\n` in `print("\n...")`?

`\n` represents a **Newline** character (the Enter key).

* **In Bash**:
  ```bash
  echo -e "\n--- Checking servers ---"
  ```
* **In Python**:
  ```python
  print("\n--- Checking servers ---")
  ```
The `\n` inserts a blank line above the text in your terminal. It makes DevOps script output much easier to read when scrolling through long CI/CD build logs.

Common escape characters:
* `\n`: Newline (Enter)
* `\t`: Tab space (indents text)

---

## 📌 Topic 6: What is `.startswith(...)`?

`.startswith()` is a built-in Python string method that checks if a string begins with specific characters. It returns either `True` or `False`.

### 🧠 The Bash vs Python Comparison

* **In Bash (wildcard match or grep)**:
  ```bash
  # Check if server starts with "web"
  if [[ "$server" == web* ]]; then
      echo "This is a web server: $server"
  fi
  ```

* **In Python**:
  ```python
  if server.startswith("web"):
      print(f"This is a web server: {server}")
  ```

### Useful DevOps String Methods:
```python
server = "k8s-worker-node-01.us-east-1.compute.internal"

server.startswith("k8s")       # Returns True
server.endswith(".internal")    # Returns True
"worker" in server             # Returns True (like: echo $server | grep worker)
```
