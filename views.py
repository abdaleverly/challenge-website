from flask import Blueprint,jsonify
from datetime import datetime

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return "<h1>Welcome to the Challenge Home Page!</h1>"

@views.route("/version")
def version():
    f = open("version.txt")
    version = f.readline()
    f.close()
    return jsonify(version=version)

@views.route("/now")
def now():
    now = datetime.now().strftime("%H:%M:%S")
    return f"<p style='font-family:Arial'>Current UTC time is <span style='color:green'>{now}</span></p>"