#!/usr/bin/python3
"""Don't forget this name"""
from flask import Flask, render_template
from models import *
from models import storage
"""Don't forget this name"""

app = Flask(__name__)


@app.teardown_appcontext
def teardown_method(exception):
    """Closing the database"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities(states):
    """Don't forget this name"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
        render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')