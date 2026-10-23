"""
Lesson 1: Variables & Reading Environment Variables
In Bash, you do:
    ENV=${ENVIRONMENT:-development}
    echo "Current env is: $ENV"
"""

import os

# 1. Variables in Python (no $ needed)
app_name = "payment-gateway"
replicas = 3
is_enabled = True

# 2. Reading Environment Variables (just like `os.getenv` or `$VARIABLE` in Bash)
# If ENVIRONMENT is not set, it defaults to 'development'
environment = os.getenv("ENVIRONMENT", "development")

# 3. Printing output (just like `echo`)
print(f"Service: {app_name}")
print(f"Replicas: {replicas}")
print(f"Target Environment: {environment}")

# 4. If / Else condition (indentation matters in Python!)
if environment == "production":
    print("⚠️ ALERT: Running in PRODUCTION mode!")
else:
    print("✅ Running in non-production mode.")
