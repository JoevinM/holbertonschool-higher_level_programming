# Python - Server-Side Rendering

## Table of Contents
- [Table of Tasks](#table-of-tasks)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)

---

## Table of Tasks

| #  | Task name                                                | Description                                                                                                       | File                  |
|----|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------|
| 0  | Creating a Simple Templating Program                     | Generate personalized invitation files from a Python string template and a list of dictionaries.                  | `task_00_intro.py`    |
| 1  | Creating a Basic HTML Template in Flask                  | Build a simple Flask app with reusable Jinja templates for headers and footers.                                  | `task_01_jinja.py`    |
| 2  | Creating a Dynamic Template with Loops and Conditions    | Use Jinja’s loops and conditionals to render dynamic lists from a JSON file in a Flask app.                       | `task_02_logic.py`    |
| 3  | Displaying Data from JSON or CSV Files in Flask          | Display product data dynamically from either JSON or CSV depending on a query parameter.                          | `task_03_files.py`    |
| 4  | Extending Dynamic Data Display to Include SQLite in Flask| Extend your Flask app to fetch and render data from a SQLite database as an additional source.                    | `task_04_db.py`       |

---

## Learning Objectives

At the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- Understand what **server-side rendering (SSR)** is and how it differs from **client-side rendering**.
- Explain the benefits of SSR in web development (SEO, performance, initial load speed).
- Implement SSR in **Python** using the **Flask** framework.
- Use the **Jinja2** templating engine to dynamically generate HTML.
- Read and render data from multiple sources: JSON, CSV, and SQLite.
- Manage dynamic routes, query parameters, and error handling in Flask.
- Handle user input and render conditional content in templates.
- Structure a Flask project with reusable templates and clean code organization.

---

## Requirements

### General
- Allowed editors: **vi, vim, emacs, Visual Studio Code, Atom, Sublime Text, etc.**
- All scripts will be executed using **Python 3.8+**.
- Flask application should run on **port 5000** by default.
- All Python files must end with a **new line**.
- Your code must follow **PEP8** style guidelines.
- You are **not allowed to use global variables** unless necessary.
- HTML updates must be handled via **server-side rendering (Jinja)** — no client-side JavaScript updates.
- You must include a **`README.md`** file at the root of the project with clear explanations.
- Reusable template components (`header.html`, `footer.html`) must be implemented.
- Proper error handling for file reading, invalid parameters, and database access must be included.

---

## Resources

Read or watch:

- [MDN Web Docs on Server-Side Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side)
- [Client-side vs. Server-side vs. Pre-rendering for Web Apps](https://www.toptal.com/front-end/client-side-vs-server-side-pre-rendering)
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/en/latest/)

---

## Description

Server-side rendering (SSR) is a technique where HTML pages are generated on the **server** before being sent to the **client**.
This project focuses on using **Python and Flask** to implement SSR through **Jinja templates**, creating dynamic, SEO-friendly, and efficient web applications.

You will:
- Start by generating static files from templates.
- Build a basic Flask server with templated pages.
- Add dynamic rendering using data from JSON, CSV, and SQLite sources.
- Extend your app to handle multiple data formats and display results dynamically.

---

## What to Expect

In this project, you’ll progressively build a Flask web application capable of:
1. **Generating templated output files** from dynamic data.
2. **Serving HTML pages** rendered entirely on the server using Flask.
3. **Integrating loops, conditionals, and includes** in Jinja templates.
4. **Displaying data from JSON, CSV, and SQLite** depending on query parameters.
5. **Handling user errors gracefully**, with helpful messages for missing files, invalid parameters, or absent records.

By the end, you’ll have a fully functional, multi-source, server-rendered web application.

---
