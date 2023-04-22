#!/usr/bin/python3
"""This script starts a Flask web application that listens 
on 0.0.0.0:5000"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This func displays an HTML page with the list of state objects 
    inside the tag 'BODY' """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """This func removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
   
