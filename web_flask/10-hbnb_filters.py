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

@app.route('/hbnb_filters')
def displaying_filters():
    states = storage.all("State").values()
    ameinties = storage.all("Amenity").values()
    return render_template('6-index.html', states=states, ameinties=ameinties)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
