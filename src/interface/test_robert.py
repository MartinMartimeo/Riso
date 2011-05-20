<<<<<<< HEAD
=======
from PyQt4 import QtGui
from ui import *
>>>>>>> e4c85fab9e17eaa0c573e9df97cd4899bc96f7b8
import sys
from PyQt4 import QtCore, QtGui
from ui import *

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
<<<<<<< HEAD
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
=======
    f = Ui_MainWindow()
    f.show()
    app.setMainWidget(f)
    app.exec_loop()
>>>>>>> e4c85fab9e17eaa0c573e9df97cd4899bc96f7b8
