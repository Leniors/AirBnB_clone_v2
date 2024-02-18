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

""" states_list route for Flask Appliction """
states = storage.all(State).values()
states_sorted = sorted(states, key=lambda state: state.name)

for state in states:
    print(state.name)
#return render_template('7-states_list.html', states=states)