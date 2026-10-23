"""
Lesson 3: Reading files line by line
In Bash:
    while IFS= read -r line; do
        echo "Server: $line"
    done < inventory.txt
"""

# 'with open' automatically opens and closes the file cleanly
filename = "00_basics_for_devops/inventory.txt"

print(f"Reading from {filename}:")

with open(filename, "r") as file:
    for line in file:
        # .strip() removes trailing newline and extra spaces (like `tr -d '\n'`)
        server_name = line.strip()
        if server_name:
            print(f"-> Target host: {server_name}")
