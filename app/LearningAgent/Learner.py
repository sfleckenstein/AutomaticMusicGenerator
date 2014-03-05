import ghmm

from Note import Note

def getNoteSeq():
    # Define all of the notes we will see
    # This will eventually be generated from the data received from The Echo Nest
    c_3 = Note('c_3', 10)
    d_3 = Note('f_3', 10)
    e_3 = Note('e_3', 10)
    f_3 = Note('f_3', 10)
    g_3 = Note('g_3', 10)
    a_3 = Note('a_3', 10)
    b_3 = Note('b_3', 10)
    c_4 = Note('c_4', 10)
    
    # This tells GHMM every possible value that it will be seeing
    alphabet = ghmm.Alphabet(
    [str(c_3), str(d_3), str(e_3),
     str(f_3), str(g_3), str(a_3), 
     str(b_3), str(c_4), str(c_3)])
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
