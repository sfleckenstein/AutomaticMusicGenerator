from PyQt4 import QtCore

class ComposeThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self):

    def __del__(self):
        self.wait()

    def run(self):
        Creator.create(style=style, max_tempo=max_tempo, min_tempo=min_tempo, key=key, time_sig=time_sig)
        self.terminate()
