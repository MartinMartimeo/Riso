# This script comes without any warranty or support.
# Use on own risk and fun.

import asynchat
import logging
import socket

from asynchat import async_chat

sockets = {}
socket_map = {}

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

        # Run
        self.connect((host, port))

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