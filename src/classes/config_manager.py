# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 11:19:38$"

import logging
import os
import yaml

"""
    Recieve Configs from a config file
"""

class ConfigManager(object):

    def __init__(self, file):

        if os.path.exists('configs/%s.yml' % file):
            with open('configs/%s.yml' % file, 'r') as stream:
                self._data = yaml.load(stream)
        else:
            self._data = {}

    def __getattribute__(self, key):

        if key.startswith("_"):
            return super(ConfigManager, self).__getattribute__(key)

        keys = key.split("/")

        data = self._data
        for key in keys:

            if not key in data.keys():
                return None

            data = data[key]

        return data

    


