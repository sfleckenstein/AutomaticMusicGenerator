import math
import ghmm
import Bar
from SongData import SongData
from Trainer import Trainer

def get_bars(songs_data):
    bars = []
    
    for song_data in songs_data:
        seg_starts = song_data.seg_starts
        bar_starts = song_data.bar_starts
        pitches = song_data.seg_pitches

        # Because of how the song data is being collected, these two
        # don't match up, even though they should
        pitches_and_segs = min(len(pitches), len(seg_starts)) - 1

        # The bars starts don't match exactly with the pitch starts,
        # hence this mess
        for i in xrange(pitches_and_segs):
            # The if should be true for bar_starts[len(bars)], but this
            # is to make sure.
            for j in range(len(bars), len(bar_starts)):
                if seg_starts[i] < bar_starts[j] < seg_starts[i+1]:
                    bars.append(str(Bar.Bar(SongData.get_pitch(pitches[i]))))
    
    return bars

def train_model(songs_data):
    """Input: list of data on several songs (could be a single song)
       Ouput: a model trained on all of the songs"""
    bars = get_bars(songs_data)
    trainer = Trainer(bars)
    m, alphabet = trainer.train()
    """
    # This tells GHMM every possible value that it will be seeing
    alphabet = ghmm.Alphabet(list(set(bars)))
    alphaLen = len(alphabet)

    # The sequence of bars gathered from the music
    train_seq = ghmm.EmissionSequence(alphabet, bars) 
 
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
    """
    return (m, alphabet)

