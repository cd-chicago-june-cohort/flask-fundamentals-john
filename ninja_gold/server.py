from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key = "09234857204934578"

session = {
    "score": 0,
    "message": []
}

@app.route("/")
def index():
    score = session["score"]
    msg = session["message"]
    return render_template("index.html", ninja_score=score, my_messages=msg)

@app.route("/process_money", methods=["POST"])
def process_money():
    
    if request.form["building"] == "farm":
        farm_rand = randint(10, 20)
        session["score"] += farm_rand
        session["message"].append("Earned " + str(farm_rand) + " golds at the farm!")
    elif request.form["building"] == "cave":
        cave_rand = randint(5,10)
        session["score"] += cave_rand
        session["message"].append("Earned " + str(cave_rand) + " golds at the farm!")
    elif request.form["building"] == "house":
        house_rand = randint(2, 5)
        session["score"] += house_rand
        session["message"].append("Earned " + str(house_rand) + " golds at the farm!")
    elif request.form["building"] == "casino":
        session["score"] += randint(-50, 50)
    
    return redirect("/")

app.run(debug=True)