import ghmm

alphabet = ghmm.Alphabet(notes)
alphalen = len(alphabet)

train_seq = ghmm.EmissionSequence(alphabet, seq)

trans_prob = 1.0 / len(alphalen)

emis_prob = 
