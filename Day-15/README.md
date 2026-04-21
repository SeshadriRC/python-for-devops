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
from flask import Flask, request                    # added extra

# creating a flask app instance
app = Flask(__name__)                               # added extra

@app.route('/createJira', methods=['GET', 'POST'])  # added get along with post
def createJira():
    if request.method == 'GET':
        return "Send POST request"                 # added extra

# Read GitHub webhook event type
    github_event = request.headers.get("X-GitHub-Event")

# Only respond to issue_comment events
    if github_event != "issue_comment":
        return "Ignored", 200

# Read the comment text from the webhook payload
    payload = request.json
    # The payload structure may vary based on the event type. For issue_comment events, the comment text is typically found in payload["comment"]["body"].
    comment_text = payload["comment"]["body"].strip().lower()

    if comment_text != "/jira":
        return "No /jira command found", 200

    url = "https://my-company.atlassian.net/rest/api/3/issue"

    API_TOKEN = "write your API token here"   # Generate API token from https://id.atlassian.com/manage-profile/security/api-tokens and use it here

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
  app.run("0.0.0.0", port=5000)
```

## 3. Create a github webhook

- Created one sample issue in `Devops-concepts` repository
- Navigate to `Settings` --> `Webhooks` --> `Add webhook`

<img width="1919" height="638" alt="image" src="https://github.com/user-attachments/assets/c17b7707-19de-4783-af54-d76126dadab2" />

- Modify below things

<img width="1907" height="873" alt="image" src="https://github.com/user-attachments/assets/929e63cd-f9f2-49d0-a24a-0d579ee5d88e" />

- select the event as `issue comments` and click `add webhook`. Make sure application is running in background before adding webhook

<img width="1797" height="824" alt="image" src="https://github.com/user-attachments/assets/c8922f22-b46f-4f67-b5c0-7135a53510b9" />

- Im just testing it in laptop first before moving to AWS
<img width="976" height="190" alt="image" src="https://github.com/user-attachments/assets/47969118-7552-4588-a60e-10b7b3739526" />

<img width="599" height="145" alt="image" src="https://github.com/user-attachments/assets/997b8a9c-3af0-47d8-9996-567d43df97a6" />

- Its not allowing, so im trying in AWS
<img width="1904" height="506" alt="image" src="https://github.com/user-attachments/assets/9db13226-55d6-4072-a167-470909d35a78" />




---
