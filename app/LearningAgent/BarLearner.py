import math, threading, time
import ghmm
import Bar
from SongData import SongData
from Trainer import Trainer

class BarLearner(threading.Thread):
    def __init__(self, thread_id, name, counter, songs_data,queue):
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
    return (m, alphabet)

