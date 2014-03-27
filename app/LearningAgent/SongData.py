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
        
        for i in xrange(len(pitches)):
            for j in xrange(len(pitches[i])):
                if pitches[i][j] > 0.95:
                     pitches[i][j] = 1
                else:
                     pitches[i][j] = 0 
        
        return pitches
    
    # TODO Please find a different way to do this.
    @staticmethod
    def get_pitch(note_vect):
        index = note_vect.find('&')
        finder = note_vect[1:index-1].split(',')
       
        for i in range(0, 11):
            if int(finder[i]) == 1:
                return(60 + i)
        # TODO hacks. Figure out why this is happening
        return 0
    
