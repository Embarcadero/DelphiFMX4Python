#!/usr/bin/env python3
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
main_window = Form(Application)
Application.MainForm = main_window

main_window.SetProps(Caption = "Hello World")
msg = Label(main_window)
msg.SetProps(Parent = main_window,
    Text = "Hello Python from Delphi FMX",
    Position = Position(PointF(20, 20)),
    Width = 200)
main_window.Show()
Application.Run() # This is the main loop
main_window.Destroy()
