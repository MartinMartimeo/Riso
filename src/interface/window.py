# This script comes without any warranty or support.
# Use on own risk and fun.

# This script comes without any warranty or support.
# Use on own risk and fun.

from PyQt4 import QtGui
from PyQt4 import QtCore

from classes.config_manager import ConfigManager

"""
    Simple QT Window
"""

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.init_ui()
        self.init_menu()


    def init_ui(self):

        self.labels = []

        # Title
        self.project_config = ConfigManager('project')
        self.setWindowTitle(self.project_config.name)

        # Resize
        self.height = 750
        self.width = 450
        self.setGeometry(250, 200, self.height, self.width)

        # Center
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def init_menu(self):

        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)