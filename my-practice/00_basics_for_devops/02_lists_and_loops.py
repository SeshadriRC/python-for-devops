"""
Lesson 2: Lists & Loops (Working with multiple servers/pods)
In Bash, you do:
    SERVERS=("web-01" "web-02" "db-01")
    for s in "${SERVERS[@]}"; do
        echo "Checking $s"
    done
"""

# 1. A List in Python (array of items)
servers = ["web-01", "web-02", "api-01", "db-01"]

print(f"Total servers: {len(servers)}")

# 2. For loop (simple iteration)
print("\n--- Iterating through all servers ---")
for server in servers:
    print(f"Checking status for: {server}")

# 3. Filtering with an `if` condition inside loop
print("\n--- Only Web servers ---")
for server in servers:
    if server.startswith("web"):
        print(f"Found Web tier server: {server}")
