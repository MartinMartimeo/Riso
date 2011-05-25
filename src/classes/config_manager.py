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

        self._file = file

        if os.path.exists('configs/%s.yml' % file):
            with open('configs/%s.yml' % file, 'r') as stream:
                self._data = yaml.load(stream)
        else:
            self._data = {}


    def __call__(self, key, default=None):

        value = self.__getitem__(key)
        if value is None:
            return default
        return value

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

    def __getitem__(self, key):
        keys = key.split("/")

        data = self._data
        for key in keys:

            if not key in data.keys():
                return None

            data = data[key]

        return data
    

    """
        Setting a Value Rekrusivly
    """
    def _setattr(self, data, keys, value):

        if len(keys) == 1:
            data[keys[0]] = value
            return data

        key = keys.pop(0)

        if not key in data.keys():
            data[key] = {}
        
        data[key] = self._setattr(data[key], keys, value)
        return data

    def __setattr__(self, key, value):

        if key.startswith("_"):
            return super(ConfigManager, self).__setattr__(key, value)

        keys = key.split("/")
        self._data = self._setattr(self._data, keys, value)

        with open('configs/%s.yml' % self._file, 'w') as stream:
            stream.write(yaml.dump(self._data))

    def __setitem__(self, key, value):

        keys = key.split("/")
        self._data = self._setattr(self._data, keys, value)

        with open('configs/%s.yml' % self._file, 'w') as stream:
            stream.write(yaml.dump(self._data))








    


