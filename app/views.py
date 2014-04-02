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
def compose(style, max_tempo=None, min_tempo=None):
    songs = song.search(style=style, 
                        max_tempo=max_tempo,
                        min_tempo=min_tempo,
                        results=1)

    song_ids = []
    for track in songs:
        song_ids.append(track.id)

    song_data = collect_data(song_ids)

    (model, alphabet) = train_model(song_data)

    comp = compose(model, alphabet)

    return render_template("compose.html", comp=comp)
