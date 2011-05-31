# This script comes without any warranty or support.
# Use on own risk and fun.

import logging

from events import event

class EventSchau(event.Event):


    def __init__(self, parser):

        from classes.riso import RisoConfigManager
        self.config = RisoConfigManager
        self.commands = {}
        for command in self.config['room/directions']:
            parser.register_user_command(self, self.room, command['direction'])
            self.commands[command['direction']] = command

    def room(self, event, id, riso, parser, command, args):

        logging.debug('room.room: %s' % command)
        self.buffer = []
        self.title = ""
        parser.aquire(event, self.description)
        return "\n".join(self.commands[command]['alias'])

    def description(self, event, id, riso, parser, line):

        line = line.strip(self.config['room/desc/release_strip'])

        if line.startswith(self.config['room/desc/release_ignore']):
            return ""

        if line.startswith(self.config['room/desc/release_parse']):
            self.title = "".join(self.buffer)
            logging.info("Room, title: %s, line: %s" % (self.title, line))
            return ""

        if line.startswith(self.config['room/desc/release_ende']):
            logging.info("Objects: %s" % self.buffer)
            parser.release(id)
            return ""

        self.buffer.append(line)
        return ""


def __init__(parser):
    return EventSchau(parser)