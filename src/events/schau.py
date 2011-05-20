# This script comes without any warranty or support.
# Use on own risk and fun.

from events import event

class EventSchau(event.Event):


    def __init__(self, parser):

        parser.register_user_command(self, self.room, 'schau')

        parser.register_user_command(self, self.room, 'n')
        parser.register_user_command(self, self.room, 's')
        parser.register_user_command(self, self.room, 'o')
        parser.register_user_command(self, self.room, 'w')

    def room(self, event, id, riso, parser, line):

        parser.aquire(event, self.description)
        return line

    def description(self, event, id, riso, parser, line):

        parser.release(id)
        return line


def __init__(parser):
    return EventSchau(parser)