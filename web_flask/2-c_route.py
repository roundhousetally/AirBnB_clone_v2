#!/usr/bin/python3
""" starts a flask web app """
from flask import Flask
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

if __name__ == "__main__":
    app.run(debug=True)
