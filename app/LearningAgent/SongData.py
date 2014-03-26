class SongData:
    """A container to hold all the useful info about songs"""

    def __init__(self, sec_starts, sec_durations,
                       bar_starts, bar_durations,
                       beat_starts, beat_durations,
                       tatum_starts, tatum_durations,
                       seg_starts, seg_durations, seg_pitches):
        self.sec_starts = sec_starts
        self.sec_durations = sec_durations

        self.bar_starts = bar_starts
        self.bar_durations = bar_durations 
        
        self.beat_starts = beat_starts
        self.beat_durations = beat_durations 
        
        self.tatum_starts = tatum_starts
        self.tatum_durations = tatum_durations 

        self.seg_starts = seg_starts
        self.seg_durations = seg_durations
        self.seg_pitches = self.clean_pitches(seg_pitches)

    def clean_pitches(self, pitches):
        """Pitches are given as a "chroma" vector, which includes info about the dominance
           of each pitch in the scale at that time. This removes every pitch from that data
           that is not particularly prevelant"""
        notes = []
        
        for pitch_vect in pitches:
            for i in xrange(len(pitch_vect)):
                if pitch_vect[i] > 0.95:
                    notes.append(self.get_note(i))
        
        return(notes)

    # TODO should probably look at the scale to determine which enharmonic note is correct
    def get_note(self, pitch):
        return {
            0 : 'c',
            1 : 'c#',
#            1 : 'd@',
            2 : 'd',
            3 : 'd#',
#            3 : 'e@',
            4 : 'e',
            5 : 'f',
            6 : 'f#',
#            6 : 'g@',
            7 : 'g',
            8 : 'g#',
#            8 : 'a@',
            9 : 'a',
            10: 'a#',
#            10:'b@'
            11:'b',
               }.get(pitch)

