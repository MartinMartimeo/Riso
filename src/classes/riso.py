import logging
from PyQt4.uic.Compiler.qtproxies import QtCore

# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 14:30:59$"

from network.custom_socket import CustomSocket
from interface.test_robert import Gui
import sys
from PyQt4 import QtGui, QtCore

class Riso(object):

    def __init__(self):

        self.socket = None
        self.app = QtGui.QApplication(sys.argv)
        self.gui = Gui()
        self.gui.show()
        self.gui.connect(self.gui.ui.lineEdit, QtCore.SIGNAL("returnPressed()"), self.callback)
    
    def callback(self):
        self.do_write(self.gui.ui.lineEdit.text())
        self.gui.ui.lineEdit.setText("")


    """
        Main Loop
    """
    def run(self):

        self.do_connect("mg.mud.de", 23)
        rtn = self.app.exec_()
        self.close(rtn)
        

    """
        Cleanup
    """
    def close(self, rtn=0):
        logging.info("riso.close()")
        if self.socket:
            self.socket.handle_close()
            self.socket.t.cancel()
            logging.info("socket.close()")
        sys.exit(rtn)


    """
        Connect to a new Server
    """
    def do_connect(self, host, port):

        if self.socket:
            self.socket.close()

        self.socket = CustomSocket(host, port)
        self.socket.riso = self
        self.socket.handle_line = self.on_line
        self.socket.threaded_connect()

    """
        New Line
    """
    def on_line(self, line):
        self.gui.write(line)

    """
        Write
    """
    def do_write(self, line):

        assert(self.socket)

        self.socket.write("%s\n" % line)
        
    




