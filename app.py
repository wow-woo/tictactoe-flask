from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [
            None, None, None], [None, None, None]]
        session["turn"] = "x"

    return render_template("game.html", game=session["board"], turn=session["turn"])


@app.route("/<int:row>/<int:col>")
def action(row, col):
    session["board"][row][col] = session["turn"]

    if session["turn"] == "x":
        session["turn"] = "y"
    else:
        session["turn"] = "x"

    return redirect(url_for("index"))


@app.route("/<string:reset>")
def replay():
    session["board"] = [[None, None, None], [
        None, None, None], [None, None, None]]
    return redirect(url_for("index"))
# changes
