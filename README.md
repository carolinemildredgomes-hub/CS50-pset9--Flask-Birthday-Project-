# ll Flask web application to store and view birthdays using SQLite.


## Features
- Add a person's name and birthday (month and day).
- View allCS50 — PSet 9: Birthdays


A sma saved birthdays in a table.
- Optional: delete birthday entries.


## Prerequisites
- Python 3.8+
- pip
- sqlite3 (optional: DB Browser for SQLite)


## Install
```bash
python3 -m venv venv
source venv/bin/activate # or venv\Scripts\Activate.ps1 on Windows
pip install --upgrade pip
pip install cs50 flask

Start the Flask server:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080


Open the forwarded URL in your browser.
Use the form to add birthdays, which will appear in the table below.

Database

If your repo doesn't include birthdays.db, create it and the table:
CREATE TABLE birthdays (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
month INTEGER NOT NULL,
day INTEGER NOT NULL
);


