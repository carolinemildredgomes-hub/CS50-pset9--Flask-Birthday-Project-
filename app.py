import os
from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///birthdays.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Insert into database if data is valid
        if name and month and day:
            db.execute(
                "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
                name,
                month,
                day,
            )

        return redirect("/")

    else:
        # Query database for all birthdays
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)

