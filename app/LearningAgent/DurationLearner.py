import threading
from SongData import SongData
from Trainer import Trainer

class DurationLearner(threading.Thread):
    def __init__(self, thread_id, name, counter, songs_data, tempo, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
        self.songs_data = songs_data
        self.tempo = tempo
        self.queue = queue

    def run(self):
        print "Starting " + self.name
        self.queue.put(train_model(self.songs_data, self.tempo))
        print "Exiting " + self.name

def get_durations(songs_data, tempo):
    durations = []
    
    for song_data in songs_data:
        durs = song_data.seg_durations

        for i in xrange(len(durs)):
            durations.append(str(SongData.get_duration(durs[i], tempo)))

    return durations

def train_model(songs_data, tempo):
    durations = get_durations(songs_data, tempo)
    dur_trainer = Trainer(durations)
    dur_model, dur_alphabet = dur_trainer.train()
    return (dur_model, dur_alphabet)
