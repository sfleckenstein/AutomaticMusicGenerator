import sys, time, Queue

from flask import render_template
from app import app
from forms import ChoiceForm
from pyechonest import song, config

from LearningAgent.BarLearner import BarLearner
from LearningAgent.NoteLearner import NoteLearner
from LearningAgent.DurationLearner import DurationLearner

from config import ECHO_NEST_API_KEY
import Composer.Composer as composer
from LearningAgent.DataCollector import collect_data
from LearningAgent.SongSelector import rank_songs

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

@app.route('/')
def index():
    return render_template("index.html", form=ChoiceForm())

@app.route('/begin')
def begin():
    #TODO: Logic for displaying to user
    return render_template("begin.html")

@app.route('/compose', methods=['GET','POST'])
def compose():
    print('Starting search')
    songs = song.search(style='folk',
                        max_tempo=150,
                        min_tempo=100,
                        results=1)

    print('Search returned')
    start = time.time()
                    
    song_ids = []
    for track in songs:
        song_ids.append(track.id)
                                            
    # TODO get the real tempo
    tempo = 120 * 4 

    print('Collecting data')
    songs_data = collect_data(song_ids)
    print('Data collected')

    print('Ranking songs')
    rank_songs(songs_data, tempo) 
    print('Songs ranked')
    print('Training models')
   
    q = Queue.Queue()
    bar_thread = BarLearner(1, "BarLearner", 1, songs_data, q)
    note_thread = NoteLearner(2, "NoteLearner", 2, songs_data, q)
    dur_thread = DurationLearner(3, "DurationLearner", 3, songs_data, tempo, q)
    
    bar_thread.start()
    note_thread.start()
    dur_thread.start()

    (bar_model, bar_alphabet) = q.get() 
    #print (bar_model, bar_alphabet)
    #(note_models, note_alphabet) = q.get()
    #print (note_models, note_alphabet)
    #(dur_model, dur_alphabet) = q.get()
    #print (dur_model, dur_alphabet)
    #(bar_model, bar_alphabet) = BarLearner.train_model(songs_data)
    (note_models, note_alphabet) = NoteLearner.train_model(songs_data)
    (dur_model, dur_alphabet) = DurationLearner.train_model(songs_data, tempo)
    print('Models trained')

    print('Composing')
    composer.compose(bar_model, note_models, dur_model, bar_alphabet, note_alphabet, dur_alphabet)
    print('Done composing')
    end = time.time()
    
    print('Total time: {}'.format(end - start))
    
    return render_template("compose.html")
