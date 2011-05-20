
# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 14:30:59$"

from network.custom_socket import CustomSocket
from interface.test_robert import Gui
import sys
from PyQt4 import QtGui

class Riso(object):

    def __init__(self):

        self.socket = None
        self.app = QtGui.QApplication(sys.argv)
        self.gui = Gui()
        self.gui.show()
        sys.exit(self.app.exec_())
        


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
        
    




