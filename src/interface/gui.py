import gtk.gdk
import logging
from gtk import *

class Gui:
    def __init__(self, writeFunc):
        self.writeFunc = writeFunc
        self.builder = gtk.Builder()
        self.builder.add_from_file("interface/ui.glade")
        self.builder.connect_signals(self)
        self.mainwindow = self.builder.get_object("window1")
        self.outputbox = self.builder.get_object("outputbox")
        self.output = self.builder.get_object("output")
        self.input = self.builder.get_object("input")
        self.buffer = gtk.TextBuffer()
        self.output.set_buffer(self.buffer)
        self.mainwindow.show_all()
        

    def run(self):
        gtk.gdk.threads_init()
        gtk.main()
        
    def on_window1_destroy(self, data ):
        logging.info("Shutting down GTK")
        gtk.main_quit()
        
    def write(self, text):
        self.buffer.insert_at_cursor(str(text))
        adj = self.outputbox.get_vadjustment()
        adj.set_value(adj.get_upper())
        
    def on_input_return(self, data):
        text = self.input.get_text()
        self.writeFunc(text)
        self.input.set_text("")
        
    
    
    
        
        