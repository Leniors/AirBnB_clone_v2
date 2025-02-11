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


if __name__ == "__main__":
    app.run()
