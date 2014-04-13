import ghmm
import Note
import BarLearner

def get_notes_and_durs(songs_data):
    notes = []
    durations = []

    for song_data in songs_data:
        note_vect = song_data.seg_pitches
        durs = song_data.seg_durations

        # This assumes that len(note_vect) and len(durations) are the same
        for i in xrange(len(note_vect)):
            # TODO remove durations from Note data
            notes.append(str(Note.Note(note_vect[i], str(durs[i]))))
            notes.append(str(durs[i]))

    return (notes, durations)

def train_model(songs_data):
    """Input: list of data on several songs (could be a single song)
       Ouput: a list of models, one for each bar type. """
    note_models = {}
    (notes, durations) = get_notes_and_durs(songs_data)

    bars = BarLearner.get_bars(songs_data)

    for bar in set(bars):
        # This tells GHMM every possible value that it will be seeing
        alphabet = ghmm.Alphabet(list(set(notes)))
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
        
        # The sequence of notes gathered from the music
        train_seq = ghmm.EmissionSequence(alphabet, notes)
        
        # Generate the model of the data
        m = ghmm.HMMFromMatrices(alphabet, ghmm.DiscreteDistribution(alphabet), trans, emiss, pi)
 
        note_models[bar] = m 

    for bar in bars:
        # Train the model based on the training sequence
        note_models[bar].baumWelch(train_seq)
   
    return (note_models, alphabet)

