from flask import render_template
from app import app
from forms import ChoiceForm

@app.route('/')
def index():
    return render_template("index.html", title='Intelligent Music Generator', form=ChoiceForm())
