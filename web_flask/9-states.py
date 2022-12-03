#!/usr/bin/python3
""" Task 10 module """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    from models.state import State
    state_list = list(storage.all(State).values())
    state_list.sort(key=lambda x: x.name)
    if id is None:
        return render_template(
            '9-states.html', states=state_list, id=0)
    else:
        for state in state_list:
            if state.id == id:
                return render_template(
                    '9-states.html', state=state, id=id)

        return "<H1>Not found!</H1>"


@app.teardown_appcontext
def finish(a=None):
    """ Remove current session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
