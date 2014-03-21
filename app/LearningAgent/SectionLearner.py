import ghmm

def get_sections():
    # TODO Implement
    pass

def get_section_sequence():
    sections = get_sections()

    alphabet = ghmm.Alphabet(sections)
    alpha_len = len(alphabet)
    
    # The sequence of sections gathered from the music
    train_seq = ghmm.EmissionSequence(alphabet, sections)

    trans_prob = 1.0 / len(alpha_len)
    trans = [[trans_prob for row in range(alpha_len)] for col in range(alpha_len)]
    
    emiss_prob = 1.0 / (alpha_len)
    emiss = [[emiss_prob for row in range(alpha_len)] for col in range(alpha_len)]

    pi = [1.0 / alpha_len] * alpha_len

    # Generate the model of the data
    m = ghmm.HMMFromMatrices(alphabet, ghmm.DiscreteDistribution(alphabet), trans, emiss, pi)

    # Train the model based on the training sequence
    m.baumWelch(train_seq)

    # Returns 5 sections represented as strings
    return(map(alphabet.external, m.sampleSingle(5)))
