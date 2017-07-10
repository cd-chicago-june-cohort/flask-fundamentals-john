
from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = "5902384572093"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    
    server_email = request.form["email"]
    server_first_name = request.form["first_name"]
    server_last_name = request.form["last_name"]
    server_password = request.form["password"]
    server_confirm_password = request.form["confirm_password"]

    if len(server_email) < 1 or len(server_first_name) < 1 or len(server_last_name) < 1 or len(server_password) < 1 or len(server_confirm_password) < 1:
        flash("All fields are required")
        return redirect("/")
    elif not (server_first_name.isalpha() or server_last_name.isalpha()):
        flash("First name and last name can only contain letters")
        return redirect("/")
    elif not EMAIL_REGEX.match(server_email):
        flash("Invalid Email Address!")
        return redirect("/")
    elif server_password != server_confirm_password:
        flash("Password confirmation must match password")
        return redirect("/")
    else:
        return render_template("accepted.html")
app.run(debug=True)