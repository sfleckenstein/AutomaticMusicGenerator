from midiutil.MidiFile import MIDIFile
from LearningAgent.Note import Note

from LearningAgent.SongData import SongData

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
    # TODO modulate the volume
    volume = 127

    # Gets a list of 100 bars
    bars = map(bar_alphabet.external, bar_model.sampleSingle(100))
    durations = map(duration_alphabet.external, duration_model.sampleSingle(100))
   
    index = 0 
    for bar in bars:
        # TODO find the right number of notes to use
        # Gets a list of four notes per bar
        notes = map(note_alphabet.external, note_models[bar].sampleSingle(4))

        for note in notes:
            duration = int(durations[index])
            song.addNote(track, channel, int(SongData.get_pitch(note)), time, duration, volume)
            time += duration
        
        index += 1

    binfile = open("output.mid", "wb")
    song.writeFile(binfile)
    binfile.close()
        
