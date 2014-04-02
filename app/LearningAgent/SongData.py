import math

PREV_PITCHES = 5 

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
        global PREV_PITCHES 

        prev_notes = []

        for i in xrange(PREV_PITCHES):
            append = ''
            for j in range(PREV_PITCHES-i, 0, -1):
                append += '00|'
            for j in range(1, i+1):
                append += str(notes[i-j]) + '|'
            append += str(notes[i])
            prev_notes.append('{}'.format(append))
        
        for i in range(PREV_PITCHES, len(notes)-2):
            append = ''
            for j in range(PREV_PITCHES+1, 0, -1):
                append += str(notes[i-j+1]) + '|'
            prev_notes.append(append[:-1])

        return prev_notes

    def attach_prev_durs(self, durations):
        """Attaches durations to the end of a list. The current duration is the last one."""
        global PREV_PITCHES 

        prev_durs = []

        for i in xrange(PREV_PITCHES):
            append = ''
            for j in range(PREV_PITCHES-i, 0, -1):
                append += '00|'
            for j in range(1, i+1):
                append += str(durations[i-j]) + '|'
            append += str(durations[i])
            prev_durs.append('{}'.format(append))
        
        for i in range(PREV_PITCHES, len(durations)-2):
            append = ''
            for j in range(PREV_PITCHES+1, 0, -1):
                append += str(durations[i-j+1]) + '|'
            prev_durs.append(append[:-1])

        return prev_durs         

    @staticmethod
    def get_pitch(note_data):
        dur_index = note_data.find('&')
        pitch_index = note_data.find('|')+1
        next_pitch_index = note_data.find('|', pitch_index)

        index = min(dur_index, next_pitch_index)
        
        return note_data[pitch_index:index]

    @staticmethod
    def get_duration(note_data, tempo):
        dur_index = note_data.find('&')+1
        next_dur_index = note_data.find('|', dur_index)
        sec = float(note_data[dur_index:next_dur_index])

        return int(math.ceil(tempo * float(sec) / 60))

