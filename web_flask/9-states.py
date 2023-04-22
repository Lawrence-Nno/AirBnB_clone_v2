#!/usr/bin/python3
"""This script starts a Flask web application that listens 
on 0.0.0.0:5000"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """This func displays an HTML page of a state object if found with
    its state id and their details and cities inside the tag 'BODY' """
    states = storage.all("State")
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """This func displays a HTML page of an id if it exists"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """This func removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
   
