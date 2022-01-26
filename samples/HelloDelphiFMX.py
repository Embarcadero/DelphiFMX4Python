#----------------------------------------------------------------
# Name:        HelloDelphiFMX.py
# Purpose:     Simple DelphiFMX for Python demonstration with OOP
#
# Author:      Jim McKeeth
#
# Created:     21/01/2022
# Copyright:   (c) Embarcadero Technologies 2022
#----------------------------------------------------------------

from delphifmx import *

class HelloForm(Form):

    def __init__(self, owner):
        self.SetProps(Caption = "Hello Python", 
            Position = "poScreenCenter", OnShow = self.__form_show)

        self.hello = Label(self)
        self.hello.SetProps(Parent = self, width = 200,
            Text = "Hello Python from Delphi FMX", Position = Position(PointF(20, 20)))

        self.clickme = Button(self)
        self.clickme.SetProps(Parent = self, Text = "Click Me", 
            Position = Position(PointF(20, 50)), OnClick = self.__button_click)

    def __form_show(self, sender):
        self.SetProps(Width = 300, Height = 400)

    def __button_click(self, sender):
        self.hello.Text = "Thanks!"
        self.Width = 300

def main():
    Application.Initialize()
    Application.Title = "Hello Delphi FMX"
    Application.MainForm = HelloForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
