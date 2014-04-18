import math

class Note:
    def __init__(self, pitch):
    	self.pitch = pitch

    def __str__(self):
    	return "{}".format(self.pitch)

    # GHMM requires this to generate the Alphabet.
    def __len__(self):
    	return 1
