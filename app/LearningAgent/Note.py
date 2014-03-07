class Note:
    def __init__(self, pitch, duration):
    	self.pitch = pitch
    	self.duration = duration

    # This is used because GHMM doesn't like learning about objects.
    # Hopefully this can go away eventually.
    def __str__(self):
    	return "{}*{}".format(self.pitch, self.duration)

    # GHMM requires this to generate the Alphabet.
    def __len__(self):
    	return 1

    # @ stands for flat
    #TODO pretty sure static method is not the Python way to do this,
    # but I can't figure out the right way currently
    @staticmethod
    def getPitch(note):
        return {
            'a_0' : 21,
            'a#_0': 22,
            'b@_0': 22,
            'b_0' : 23,
            'c_1' : 24,
            'c#_1': 25,
            'd_1' : 26,
        # This assumes that each of the note durations
        # are given as a string of three characters
         }[note[:-2]]

