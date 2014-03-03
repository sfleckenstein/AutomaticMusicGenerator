from pyechonest import config, song
import urllib2, json
import config as con

config.ECHO_NEST_API_KEY=con.ECHO_NEST_API_KEY
analysis_urls = [] 

def get_songs(style, max_tempo=None, min_tempo=None, key=None, time_signature=None):
    songs = song.search(style=style, 
                        max_tempo=max_tempo, 
                        min_tempo=min_tempo, 
                        key=key, 
                        results=100)
    if songs:
        ts = songs[0]
        for a_song in songs:
            analysis_url = ts.audio_summary['analysis_url']
            analysis_urls.append(analysis_url)
            print (a_song.artist_name, a_song.title)
    else:
        print 'No songs found'

def get_songs_json(songs):
    for a_song in songs:
        request = urllib2.urlopen(a_song)
        json_string = request.read()
        print json.loads(json_string)

if __name__ == "__main__":
    get_songs(style='rock', key=0, min_tempo=180, max_tempo=200)
