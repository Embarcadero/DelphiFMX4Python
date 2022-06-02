#----------------------------------------------------------------
# Name:        hello_highdpi.py
# Purpose:     Test of High DPI Awareness
#
# Author:      Lucas Belo
#
# Created:     01/June/2022
# Copyright:   (c) Embarcadero Technologies 2022
# License:     MIT - Free to reuse and modify as you see fit.
#----------------------------------------------------------------

from delphifmx import *

class HelloForm(Form):

    def __init__(self, owner):
        self.SetProps(Caption = "Hello High DPI",
            Position = "poScreenCenter", OnShow = self.__form_show)

        self.hello = Label(self)
        self.hello.SetProps(Parent = self, width = 200, AutoSize = True,
            Text = "Per Monitor v2 High DPI is enabled by default. Check the console and source code for some details.", Position = Position(PointF(20, 20)))

        self.clickme = Button(self)
        self.clickme.SetProps(Parent = self, Text = "Click Me",
            Position = Position(PointF(20, 80)), OnClick = self.__button_click)

    def __form_show(self, sender):
        self.SetProps(Width = 300, Height = 400)

    def __button_click(self, sender):
        self.hello.Text = "Thanks!"
        self.Width = 300

def main():

    print("Is DPI aware?", IsDpiAware())
    print("Which is the process DPI awareness?", GetProcessDpiAwareness())
    print("Let DelphiFMX chooses the best dpi for us: ", SetHighDpiAware())
    print("Did DelphiFMX choose DPI aware?", IsDpiAware())

    """
    Possible result values:
    S_OK = 0
    E_ACCESSDENIED = 2147942405
    E_INVALIDARG = 2147942487
    """
    print("or else we can set it by ourselves to PROCESS_PER_MONITOR_DPI_AWARE = 2. Result: ", SetProcessDpiAwareness(2))

    """
    Possible result values:
    S_OK = 0
    E_ACCESSDENIED = 2147942405
    E_INVALIDARG = 2147942487
    """
    err_code, dpi_awareness = GetProcessDpiAwareness()
    if (err_code != 0):
        print("Something went wrong while requesting for dpi awareness. ", "Err_code: ", err_code)
    else:
        print("Which DPI awareness have we set?", dpi_awareness)
    print("Is DPI aware?", IsDpiAware())

    Application.Initialize()
    Application.Title = "Hello Delphi FMX"
    Application.MainForm = HelloForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()