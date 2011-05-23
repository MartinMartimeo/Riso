import logging
# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$20.05.2011 15:20:45$"

import events
from events import *

class Parser(object):

    def __init__(self, riso):
        super(Parser, self).__init__()

        self._user_commands = {}
        self._aquires = {}

        self._riso = riso

        self._events = {}
        for module in dir(events):
            if module.startswith("_"):
                continue
            logging.info("Registering Module %s as Event for Parser" % module)
            self._events[module] = getattr(events, module).__init__(self)



    """
        Line of Mud
    """
    def mud_line(self, data):

        lines = []
        for line in data.splitlines():
            for dict in self._aquires.values():
                if not dict:
                    continue
                line = dict['function'](event=dict['event'], id=dict['id'], riso=self._riso, parser=self, line=line)
            lines.append(line)
        return lines


    """
        Userline
    """
    def user_line(self, line):

        args = line.split()

        if not args:
            return line

        for (command, list) in self._user_commands.items():
            if args[0] == command:
                for dict in list.values():
                    line = dict['function'](event=dict['event'], id=dict['id'], riso=self._riso, parser=self, command=command, args=args)

        return line



    """
        Register an Command
    """
    def register_user_command(self, event, function, command):

        logging.info("Registering Event as User Command on Command %s" % command)

        if not command in self._user_commands.keys():
            self._user_commands[command] = {}
        list = self._user_commands[command]

        self._user_commands[command]["%u" % len(list.keys())] = {'id': len(list.keys()), 'function': function, 'event': event}

    """
        Aquire that all lines following will be sent to event.function
    """
    def aquire(self, event, function):

        logging.info("Aquire!")
        self._aquires["%u" % len(self._aquires.keys())] = {'id': len(self._aquires.keys()), 'function': function, 'event': event}

    """
        Release an aquirement
    """
    def release(self, id):

        logging.info("Release!")
        self._aquires["%u" % id] = None
    


