#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes connection with db"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns a dictionary of state objects"""
    return render_template("7-states_list.html", states=storage.all(State))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
