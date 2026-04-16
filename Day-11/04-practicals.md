# Practice Exercises and Examples

## Example: Managing a Dictionary of Server Configurations and Optimizing Retrieval

### Scenario:
Suppose you are managing server configurations using a dictionary.

```python
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
```

### Function for Retrieval:
```python
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
```

### Example Usage:
```python
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
```

In this example, the function `get_server_status` optimizes the retrieval of the server status by using the `get` method and providing a default value if the server name is not found.

# Explanation

Let’s break this step by step in a simple way.

---

## 🧩 1. Dictionary structure (`server_config`)

```python
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
```

👉 This is a **nested dictionary**.

### Think of it like:

* Outer dictionary → list of servers
* Inner dictionary → details of each server

Example:

```
server2
  ├── ip: 192.168.1.2
  ├── port: 8000
  └── status: inactive
```

---

## 🧠 2. Function: `get_server_status`

```python
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
```

This line is doing **safe lookup in 2 steps**.

---

### 🔹 Step 1: Get server block

```python
server_config.get(server_name, {})
```

* If `server_name` exists → returns its details dictionary
* If NOT exists → returns `{}` (empty dictionary)

Example:

```python
server_config.get('server2')
# returns:
{'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'}
```

---

### 🔹 Step 2: Get status inside that server

```python
... .get('status', 'Server not found')
```

* Looks for `"status"` inside the inner dictionary
* If missing → returns `"Server not found"`

---

## ⚙️ 3. Execution part

```python
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
```

### What happens:

1. `server_name = 'server2'`
2. Function is called:

   ```python
   get_server_status('server2')
   ```
3. It finds:

   ```python
   'inactive'
   ```
4. Output:

```
server2 status: inactive
```

---

## 🚨 Why `.get()` is used twice?

It prevents errors like:

### ❌ Without `.get()`

```python
server_config['server4']['status']
```

→ would crash (KeyError)

### ✅ With `.get()`

* Safe even if server or status is missing

---

## 🧠 Final simple understanding

This code means:

> “Give me the status of a server if it exists, otherwise tell me it’s not found.”

---

If you want, I can also show:

* same logic using `if-else`
* or how DevOps engineers use this pattern in real monitoring scripts 👍
