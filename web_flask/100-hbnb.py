#!/usr/bin/python3
"""This script starts a Flask web application that listens 
on 0.0.0.0:5000"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays a previously coded HTML page '8-index.html' """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template('100-hbnb.html', states=states,
           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """This func removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
