#!/usr/bin/python3
""" Task 4 module """
from flask import Flask, render_template
from models import storage
from os import getenv

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def home():
    """ Home route """
    from models.state import State
    from models.city import City
    state_list = list(storage.all(State).values())
    state_list.sort(key=lambda x: x.name)
    city_list = []
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        city_list = list(storage.all(City).values())
        city_list.sort(key=lambda x: x.name)
    else:
        for state in state_list:
            city_list.extend(state.cities)

    return render_template(
        '8-cities_by_states.html',
        states=state_list, cities=city_list)


@app.teardown_appcontext
def finish(self):
    """ Remove current session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
