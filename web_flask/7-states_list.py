#!/usr/bin/python3
""" starts a flask web app """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def slist():
    """ displays html page """
    allstates = storage.all(State)
    return render_template("7-states_list.html", allstates=allstates)


@app.teardown_appcontext
def tear(exc):
    """ remove the sqlalchemy sesh """
    storage.close()


if __name__ == "__main__":
    app.run()
