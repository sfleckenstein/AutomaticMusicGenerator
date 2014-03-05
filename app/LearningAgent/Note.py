class Note:
    def __init__(self, pitch, duration):
    	self.pitch = pitch
    	self.duration = duration

    # This is used because GHMM doesn't like learning about objects.
    # Hopefully this can go away eventually.
    def __str__(self):
    	return "{}{}".format(self.pitch, self.duration)

    # GHMM requires this to generate the Alphabet.
    def __len__(self):
    	return 1
