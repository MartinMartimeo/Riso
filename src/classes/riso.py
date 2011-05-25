# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 14:30:59$"

import logging
import socket
import sys

from classes.config_manager import ConfigManager
from classes.database import Database
from classes.parser import Parser
from gtk import gdk
from interface.gui import Gui
from network.custom_socket import CustomSocket

RisoConfigManager = None

class Riso(object):

    def __init__(self):

        # Our Socket
        self.socket = None

        # Initalisate ConfigManager
        global RisoConfigManager
        self.config = ConfigManager('project')
        RisoConfigManager = self.config

        # Connect to Database, adds self.data for queriyng
        self.database = Database(riso=self)

        # Gui
        self.gui = Gui(self.do_write)

        # Parser
        self.parser = Parser(riso=self)

    """
        Main Loop
    """
    def run(self):

        if self.config['connect/autoconnect']:
            self.do_connect(self.config['connect/server'], self.config['connect/port'])
        self.gui.run()
        self.close(0)
        

    """
        Cleanup
    """
    def close(self, rtn=0):
        if self.socket:
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
                self.socket.handle_close()
                self.socket.t.cancel()
            except socket.error:
                pass
            self.socket = None
        if not self.gui.destroyed:
            gdk.threads_enter()
            self.gui.on_window1_destroy(self)
            gdk.threads_leave()
        sys.exit("Shuting Down")


    """
        Connect to a new Server
    """
    def do_connect(self, host, port):

        if self.socket:
            self.socket.close()

        lhost = None
        if self.config['connect/bind']:
            lhost = self.config['connect/bind']

        self.socket = CustomSocket(host=host, port=port, lhost=lhost, ignore_unknown_chars=self.config['socket/ignore_unknown_chars'])
        self.socket.riso = self
        self.socket.handle_line = self.on_line
        self.socket.threaded_connect()

    """
        New Line
    """
    def on_line(self, line):

        lines = self.parser.mud_line(line)
        if lines:
            #gobject.idle_add(self.gui.write, line)
            gdk.threads_enter()
            for line in lines:
                if line:
                    self.gui.write("%s\n" % line)
            gdk.threads_leave()

    """
        Write
    """
    def do_write(self, line):

        if not self.socket:
            logging.error("Trying to sent line without socket: %s" % line)
            return

        self.gui.write(line)
        line = "%s\n" % self.parser.user_line(line)        
        if line:
            self.socket.write("%s" % line)
        
    




