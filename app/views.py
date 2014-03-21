from flask import render_template
from app import app
from forms import ChoiceForm

@app.route('/')
def index():
    return render_template("index.html", form=ChoiceForm())

@app.route('/begin')
def begin():
    #TODO: Logic for displaying to user
    return render_template("begin.html")


@app.route('/compose')
def compose():
    #TODO: Logic for composing goes here
    return render_template("compose.html")
