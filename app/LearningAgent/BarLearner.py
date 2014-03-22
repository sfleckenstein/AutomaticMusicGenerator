import ghmm

def get_bars():
    #TODO Implement
    pass

def get_bar_sequence():
    bars = get_bars()

    alphabet = ghmm.Alphabet(bars)
    alpha_len = len(alphabet)

    train_seq = ghmm.EmissionSequence(alphabet, bars)

    trans_prob = 1.0 / alpha_len
    trans = [[trans_prob for row in range(alpha_len)] for col in range(alpha_len)]

    emiss_prob = 1.0 / alpha_len
    emiss = [[emiss_prob for row in range(alpha_len)] for col in range(alpha_len)]

    pi = [1.0 / alpha_len] * alpha_len

    m = ghmm.HMMFromMatrices(alphabet, ghmm.DiscreteDistribution(alphabet), trans, emiss, pi)

    m.baumWelch(train_seq)

    return(map(alphabet.external, m.sampleSingle(100)))
