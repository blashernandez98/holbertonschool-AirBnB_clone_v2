#!/usr/bin/python3
""" Task 4 module """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def home():
    """ Home route """
    from models.state import State
    state_list = list(storage.all(State).values())
    state_list.sort(key=lambda x: x.name)
    return render_template(
        '7-states_list.html',
        states=state_list)


@app.teardown_appcontext
def finish(self):
    """ Remove current session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
