#!/usr/bin/python3
""" This python script starts a web application
that listens on 0.0.0.0, and port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function displays 'Hello HBNB'"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
