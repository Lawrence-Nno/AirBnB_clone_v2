#!/usr/bin/python3
"""This script starts a Flask web application that listens 
on 0.0.0.0:5000"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a previously coded HTML page '6-index.html' """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """This func removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
