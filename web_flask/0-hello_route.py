#!/usr/bin/python3
""" starts a flask web app """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ returns hello hb """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(debug=True)
