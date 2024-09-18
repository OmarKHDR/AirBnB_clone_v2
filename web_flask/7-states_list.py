#!/usr/bin/python3
""" Don't forget this name 
    cd ls mk
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_method(exception):
    """Closing the database"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_static(states):
    """A route here"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    """Starting the app"""
    app.run(host='0.0.0.0')
