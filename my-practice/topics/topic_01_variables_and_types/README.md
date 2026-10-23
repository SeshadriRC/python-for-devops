# Topic 1: Variables & Data Types (DevOps Practical)

## 🎯 What is this topic?
In DevOps scripts, you constantly work with server names, IP addresses, port numbers, CPU utilization percentages, and status flags. Python stores these in **Variables** using 4 basic **Data Types**.

---

## 4 Core Data Types in DevOps

| Data Type | What it is | DevOps Example | Code |
| :--- | :--- | :--- | :--- |
| **String (`str`)** | Text inside quotes | Server name, IP, Docker image | `server = "web-01"` |
| **Integer (`int`)** | Whole number | Port number, Replica count | `port = 8080` |
| **Float (`float`)** | Decimal number | CPU usage %, memory in GB | `cpu_usage = 74.5` |
| **Boolean (`bool`)** | `True` or `False` | Is container running?, SSL enabled? | `is_running = True` |

---

## 💡 Key Rules:
1. **No dollar sign (`$`)**: Unlike Bash where you declare `PORT=80` and call `$PORT`, in Python you write `port = 80` and use `port` directly.
2. **Checking Types**: You can check the type of any variable using `type(variable)`.
3. **Type Conversion**:
   - String to Int: `int("8080")` -> `8080`
   - Int to String: `str(8080)` -> `"8080"`
