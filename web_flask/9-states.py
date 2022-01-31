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


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def state_w_id(id=None):
    """Returns a list of state objects. If id exists, returns
    a specific state"""
    states = storage.all(State)
    state = None
    if id:
        if "State." + id in states.keys():
            state = states["State." + id]
    return render_template("9-states.html", **(locals()))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
