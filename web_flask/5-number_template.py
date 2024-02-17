#!/usr/bin/python3
"""
Flask Application
"""
from flask import Flask, render_template

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
    """ c/<text> route for Flask Appliction """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ python/<text> route for Flask Appliction """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ number/<n> route for Flask Appliction """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ number_template/<n> route for Flask Appliction """
    content = f"Number {n}"
    return render_template('5-number.html', content=content)


if __name__ == "__main__":
    """ only when called """
    app.run(host='0.0.0.0', port=5000)
