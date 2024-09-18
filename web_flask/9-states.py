#!/usr/bin/python3
"""Don't forget this name"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_method(exception):
    """Closing the database"""
    storage.close()

@app.route('/states', strict_slashes=False)
def list_static():
    """A route here"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)

@app.route('/states/<id>', strict_slashes=False)
def list_static_id(id):
    """A route here"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
