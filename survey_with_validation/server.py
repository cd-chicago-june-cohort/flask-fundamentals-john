from flask import Flask, render_template, redirect, request, flash

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

    if len(server_name) < 1:
        return render_template("error.html", your_error="You must enter a name!")
    elif len(server_comment) < 1:
        return render_template("error.html", your_error="You must enter a comment!")
    elif len(server_comment) > 120:
        return render_template("error.html", your_error="Comment cannot exceed 120 characters!")
    else:
        return render_template("results.html", template_name=server_name, template_location=server_location, template_language=server_language, template_comment=server_comment)

app.run(debug=True)