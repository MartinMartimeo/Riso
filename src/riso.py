# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 09:52:48$"

import logging
import sys

from classes.riso import Riso

if __name__ == "__main__":

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s %(threadName)-10s %(levelname)-8s %(message)s')

    riso = Riso()
    riso.run()