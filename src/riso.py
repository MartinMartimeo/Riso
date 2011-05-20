# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 09:52:48$"

import sys

from PyQt4 import QtGui

from interface.window import Window

if __name__ == "__main__":

    app = QtGui.QApplication([])
    exm = Window()
    exm.show()
    sys.exit(app.exec_())
