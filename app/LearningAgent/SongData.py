import math

class SongData:
    """A container to hold all the useful info about songs"""

    PREV_PITCHES = 1

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
        self.seg_durations = self.attach_prev_durs(seg_durations)
        self.seg_pitches = self.clean_pitches(seg_pitches)

    def clean_pitches(self, pitches):
        """Pitches are given as a "chroma" vector, which includes info about the dominance
           of each pitch in the scale at that time. This removes every pitch from that data
           that is not particularly prevelant. Also attaches the previous pitch(es) to the
           current one. The first note is the current one. Notes are separated by a |."""
        midi_values = []

        for i in xrange(len(pitches)):
            for j in xrange(len(pitches[i])):
                if pitches[i][j] > 0.95:
                     pitches[i][j] = 1
                else:
                     pitches[i][j] = 0 

            midi_values.append(self.get_note(pitches[i]))

        return self.attach_prev_notes(midi_values) 

    def get_note(self, note_vect):
        for i in range(0, 12):
            if int(note_vect[i]) == 1:
               return 60 + i 
   
    def attach_prev_notes(self, notes):
        prev_notes = []


        prev_notes.append('00|{}'.format(notes[0]))
        # TODO fix the edge values in the range
        # TODO fix to use PREV_NOTES
        for i in range(1, len(notes)):
            prev_notes.append('{}|{}'.format(notes[i], notes[i-1]))

        print(prev_notes)
        return prev_notes

    def attach_prev_durs(self, durations):
        """Attaches durations to the end of a list. The current duration is the last one."""
        prev_durs = []
        prev_durs.append('{}|00'.format(durations[len(durations)-1]))
        for i in range(0, len(durations) - 1):
            prev_durs.append('{}|{}'.format(durations[i], durations[i+1]))

        return prev_durs         

    @staticmethod
    def get_pitch(note_data):
        dur_index = note_data.find('&')
        pitch_index = note_data.find('|')+1
        
        return note_data[pitch_index:dur_index]

    @staticmethod
    def get_duration(note_data, tempo):
        dur_index = note_data.find('&')+1
        next_dur_index = note_data.find('|', dur_index)
        sec = float(note_data[dur_index:next_dur_index])

        return int(math.ceil(tempo * float(sec) / 60))

