import ghmm
import Note

def get_notes(song_data):
    note_vect = song_data.seg_pitches
    durations = song_data.seg_durations

    notes = []

    # This assumes that len(note_vect) and len(durations) are the same
    for i in xrange(len(note_vect)):
        notes.append(str(Note.Note(note_vect[i], str(durations[i]))))

    return notes

def train_model(song_data):
    notes = get_notes(song_data) 
 
    # This tells GHMM every possible value that it will be seeing
    alphabet = ghmm.Alphabet(list(set(notes)))
    alphaLen = len(alphabet)

    # The sequence of notes gathered from the music
    train_seq = ghmm.EmissionSequence(alphabet, notes) 
 
    # Initiaize the probabilities of transitioning from each state to each other
    # state. There is probably a better way to do this, but this is nice and simple.
    trans_prob = 1.0 / (alphaLen)
    trans = [[trans_prob for row in range(alphaLen)] for col in range(alphaLen)]
    
    # Initialize the probabilities of seeing each output from each state.
    # Again, there is probably a better way to do this, but this is simple.
    emiss_prob = 1.0 / (alphaLen)
    emiss = [[emiss_prob for row in range(alphaLen)] for col in range(alphaLen)]
    
    # Some grease to get GHMM to work
    pi = [1.0/alphaLen] * alphaLen 
    
    # Generate the model of the data
    m = ghmm.HMMFromMatrices(alphabet, ghmm.DiscreteDistribution(alphabet), trans, emiss, pi)
    
    # Train the model based on the training sequence
    m.baumWelch(train_seq)
   
    return (m, alphabet)

    # Returns 20 notes represented as strings
    #return(map(alphabet.external, m.sampleSingle(20)))
