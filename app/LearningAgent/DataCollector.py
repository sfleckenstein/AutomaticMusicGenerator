from pyechonest import config, song, track
from config import ECHO_NEST_API_KEY 
import SongData
import json, requests

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def get_genres():
    genres = []
    url = 'http://developer.echonest.com/api/v4/genre/list?api_key=' + ECHO_NEST_API_KEY + '&format=json'

    resp = requests.get(url=url)
    data = json.loads(resp.content)
    genres = data['response']['genres']
    return [genre.values()[0].encode('utf-8') for genre in genres]

def collect_data(song_ids):
    """Input: a list of song IDs
       Output: a list of SongData objects fulled with useful information about the songs"""

    song_data = []
    print song_ids
    for song_id in song_ids:
        this_song = song.profile(song_id)
        summary = this_song[0].audio_summary
        print summary
        url  = summary['analysis_url']
        musical_events = dict(
            sects='sections',
            brs='bars',
            bts='beats',
            ttms='tatums',
            sgmnts='segments')

        resp = requests.get(url=url,params=musical_events)
        data = json.loads(resp.content)
        
        # Separate the musical elements
        sections = data["sections"]
        bars = data["bars"]
        beats = data["beats"]
        tatums = data["tatums"]
        segments = data["segments"]

        """ Get relevant information from the sections, bars, beats, tatums, and segments"""
        sec_starts = []
        sec_durations = []
        for section in xrange(len(sections)):
            sec_starts.append(sections[section]["start"])
            sec_durations.append(sections[section]["duration"])

        bar_starts = []
        bar_durations = []
        for bar in xrange(len(bars)):
            bar_starts.append(bars[bar]["start"])
            bar_durations.append(bars[bar]["duration"])

        beat_starts = []
        beat_durations = []
        for beat in xrange(len(beats)):
            beat_starts.append(beats[beat]["start"])
            beat_durations.append(beats[beat]["duration"])

        tatum_starts = []
        tatum_durations = []
        for tatum in xrange(len(tatums)):
            tatum_starts.append(tatums[tatum]["start"])
            tatum_durations.append(tatums[tatum]["duration"])

        seg_starts = []
        seg_durations = []
        seg_pitches = []
        for segment in xrange(len(segments)):
            seg_starts.append(segments[segment]["start"])
            seg_durations.append(segments[segment]["duration"])
            seg_pitches.append(segments[segment]["pitches"])

        song_data.append(SongData.SongData(sec_starts, sec_durations,
                                           bar_starts, bar_durations,
                                           beat_starts, beat_durations,
                                           tatum_starts, tatum_durations,
                                           seg_starts, seg_durations, seg_pitches))

    return song_data
