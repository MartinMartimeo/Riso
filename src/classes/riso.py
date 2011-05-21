import socket
# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 14:30:59$"

import gobject
import logging
import sys

from network.custom_socket import CustomSocket
from classes.parser import Parser
from interface.gui import Gui
from gtk import gdk


class Riso(object):

    def __init__(self):

        self.socket = None
        self.gui = Gui(self.do_write)
        self.parser = Parser(riso=self)


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
        if self.socket:
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.handle_close()
            self.socket.t.cancel()
        sys.exit("Shuting Down")


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

        line = self.parser.mud_line(line)
        if line:
            #gobject.idle_add(self.gui.write, line)
            gdk.threads_enter()
            self.gui.write(line)
            gdk.threads_leave()

    """
        Write
    """
    def do_write(self, line):

        if not self.socket:
            logging.error("Trying to sent line without socket: %s" % line)
            return

        line = self.parser.user_line(line)
        if line:
            self.socket.write("%s\n" % line)
        
    




