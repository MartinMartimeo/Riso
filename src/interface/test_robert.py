from PyQt4 import QtGui
from ui import *
import sys
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    f = Ui_MainWindow()
    f.show()
    app.setMainWidget(f)
    app.exec_loop()
