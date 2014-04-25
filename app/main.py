import sys
from PyQt4 import QtGui, QtCore
import Creator
from LearningAgent import DataCollector
from ExtendedComboBox import ExtendedComboBox

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        genre_label = QtGui.QLabel('Genre: ')
        max_tempo_label = QtGui.QLabel('Max Tempo: ')
        min_tempo_label = QtGui.QLabel('Min Tempo: ')
        key_label   = QtGui.QLabel('Key Signature: ')
        time_sig_label  = QtGui.QLabel('Time Signature: ')

        genre_edit = ExtendedComboBox()
        for genre in DataCollector.get_genres():
            genre_edit.addItem(genre)
        
        tempos = list(xrange(1,499))
        max_tempo_edit = ExtendedComboBox()
        min_tempo_edit = ExtendedComboBox()
        for tempo in tempos:
            max_tempo_edit.addItem(str(tempo))
            min_tempo_edit.addItem(str(tempo))

        keys = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#','G','Ab','A','Bb','B']
        key_edit   = ExtendedComboBox()
        for key in keys:
            key_edit.addItem(key)

        time_sig_edit  = ExtendedComboBox()
        time_sigs = ['3/4','4/4','5/4','6/4','7/4']
        for time_sig in time_sigs:
            time_sig_edit.addItem(time_sig)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(genre_label, 1, 0)
        grid.addWidget(genre_edit, 1, 1)
        
        grid.addWidget(max_tempo_label, 2, 0)
        grid.addWidget(max_tempo_edit, 2, 1)

        grid.addWidget(min_tempo_label, 3, 0)
        grid.addWidget(min_tempo_edit, 3, 1)

        grid.addWidget(key_label, 4, 0)
        grid.addWidget(key_edit, 4, 1)

        grid.addWidget(time_sig_label, 5, 0)
        grid.addWidget(time_sig_edit, 5, 1)
        
        compose_btn = QtGui.QPushButton('Compose', self)
        compose_btn.resize(compose_btn.sizeHint())
        # links the creation to the clicking of the button
        compose_btn.clicked.connect(self.create)

        grid.addWidget(compose_btn, 6, 1)
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
        Creator.create(style='folk', max_tempo=180, min_tempo=100)

def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
