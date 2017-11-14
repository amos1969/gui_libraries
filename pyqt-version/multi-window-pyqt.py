import sys
from PyQt4 import QtGui, QtCore, uic

punchline_ui = uic.loadUiType("punchline.ui")[0]
mainwindow_ui = uic.loadUiType("jokemachine.ui")[0]


class PunchLine(QtGui.QWidget, punchline_ui):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.punch_line_label.setText("You can't wash your hands in a buffalo!")
        self.okay_btn.setText("Okay")
        self.close_btn.setText("Close")

        self.okay_btn.clicked.connect(self.okay_clicked)
        self.close_btn.clicked.connect(self.close_clicked)

    def okay_clicked(self):
        main_window.show()
        punch_line.hide()

    def close_clicked(self):
        QtGui.QApplication.closeAllWindows()

class MainWindow(QtGui.QWidget, mainwindow_ui):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.joke_label.setText("What's the difference between a Buffalo and a Bison?")
        self.punch_line_btn.setText("Punch Line")
        self.punch_line_btn.clicked.connect(self.punch_line_btn_clicked)

    def punch_line_btn_clicked(self):
        main_window.hide()
        punch_line.show()


def main():
    global punch_line
    global main_window
    application = QtGui.QApplication(sys.argv)
    punch_line = PunchLine(None)
    main_window = MainWindow(None)
    main_window.show()
    punch_line.hide()
    application.exec()


if __name__ == '__main__':
    main()
