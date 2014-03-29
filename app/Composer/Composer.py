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
    
    song.addTempo(track, time, tempo) 

    channel = 0
    pitch = 0
    time = 0
    # TODO modulate the volume
    volume = 127

    for note_data in notes:
        duration = int(SongData.get_duration(note_data, tempo))
        song.addNote(track, channel, int(SongData.get_pitch(note_data)), time, duration, volume)
        #print('Dur: {} Pitch: {}'.format(duration, SongData.get_pitch(note_data)))
        time += duration

    binfile = open("output.mid", "wb")
    song.writeFile(binfile)
    binfile.close()

