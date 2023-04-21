#!/usr/bin/python3
""" This python script starts a web application
that listens on 0.0.0.0, and port 5000"""

import string
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function displays 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This url/page displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """This func displays "C" followed by any variable
    provided to it"""
    return 'C %s' % escape(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
