from pyechonest import config, song, track
from config import ECHO_NEST_API_KEY 
import SongData
import json, requests

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def collect_data(song_ids):
    """Input: a list of song IDs
       Output: a list of SongData objects fulled with useful information about the songs"""

    song_data = []

    for song_id in song_ids:
        this_song = song.profile(song_id)
        summary = this_song[0].audio_summary
    
        url  = summary['analysis_url']
        print url
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
        sec_loudnesses = []
        sec_tempos = []
        sec_time_sigs = []
        sec_keys = []
        sec_modes = []
        for section in xrange(len(sections)):
            sec_starts.append(sections[section]["start"])
            sec_durations.append(sections[section]["duration"])
            sec_loudnesses.append(sections[section]["loudness"])
            sec_tempos.append(sections[section]["tempo"])
            sec_time_sigs.append(sections[section]["time_signature"])
            sec_keys.append(sections[section]["key"])
            sec_modes.append(sections[section]["mode"])
        
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

        segment_pitches = []
        segment_durations = []
        for segment in xrange(len(segments)):
            segment_pitches.append(segments[segment]["pitches"])
            segment_durations.append(segments[segment]["duration"])
        
        song_data.append(SongData.SongData(bar_starts, bar_durations,
                                           beat_starts, beat_durations,
                                           tatum_starts, tatum_durations,
                                           segment_pitches, segment_durations,
                                           sec_starts, sec_durations, 
                                           sec_loudnesses, sec_tempos, 
                                           sec_time_sigs, sec_keys, sec_modes))
    return song_data
