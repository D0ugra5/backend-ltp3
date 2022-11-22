import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return '22223'


@app.route('/')
@app.route('/home')
def home():
    return "Hello World"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
