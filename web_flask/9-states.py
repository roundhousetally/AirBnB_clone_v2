#!/usr/bin/python3
""" starts a flask web app """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def statesid(id=None):
    """ displays html page """
    allstates = storage.all(State)
    if id is None:
        return render_template("9-states.html", allstates=allstates)
    statewid = allstates.get("State." + str(id))
    return render_template("9-states.html", statewid=statewid)


@app.teardown_appcontext
def tear(exc):
    """ remove the sqlalchemy sesh """
    storage.close()


if __name__ == "__main__":
    app.run()
