# School Tasks Project: Curriculum - SE Foundations

## Project Details
- **By:** Guillaume
- **Weight:** 1
- **Project Start:** Feb 14, 2024 6:00 AM
- **Project End:** Feb 15, 2024 6:00 AM
- **Checker Release:** Feb 14, 2024 12:00 PM
- **Auto Review:** Will be launched at the deadline

## Resources
- **Read or watch:**
  - [How To Create a New User and Grant Permissions in MySQL](#)
  - [How To Use MySQL GRANT Statement To Grant Privileges To a User](#)
  - [MySQL constraints](#)
  - [SQL technique: subqueries](#)
  - [Basic query operation: the join](#)
  - [SQL technique: multiple joins and the distinct keyword](#)
  - [SQL technique: join types](#)
  - [SQL technique: union and minus](#)
  - [MySQL Cheat Sheet](#)
  - [The Seven Types of SQL Joins](#)
  - [MySQL Tutorial](#)
  - [SQL Style Guide](#)
  - [MySQL 8.0 SQL Statement Syntax](#)
- **Extra resources around relational database model design:**
  - Design
  - Normalization
  - ER Modeling

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements
- **General:**
  - Allowed editors: vi, vim, emacs
  - All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
  - All your files should end with a new line
  - All your SQL queries should have a comment just before (i.e. syntax above)
  - All your files should start by a comment describing the task
  - All SQL keywords should be in uppercase (SELECT, WHERE…)
  - A README.md file, at the root of the folder of the project, is mandatory
  - The length of your files will be tested using wc
- **More Info:**
  - Comments for your SQL file: `$ cat my_script.sql`
  - Install MySQL 8.0 on Ubuntu 20.04 LTS
  - Connect to your MySQL server: `$ sudo mysql`
  - Use “container-on-demand” to run MySQL
  - How to import a SQL dump

## Tasks
1. **My privileges!**
   - Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
   - Example: `$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p`

2. **Root user**
   - Write a script that creates the MySQL server user user_0d_1.
   - Example: `$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p`

3. **Read user**
   - Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
   - Example: `$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p`



