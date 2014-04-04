class Bar:
    """ Bars are classified by their first note. """
    def __init__(self, first_note):
        self.first_note = first_note

    def __str__(self):
        return '{}'.format(self.first_note)

    def __len__(self):
        return 1
