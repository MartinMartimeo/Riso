from PyQt4 import QtGui
from ui import *

class Gui(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def write(self, text):
            self.ui.textBrowser.append(text)
            
    
    
            

if __name__ == "__main__":
    
