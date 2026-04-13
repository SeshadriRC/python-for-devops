
## Command-Line Arguments (1:36 - 20:35)

Instead of modifying source code to change inputs, you can pass values directly when executing a script `(e.g., python calculator.py 2 add 3)`

- The `sys module:` This is an built-in Python module used to read these arguments (8:36).
- sys.argv: Arguments are accessed via this list, where `sys.argv[1], sys.argv[2]`, etc., represent the inputs provided after the script name (9:00).
- Important Note: Python reads these inputs as strings by default, so you must convert them (e.g., using int() or float()) if you intend to perform mathematical operations (15:27 - 17:45).

```python
import sys

def addition(num1, num2):
    add = num1 + num2
    return add  # sends the value back to the caller (function result)

def subtraction(num1, num2):
    s = num1 - num2
    print(s)  # just displays output on the screen, nothing is sent back to the caller

def multiplication(num1, num2):
    m = num1 * num2
    print(m)

num1=int(sys.argv[1])  # command line arguments are passed as strings, so we need to convert them to integers
operation = sys.argv[2] # the second command line argument will be the operation we want to perform
num2=int(sys.argv[3])  # the third command line argument will be the second number

if operation == 'add':
    result = addition(num1, num2)  # we can store the result of the function in a variable
    print(result)  # and then print the result
elif operation == 'sub':
    result = subtraction(num1, num2)
    print(result)
elif operation == 'mul':
    result = multiplication(num1, num2)
    print(result)
```

---

2. Environment Variables (20:40 - 29:42)
Environment variables are the preferred way to handle sensitive information like passwords, API keys, or tokens.

Security: Unlike command-line arguments, which might be exposed in logs or history, environment variables keep sensitive data out of the source code and the command line execution string (21:12 - 27:50).
The os module: Use import os and the os.getenv() function to read these variables within your code (24:30 - 25:10).
Setting them: You can export variables in your terminal (e.g., export password=mysecret) before running your script (23:55).
By using these methods, you create more robust and secure programs that are ready for professional DevOps environments, such as CI/CD pipelines (26:58).
