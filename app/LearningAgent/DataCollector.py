import urllib2
from pyechonest import config, song, track
from config import ECHO_NEST_API_KEY 
import SongData

config.ECHO_NEST_API_KEY=ECHO_NEST_API_KEY

def collect_data(song_ids):
    """Input: a list of song IDs
       Output: a list of SongData objects fulled with useful information about the songs"""

    song_data = []

    for i in range(0, len(song_ids)): 
        this_song = song.profile(song_ids[i])
        summary = this_song[0].audio_summary
    
        url  = urllib2.urlopen(summary['analysis_url'])
    
        data = ''
        for line in url.readlines():
            data = data + line
    
        split = data.split('}')
    
        bars = []
        beats = []
        tatums = []
        segments = []
        sections = []   
 
        append_bars = False
        append_beats = False
        append_tatums = False
        append_segments = False
        append_sections = False    

        # This seems like a silly way to do this, but Python doesn't
        # support switch statements. Suggestions welcome.
        for line in split:
            if 'bars' in line:
                append_bars = True
                append_beats = False
                append_tatums = False
                append_segments = False
                append_sections = False    
            if 'beats' in line:
                append_bars = False 
                append_beats = True 
                append_tatums = False
                append_segments = False
                append_sections = False    
            if 'tatums' in line:
                append_bars = False 
                append_beats = False 
                append_tatums = True 
                append_segments = False
                append_sections = False    
            if 'segments' in line:
                append_bars = False 
                append_beats = False 
                append_tatums = False 
    	        append_segments = True
                append_sections = False    
            if 'sections' in line:
                append_bars = False 
                append_beats = False 
                append_tatums = False 
    	        append_segments = False 
                append_sections = True 
    
            if append_bars:
                bars.append(line)
            if append_beats:
                beats.append(line)
            if append_tatums:
                tatums.append(line)
            if append_segments:
                segments.append(line)
            if append_sections:
                sections.append(line)
    
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
    
    for i in range(0, len(units)):
        for data in units[i].split():
            if 'start' in data:
                start_loc = str(units[i]).find('start') + len('start') + 2 
                end_loc   = str(units[i]).find(',', start_loc, len(str(units[i])))
                starts.append(str(units[i])[start_loc:end_loc])
  
            if 'duration' in data:
                start_loc = str(units[i]).find('duration') + len('duration') + 2 
                end_loc   = str(units[i]).find(',', start_loc, len(str(units[i])))
                durations.append(str(units[i])[start_loc:end_loc])
      
    return (starts, durations) 

def seg_pitches_and_durations(segments):
    """This function gets all of the pitches from a segment, and returns them
       as a list. The pitches comprising a single note are surrounded by single quotes"""
    pitches = []
    durations = []
    for i in range(0, len(segments)):
        for data in segments[i].split():
            if 'pitches' in data: 
                start_loc = str(segments[i]).find('pitches') + len('pitches') + 3
                end_loc   = str(segments[i]).find(']', start_loc, len(str(segments[i])))
                pitches.append(str(segments[i])[start_loc:end_loc])
            
            if 'duration' in data:
                start_loc = str(segments[i]).find('duration') + len('duration') + 2
                end_loc   = str(segments[i]).find(',', start_loc, len(str(segments[i])))
                durations.append(str(segments[i])[start_loc:end_loc])

    return (pitches, durations)

def section_data(sections):
    starts = []
    durations = []
    loudness = 0
    tempo = 0
    time_sig = 0
    key = 0
    mode = 2   
 
    for i in range(0, len(sections)):
        for data in sections[i].split():
            if 'start' in data:
                start_loc = str(sections[i]).find('start') + len('start') + 2 
                end_loc   = str(sections[i]).find(',', start_loc, len(str(sections[i])))
                starts.append(str(sections[i])[start_loc:end_loc])
  
            if 'duration' in data:
                start_loc = str(sections[i]).find('duration') + len('duration') + 2 
                end_loc   = str(sections[i]).find(',', start_loc, len(str(sections[i])))
                durations.append(str(sections[i])[start_loc:end_loc])
            
            if 'loudness' in data:
                start_loc = str(sections[i]).find('loudness') + len('loudness') + 2 
                end_loc   = str(sections[i]).find(',', start_loc, len(str(sections[i])))
                loudness = float(str(sections[i])[start_loc:end_loc])
      
            if 'tempo' in data:
                start_loc = str(sections[i]).find('tempo') + len('tempo') + 2 
                end_loc   = str(sections[i]).find(',', start_loc, len(str(sections[i])))
                tempo = float(str(sections[i])[start_loc:end_loc])
  
            if 'time_signature' in data:
                start_loc = str(sections[i]).find('time_signature') + len('time_signature') + 2 
                end_loc   = str(sections[i]).find(',', start_loc, len(str(sections[i])))
                time_sig = int(str(sections[i])[start_loc:end_loc])
            
            if 'key' in data:
                start_loc = str(sections[i]).find('key') + len('key') + 2 
                end_loc   = str(sections[i]).find(',', start_loc, len(str(sections[i])))
                key = int(str(sections[i])[start_loc:end_loc])
            
            if 'mode' in data:
                start_loc = str(sections[i]).find('mode') + len('mode') + 2 
                end_loc   = str(sections[i]).find(',', start_loc, len(str(sections[i])))
                mode = int(str(sections[i])[start_loc:end_loc])
    
    return(starts, durations, loudness, tempo, time_sig, key, mode) 

