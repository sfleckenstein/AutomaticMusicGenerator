import urllib2
from pyechonest import config, song, track
from config import ECHO_NEST_API_KEY 
import SongData

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def collect_data(song_ids):
    """Input: a list of song IDs
       Output: a list of SongData objects fulled with useful information about the songs"""

    song_data = []

    for song_id in song_ids:
        this_song = song.profile(song_id)
        summary = this_song[0].audio_summary
    
        url  = urllib2.urlopen(summary['analysis_url'])
    
        data = ''
        for line in url.readlines():
            data = data + line
    
        split = data.split('}')
        
        sections = []
        bars = []
        beats = []
        tatums = []
        segments = []

        for line in split:
            if 'sections' in line:
                sections.append(line)
            if 'bars' in line:
                bars.append(line)
            if 'beats' in line:
                beats.append(line)
            if 'tatums' in line:
                tatums.append(line)
            if 'segments' in line:
                segments.append(line)
    
        (bar_starts, bar_durations) = starts_and_durations(bars)
        (beat_starts, beat_durations) = starts_and_durations(beats)
        (tatum_starts, tatum_durations) = starts_and_durations(tatums)
        (seg_pitches, sec_durations) = seg_pitches_and_durations(segments)
        (sec_starts, sec_durations, sec_loudness, sec_tempo, sec_time_sig, sec_key, sec_mode) = section_data(sections)  
 
        song_data.append(SongData.SongData(bar_starts, bar_durations,
                                           beat_starts, beat_durations,
                                           tatum_starts, tatum_durations,
                                           seg_pitches, sec_durations,
                                           sec_starts, sec_durations, sec_loudness, sec_tempo, sec_time_sig, sec_key, sec_mode))

    return song_data

def starts_and_durations(units):
    """Returns a tuple with the unit starts and durations. Can be applied to bars, or beats."""
    starts = []
    durations = []
    
    for unit in units:
        for data in unit.split():
            if 'start' in data:
                start_loc = str(unit).find('start') + len('start') + 2 
                end_loc   = str(unit).find(',', start_loc, len(str(unit)))
                starts.append(str(unit)[start_loc:end_loc])
  
            if 'duration' in data:
                start_loc = str(unit).find('duration') + len('duration') + 2 
                end_loc   = str(unit).find(',', start_loc, len(str(unit)))
                durations.append(str(unit)[start_loc:end_loc])
      
    return (starts, durations) 

def seg_pitches_and_durations(segments):
    """This function gets all of the pitches from a segment, and returns them
       as a list. The pitches comprising a single note are surrounded by single quotes"""
    pitches = []
    durations = []
    for segment in segments:
        for data in segment.split():
            if 'pitches' in data: 
                start_loc = str(segment).find('pitches') + len('pitches') + 3
                end_loc   = str(segment).find(']', start_loc, len(str(segment)))
                pitches.append(str(segment)[start_loc:end_loc])
            
            if 'duration' in data:
                start_loc = str(segment).find('duration') + len('duration') + 2
                end_loc   = str(segment).find(',', start_loc, len(str(segment)))
                durations.append(str(segment)[start_loc:end_loc])

    return (pitches, durations)

def section_data(sections):
    starts = []
    durations = []
    loudness = 0
    tempo = 0
    time_sig = 0
    key = 0
    mode = 2   
 
    for section in sections:
        for data in section.split():
            if 'start' in data:
                start_loc = str(section).find('start') + len('start') + 2 
                end_loc   = str(section).find(',', start_loc, len(str(section)))
                starts.append(str(section)[start_loc:end_loc])
  
            if 'duration' in data:
                start_loc = str(section).find('duration') + len('duration') + 2 
                end_loc   = str(section).find(',', start_loc, len(str(section)))
                durations.append(str(section)[start_loc:end_loc])
            
            if 'loudness' in data:
                start_loc = str(section).find('loudness') + len('loudness') + 2 
                end_loc   = str(section).find(',', start_loc, len(str(section)))
                loudness = float(str(section)[start_loc:end_loc])
      
            if 'tempo' in data:
                start_loc = str(section).find('tempo') + len('tempo') + 2 
                end_loc   = str(section).find(',', start_loc, len(str(section)))
                tempo = float(str(section)[start_loc:end_loc])
  
            if 'time_signature' in data:
                start_loc = str(section).find('time_signature') + len('time_signature') + 2 
                end_loc   = str(section).find(',', start_loc, len(str(section)))
                time_sig = int(str(section)[start_loc:end_loc])
            
            if 'key' in data:
                start_loc = str(section).find('key') + len('key') + 2 
                end_loc   = str(section).find(',', start_loc, len(str(section)))
                key = int(str(section)[start_loc:end_loc])
            
            if 'mode' in data:
                start_loc = str(section).find('mode') + len('mode') + 2 
                end_loc   = str(section).find(',', start_loc, len(str(section)))
                mode = int(str(section)[start_loc:end_loc])
    
    return(starts, durations, loudness, tempo, time_sig, key, mode) 

