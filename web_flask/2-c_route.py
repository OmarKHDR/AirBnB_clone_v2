#!/usr/bin/python3
"""Don't forget this name"""
from flask import Flask
from markupsafe import escape
import re

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_func(text):
    the_text = re.sub('_', ' ', text)
    return f'C {escape(the_text)}'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
