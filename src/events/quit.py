# This script comes without any warranty or support.
# Use on own risk and fun.

import logging

from classes.config_manager import ConfigManager
from events import event

class EvenQuit(event.Event):

    def __init__(self, parser):

        from classes.riso import RisoConfigManager
        self.config = RisoConfigManager

        parser.register_user_command(self, self.quit, '/quit')
        
    def quit(self, event, id, riso, parser, command, args):

        command = self.config['quit/release']
        riso.socket.write("%s\n" % command)
        parser.aquire(event, self.close)
        return ""

    def close(self, event, id, riso, parser, line):
        
        if line.strip().startswith(self.config['quit/aquire']):
            riso.close()
        parser.release()
        return line

def __init__(parser):
    return EvenQuit(parser)

