from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)


def read_recipients():
    with open("recipients.json", "r", encoding="utf-8") as f:
        return json.load(f)


def write_recipients(recipients):
    with open("recipients.json", "w", encoding="utf-8") as f:
        json.dump(recipients, f, ensure_ascii=False, indent=2)


@app.route("/", methods=["GET"])
def home():
    recipients = read_recipients()
    return render_template("index.html", recipients=recipients)


@app.route("/save_recipients", methods=["POST"])
def save_recipients():
    global recipients
    data = request.get_json()

    write_recipients(data)

    return jsonify({"message": "Список отримувачів збережено"}), 200


if __name__ == "__main__":
    app.run()
