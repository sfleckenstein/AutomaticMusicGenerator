import sys
import time 

from flask import render_template
from app import app
from forms import ChoiceForm

from pyechonest import song, config
from config import ECHO_NEST_API_KEY

from Composer import Composer
from LearningAgent import NoteLearner
from LearningAgent import DataCollector

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

@app.route('/')
def index():
    return render_template("index.html", form=ChoiceForm())

@app.route('/begin')
def begin():
    #TODO: Logic for displaying to user
    return render_template("begin.html")


@app.route("/compose", methods=["GET","POST"])
def compose(style, max_tempo=None, min_tempo=None):
    songs = song.search(style=style, 
                        max_tempo=max_tempo,
                        min_tempo=min_tempo,
                        results=1)

    song_ids = []
    for song in songs:
        song_ids.append(song.id)

    song_data = DataCollector.collect_data(song_ids)

    (model, alphabet) = NoteLearner.train_model(song_data)

    comp = Composer.compose(model, alphabet)

    return render_template("compose.html", comp=comp)
