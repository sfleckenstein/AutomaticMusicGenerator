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
    def get_pitch(note):
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

            'c_5' : 72,
            'c#_5': 73,
            'd@_5': 73,
            'd_5' : 74,
            'd#_5': 75,
            'e@_5': 75,
            'e_5' : 76,
            'f_5' : 77,
            'f#_5': 78,
            'g@_5': 78,
            'g_5' : 79,
            'g#_5': 80,
            'a@_5': 80,
            'a_5' : 81,
            'a#_5': 82,
            'b@_5': 82,
            'b_5' : 83,

            'c_6' : 84,
            'c#_6': 85,
            'd@_6': 85,
            'd_6' : 86,
            'd#_6': 87,
            'e@_6': 87,
            'e_6' : 88,
            'f_6' : 89,
            'f#_6': 90,
            'g@_6': 90,
            'g_6' : 91,
            'g#_6': 92,
            'a@_6': 92,
            'a_6' : 93,
            'a#_6': 94,
            'b@_6': 94,
            'b_6' : 95,

            'c_7' : 96,
            'c#_7': 97,
            'd@_7': 97,
            'd_7' : 98,
            'd#_7': 99,
            'e@_7': 99,
            'e_7' : 100,
            'f_7' : 101,
            'f#_7': 102,
            'g@_7': 102,
            'g_7' : 103,
            'g#_7': 104,
            'a@_7': 104,
            'a_7' : 105,
            'a#_7': 106,
            'b@_7': 106,
            'b_7' : 107,

            'c_8' : 108,
        }.get(note[:-3])
    
    @staticmethod
    def get_duration(note):
        return note[-3:]

