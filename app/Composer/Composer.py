from midiutil.MidiFile import MIDIFile
from LearningAgent.Note import Note

from LearningAgent.SongData import SongData

import ghmm

def compose(bar_model, note_models, bar_alphabet, note_alphabet):
    song = MIDIFile(1)

    time = 0
    track = 0
    # TODO find the right tempo
    tempo = 120

    song.addTrackName(track, time, 'Track 1')
    song.addTempo(track, time, tempo)

    channel = 0
    pitch = 0
    # TODO modulate the volume
    volume = 127

    bars = map(bar_alphabet.external, bar_model.sampleSingle(100))
    
    for bar in bars:
        notes = map(note_alphabet.external, note_models[bar].sampleSingle(4))

        for note in notes:
            duration = int(SongData.get_duration(note, tempo))
            song.addNote(track, channel, int(SongData.get_pitch(note)), time, duration, volume)
            time += duration

    binfile = open("output.mid", "wb")
    song.writeFile(binfile)
    binfile.close()
        
