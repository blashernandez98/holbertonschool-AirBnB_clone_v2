#!/usr/bin/python3
""" Task 11 module """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def state_id(id=None):
    from models.state import State
    from models.amenity import Amenity
    state_list = list(storage.all(State).values())
    amenity_list = list(storage.all(Amenity).values())
    state_list.sort(key=lambda x: x.name)
    amenity_list.sort(key=lambda x: x.name)
    return render_template(
        '10-hbnb_filters.html', states=state_list, amenities=amenity_list)


@app.teardown_appcontext
def finish(a=None):
    """ Remove current session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
