#!/usr/bin/python3
"""
Flask Application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ root route for Flask Appliction """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb route for Flask Appliction """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ hbnb route for Flask Appliction """
    return f"C {text}"


if __name__ == "__main__":
    app.run()
