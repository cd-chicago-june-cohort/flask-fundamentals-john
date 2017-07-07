from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    server_name = request.form["name"]
    server_location = request.form["location"]
    server_language = request.form["language"]
    server_comment = request.form["comment"]
    return render_template("results.html", template_name=server_name, template_location=server_location, template_language=server_language, template_comment=server_comment)

app.run(debug=True)