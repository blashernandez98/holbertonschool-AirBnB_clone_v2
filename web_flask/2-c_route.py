#!/usr/bin/python3
"""" Task 2 module """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    return f"C {text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
