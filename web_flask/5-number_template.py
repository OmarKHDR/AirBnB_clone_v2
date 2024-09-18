#!/usr/bin/python3
"""Don't forget this name"""
from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_fun(text):
    the_text = re.sub('_', ' ', text)
    return f'Python {escape(the_text)}'


@app.route('/number/<int:n>')
def my_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def show_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
