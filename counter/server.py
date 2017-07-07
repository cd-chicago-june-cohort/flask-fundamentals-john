from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "2904582734905827409"

@app.route("/")
def index(count=0):
    if "counter" not in session:
        session["counter"] = count
    else:
        session["counter"] += 1
    return render_template("index.html", my_counter=session["counter"])

@app.route("/double_counter")
def double():
    session["counter"] += 1
    return redirect("/")

@app.route("/reset")
def reset():
    session["counter"] = -1
    return redirect("/")

app.run(debug=True)