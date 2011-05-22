# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 13:33:50$"

import logging
import sys

from classes.config_manager import ConfigManager

# Testing
c = ConfigManager("test")

i = c["tested"]
if not i:
    i = 0
i += 1
c["tested"] = i



d = ConfigManager("project")

print d["name"]

c["test/name"] = d["name"]
