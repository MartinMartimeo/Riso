import socket
# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 13:33:50$"

import logging
import sys

from network.custom_socket import CustomSocket

# Testing

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(threadName)-10s %(levelname)-8s %(message)s')
socket = CustomSocket('mg.mud.de', 23)
socket.threaded_connect()
