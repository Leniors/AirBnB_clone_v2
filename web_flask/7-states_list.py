#!/usr/bin/python3
"""
Flask Application
"""
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from flask import Flask, render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy Session after each request."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ states_list route for Flask Appliction """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=states_sorted)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
