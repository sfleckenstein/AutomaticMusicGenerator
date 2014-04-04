from pyechonest import song, config

from config import ECHO_NEST_API_KEY

from Composer.Composer import compose 
import LearningAgent.BarLearner as BarLearner
import LearningAgent.NoteLearner as NoteLearner
from LearningAgent.DataCollector import collect_data

import time
import sys

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def main():
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

    print('Collecting data')
    songs_data = collect_data(song_ids)
    print('Data collected')

    print('Training models')
    (bar_model, bar_alphabet) = BarLearner.train_model(songs_data)
    (note_models, note_alphabet) = NoteLearner.train_model(songs_data)
    print('Models trained')

    print('Composing')
    compose(bar_model, note_models, bar_alphabet, note_alphabet)
    print('Done composing')
    end = time.time()
    
    print('Total time: {}'.format(end - start))

if __name__ == "__main__":
    main()
