from midiutil.MidiFile import MIDIFile

from LearningAgent.Note import Note

def compose(notes):
    song = MIDIFile(1)

    time = 0
    track = 0

    song.addTrackName(track, time, "Test Track")
    
    # TODO find the actual tempo of the song
    song.addTempo(track, time, 120) 

    channel = 0
    pitch = 0
    time = 0
    volume = 127

    for note in notes:
        duration = int(Note.getDuration(note))
        song.addNote(track, channel, Note.getPitch(note), time, duration, volume)
        time += duration

    binfile = open("output.mid", 'wb')
    song.writeFile(binfile)
    binfile.close()

