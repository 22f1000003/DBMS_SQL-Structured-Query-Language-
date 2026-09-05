## this repo for database connectivity
## by using python and java and c 
# DBMS Course — PostgreSQL CRUD Scripts (Python + psycopg2)

Simple Python scripts using `psycopg2` to perform basic CRUD (Create, Read, Update, Delete)
operations on a PostgreSQL database, written as part of DBMS coursework.

## Requirements

- Python 3.x
- PostgreSQL server running and accessible
- `psycopg2-binary` package

Install dependencies:

```bash
pip install psycopg2-binary
```

## Database Connection

All scripts connect using the following parameters (update as needed for your setup):

| Parameter | Value           |
|-----------|-----------------|
| database  | `sqliitm`       |
| user      | `postgres`      |
| host      | `127.0.0.1`     |
| port      | `5433`          |

> Passwords are hardcoded in these scripts for coursework simplicity. In real projects,
> use environment variables or a config file instead of hardcoding credentials.

## Scripts

### `createtable.py`
Creates the `employee` table with columns: `emp_num` (primary key), `emp_name`, `department`.

```bash
python createtable.py
```

### `insertrow.py`
Inserts a new row into the `employee` table.

```python
insertrow(emp_num, emp_name, department)
```

Example:
```python
insertrow(100, 'bhaskara', 'HR')
```

### `deleterow.py`
Deletes a row from the `employee` table by `emp_num`.

```python
deleterow(emp_num)
```

Example:
```python
deleterow(100)
```

### `updatevalue.py`
Updates a student's `name` in the `student` table, matched by `rollno`.

```python
updatevalue(nameofstudent, rollnumber)
```

Example:
```python
updatevalue('sdf', '22f1000003')
```

## Common Patterns Used

- **Parameterized queries** (`%s` placeholders) are used instead of string formatting,
  to prevent SQL injection and correctly handle types.
- Each script follows a `try / except / finally` structure:
  - `try`: connect, execute query, commit
  - `except`: catch and print `psycopg2.DatabaseError`
  - `finally`: always close the connection, guarded by `if conn is not None`
- `conn.commit()` is required after INSERT/UPDATE/DELETE to persist changes
  (`cur.commit()` does **not** exist — only the connection has `commit()`).

## Notes / Gotchas Learned

- A single-value tuple needs a trailing comma: `(value,)`, not `(value)`.
- The order of values in the parameter tuple must exactly match the order of `%s`
  placeholders in the SQL string.
- Function calls should not be placed inside the function's own body — call them at
  module level (unindented), otherwise it triggers unwanted recursion.
- String arguments (names, alphanumeric roll numbers) must be quoted in Python;
  unquoted identifiers are treated as variable names and will raise `NameError`.

## Running a Script

```bash
cd path/to/project
python script_name.py
```

If `python` isn't recognized, try `py` or `python3` instead.
