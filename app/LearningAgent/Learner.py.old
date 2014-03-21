import ghmm

from Note import Note

def get_note_seq():
    # Define all of the notes we will see
    # This will eventually be generated from the data received from The Echo Nest
    notes = []

    c_3 = Note('c_3', '016')
    notes.append(str(c_3))

    d_3 = Note('d_3', '002')
    notes.append(str(d_3))
    
    e_3 = Note('e_3', '014')
    notes.append(str(e_3))
    
    f_3 = Note('f_3', '002')
    notes.append(str(f_3))
    
    g_3 = Note('g_3', '012')
    notes.append(str(g_3))
    
    a_3 = Note('a_3', '004')
    notes.append(str(a_3))
    
    b_3 = Note('b_3', '006')
    notes.append(str(b_3))
    
    c_4 = Note('c_4', '010')
    notes.append(str(c_4))
 
    # This tells GHMM every possible value that it will be seeing
    alphabet = ghmm.Alphabet(notes)
    alphaLen = len(alphabet)

    # The sequence of notes gathered from the music
    train_seq = ghmm.EmissionSequence(alphabet, [str(c_3), str(c_3), str(d_3)])
    
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
    
    # Returns 20 notes represented as strings
    return(map(alphabet.external, m.sampleSingle(20)))
