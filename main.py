#!/usr/bin/python

from gi.repository import Gtk
import json

class Signals:
    def setBuilder(self, builder):
        self.builder = builder
    def onDeleteWindow(self, *args):
        Gtk.main_quit(args)
    def onAddButtonClick(self, *args):
        self.addTodo = self.builder.get_object("dialog")
        self.addTodo.run()
    def onSubmit(self, *args):
        f = open("lists/todo.json", "r")
        data = json.loads(f.read())
        NewTodoName = self.builder.get_object("NameTextInput");
        NewTodoName = NewTodoName.get_text()
        NewTodoDescription = self.builder.get_object("DescriptionTextInput");
        buf = NewTodoDescription.get_buffer()
        NewTodoDescription = buf.get_text(buf.get_start_iter(), buf.get_end_iter(), True)
        data.append([NewTodoName, NewTodoDescription])
        print(data)
        f = open("To-Do.list", "w")
        f.write(json.dumps(data))
        self.addTodo.hide()
    def onCancel(self, *args):
        self.addTodo.hide()

builder = Gtk.Builder()
signals = Signals()
signals.setBuilder(builder)
builder.add_from_file("main.glade");
builder.connect_signals(signals)

window = builder.get_object("window")
window.show_all()
Gtk.main()

