#!/usr/bin/python3
"""A script to start a web app on port 5000 and return Hello HBNB!"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Function that returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ Function that displays variable"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """ Function that displays python followed by value of text"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/python', strict_slashes=False)
def python():
    """ Function that returns python is cool"""
    return "Python is cool"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
