# This script comes without any warranty or support.
# Use on own risk and fun.

import asynchat
import asyncore
import logging
import socket

from asynchat import async_chat
from threading import Timer

sockets = {}
socket_map = {}
socket_thread = None

def connect_socket(id):
    global sockets, socket_thread, socket_map
    
    sockets[id].connect((sockets[id].host, sockets[id].port))

    if not socket_thread:
        asyncore.loop(map=socket_map)


class CustomSocket(async_chat):

    def __init__(self, host, port, lhost='0.0.0.0'):

        # Settings
        self.set_terminator('\n')
        self.buffer = ""

        # Initalisation
        global socket_map
        asynchat.async_chat.__init__(self, map=socket_map)

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

        self.t = Timer(0.1, connect_socket, args=[self.id])
        self.t.name="Socket-%u" % self.id
        self.t.start()

    """
        Alias for push
    """
    def write(self, msg):

        logging.debug('>>>%s:%u %s' % (self.host, self.port, msg))
        asynchat.async_chat.push(self, "%s\n" % msg)

    def collect_incoming_data(self, data):
        self.buffer += data

    def found_terminator(self):
        self.handle_line(self.buffer)
        logging.debug('<<<%s:%u %s' % (self.host, self.port, self.buffer))
        self.buffer = ""

    def handle_connect(self):
        # Logging
        logging.info('Established Connection#%u from %s:%u' % (self.id, self.host, self.port))

    def handle_line(self, line):
        pass

    def handle_close(self):
        # Unregistration
        global sockets
        sockets[self.id] = None
        # Cleaning up
        self.close()
        # Logging
        logging.info('Closing Connection#%u to %s:%u' % (self.id, self.host, self.port))