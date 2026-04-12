# Python Functions, Modules and Packages

## 1. Differences Between Functions, Modules, and Packages

### Functions

A function in Python is a block of code that performs a specific task. Functions are defined using the `def` keyword and can take inputs, called arguments. They are a way to encapsulate and reuse code.

**Example:**

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

In this example, `greet` is a function that takes a `name` argument and returns a greeting message.


**Not recommended**
*filname*: calculator.py
```python
num1=5
num2=10
addition=num1+num2
print("The addition of is " + str(addition))

subtraction=num1-num2
print("The subtraction of", num1, "and", num2, "is", subtraction)

```

**Recommended approach**
*filname*: calculator-new.py

```python
num1=10
num2=5

def addition():
    add = num1 + num2
    print(add)

def subtraction():
    s = num1 - num2
    print(s)

def multiplication():
    m = num1 * num2
    print(m)

# once we write the functions we need to call them to execute the code
addition()
subtraction()   
multiplication()


def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

- Functions improve **readability, reusability (or modularity), and debugging**
- Why use functions?

    - Readability: They help organize your code into logical sections rather than a long, linear script (4:09).
    - Reusability: You can write a function once and use it across different parts of your program or even in other files (4:47).
    - Debugging: If an error occurs, you know exactly which function contains the problematic logic, making it much easier to troubleshoot (24:18).

- DevOps Use Case: Functions allow you to break down large tasks—like managing AWS resources like S3 buckets or EC2 instances—into smaller, manageable blocks of logic (29:14 - 31:43).

**Most Recommended approach**

- Functions are most efficient when they accept inputs (parameters), process them, and use the return keyword to send back an output (41:37).

```python
def addition(num1, num2):
    add = num1 + num2
    return add  # sends the value back to the caller (function result)

def subtraction(num1, num2):
    s = num1 - num2
    print(s)  # just displays output on the screen, nothing is sent back to the caller

def multiplication(num1, num2):
    m = num1 * num2
    print(m)

# Below we are calling the functions with arguments to execute the code
print(addition(10, 5))
print(subtraction(10, 5)) 
multiplication(10, 5)

```

<img width="1410" height="973" alt="image" src="https://github.com/user-attachments/assets/5ca72e73-4861-4775-b681-b51de82f1f75" />


---

### Modules

A module is a Python script containing Python code. It can define functions, classes, and variables that can be used in other Python scripts. Modules help organize and modularize your code, making it more maintainable.

**Example:**

Suppose you have a Python file named `my_module.py`:

```python
# my_module.py , make sure filname using underscore. If you use any different character (-), then while calling it won't work.
def square(x):
    return x ** 2

pi = 3.14159265
```

You can use this module in another script:

```python
import my_module                

result = my_module.square(5)
print(result)
print(my_module.pi)
```

In this case, `my_module` is a Python module containing the `square` function and a variable `pi`.

<img width="1246" height="298" alt="image" src="https://github.com/user-attachments/assets/930847ec-33ef-41e9-a268-02f53d89a1d3" />

---

### Packages

A package is a collection of modules organized in directories. Packages help you organize related modules into a hierarchy. They contain a special file named `__init__.py`, which indicates that the directory should be treated as a package.

**Example:**

Suppose you have a package structure as follows:

```
my_package/
    __init__.py
    module1.py
    module2.py
```

You can use modules from this package as follows:

```python
from my_package import module1

result = module1.function_from_module1()
```

In this example, `my_package` is a Python package containing modules `module1` and `module2`.

## 2. How to Import a Package

Importing a package or module in Python is done using the `import` statement. You can import the entire package, specific modules, or individual functions/variables from a module.

**Example:**

```python
# Import the entire module
import math

# Use functions/variables from the module
result = math.sqrt(16)
print(result)

# Import specific function/variable from a module
from math import pi
print(pi)
```

In this example, we import the `math` module and then use functions and variables from it. You can also import specific elements from modules using the `from module import element` syntax.

## 3. Python Workspaces

Python workspaces refer to the environment in which you develop and run your Python code. They include the Python interpreter, installed libraries, and the current working directory. Understanding workspaces is essential for managing dependencies and code organization.

Python workspaces can be local or virtual environments. A local environment is the system-wide Python installation, while a virtual environment is an isolated environment for a specific project. You can create virtual environments using tools like `virtualenv` or `venv`.

- As explained in the video (1:00:12 - 1:07:40), it is essential for DevOps engineers because it solves dependency conflicts when working on multiple projects that might require different versions of the same library or module.

Key points about Virtual Environments:

   - Isolated workspaces: By creating a virtual environment for each project, you ensure that the packages installed for one project do not conflict with those of another (1:02:49 - 1:03:02).

   - Project-specific dependencies: You can install specific versions of libraries (e.g., Jira version 1.2.3 vs 1.5.6) within their respective virtual environments without affecting your global Python installation or other project folders (1:05:33 - 1:06:06).

**Example:**

```bash
# Install virtual env
pip install virtualenv

---
# Create a virtual environment
python -m venv myenv

user@LAPTOP-QMBUJPPJ MINGW64 /e/my-git/python-for-devops/Day-04 (main)
$ ls
__pycache__/  calculator.py  calculator_new.py  module-calc.py  myenv/  package.py  README.md

---

# Activate the virtual environment (on Windows)
source myenv/Scripts/activate

# To come out of venv
deactivate

# Activate the virtual environment (on macOS/Linux)
source myenv/bin/activate
```

Once activated, you work in an isolated workspace with its Python interpreter and library dependencies.

- So here we created two venv `myenv` and `myenv-2`. And installed `Jira` only in `myenv`, so it will be there only in `myenv` not on other `myenv-2`

<img width="327" height="691" alt="image" src="https://github.com/user-attachments/assets/8583507e-c208-42a4-9675-1aaa3b9df2fd" />

<img width="367" height="653" alt="image" src="https://github.com/user-attachments/assets/be784e8f-a565-4f57-a79d-0e0a759fbe40" />

---
