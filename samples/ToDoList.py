#----------------------------------------------------------------
# Name:        ToDoList.py
# Purpose:     Simple ToDo List built with Delphi FMX
#              Saves list to a text file
#
# Author:      Jim McKeeth
#
# Created:     21/01/2022
# Copyright:   (c) Embarcadero Technologies 2022
#----------------------------------------------------------------

from delphifmx import *
from os.path import exists

class HelloForm(Form):

    def __init__(self, owner):
        self.SetProps(Caption = "My To Do List", OnShow = self.__form_show, OnClose = self.__form_close)

        self.hello = Label(self)
        self.hello.SetProps(Parent = self, Text = "Next Do: ", Position = Position(PointF(20, 20)))

        self.edit = Edit(self)
        self.edit.SetProps(Parent = self, Position = Position(PointF(80,18)))

        self.clickme = Button(self)
        self.clickme.SetProps(Parent = self, Text = "Add", Position = Position(PointF(190, 18)), Width = 80, OnClick = self.__button_click)

        self.list = ListBox(self)
        self.list.SetProps(Parent = self, Position = Position(PointF(20, 60)), Width = 250, OnClick = self.__list_item_click)

    def __list_item_click(self, sender):
        if (self.list.itemindex > -1):
            self.list.items.delete(self.list.itemindex)

    def __form_show(self, sender):
        self.SetProps(Width = 300, Height = 320)
        if exists("todo.txt"):
            self.list.items.loadfromfile("todo.txt")

    def __form_close(self, sender, action):
        self.list.items.savetofile("todo.txt")
        action = "caFree"

    def __button_click(self, sender):
        self.list.items.add(self.edit.text)
        self.edit.text = ""

def main():
    Application.Initialize()
    Application.Title = "Hello Delphi FMX"
    Application.MainForm = HelloForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
