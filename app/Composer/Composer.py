from midiutil.MidiFile import MIDIFile

from LearningAgent.Note import Note

def compose(notes):
     for note in notes:
        print(Note.getPitch(note))
#    midi = MIDIFile(1)
#
#    time = 0	
#    track = 0
#    
#    midi.addTrackName(track, time, "Test Track")
#    midi.addTempo(track, time, 120)
#
#    track = 0
#    channel = 0
#    pitch = 60
#    time = 0
#    duration = 1
#    volume = 127 
#
#    midi.addNote(track, channel, pitch, time, duration, volume)
#    
#    pitch += 1
#    time += 2
#    midi.addNote(track, channel, pitch, time, duration, volume)
#
#    pitch += 1
#    time += 2
#    midi.addNote(track, channel, pitch, time, duration, volume)
#    
#    pitch += 1
#    time += 2
#    midi.addNote(track, channel, pitch, time, duration, volume)
#    
#    pitch += 1
#    time += 2
#    midi.addNote(track, channel, pitch, time, duration, volume)
#    
#    binfile = open("output.mid", 'wb')
#    midi.writeFile(binfile)
#    binfile.close()
