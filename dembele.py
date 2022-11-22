import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "Hello World"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
