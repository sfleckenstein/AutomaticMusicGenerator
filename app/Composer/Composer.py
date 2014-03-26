from midiutil.MidiFile import MIDIFile
from LearningAgent.Note import Note
import ghmm

def compose(model, alphabet):
    write_to_disk(map(alphabet.external, model.sampleSingle(20)))

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
    volume = 127

    for note in notes:
        duration = int(Note.get_duration(note, tempo))
        song.addNote(track, channel, Note.get_pitch(note), time, duration, volume)
        print('Dur: {} Pitch: {}'.format(duration, Note.get_pitch(note)))
        time += duration

    binfile = open("output.mid", 'wb')
    song.writeFile(binfile)
    binfile.close()

