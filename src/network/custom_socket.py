# -*- coding: utf-8 -*-
# This script comes without any warranty or support.
# Use on own risk and fun.

import asyncore
import logging
import socket

from threading import Timer

sockets = {}
socket_map = {}
socket_thread = None

def connect_socket(id):
    global sockets, socket_thread, socket_map
    
    sockets[id].connect((sockets[id].host, sockets[id].port))

    if not socket_thread:
        socket_thread = sockets[id].t
        asyncore.loop(map=socket_map)
    else:
        sockets[id].t = socket_thread


class CustomSocket(asyncore.dispatcher):

    def __init__(self, host, port, lhost='0.0.0.0'):

        # Settings
        self.write_buffer = ""

        # Initalisation
        global socket_map
        asyncore.dispatcher.__init__(self, map=socket_map)

        # Registration
        global sockets
        self.id = len(sockets)
        sockets[self.id] = self

        # Connection
        self.host = host
        self.port = port
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lhost = lhost
        self.lport = 0
        self.bind((self.lhost, 0))

        # Logging
        logging.info('Connection#%u from %s:%u' % (self.id, self.lhost, self.lport))
        logging.info('Connection#%u to %s:%u' % (self.id, self.host, self.port))

    """
        Starts a Timer that will connect the socket after a delay of 0.1
        in an own Thread
    """
    def threaded_connect(self):

        self.t = Timer(0.5, connect_socket, args=[self.id])
        self.t.name="Socket-%u" % self.id
        self.t.start()

    """
        Füge Daten zum Buffer hinzu
    """
    def write(self, msg):

        logging.debug('>>>%s:%u %s' % (self.host, self.port, msg))
        self.write_buffer += "%s\n" % msg

    """
        Teile Loop mit, dass wir schreiben wollen
    """
    def writeable(self):
        return len(self.write_buffer)

    """
        Schreibprozess
    """
    def handle_write(self):
        sent = self.send(self.write_buffer)
        self.write_buffer = self.write_buffer[sent:]


    """
        Leseprozess
    """
    def handle_read(self):
        buffer = unicode("%s" % self.recv(8192), errors='replace')
        # buffer = buffer.strip()
        if buffer:
            self.handle_line(buffer)
            logging.debug('<<<%s:%u %s' % (self.host, self.port, buffer))
        buffer = ""

    def handle_connect(self):
        # Logging
        logging.info('Established Connection#%u from %s:%u' % (self.id, self.host, self.port))

    def handle_line(self, line):
        pass

    #def handle_error(self):
    #    logging.error('Socket Error on %u' % self.id)
    #    self.close()
        
    def handle_close(self):
        # Unregistration
        global sockets
        sockets[self.id] = None
        # Cleaning up
        self.close()
        # Logging
        logging.info('Closing Connection#%u to %s:%u' % (self.id, self.host, self.port))