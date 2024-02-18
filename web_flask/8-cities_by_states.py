#!/usr/bin/python3
"""
Flask Application
"""
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from flask import Flask, render_template
from models import storage
from models.state import State
from models.state import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy Session after each request."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ cities_by_states route for Flask Appliction """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)

    cities = storage.all(City).values()
    cities_sorted = sorted(cities, key=lambda city: city.name)

    return render_template('8-cities_by_states.html', states=states_sorted, cities=cities_sorted)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
