# Github-JIRA intergration Project - Part 1

- Problem Statement: Developers and QE engineers manually triage bugs in GitHub and then manually recreate them in JIRA. The goal is to automate this so that typing a command like `/jira` in a GitHub issue comment automatically triggers the creation of a corresponding JIRA ticket (8:30-10:00).

- The Solution Architecture: The project uses a GitHub Webhook to send a JSON payload to a custom Python/Flask application hosted on an AWS EC2 instance. This application then interacts with the JIRA API to create the ticket (10:00-13:00).

Project Strategy: The instructor is splitting the project into two parts. In the first part (covered in this segment), the focus is on:
  - JIRA setup (15:00 onwards)
  - Understanding JIRA API calls
  - Writing the Python automation script using the requests module

Executing the script to test ticket creation.

The second part (scheduled for the next video) will cover converting the script into a Flask web application, hosting it on an EC2 instance, and configuring the GitHub Webhook (13:15-14:50).

<img width="1182" height="583" alt="image" src="https://github.com/user-attachments/assets/5e685c2f-469e-4b3a-8207-b83c8ca22612" />

<img width="1184" height="582" alt="image" src="https://github.com/user-attachments/assets/97ebea65-0c45-4799-90d7-b6a80832a8de" />

<img width="946" height="398" alt="image" src="https://github.com/user-attachments/assets/72b66b25-b438-40ef-bdc0-0d8bfb238564" />

---

## Step 1: Login to Jira and Create a Project/Space

[url](https://www.atlassian.com/software/jira)

- Signed in using gmail

<img width="1919" height="565" alt="image" src="https://github.com/user-attachments/assets/19b8ac46-dba7-46b5-a184-85e732d33d73" />

- Create a Space

<img width="1919" height="520" alt="image" src="https://github.com/user-attachments/assets/7a9ba5ef-3a0e-4751-bba3-3a14a5655641" />

- Select Scrum

<img width="1268" height="822" alt="image" src="https://github.com/user-attachments/assets/17272e51-def3-4d96-a9b0-19c029dfb5a6" />

- Enter your team name. i entered `my-team`

<img width="1834" height="852" alt="image" src="https://github.com/user-attachments/assets/cb26cd3f-1b05-4911-a434-83b55413c79b" />

   - How your space is managed - `Team managed`
   - Key - `automatically it will get filled`

<img width="1919" height="858" alt="image" src="https://github.com/user-attachments/assets/173be705-3aba-423e-aab1-76800a579b9b" />

  - click `next` and `next` , then click `i'll do this later`

<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/5badb72e-eccf-4c65-8d4e-17d67e3385d3" />

---

## Step 2: Create a API token in Jira, so that python able to communicate

*Note*: There are 2 ways , we can communicate with Application ( CLI and API ) . So here we are using API method.

profile --> Account Settings --> Security --> Create API Token --> select date and click create, then copy the token to your notepad

<img width="1908" height="660" alt="image" src="https://github.com/user-attachments/assets/9508d0cf-6946-4834-8442-5c1f643dbd30" />

---

## Step 3: Make an API call and list the projects

```python
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://my-company.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0Pg7bCE57yqPsAAiywjY0kRkXvJ1UvIdJwvRNR7x5nkSZ_ERR1tdshGq7mXxZ1qvJGKjGBsV31Mmod2nqfeyhEtmw4MYJHp-pZCWQYoqtauld21GKnjGt247ZqU_5RSsA05EKeUHx3XM5DiCOwPkJsLE1gLUT6IHUalXEpLSOoTA=69D45E49"

auth = HTTPBasicAuth("seshaec1999@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
```

- Search for `Rest API` for Jira in google and get the API code for the project.

- Copy the `python` code of the below.

[Jira-Get-all-projects-API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get)

<img width="1919" height="528" alt="image" src="https://github.com/user-attachments/assets/da30e4d4-5b79-4653-a25a-065410de278e" />

<img width="1883" height="1007" alt="image" src="https://github.com/user-attachments/assets/adfd5ee4-2343-4957-b102-3da4756066b3" />

- Now its giving all the details of the two projects, so we don't need that.

<img width="1919" height="990" alt="image" src="https://github.com/user-attachments/assets/ed7e043f-e964-46a8-a4ba-0329afbfa84d" />


---

## Step 4: Create an Issue in Jira

- Before creating we need to know the mandatory field. so below are the 4 mandatory fields. However Reporter is taken from the API call, so we can ignore that

<img width="1001" height="717" alt="image" src="https://github.com/user-attachments/assets/176908d9-0883-4745-bc54-b1504c86c397" />
<img width="986" height="457" alt="image" src="https://github.com/user-attachments/assets/cbbc8f34-3878-4ba6-b852-3d1327b058f2" />

- Now Search for Jira Rest API for create issue.

[Jira-link-create-issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)

- Now Remove the unnecessary lines, below is the final code

```python
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://my-company.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0Pg7bCE57yqPsAAiywjY0kRkXvJ1UvIdJwvRNR7x5nkSZ_ERR1tdshGq7mXxZ1qvJGKjGBsV31Mmod2nqfeyhEtmw4MYJHp-pZCWQYoqtauld21GKnjGt247ZqU_5RSsA05EKeUHx3XM5DiCOwPkJsLE1gLUT6IHUalXEpLSOoTA=69D45E49"

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
    "summary": "FIRST JIRA TICKET",
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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

```


- Jira story created

  <img width="1812" height="436" alt="image" src="https://github.com/user-attachments/assets/e348b52a-7433-40b5-bcd4-7bc84eaf8700" />

<img width="1919" height="872" alt="image" src="https://github.com/user-attachments/assets/2b0784db-b8bc-41ca-94f9-2966afbaaa24" />



---
