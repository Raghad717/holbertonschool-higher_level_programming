# MySQL - Advanced Queries and Database Management

This repository contains SQL scripts for practicing advanced MySQL concepts, including user management, constraints, joins, subqueries, and complex data retrieval techniques.

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Project Files](#project-files)


## Learning Objectives

At the end of this project, you should be able to explain:

### General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a PRIMARY KEY
- What's a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS
- **MySQL Version**: 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before the syntax
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)
- A README.md file is mandatory
- File length will be tested using `wc`

## Project Files

| File | Description |
|------|-------------|
| `0-my_privileges.sql` | Script to list privileges of MySQL users |
| `1-root_user.sql` | Creates MySQL server user with all privileges |
| `2-read_user.sql` | Creates a user with read-only privileges |
| `3-always_name.sql` | Creates table with NOT NULL constraint |
| `4-id_not_null.sql` | Creates table with ID that can't be NULL |
| `5-unique_id.sql` | Creates table with UNIQUE constraint on ID |
| `6-states.sql` | Creates database and table 'states' |
| `7-cities.sql` | Creates table 'cities' with FOREIGN KEY |
| `8-cities_of_california.sql` | Lists all cities of California |
| `9-cities_by_states.sql` | Lists all cities with state names using JOIN |
| `10-genre_id_by_show.sql` | Lists shows with genre IDs using JOIN |
| `11-genre_id_all_shows.sql` | Lists all shows with their genre IDs |
| `12-no_genre.sql` | Lists shows without a genre |
| `13-count_shows_by_genre.sql` | Counts shows by genre |
| `14-my_genres.sql` | Lists genres of a specific show |
| `15-only_comedy.sql` | Lists only comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their genres |

### This README provides a comprehensive overview of the project, including setup instructions, file descriptions, usage guidelines, and learning resources. It's formatted to be clear and easy to navigate for anyone working with these SQL scripts.

## Author
**Raghad Almalk**
