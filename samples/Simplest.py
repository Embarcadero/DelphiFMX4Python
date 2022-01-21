#-----------------------------------------------
# Name:        Simplest.py
# Purpose:     The simplest demo of Delphi FMX
#
# Author:      Jim McKeeth
#
# Created:     21/01/2022
# Copyright:   (c) Embarcadero Technologies 2022
#-----------------------------------------------

from delphifmx import *

Application.Initialize()
Application.Title = "Hello Delphi FMX"
Application.MainForm = Form(Application)
Application.MainForm.SetProps(Caption = "Hello World")
msg = Label(Application.MainForm)
msg.SetProps(Parent = Application.MainForm,
    Text = "Hello Python from Delphi FMX",
    Position = Position(PointF(20, 20)),
    Width = 200)
Application.MainForm.Show()
Application.Run() # This is the main loop
Application.MainForm.Destroy()