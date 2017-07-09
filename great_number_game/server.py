from flask import Flask, render_template, session, redirect, request
from random import randint

app = Flask(__name__)
app.secret_key = "02094385792824t98"

session = {"message": ""}

@app.route("/")
def index():
    session["random"] = randint(1, 100)
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    num = session["random"]
    print num
    guess = int(request.form["guess"])
    msg = ""
    if guess != num:
        if guess > num:
            msg = "Too high"
        elif guess < num:
            msg = "Too low"
        session["message"] = msg
        return render_template("result_page.html",  my_message=session["message"])
    else:
        return render_template("winner_page.html")

@app.route("/play_again")
def play_again():
    return redirect("/")

app.run(debug=True)