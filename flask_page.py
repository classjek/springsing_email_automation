from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("display.html", agent="Dude", celeb="Gracie Abram", celeb_informal="Gracie", pronoun="she")

@app.route("/input/", methods=["POST", "GET"])
def login():
    return render_template("input.html")

if __name__ == "__main__":
    app.run()