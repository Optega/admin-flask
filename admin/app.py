from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from dotenv import load_dotenv
from datetime import timedelta
import json
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY")
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)


def read_recipients():
    with open("recipients.json", "r", encoding="utf-8") as f:
        return json.load(f)


def write_recipients(recipients):
    with open("recipients.json", "w", encoding="utf-8") as f:
        json.dump(recipients, f, ensure_ascii=False, indent=2)


def valid_login(username, password):
    return username == os.getenv("LOGIN") and password == os.getenv("PASSWORD")


def do_the_login():
    username = request.form["username"]
    password = request.form["password"]

    error = None
    if valid_login(username, password):
        session["username"] = username
        session.permanent = True
        return redirect(url_for("home"))
    else:
        error = "Невірний логін або пароль"
        return render_template("login.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        if "username" in session:
            return redirect(url_for("home"))
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/save_recipients", methods=["POST"])
def save_recipients():
    global recipients
    data = request.get_json()

    write_recipients(data)

    return jsonify({"message": "Список отримувачів збережено"}), 200


@app.route("/", methods=["GET"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    recipients = read_recipients()
    return render_template("index.html", recipients=recipients)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
