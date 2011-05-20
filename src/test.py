# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 13:33:50$"

import asyncore
import logging

from network.custom_socket import CustomSocket, socket_map

# Testing

logging.basicConfig(level=logging.DEBUG)
CustomSocket('mg.mud.de', 23)
asyncore.loop(map=socket_map)
