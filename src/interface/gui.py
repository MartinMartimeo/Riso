import gtk.gdk
import logging
from gtk import *

__author__  = "Robert Heumueller <robert@heum.de"
__date__    = "$25.05.2011 12:00:00$"


class Gui:
    def __init__(self, writeFunc):
        from classes.riso import RisoConfigManager
        self.config = RisoConfigManager
        self.destroyed = False
        
        self.writeFunc = writeFunc
        self.builder = gtk.Builder()
        self.builder.add_from_file("interface/ui.glade")
        self.builder.connect_signals(self)
        self.mainwindow = self.builder.get_object("window1")
        self.outputbox = self.builder.get_object("outputbox")
        self.output = self.builder.get_object("output")
        self.output.set_editable(False)
        self.color = self.builder.get_object("colorselection")
        self.input = self.builder.get_object("input")
        self.buffer = self.output.get_buffer()
        self.output.set_buffer(self.buffer)
        if self.config["gui/color"] is None:
            self.config["gui/color/bg"] = gtk.gdk.color_parse("black").to_string()
            self.config["gui/color/text"] = gtk.gdk.color_parse("grey").to_string()
        self.output.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse(self.config["gui/color/text"]))
        self.output.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse(self.config["gui/color/bg"]))
        self.end_text = self.buffer.create_mark("end", self.buffer.get_end_iter(), False)
        self.mainwindow.show_all()
        self.inputcache_stack1 = []
        self.inputcache_stack2 = []
        

    def run(self):
        gtk.gdk.threads_init()
        gtk.main()
        
    def on_window1_destroy(self, data ):
        self.destroyed = True
        logging.info("Shutting down GTK")
        gtk.main_quit()
        
    def write(self, text):
        self.buffer.place_cursor(self.buffer.get_end_iter())
        self.buffer.insert_at_cursor(str(text))
        self.output.scroll_to_mark(self.end_text, 0.05, True, 0.0, 1.0)
        
    def on_input_return(self, data):
        text = self.input.get_text()
        self.writeFunc(text)
        self.input.set_text("")
        self.inputcache_stack1.append(text)
        
    def up_key_pressed(self, widget, data2):
        self.input.grab_focus()
        if gtk.gdk.keyval_name(data2.keyval) == "Up":
            logging.debug("Go")
        
        
    def color_changed(self, data):
        color = self.color.get_current_color()
        if self.builder.get_object("texttoggle").get_active():
            self.output.modify_text(gtk.STATE_NORMAL, color)
            self.config["gui/color/text"] = color.to_string()
        else:
            self.output.modify_base(gtk.STATE_NORMAL, color)
            self.config["gui/color/bg"] = color.to_string()
            
    def on_bgtoggle_toggle(self, data):
        if self.builder.get_object("texttoggle").get_active():
            self.color.set_current_color(gtk.gdk.color_parse(self.config["gui/color/text"]))
        else:
            self.color.set_current_color(gtk.gdk.color_parse(self.config["gui/color/bg"]))
        
    
    
    
        
        