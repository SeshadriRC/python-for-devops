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

## Step 3: Make an API call

- Search for `Rest API` for Jira in google and get the API code for the project.

- Copy the `python` code of the below.

[Jira-Get-all-projects-API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get)


---

---
