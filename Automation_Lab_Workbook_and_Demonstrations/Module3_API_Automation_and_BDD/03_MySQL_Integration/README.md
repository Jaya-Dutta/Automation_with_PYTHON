# 03 - MySQL Integration

This submodule covers MySQL database integration with Python API automation.

## Objectives

* Connect Python with MySQL
* Use `mysql-connector-python`
* Execute SQL queries from Python
* Fetch database records
* Use parameterized SQL queries
* Insert and verify test data
* Commit database changes
* Clean up test data
* Integrate API automation data with a database

## Files

### `code/mysql_api_data.py`

Covers:

* MySQL connection
* Database and cursor handling
* SELECT query
* `fetchall()`
* Parameterized INSERT
* `commit()`
* `fetchone()`
* Data validation
* DELETE cleanup
* Resource cleanup

### `test_data/setup_database.sql`

Creates:

* `api_automation_db` database
* `api_users` table
* Initial API-style user test data

## Database

Database:

```text
api_automation_db
```

Table:

```text
api_users
```

Columns:

```text
id
name
email
city
```

## Run

From the Module 3 root directory:

```powershell
Get-Content ".\03_MySQL_Integration\test_data\setup_database.sql" | mysql -u root -p
python .\03_MySQL_Integration\code\mysql_api_data.py
```

## Result

MySQL integration executed successfully.

* Database connection: Passed
* Data retrieval: Passed
* Parameterized INSERT: Passed
* Data verification: Passed
* Test data cleanup: Passed
