#!/usr/bin/python3
""" Task 4 module """
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ Python route """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n=43):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
