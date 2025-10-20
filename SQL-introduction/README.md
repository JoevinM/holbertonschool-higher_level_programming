# SQL - Introduction

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks

| #  | Task name                        | Description                                                                     | File                          |
|----|----------------------------------|---------------------------------------------------------------------------------|--------------------------------|
| 0  | List all databases               | Display all databases present on the MySQL server.                              | `0-list_databases.sql`         |
| 1  | Create database if missing       | Create the database `hbtn_0c_0` if it does not already exist.                   | `1-create_database_if_missing.sql` |
| 2  | Delete a database                | Delete the database `hbtn_0c_0` if it exists.                                   | `2-remove_database.sql`        |
| 3  | List tables                      | List all the tables in a given database.                                        | `3-list_tables.sql`            |
| 4  | Create first table               | Create the table `first_table` with fields `id` and `name`.                     | `4-first_table.sql`            |
| 5  | Full table description           | Display the `CREATE TABLE` statement describing `first_table`.                  | `5-full_table.sql`             |
| 6  | List all rows                    | List all rows from `first_table`.                                               | `6-list_values.sql`            |
| 7  | Insert a record                  | Insert a record (`id = 89`, `name = 'Best School'`) into `first_table`.         | `7-insert_value.sql`           |
| 8  | Count records with id = 89       | Count how many rows in `first_table` have `id = 89`.                            | `8-count_89.sql`               |
| 9  | Create & populate second_table   | Create the table `second_table` and insert multiple rows.                       | `9-full_creation.sql`          |
| 10 | List by best score               | List all records from `second_table` ordered by score (highest first).          | `10-top_score.sql`             |
| 11 | Select best scores               | Display only rows with `score >= 10` ordered by score.                          | `11-best_score.sql`            |
| 12 | Update Bob’s score               | Update the score of Bob to 10 based on the `name` field only.                   | `12-no_cheating.sql`           |
| 13 | Remove low scores                | Remove records where `score <= 5` from `second_table`.                          | `13-change_class.sql`          |
| 14 | Compute average score            | Display the average score of all records.                                       | `14-average.sql`               |
| 15 | Number by score                  | Group the number of records by score, ordered by frequency (descending).        | `15-groups.sql`                |
| 16 | Say my name                      | List all non-null names ordered by score in descending order.                   | `16-no_link.sql`               |

---

## Learning Objectives

- Understand what a **database** is  
- Understand what a **relational database** is  
- Know what **SQL** stands for  
- Understand what **MySQL** is and how it works  
- Learn the difference between **DDL** (Data Definition Language) and **DML** (Data Manipulation Language)  
- Know how to:
  - CREATE or DROP a database
  - CREATE and ALTER a table
  - SELECT records from a table
  - INSERT, UPDATE or DELETE data
  - Use SQL functions (COUNT, AVG, etc.)
  - Write basic subqueries

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`  
- All files will be executed on **Ubuntu 22.04 LTS** using **MySQL 8.0**  
- All SQL files should end with a new line  
- All SQL queries should have a comment before them  
- All files must start with a comment describing the task  
- All SQL keywords must be in **UPPERCASE** (`SELECT`, `WHERE`, `INSERT`, etc.)  
- A `README.md` file at the root of the repository is mandatory  
- File length will be tested using `wc`

---

## Resources

Read or watch:  
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)  
- [Install MySQL (MySQL Server)](https://www.youtube.com/watch?v=9h3ctGFTz9w)  
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)  
- [Basic SQL statements: DDL and DML](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_ddl_dml.md)  
- [Basic queries: SQL and RA](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_queries.md)  
- [SQL technique: functions](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_functions.md)  
- [SQL technique: subqueries](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_subqueries.md)  
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)  
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)  
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)  
- [W3School SQL](https://www.w3schools.com/sql/default.asp)