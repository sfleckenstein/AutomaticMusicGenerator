import threading
import ghmm
import Note, BarLearner
from SongData import SongData
from Trainer import Trainer

class NoteLearner(threading.Thread):
    # TODO: This is just the setup, we need to actually use this as thread
    def __init__(self, thread_id, name, counter, songs_data, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
        self.songs_data = songs_data
        self.queue = queue

    def run(self):
        print "Starting " + self.name
        self.queue.put(train_model(self.songs_data))
        print "Exiting " + self.name

def get_notes(songs_data):
    notes = []

    for song_data in songs_data:
        note_vect = song_data.seg_pitches

        for i in xrange(len(note_vect)):
            notes.append(str(Note.Note(note_vect[i])))

    return notes

def train_model(songs_data):
    """Input: list of data on several songs (could be a single song)
       Ouput: a list of models, one for each bar type. """
    note_models = {}
    notes = get_notes(songs_data)
    
    # This tells GHMM every possible value that it will be seeing
    note_alphabet = ghmm.Alphabet(list(set(notes)))
    note_alpha_len = len(note_alphabet)
 
    # Initiaize the probabilities of transitioning from each state to each other
    # state. There is probably a better way to do this, but this is nice and simple.
    note_trans_prob = 1.0 / (note_alpha_len)
    trans = [[note_trans_prob for row in range(note_alpha_len)] for col in range(note_alpha_len)]
    
    # Initialize the probabilities of seeing each output from each state.
    # Again, there is probably a better way to do this, but this is simple.
    note_emiss_prob = 1.0 / (note_alpha_len)
    emiss = [[note_emiss_prob for row in range(note_alpha_len)] for col in range(note_alpha_len)]
    
    # Some grease to get GHMM to work
    pi = [1.0/note_alpha_len] * note_alpha_len 
    
    # The sequence of notes gathered from the music
    note_train_seq = ghmm.EmissionSequence(note_alphabet, notes)

    bars = BarLearner.get_bars(songs_data)
    for bar in set(bars):
        # Generate the model of the data
        note_models[bar] = ghmm.HMMFromMatrices(note_alphabet, ghmm.DiscreteDistribution(note_alphabet), trans, emiss, pi)

    for bar in bars:
        # Train the model based on the training sequence
        note_models[bar].baumWelch(note_train_seq)
 
    return (note_models, note_alphabet)

