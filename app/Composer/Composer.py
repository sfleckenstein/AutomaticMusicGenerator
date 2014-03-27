from midiutil.MidiFile import MIDIFile
from LearningAgent.Note import Note

from LearningAgent.SongData import SongData

import ghmm

def compose(model, alphabet):
    write_to_disk(map(alphabet.external, model.sampleSingle(100)))

def write_to_disk(notes):
    song = MIDIFile(1)

    time = 0
    track = 0
    # TODO find the actual tempo of the song
    tempo = 120 

    song.addTrackName(track, time, "Test Track")
    
    song.addTempo(track, time, 1000) 

    channel = 0
    pitch = 0
    time = 0
    # TODO modulate the volume
    volume = 127

    for note_vect in notes:
        duration = int(Note.get_duration(note_vect, tempo))
        song.addNote(track, channel, int(SongData.get_pitch(note_vect)), time, duration, volume)
        time += duration

    binfile = open("output.mid", 'wb')
    song.writeFile(binfile)
    binfile.close()

