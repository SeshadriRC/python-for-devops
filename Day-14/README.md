# Github-JIRA intergration Project - Part 1

- Problem Statement: Developers and QE engineers manually triage bugs in GitHub and then manually recreate them in JIRA. The goal is to automate this so that typing a command like `/jira` in a GitHub issue comment automatically triggers the creation of a corresponding JIRA ticket (8:30-10:00).

- The Solution Architecture: The project uses a GitHub Webhook to send a JSON payload to a custom Python/Flask application hosted on an AWS EC2 instance. This application then interacts with the JIRA API to create the ticket (10:00-13:00).

Project Strategy: The instructor is splitting the project into two parts. In the first part (covered in this segment), the focus is on:
  - JIRA setup (15:00 onwards)
  - Understanding JIRA API calls
  - Writing the Python automation script using the requests module

Executing the script to test ticket creation.

The second part (scheduled for the next video) will cover converting the script into a Flask web application, hosting it on an EC2 instance, and configuring the GitHub Webhook (13:15-14:50).

---
