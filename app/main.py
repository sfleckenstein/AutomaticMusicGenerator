import sys
from PyQt4 import QtGui, QtCore
import Creator

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        genre = QtGui.QLabel('Genre: ')
        tempo = QtGui.QLabel('Tempo: ')
        key   = QtGui.QLabel('Key Signature: ')
        time  = QtGui.QLabel('Time Signature: ')

        genre_edit = QtGui.QComboBox()
        tempo_edit = QtGui.QComboBox()
        key_edit   = QtGui.QComboBox()
        time_edit  = QtGui.QComboBox()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(genre, 1, 0)
        grid.addWidget(genre_edit, 1, 1)
        
        grid.addWidget(tempo, 2, 0)
        grid.addWidget(tempo_edit, 2, 1)

        grid.addWidget(key, 3, 0)
        grid.addWidget(key_edit, 3, 1)

        grid.addWidget(time, 4, 0)
        grid.addWidget(time_edit, 4, 1)
        
        compose_btn = QtGui.QPushButton('Compose', self)
        compose_btn.resize(compose_btn.sizeHint())
        # links the creation to the clicking of the button
        compose_btn.clicked.connect(self.create)

        grid.addWidget(compose_btn, 5, 1)
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
