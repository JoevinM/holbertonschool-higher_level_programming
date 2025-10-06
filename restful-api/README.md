# Python - RESTful API

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks

| #  | Task name                                   | Description                                                                                                        | File                          |
|----|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------|
| 0  | Basics of HTTP/HTTPS                        | Understand the foundation of web communication, differentiate HTTP and HTTPS, identify methods and status codes.   | `task_00_http_basics.md`      |
| 1  | Consume data from an API using command line | Use `curl` to interact with APIs, send requests, and interpret responses.                                          | `task_01_curl.sh`             |
| 2  | Consuming and processing data with Python   | Fetch and process API data using Python’s `requests` module and export results to CSV.                             | `task_02_requests.py`         |
| 3  | Develop a simple API with `http.server`     | Build a basic web API using Python’s built-in `http.server` module with GET and JSON responses.                    | `task_03_http_server.py`      |
| 4  | Develop a simple API with Flask             | Create a RESTful API using Flask, defining routes, handling GET/POST requests, and returning JSON data.            | `task_04_flask.py`            |
| 5  | API Security and Authentication Techniques  | Implement Basic and JWT authentication in Flask, securing routes and adding role-based access control.             | `task_05_basic_security.py`   |

---

## Learning Objectives

- **HTTP/HTTPS Basics:** Understand how web communication works, including the structure of requests and responses, and the difference between secure (HTTPS) and non-secure (HTTP) connections.  
- **API Consumption with Command Line Tools:** Learn to interact with REST APIs using `curl` to perform GET, POST, and other HTTP methods.  
- **API Consumption with Python:** Use Python’s `requests` library to fetch, parse, and process JSON data from APIs, and export structured results to files such as CSV.  
- **API Development with `http.server`:** Explore Python’s built-in HTTP server to create simple REST endpoints without external dependencies.  
- **API Development with Flask:** Build RESTful APIs using Flask, focusing on routing, JSON handling, and handling dynamic and POST routes.  
- **API Security & Authentication:** Implement API security best practices using Basic Auth and JWT authentication to protect and restrict access to endpoints.  
- **API Documentation & Standards:** Understand how structured documentation (like OpenAPI/Swagger) supports clarity, maintainability, and usability of APIs.  

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`  
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3 (version 3.8.5)`  
- All files should end with a new line  
- The first line of all Python files should be exactly `#!/usr/bin/python3`  
- A `README.md` file at the root of the project folder is mandatory  
- Your code should use **pycodestyle (version 2.7.\*)**  
- All files must be executable  
- File length will be tested using `wc`  
- All modules must have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)  
- All classes must have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)  
- All functions (inside and outside a class) must have documentation  
- Documentation must be a **real sentence** explaining the purpose of the module/class/method  

---

## Resources

Read or watch:  
- [Mozilla Developer Network (MDN) - An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)  
- [Difference between HTTP and HTTPS](https://www.cloudflare.com/fr-fr/learning/ssl/why-is-http-not-secure/)  
- [List of HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)  
- [curl - Everything curl](https://ec.haxx.se/)  
- [Using cURL to interact with HTTP APIs](https://flaviocopes.com/http-curl/)  
- [Public API to play with: JSONPlaceholder](https://jsonplaceholder.typicode.com/)  
- [Python Requests Library](https://docs.python-requests.org/en/latest/)  
- [Working with JSON data in Python](https://realpython.com/python-json/)  
- [Python docs: http.server — HTTP servers](https://docs.python.org/3/library/http.server.html)  
- [A simple example of using Python’s http.server](https://www.afternerd.com/blog/python-http-server/)  
- [Flask Official Documentation](https://flask.palletsprojects.com/en/stable/)  
- [Flask-HTTPAuth)](https://flask-httpauth.readthedocs.io/en/latest/)  
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)  
- [Introduction to JSON Web Tokens](https://www.jwt.io/introduction)  
