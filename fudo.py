#!/usr/bin/python

from gi.repository import Gtk
import json

class Fudo:
    def __init__(self, builder, window):
        self.builder = builder
        self.window = window
        self.todoViewport = builder.get_object("todoViewport")
        self.todoVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        f = open("lists/todo.json", "r")
        data = json.loads(f.read())
        for fudo in data:
            button = Gtk.Button(fudo[0])
            self.todoVBox.add(button);
        self.todoViewport.add(self.todoVBox)
    def onDeleteWindow(self, *args):
        Gtk.main_quit(args)
    def onAddButtonClick(self, *args):
        self.addFudo = self.builder.get_object("addFudoDialog")
        self.addFudo.run()
    def onSubmit(self, *args):
        f = open("lists/todo.json", "r")
        data = json.loads(f.read())
        NewFudoName = self.builder.get_object("NameTextInput");
        NewFudoNameText = NewFudoName.get_text()
        NewFudoName.set_text("")
        NewFudoDescription = self.builder.get_object("DescriptionTextInput");
        buf = NewFudoDescription.get_buffer()
        NewFudoDescriptionText = buf.get_text(buf.get_start_iter(), buf.get_end_iter(), True)
        buf.set_text("")
        NewFudoDescription.set_buffer(buf)
        data.append([NewFudoNameText, NewFudoDescriptionText])
        button = Gtk.Button(NewFudoNameText)
        self.todoVBox.add(button)
        print(data)
        f = open("lists/todo.json", "w")
        f.write(json.dumps(data))
        self.window.show_all()
        self.addFudo.hide()
    def onCancel(self, *args):
        NewFudoName = self.builder.get_object("NameTextInput")
        NewFudoName.set_text("")
        NewFudoDescription = self.builder.get_object("DescriptionTextInput")
        buf = NewFudoDescription.get_buffer();
        buf.set_text("")
        NewFudoDescription.set_buffer(buf)
        self.addFudo.hide()

if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("fudo.glade")
    window = builder.get_object("window")
    builder.connect_signals(Fudo(builder, window))
    window.show_all()
    Gtk.main()
