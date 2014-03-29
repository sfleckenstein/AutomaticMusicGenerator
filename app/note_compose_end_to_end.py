from pyechonest import song, config

from config import ECHO_NEST_API_KEY

from Composer.Composer import compose 
from LearningAgent.NoteLearner import train_model 
from LearningAgent.DataCollector import collect_data

import time
import sys

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def main():
    start = time.time()
    #print('Start time: {}'.format(start))
    #print('Starting search')
    songs = song.search(style='folk',
                        max_tempo=150,
                        min_tempo=100,
                        results=1)
    #print('Search returned')

    song_ids = []
    for track in songs:
        song_ids.append(track.id)

    #print('Collecting data')
    song_data = collect_data(song_ids)
    #print('Data collected')

    #print('Training model')
    (model, alphabet) = train_model(song_data)
    #print('Model trained')

    #print('Composing')
    compose(model, alphabet)
    #print('Done composing')
    end = time.time()
    #print('End time: {}'.format(end))
    print('Total time: {}'.format(end - start))

if __name__ == "__main__":
    main()
