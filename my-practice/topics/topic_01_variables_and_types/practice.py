"""
Topic 1: Practice Script - Variables & Data Types
Run this file with: python3 practice.py
"""

# 1. String (str) - used for names, IDs, paths
container_name = "nginx-frontend"
docker_image = "nginx:1.25-alpine"

# 2. Integer (int) - used for counts, ports, status codes
http_port = 80
desired_replicas = 3

# 3. Float (float) - used for percentages, memory, metrics
cpu_usage_percent = 45.8
memory_free_gb = 12.4

# 4. Boolean (bool) - used for flags (Must be True or False, capitalized)
is_healthy = True
is_maintenance_mode = False

# --- Printing Variables and their Types ---
print("--- Container Deployment Summary ---")
print(f"Container: {container_name}")
print(f"Image:     {docker_image}")
print(f"Port:      {http_port} (Type: {type(http_port).__name__})")
print(f"Replicas:  {desired_replicas}")
print(f"CPU Load:  {cpu_usage_percent}%")
print(f"Healthy:   {is_healthy} (Type: {type(is_healthy).__name__})")

# --- Type Conversion in DevOps ---
# In DevOps, environment variables and command outputs always come as STRINGS!
raw_port_from_env = "8080"  # This is a string because of quotes

# Convert to integer so we can do math or validate port range
port_number = int(raw_port_from_env)
print(f"\nConverted '{raw_port_from_env}' from {type(raw_port_from_env).__name__} to {type(port_number).__name__}: {port_number}")
