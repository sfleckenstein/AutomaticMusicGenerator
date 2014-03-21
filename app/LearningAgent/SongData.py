class SongData:
    """A container to hold all the useful info about songs"""

    def __init__(self, bar_starts, bar_durations,
                      beat_starts, beat_durations,
                      tatum_starts, tatum_durations,
                      pitches, durations,
                      sec_starts, sec_durations, loudness, tempo, time_signature, key, mode):
        self.bar_starts = bar_starts
        self.bar_durations = bar_durations 
        
        self.beat_starts = beat_starts
        self.beat_durations = beat_durations 
        
        self.tatum_starts = tatum_starts
        self.tatum_durations = tatum_durations 
        
        self.pitches = pitches
        self.durations = durations
        
        self.sec_starts = sec_starts
        self.sec_durations = sec_durations
        self.loudness = loudness
        self.tempo = tempo
        self.time_signature = time_signature
        self.key = key
        self.mode = mode

