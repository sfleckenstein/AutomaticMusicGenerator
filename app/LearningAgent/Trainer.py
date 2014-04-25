import ghmm

class Trainer:
    def __init__(self, events):
        self.events = events

    def train(self):
        # This tells GHMM every possible value that it will be seeing
        alphabet = ghmm.Alphabet(list(set(self.events)))
        alphaLen = len(alphabet)

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
    
        # The sequence of musical events gathered from the music
        train_seq = ghmm.EmissionSequence(alphabet, self.events) 
 
        # Generate the model of the data
        m = ghmm.HMMFromMatrices(alphabet, ghmm.DiscreteDistribution(alphabet), trans, emiss, pi)
    
        # Train the model based on the training sequence
        m.baumWelch(train_seq)

        return (m, alphabet)
