#!/usr/bin/python3
""" Task 3 module """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Home route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def clang(text):
    """ C route """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ Python route """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
