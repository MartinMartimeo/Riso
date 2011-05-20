import gtk.gdk
from gtk import *

class Gui:
    def __init__(self, writeFunc):
        self.writeFunc = writeFunc
        self.main = Window(gtk.WINDOW_TOPLEVEL)
        self.main.connect("destroy", lambda w: gtk.main_quit())
        self.layout = gtk.VBox()
        self.output = gtk.TextView()
        self.buffer = gtk.TextBuffer()
        self.output.set_buffer(self.buffer)
        self.outputbox = gtk.ScrolledWindow()
        self.outputbox.add(self.output)
        self.input = gtk.Entry()
        self.input.connect("activate", self.writeSocket)
        self.layout.pack_start(self.outputbox)
        self.layout.pack_start(self.input)
        self.main.add(self.layout)
        self.main.show_all()

    def run(self):
        gtk.gdk.threads_init()
        gtk.main()
        
    def write(self, text):
        self.buffer.insert_at_cursor(str(text))
        adj = self.outputbox.get_vadjustment()
        adj.set_value(adj.get_upper())
        
    def writeSocket(self, data):
        text = self.input.get_text()
        self.writeFunc(text)
        self.input.set_text("")
        
    
    
    
        
        