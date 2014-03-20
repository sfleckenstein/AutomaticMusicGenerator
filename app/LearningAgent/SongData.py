class SongData:
    def __init__(self, bar_starts, bar_durations,
                      beat_starts, beat_durations,
                      tatum_starts, tatum_durations,
                      pitches, durations):
        self.bar_starts = bar_starts
        self.bar_durations = bar_durations 
        self.beat_starts = beat_starts
        self.beat_durations = beat_durations 
        self.tatum_starts = tatum_starts
        self.tatum_durations = tatum_durations 
        self.pitches = pitches
        self.durations = durations  
