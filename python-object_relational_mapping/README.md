# Python - Object-relational mapping

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks

| #  | Task name                  | Description                                                                       | File                          |
|----|---------------------------|-----------------------------------------------------------------------------------|-------------------------------|
| 0  | Get all states            | List all states from database (`MySQLdb` - direct SQL).                           | `0-select_states.py`          |
| 1  | Filter states             | List all states starting with `N` (MySQLdb filtering).                            | `1-filter_states.py`          |
| 2  | Filter by user input     | Display states matching user input (⚠️ vulnerable SQL).                            | `2-my_filter_states.py`       |
| 3  | SQL Injection…           | Same as previous, but safe from SQL injections (parameterized query).             | `3-my_safe_filter_states.py`  |
| 4  | Cities by states         | List all cities with their state names (JOIN using MySQLdb).                      | `4-cities_by_state.py`        |
| 5  | All cities by state      | List cities of a given state name (safe from SQL injection).                       | `5-filter_cities.py`          |
| 6  | First state model        | Define SQLAlchemy ORM class `State`.                                               | `model_state.py`              |
| 7  | All states via ORM       | Retrieve all `State` objects using SQLAlchemy session.                            | `7-model_state_fetch_all.py`  |
| 8  | First state via ORM      | Print the first `State` object.                                                   | `8-model_state_fetch_first.py`|
| 9  | Contains 'a'             | List states containing the letter `a`.                                            | `9-model_state_filter_a.py`   |
| 10 | Get a state              | Search state by name (safe from SQL injection via ORM).                           | `10-model_state_my_get.py`    |
| 11 | Add new state            | Insert a new `State` using ORM.                                                   | `11-model_state_insert.py`    |
| 12 | Update a state           | Update a state’s name using ORM.                                                  | `12-model_state_update_id_2.py`|
| 13 | Delete states            | Delete all states containing `a` using ORM.                                       | `13-model_state_delete_a.py`  |
| 14 | Cities in state          | Define `City` ORM model + print cities grouped by state.                          | `model_city.py`, `14-model_city_fetch_by_state.py` |

---

## Learning Objectives

By the end of this project, you should be able to explain, **without the help of Google**:

### General
- How to **connect to a MySQL database from a Python script**
- How to **SELECT rows** in a MySQL table using Python
- How to **INSERT rows** using Python
- What an **ORM (Object-Relational Mapper)** is
- The difference between **raw SQL queries** (MySQLdb) and **object manipulation** (SQLAlchemy)
- How to **map a Python class to a MySQL table** using SQLAlchemy
- How sessions work in SQLAlchemy (open/query/commit/close)
- How to guard against **SQL injection** in Python

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5)
- MySQLdb version: **2.0.x**
- SQLAlchemy version: **1.4.x**
- The first line of all files must be:
- All files should end with a new line
- A `README.md` file at the root of the project is **mandatory**
- Code must follow **pycodestyle** (version 2.7.\*)
- All files must be **executable**
- File lengths will be tested using `wc`
- All modules must have **documentation**
- All classes must have **documentation**
- All functions (inside and outside classes) must have **documentation**
- A documentation is a **real sentence**, not a single word
- You are **not allowed** to use `execute()` with SQLAlchemy (only ORM queries)

---

## Resources

Read or watch:
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQL constraints](https://www.mikusa.com/python-mysql-docs/index.html)
- [MySQLdb tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW&cbrd=1&ucbcb=1)
- [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://www.pythonsheets.com/notes/database/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers ](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)