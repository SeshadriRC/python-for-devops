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
