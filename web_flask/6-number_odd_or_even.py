#!/usr/bin/python3
""" Script to start a web app on port 5000 and return Hello HBNB!"""
from flask import Flask, render_template
from markupsafe import escape
from jinja2 import FileSystemLoader

app = Flask(__name__)


app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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
    """Function that displays python followed by value of text"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/python', strict_slashes=False)
def python():
    """ Function that returns python is cool"""
    return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def prnt_number(n):
    """ Function that returns n """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def disp_number(n):
    """ Function that return a web page if the number is an int"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """ Function that returns a page if the number is even or odd"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
