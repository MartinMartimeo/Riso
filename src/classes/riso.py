# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 14:30:59$"

import logging
import sys

from network.custom_socket import CustomSocket
from interface.gui import Gui

from PyQt4 import QtGui, QtCore

class Riso(object):

    def __init__(self):

        self.socket = None
        self.gui = Gui(self.do_write)
        


    """
        Main Loop
    """
    def run(self):

        self.do_connect("mg.mud.de", 23)
        self.gui.run()
        self.close(0)
        

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

        if not self.socket:
            logging.error("Trying to sent line without socket: %s" % line)
            return

        self.socket.write("%s\n" % line)
        
    




