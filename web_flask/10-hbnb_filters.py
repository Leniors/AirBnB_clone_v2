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
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy Session after each request."""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ hbnb_filters route for Flask Appliction """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)

    cities = storage.all(City).values()
    cities_sorted = sorted(cities, key=lambda city: city.name)

    amenities = storage.all(Amenity).values()
    amenities_sorted = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html', states=states_sorted, cities=cities_sorted, amenities=amenities_sorted)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
