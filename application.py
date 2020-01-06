from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('game.html')


if __name__ == "__main__":
    app.run(debug=True)
