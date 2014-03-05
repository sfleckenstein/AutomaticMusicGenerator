import urllib2, json
from config import ECHO_NEST_API_KEY
from pyechonest import config, song


config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def get_songs(style=None, max_tempo=None, min_tempo=None, key=None, time_signature=None):
    songs = song.search(style=style,
                        max_tempo=max_tempo, 
                        min_tempo=min_tempo, 
                        key=key, 
                        results=100) # adjust number of results as necessary
                                     # max per search call is 100

    song_ids = [a_song.id for a_song in songs]
    return song_ids
