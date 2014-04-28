import sys
from PyQt4 import QtGui, QtCore
import pygame

from Creator import CreatorThread
from LearningAgent import DataCollector
from ExtendedComboBox import ExtendedComboBox

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()
        self.paused = True

    def init_ui(self):
        genre_label = QtGui.QLabel('Genre: ')
        max_tempo_label = QtGui.QLabel('Max Tempo: ')
        min_tempo_label = QtGui.QLabel('Min Tempo: ')
        key_label   = QtGui.QLabel('Key Signature: ')

        # Create the genre combo box and fill it with genres
        self.genre_edit = ExtendedComboBox()
        for genre in DataCollector.get_genres():
            self.genre_edit.addItem(genre)
        
        # Create the tempo combo boxes and fill it with tempos
        tempos = list(xrange(1,499))
        self.max_tempo_edit = ExtendedComboBox()
        self.min_tempo_edit = ExtendedComboBox()
        for tempo in tempos:
            self.max_tempo_edit.addItem(str(tempo))
            self.min_tempo_edit.addItem(str(tempo))

        # Create the key combo box and fill it with keys
        keys = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#','G','Ab','A','Bb','B']
        self.key_edit   = QtGui.QComboBox()
        for key in keys:
            self.key_edit.addItem(key)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(genre_label, 1, 0)
        grid.addWidget(self.genre_edit, 1, 1)
        
        grid.addWidget(max_tempo_label, 2, 0)
        grid.addWidget(self.max_tempo_edit, 2, 1)

        grid.addWidget(min_tempo_label, 3, 0)
        grid.addWidget(self.min_tempo_edit, 3, 1)

        grid.addWidget(key_label, 4, 0)
        grid.addWidget(self.key_edit, 4, 1)

        # Add a compose button
        compose_btn = QtGui.QPushButton('Compose', self)
        compose_btn.resize(compose_btn.sizeHint())
        # links the creation to the clicking of compose
        compose_btn.clicked.connect(self.create)
        grid.addWidget(compose_btn, 5, 1)
        
        # Add a play button
        play_btn = QtGui.QPushButton('Play', self)
        play_btn.resize(play_btn.sizeHint())
        # links the creation to the clicking of play
        play_btn.clicked.connect(self.play)
        grid.addWidget(play_btn, 6, 1)
        
        # Add a pause button
        pause_btn = QtGui.QPushButton('Pause', self)
        pause_btn.resize(pause_btn.sizeHint())
        # links the creation to the clicking of pause
        pause_btn.clicked.connect(self.pause)
        grid.addWidget(pause_btn, 8, 1)
        
        # pygame intialization
        freq = 44100
        bitsize = -16
        channels = 2
        _buffer = 1024
        pygame.mixer.init(freq, bitsize, channels, _buffer)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.center()
        self.setWindowTitle('Automatic Music Generator')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create(self):
        style = str(self.genre_edit.currentText())
        max_tempo = str(self.max_tempo_edit.currentText())
        min_tempo = str(self.min_tempo_edit.currentText())
        key = self.key_edit.currentIndex()
        
        # Create a worked thread to learn and compose in the background
        self.thread = QtCore.QThread()
        self.worker = CreatorThread(style, max_tempo, min_tempo, key)
        self.worker.moveToThread(self.thread)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL('started()'), self.worker.process)
        QtCore.QObject.connect(self.worker, QtCore.SIGNAL('finished()'), self.thread.quit)
        QtCore.QObject.connect(self.worker, QtCore.SIGNAL('finished()'), self.worker.deleteLater)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL('finished()'), self.thread.deleteLater)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL('finished()'), self.load_file)
        self.thread.start()

    def load_file(self):
        try:
            pygame.mixer.music.load("output.mid")
            print "Output file loaded!"
        except pygame.error:
            print "File output.mid not found!"
            return

    def play(self):
        pygame.mixer.music.play()
        self.paused = not self.paused

    def pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = not self.paused
        else:
            pygame.mixer.music.pause()
            self.paused = not self.paused

def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
