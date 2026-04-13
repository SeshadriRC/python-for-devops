## Environment Variables (20:40 - 29:42)

- Environment variables are the preferred way to handle sensitive information like passwords, API keys, or tokens.

    - Security: Unlike command-line arguments, which might be exposed in logs or history, environment variables keep **sensitive data** out of the source code and the command line execution string (21:12 - 27:50).

    - The os module: Use `import os` and the `os.getenv()` function to read these variables within your code (24:30 - 25:10).

    - Setting them: You can export variables in your terminal (e.g., export password=mysecret) before running your script (23:55).

By using these methods, you create more robust and secure programs that are ready for professional DevOps environments, such as CI/CD pipelines (26:58).

<img width="1886" height="836" alt="image" src="https://github.com/user-attachments/assets/5a1e7ac2-f087-43b1-9577-1b1ce841151c" />


```python
import os
print(os.getenv("password"))  # this will print the value of the environment variable "password"
print(os.getenv("apitoken"))  # this will print the value of the environment variable "apitoken"
```

---
