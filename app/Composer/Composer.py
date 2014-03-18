from LearningAgent.Note import Note 
from midiutil.MidiFile import MIDIFile

def compose(notes):
    midi = MIDIFile(1)

    time = 0    
    track = 0
    
    midi.addTrackName(track, time, "Test Track")
    midi.addTempo(track, time, 120)

    track = 0
    channel = 0
    pitch = 60
    time = 0
    duration = 1
    volume = 127 

    for note in notes:
       duration = int(Note.getDuration(note))
       pitch = Note.getPitch(note)

       midi.addNote(track, channel, pitch, time, duration, volume)
       time += duration

    binfile = open("output.mid", 'wb')
    midi.writeFile(binfile)
    binfile.close()
