# SQL - More Queries

This project covers more advanced SQL concepts such as user management, privileges, constraints, foreign keys, and how to retrieve data across multiple tables using JOINs and subqueries.

## Table of Contents
- [Table of Tasks](#table-of-tasks)  
- [Learning Objectives](#learning-objectives)  
- [Requirements](#requirements)  
- [Resources](#resources)  

---

## Table of Tasks

| #  | Task name                    | Description                                                                                   | File                          |
|----|-----------------------------|-----------------------------------------------------------------------------------------------|-------------------------------|
| 0  | My privileges!              | List all privileges of the MySQL users `user_0d_1` and `user_0d_2`.                          | `0-privileges.sql`           |
| 1  | Root user                   | Create user `user_0d_1` with all privileges.                                                 | `1-create_user.sql`          |
| 2  | Read user                   | Create DB `hbtn_0d_2` and user `user_0d_2` with only SELECT privilege on it.                | `2-create_read_user.sql`     |
| 3  | Always a name               | Create table `force_name` where `name` cannot be NULL.                                      | `3-force_name.sql`           |
| 4  | ID can't be null            | Create table `id_not_null` where `id` defaults to 1 and cannot be null.                     | `4-never_empty.sql`          |
| 5  | Unique ID                   | Create table `unique_id` where `id` is unique by constraint.                                | `5-unique_id.sql`            |
| 6  | States table                | Create DB `hbtn_0d_usa` and table `states` with `id` as PRIMARY KEY.                       | `6-states.sql`               |
| 7  | Cities table                | Create table `cities` with foreign key referencing `states.id`.                             | `7-cities.sql`               |
| 8  | Cities of California        | List all cities in California using a subquery (no JOIN).                                   | `8-cities_of_california_subquery.sql` |
| 9  | Cities by States            | List all cities and their corresponding states (JOIN).                                      | `9-cities_by_state_join.sql` |
| 10 | Genre ID by show            | List all shows and linked genres (INNER JOIN).                                              | `10-genre_id_by_show.sql`    |
| 11 | Genre ID for all shows      | Same as above but show NULL if no genre linked (LEFT JOIN).                                 | `11-genre_id_all_shows.sql`  |
| 12 | No genre                    | List all shows without a linked genre.                                                      | `12-no_genre.sql`            |
| 13 | Number of shows by genre    | Display number of shows per genre, sorted by count DESC.                                    | `13-count_shows_by_genre.sql` |
| 14 | My genres                  | List all genres of the show “Dexter”.                                                       | `14-my_genres.sql`           |
| 15 | Only Comedy                | List all “Comedy” shows.                                                                    | `15-comedy_only.sql`         |
| 16 | List shows and genres      | List all shows and genres (LEFT JOIN) including NULL when no genre.                         | `16-shows_by_genre.sql`      |

---

## Learning Objectives

By the end of this project, you should be able to explain:

- How to **create a new MySQL user**
- How to **manage privileges** for a user (GRANT / REVOKE)
- What a **PRIMARY KEY** is
- What a **FOREIGN KEY** is
- How to use **NOT NULL** and **UNIQUE** constraints
- How to **retrieve data from multiple tables** in one query
- What **subqueries** are and when to use them
- The difference between **JOIN** types (INNER, LEFT, etc.) and **UNION**

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0**
- All files should end with a **new line**
- Each SQL query should have a **comment before it**
- Each file must start with a **description comment**
- All SQL keywords must be in **UPPERCASE**
- A `README.md` file at the root of the project is **mandatory**
- File length will be tested using **wc**

---

## Resources

Read or watch:      
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)  
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)  
- [MySQL constraints](https://zetcode.com/mysql/constraints/)  
- [SQL technique: multiple joins and the distinct keyword](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_join.md)  
- [Basic queries: SQL and RA](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_multiple_joins.md)  
- [SQL technique: join types](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_join_types.md)  
- [SQL technique: subqueries](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_subqueries.md)  
- [SQL technique: union and minus](https://github.com/hs-hq/project_resources/blob/main/sql/database_design_union_minus.md)  
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)  
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)  
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide/)  
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)  
- [Design](https://www.guru99.com/database-design.html)  
- [Normalization](https://www.guru99.com/database-normalization.html)  
- [ER Modeling](https://www.guru99.com/er-modeling.html)