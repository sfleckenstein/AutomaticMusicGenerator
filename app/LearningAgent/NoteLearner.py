import ghmm
import Note
import BarLearner
from SongData import SongData

def get_notes_and_durs(songs_data, tempo):
    notes = []
    durations = []

    for song_data in songs_data:
        note_vect = song_data.seg_pitches
        durs = song_data.seg_durations

        # This assumes that len(note_vect) and len(durations) are the same
        for i in xrange(len(note_vect)):
            # TODO remove durations from Note data
            notes.append(str(Note.Note(note_vect[i], str(durs[i]))))
            durations.append(str(SongData.get_duration(durs[i], tempo)))

    return (notes, durations)

def train_model(songs_data, tempo):
    """Input: list of data on several songs (could be a single song)
       Ouput: a list of models, one for each bar type. """
    note_models = {}
    (notes, durations) = get_notes_and_durs(songs_data, tempo)

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
 
    # Train the duration model 
    dur_alphabet = ghmm.Alphabet(list(set(durations)))
    dur_alpha_len = len(dur_alphabet)

    dur_trans_prob = 1.0 / (dur_alpha_len)
    trans = [[dur_trans_prob for row in range(dur_alpha_len)] for col in range(dur_alpha_len)]
    
    # Initialize the probabilities of seeing each output from each state.
    # Again, there is probably a better way to do this, but this is simple.
    dur_emiss_prob = 1.0 / (dur_alpha_len)
    emiss = [[dur_emiss_prob for row in range(dur_alpha_len)] for col in range(dur_alpha_len)]
    
    # Some grease to get GHMM to work
    pi = [1.0/dur_alpha_len] * dur_alpha_len 
    
    # The sequence of durs gathered from the music
    dur_train_seq = ghmm.EmissionSequence(dur_alphabet, durations)
    duration_model = ghmm.HMMFromMatrices(dur_alphabet, ghmm.DiscreteDistribution(dur_alphabet), trans, emiss, pi)
 
    return (note_models, duration_model, note_alphabet, dur_alphabet)

