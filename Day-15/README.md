# Github-JIRA intergration Project - (Part-2)

<img width="1820" height="791" alt="image" src="https://github.com/user-attachments/assets/a9885365-5f72-4bf5-bc65-c0d8c765ef92" />

<img width="1804" height="849" alt="image" src="https://github.com/user-attachments/assets/6a19b474-ea0d-4638-9095-10508d944598" />

<img width="1437" height="673" alt="image" src="https://github.com/user-attachments/assets/86b58f7e-9938-4b2a-b62b-773fe7a97d0c" />


# GitHub and Jira Integration using Python & Flask

In this video, the instructor explains how to automate GitHub and Jira integration using Python and the Flask framework.

---

## API (Application Programming Interface)

- An API is described as an **application interface** that allows programs to communicate with each other.
- Unlike a **User Interface (UI)**, which is designed for humans to interact with using clicks and keyboards, an API is designed for **programmatic interaction**.
- It enables developers to send automated requests to a service to perform tasks, such as creating a Jira ticket using a Python script.

---

## HTTP Request Types

APIs operate on the **HTTP protocol** and use specific request methods to perform actions on a server.

### Primary HTTP Methods

- **POST**  
  Used to send information to a server.  
  Example: Submitting booking details or creating a Jira issue.

- **GET**  
  Used to retrieve information from a server.

- **PUT**  
  Used to modify or update existing records on a server.

- **DELETE**  
  Used to remove a record from a server.

### Project Usage

In this project, the Flask API is configured to use the **POST** method because GitHub sends (**posts**) JSON payload data to the application.

---

## Flask Framework

- **Flask** is a lightweight Python framework used to create efficient APIs.
- It includes an **inbuilt development server**, allowing you to run and test your API directly on a machine (such as an EC2 instance).
- This avoids the need for heavy production servers like **Tomcat** or **WebSphere** during development.

---

# Practicals

## 1. Write a Sample Hello world Flask API before writing actuall API

- Run the below python code in EC2 instance.
  
```python
# Install flask
pip install flask

from flask import Flask    # importing Flask module from the flask package

app = Flask(__name__)  # Its a common line, every flask program will have this. we are creating a flask app instance

@app.route('/')        # A decorator is a shortcut that adds extra functionality to a function using @ syntax. It tells Flask: when someone visits /, run the hello_world() function. It will be used before functions and it will be executed at first.
def hello_world():
    return 'Hello, World!'
    
    app.run("0.0.0.0")     # Run on the local machine ip address, by default flask application will run on port 5000

```

- Access the URL, it will show the output as `Hello world`.
- Now Access the URL with `/something`, it will show `Not Found`. How if showing `Not Found`, its because of the `app.route` which we used.

<img width="1244" height="314" alt="image" src="https://github.com/user-attachments/assets/95e42cee-565c-451c-886b-f78188f1b749" />

## 2. Now Write a real Flask API

- We already have the api code which we written in `Day-14` and do some alterations

```python
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask             # added extra

# creating a flask app instance
app = Flask(__name__)               # added extra

@app.route("/createJIRA")           # added extra
def CreateJIRA():                   # added extra

    url = "https://my-company.atlassian.net/rest/api/3/issue"

    API_TOKEN = "API token"

    auth = HTTPBasicAuth("seshaec1999@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My First Jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10082"  # to find the issuetype, first naviage to particular myspace --> configure board --> left side(worktypes) --> click story --> then in the URL you can able to see the id
        },
        "project": {
        "key": "MST"     # Instead of id, you can also use project key. Ex: "key": "TEST"
        },
        "summary": "JIRA TICKET created using github",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))   # Altered

if __name__ == '__main__':
  app.run("0.0.0.0", port=8080)
```

## 3. Create a github webhook

```python

```

---
