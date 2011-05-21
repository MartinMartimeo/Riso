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
        self.color = self.builder.get_object("colorselection")
        self.input = self.builder.get_object("input")
        self.buffer = self.output.get_buffer()
        self.output.set_buffer(self.buffer)
        self.output.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("gray"))
        self.output.modify_base(gtk.STATE_NORMAL, gtk.gdk.Color(0,0,0))
        self.end_text = self.buffer.create_mark("end", self.buffer.get_end_iter(), False)
        
        self.mainwindow.show_all()
        

    def run(self):
        gtk.gdk.threads_init()
        gtk.main()
        
    def on_window1_destroy(self, data ):
        logging.info("Shutting down GTK")
        gtk.main_quit()
        
    def write(self, text):
        self.buffer.insert_at_cursor(str(text))
        self.output.scroll_to_mark(self.end_text, 0.05, True, 0.0, 1.0)
        
    def on_input_return(self, data):
        text = self.input.get_text()
        self.writeFunc(text)
        self.input.set_text("")
        
    def color_changed(self, data):
        color = self.color.get_current_color()
        if self.builder.get_object("texttoggle").get_active():
            self.output.modify_text(gtk.STATE_NORMAL, color)
        else:
            self.output.modify_base(gtk.STATE_NORMAL, color)
        
    
    
    
        
        