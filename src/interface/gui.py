import gtk.gdk
from gtk import *

class Gui:
    def __init__(self, writeFunc):
        self.writeFunc = writeFunc
        self.main = Window()
        self.layout = gtk.VBox()
        self.output = gtk.TextView()
        self.buffer = gtk.TextBuffer()
        self.output.set_buffer(self.buffer)
        self.input = gtk.Entry()
        self.input.connect("activate", self.writeSocket)
        self.layout.pack_start(self.output)
        self.layout.pack_start(self.input)
        self.main.add(self.layout)
        self.main.show_all()
        gtk.gdk.threads_init()
        gtk.main()
        
    def write(self, text):
        self.buffer.insert_at_cursor(text)
        
    def writeSocket(self, data):
        text = self.input.get_text()
        self.writeFunc(text)
        self.input.set_text("")
        
    
    
    
        
        