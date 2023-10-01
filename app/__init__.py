from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return "Hello from Flask!"

@app.route("/html")
def index_html():
    python_people = ["Tiesto", "Kodak Black", "Michael Jackson", "Pop Smoke", "LiL Baby"]
    return render_template("index.html", message="Hello from my template", red=True, html_people=python_people)

@app.route("/json")
def json():
    return {"message": "Hello from my updated API!"}