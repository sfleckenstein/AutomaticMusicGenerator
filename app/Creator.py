import time
import sys

from pyechonest import song, config

import LearningAgent.BarLearner as BarLearner
import LearningAgent.NoteLearner as NoteLearner
import LearningAgent.DurationLearner as DurationLearner

from config import ECHO_NEST_API_KEY
from Composer.Composer import compose
from LearningAgent.DataCollector import collect_data
from LearningAgent.SongSelector import rank_songs


config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def create(style, max_tempo=None, min_tempo=None, key=None, time_sig=None):
    print('Starting search')
    songs = song.search(style=style,
                        max_tempo=max_tempo,
                        min_tempo=min_tempo,
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
    (bar_model, bar_alphabet) = BarLearner.train_model(songs_data)
    print str(bar_model), str(bar_alphabet)
    (note_models, note_alphabet) = NoteLearner.train_model(songs_data)
    print str(note_models), str(note_alphabet)
    (duration_model, duration_alphabet) = DurationLearner.train_model(songs_data, tempo)
    print str(duration_model), str(duration_alphabet)
    print('Models trained')

    print('Composing')
    compose(bar_model, note_models, duration_model, bar_alphabet, note_alphabet, duration_alphabet)
    print('Done composing')
    end = time.time()
    
    print('Total time: {}'.format(end - start))
