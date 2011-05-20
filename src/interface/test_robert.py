from PyQt4 import QtGui
from ui import *

class Gui(QtGui.QMainWindow):
    def __init__(self, parent=None, writeSocketFunc):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.writeSocketFunc = writeSocketFunc
        self.connect(self.ui.lineEdit, QtCore.SIGNAL("returnPressed()"), self.writeToSocket())

    def write(self, text):
            self.ui.textBrowser.append(text)
            self.ui.textBrowser.ensureCursorVisible()
            
    def writeToSocket(self):
        self.writeSocketFunc(self.ui.lineEdit.text())
        self.gui.ui.lineEdit.setText("")

if __name__ == "__main__":
    pass
