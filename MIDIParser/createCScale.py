import midi
# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.C_3)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.C_3)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.D_3)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.D_3)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.E_3)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.E_3)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.F_3)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.F_3)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.G_3)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.A_3)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.A_3)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.B_3)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.B_3)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.C_4)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.C_4)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.D_4)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.D_4)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.E_4)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.E_4)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.F_4)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.F_4)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.G_4)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.G_4)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.A_4)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.A_4)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.B_4)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.B_4)
track.append(off)

on = midi.NoteOnEvent(tick=100, velocity=127, pitch=midi.C_5)
track.append(on)
off = midi.NoteOffEvent(tick=100, pitch=midi.C_5)
track.append(off)

# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=100)
track.append(eot)
# Print out the pattern
print pattern
# Save the pattern to disk
midi.write_midifile("example.mid", pattern)