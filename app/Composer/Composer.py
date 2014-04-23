from midiutil.MidiFile import MIDIFile
from ..LearningAgent.Note import Note
from ..LearningAgent.SongData import SongData

import ghmm

def compose(bar_model, note_models, duration_model, bar_alphabet, note_alphabet, duration_alphabet):
    song = MIDIFile(1)

    time = 0
    track = 0
    # TODO find the right tempo
    tempo = 120 * 4

    song.addTrackName(track, time, 'Track 1')
    song.addTempo(track, time, tempo)

    channel = 0
    pitch = 0
    volume = 127

    num_bars = 100
    notes_per_bar = 4

    # Gets a list of 100 bars
    bars = map(bar_alphabet.external, bar_model.sampleSingle(num_bars))

    # Gets a list of 100 note durations    
    durations = map(duration_alphabet.external, duration_model.sampleSingle(num_bars * notes_per_bar))
   
    index = 0 
    for bar in bars:
        # Gets a list of four notes per bar
        notes = map(note_alphabet.external, note_models[bar].sampleSingle(notes_per_bar))

        # Appends each note onto the end of the song
        for note in notes:
            duration = int(durations[index])
            song.addNote(track, channel, int(SongData.get_pitch(note)), time, duration, volume)
            time += duration
        
        index += 1

    binfile = open("output.mid", "wb")
    song.writeFile(binfile)
    binfile.close()
        
