#!/usr/bin/python

from gi.repository import Gtk
import json

class Signals:
    def setBuilder(self, builder):
        self.builder = builder
    def onDeleteWindow(self, *args):
        Gtk.main_quit(args)
    def onAddButtonClick(self, *args):
        self.addFudo = self.builder.get_object("addFudoDialog")
        self.addFudo.run()
    def onSubmit(self, *args):
        f = open("lists/todo.json", "r")
        data = json.loads(f.read())
        NewFudoName = self.builder.get_object("NameTextInput");
        NewFudoName = NewFudoName.get_text()
        NewFudoDescription = self.builder.get_object("DescriptionTextInput");
        buf = NewFudoDescription.get_buffer()
        NewFudoDescription = buf.get_text(buf.get_start_iter(), buf.get_end_iter(), True)
        data.append([NewFudoName, NewFudoDescription])
        print(data)
        f = open("lists/todo.json", "w")
        f.write(json.dumps(data))
        self.addFudo.hide()
    def onCancel(self, *args):
        self.addFudo.hide()

builder = Gtk.Builder()
signals = Signals()
signals.setBuilder(builder)
builder.add_from_file("fudo.glade");
builder.connect_signals(signals)

window = builder.get_object("window")
window.show_all()
Gtk.main()

