from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "mykey"

@app.route("/")
def home():
    return render_template("display.html", agent="Dude", celeb="Gracie Abram", celeb_informal="Gracie", pronoun="she")

@app.route("/input/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"]= user
        return redirect(url_for("user"))
    else:
        return render_template("input.html")

@app.route("/usr")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()