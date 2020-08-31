#!/usr/bin/python3
""" starts a flask web app """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ returns hello hb """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ displays hbnb """
    return "HBHB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ displays C and text """
    txt = text.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py(text="is cool"):
    """ route """
    txt = text.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """ displays n is a number is n is int """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numtemp(n):
    """ returns an html page if n is int """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(debug=True)
