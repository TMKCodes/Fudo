#!/usr/bin/python

from gi.repository import Gtk
import json
import time

class Fudo:
    def loadMainData(self):
        if hasattr(self, 'todoVBox'):
            self.todoViewport.remove(self.todoVBox);
            del self.todoVBox;
        if hasattr(self, 'todoViewport') == False:
            self.todoViewport = self.builder.get_object("todoViewport")
        self.todoVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        f = open("lists/todo.json", "r")
        data = json.loads(f.read())
        for fudo in data:
            button = Gtk.Button(fudo[0])
            button.connect("clicked", self.onToDoClick)
            self.todoVBox.add(button);
        self.todoViewport.add(self.todoVBox)
        if hasattr(self, "doingVBox"):
            self.doingViewport.remove(self.doingVBox);
            del self.doingVBox;
        if hasattr(self, "doingViewport") == False:
            self.doingViewport = self.builder.get_object("doingViewport");
        self.doingVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        f = open("lists/doing.json", "r");
        doing = json.loads(f.read())
        for fudo in doing:
            button = Gtk.Button(fudo[0]);
            button.connect("clicked", self.onDoingClick);
            self.doingVBox.add(button);
        self.doingViewport.add(self.doingVBox);
        if hasattr(self, "doneVBox"):
            self.doneViewport.remove(self.doneVBox);
            del self.doneVBox;
        if hasattr(self, "doneViewport") == False:
            self.doneViewport = self.builder.get_object("doneViewport");
        self.doneVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=1)
        f = open("lists/done.json", "r");
        done = json.loads(f.read())
        for fudo in done:
            button = Gtk.Button(fudo[0]);
            button.connect("clicked", self.onDoneClick);
            self.doneVBox.add(button);
        self.doneViewport.add(self.doneVBox);
    def __init__(self, builder, window):
        self.builder = builder
        self.window = window
        self.loadMainData();
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
        button.connect("clicked", self.onToDoClick)
        self.todoVBox.add(button)
        print(data)
        f = open("lists/todo.json", "w")
        f.write(json.dumps(data, indent=4))
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
    def onToDoClick(self, *args):
        self.Fudo = self.builder.get_object("fudoDialog");
        f = open("lists/todo.json", "r")
        data = json.loads(f.read())
        for fudo in data:
            if fudo[0] == args[0].get_label():
                name = self.builder.get_object("FudoName");
                buf = name.get_buffer();
                buf.set_text(fudo[0]);
                name.set_buffer(buf);
                description = self.builder.get_object("FudoDescription");
                buf = description.get_buffer();
                buf.set_text(fudo[1]);
                description.set_buffer(buf);
                progress = self.builder.get_object("FudoProgress");
                buf = progress.get_buffer();
                buf.set_text("Fudo should be started.");
                progress.set_buffer(buf);
        self.Fudo.run();
    def onDoingClick(self, *args):
        self.Fudo = self.builder.get_object("fudoDialog");
        f = open("lists/doing.json", "r")
        data = json.loads(f.read())
        for fudo in data:
            if fudo[0] == args[0].get_label():
                name = self.builder.get_object("FudoName");
                buf = name.get_buffer();
                buf.set_text(fudo[0]);
                name.set_buffer(buf);
                description = self.builder.get_object("FudoDescription");
                buf = description.get_buffer();
                buf.set_text(fudo[1]);
                description.set_buffer(buf);
                progress = self.builder.get_object("FudoProgress");
                buf = progress.get_buffer();
                seconds = int(time.time() - fudo[2]);
                minutes, seconds = divmod(seconds, 60);
                hours, minutes = divmod(minutes, 60);
                buf.set_text("Time wasted: " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds");
                progress.set_buffer(buf);
        self.Fudo.run();
    def onDoneClick(self, *args):
        self.Fudo = self.builder.get_object("fudoDoneDialog");
        f = open("lists/done.json", "r")
        data = json.loads(f.read())
        for fudo in data:
            if fudo[0] == args[0].get_label():
                name = self.builder.get_object("FudoDoneName");
                buf = name.get_buffer();
                buf.set_text(fudo[0]);
                name.set_buffer(buf);
                description = self.builder.get_object("FudoDoneDescription");
                buf = description.get_buffer();
                buf.set_text(fudo[1]);
                description.set_buffer(buf);
                progress = self.builder.get_object("FudoDoneProgress");
                buf = progress.get_buffer();
                seconds = int(fudo[2]);
                minutes, seconds = divmod(seconds, 60);
                hours, minutes = divmod(minutes, 60);
                buf.set_text("The Fudo was done in " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds");
                progress.set_buffer(buf);
        self.Fudo.run();
    def onFudoComplete(self, *args):
        f = open("lists/doing.json", "r");
        doing = json.loads(f.read());
        name = self.builder.get_object("FudoName").get_buffer()
        name = name.get_text(name.get_start_iter(), name.get_end_iter(), True);
        for x in range(0, len(doing)):
            if doing[x][0] == name:
                f = open("lists/done.json", "r");
                done = json.loads(f.read());
                done.append([doing[x][0], doing[x][1], (time.time() - doing[x][2])]);
                f = open("lists/done.json", "w");
                f.write(json.dumps(done, indent=4));
                doing.pop(x);
                break;
        f = open("lists/doing.json", "w");
        if len(doing) > 0:
            f.write(json.dumps(doing, indent=4));
        else:
            f.write("[]");
    def onFudoPause(self, *args):
        return 0;
    def onFudoStart(self, *args):
        f = open("lists/todo.json", "r");
        data = json.loads(f.read());
        name = self.builder.get_object("FudoName").get_buffer()
        name = name.get_text(name.get_start_iter(), name.get_end_iter(), True);
        for x in range(0, len(data)):
            if data[x][0] == name:
                f = open("lists/doing.json", "r");
                doing = json.loads(f.read());
                doing.append([data[x][0], data[x][1], time.time()]);
                f = open("lists/doing.json", "w");
                f.write(json.dumps(doing, indent=4));
                data.pop(x);
                break;
        f = open("lists/todo.json", "w");
        if len(data) > 0:
            f.write(json.dumps(data, indent=4));
        else:
            f.write("[]");
    def onFudoClose(self, *args):
        self.loadMainData();
        self.window.show_all()
        self.Fudo.hide();

if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("fudo.glade")
    window = builder.get_object("window")
    builder.connect_signals(Fudo(builder, window))
    window.show_all()
    Gtk.main()
