# This script comes without any warranty or support.
# Use on own risk and fun.

from events import event

class EventLs(event.Event):

    def __init__(self, parser):

        from classes.riso import RisoConfigManager
        self.config = RisoConfigManager

        parser.register_user_command(self, self.ls, 'ls')

    def ls(self, event, id, riso, parser, command, args):

        command = self.config['ls/command']
        if not command:
            command = "schau"
        return command

def __init__(parser):
    return EventLs(parser)


