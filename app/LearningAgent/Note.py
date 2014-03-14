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
            'd@_1': 25,
            'd_1' : 26,
            'd#_1': 27,
            'e@_1': 27,
            'e_1' : 28,
            'f_1' : 29,
            'f#_1': 30,
            'g@_1': 30,
            'g_1' : 31,
            'g#_1': 32,
            'a@_1': 32,
            'a_1' : 33,
            'a#_1': 34,
            'b@_1': 34,
            'b_1' : 35,

            'c_2' : 36,
            'c#_2': 37,
            'd@_2': 37,
            'd_2' : 38,
            'd#_2': 39,
            'e@_2': 39,
            'e_2' : 40,
            'f_2' : 41,
            'f#_2': 42,
            'g@_2': 42,
            'g_2' : 43,
            'g#_2': 44,
            'a@_2': 44,
            'a_2' : 45,
            'a#_2': 46,
            'b@_2': 46,
            'b_2' : 47,

            'c_3' : 48,
            'c#_3': 49,
            'd@_3': 49,
            'd_3' : 50,
            'd#_3': 51,
            'e@_3': 51,
            'e_3' : 52,
            'f_3' : 53,
            'f#_3': 54,
            'g@_3': 54,
            'g_3' : 55,
            'g#_3': 56,
            'a@_3': 56,
            'a_3' : 57,
            'a#_3': 58,
            'b@_3': 58,
            'b_3' : 59,
            
            'c_4' : 60,
            'c#_4': 61,
            'd@_4': 61,
            'd_4' : 62,
            'd#_4': 63,
            'e@_4': 63,
            'e_4' : 64,
            'f_4' : 65,
            'f#_4': 66,
            'g@_4': 66,
            'g_4' : 67,
            'g#_4': 68,
            'a@_4': 68,
            'a_4' : 69,
            'a#_4': 70,
            'b@_4': 70,
            'b_4' : 71,

            'c_5' : 73,
            'c#_5': 74,
            'd@_5': 74,
            'd_5' : 75,
            'd#_5': 76,
            'e@_5': 76,
            'e_5' : 77,
            'f_5' : 78,
            'f#_5': 79,
            'g@_5': 79,
            'g_5' : 80,
            'g#_5': 81,
            'a@_5': 81,
            'a_5' : 82,
            'a#_5': 83,
            'b@_5': 83,
            'b_5' : 84,

            'c_6' : 85,
            'c#_6': 86,
            'd@_6': 86,
            'd_6' : 87,
            'd#_6': 88,
            'e@_6': 88,
            'e_6' : 89,
            'f_6' : 90,
            'f#_6': 91,
            'g@_6': 91,
            'g_6' : 92,
            'g#_6': 93,
            'a@_6': 93,
            'a_6' : 94,
            'a#_6': 95,
            'b@_6': 95,
            'b_6' : 96,
   
            'c_7' : 97,
            'c#_7': 98,
            'd@_7': 98,
            'd_7' : 99,
            'd#_7': 100,
            'e@_7': 100,
            'e_7' : 101,
            'f_7' : 102,
            'f#_7': 103,
            'g@_7': 103,
            'g_7' : 104,
            'g#_7': 105,
            'a@_7': 105,
            'a_7' : 106,
            'a#_7': 107,
            'b@_7': 107,
            'b_7' : 108,
        # This assumes that each of the note durations
        # are given as a string of three characters
         }[note[:-3]]
    
    @staticmethod
    def getDuration(note):
        return note[-3:]
