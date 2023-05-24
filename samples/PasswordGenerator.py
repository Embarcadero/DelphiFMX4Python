#!/usr/bin/env python3
#----------------------------------------------------------------
# Name:        PasswordGenerator.py
# Purpose:     Password Generator built with DelphiFMX GUI Framework
#
# Author:      Shaun Roselt
#
# Created:     26/02/2023
# License:     MIT - Free to reuse and modify as you see fit.
#----------------------------------------------------------------

import os
import random
from delphifmx import *

class frmMain(Form):

    def __init__(self, owner):
        self.Caption = 'Password Generator'
        self.Width = 1000
        self.Height = 900
        self.Position = "ScreenCenter"
        self.OnShow = self.Form_OnShow

        self.layBottom = Layout(self)
        self.layBottom.Parent = self
        self.layBottom.Align = "Client"
        self.layBottom.Padding.Top = 20
        self.layBottom.Padding.Right = 20
        self.layBottom.Padding.Bottom = 20
        self.layBottom.Padding.Left = 20

        self.memTitleOutput = Label(self)
        self.memTitleOutput.Parent = self.layBottom
        self.memTitleOutput.Text = "Passwords"
        self.memTitleOutput.Align = "Top"
        self.memTitleOutput.Height = 36
        self.memTitleOutput.StyledSettings = ""
        self.memTitleOutput.TextSettings.Font.Size = 20

        self.btnRefresh = Button(self)
        self.btnRefresh.Parent = self.memTitleOutput
        self.btnRefresh.Text = "Refresh"
        self.btnRefresh.Align = "Right"
        self.btnRefresh.Width = 75
        self.btnRefresh.Margins.Top = 1
        self.btnRefresh.Margins.Right = 3
        self.btnRefresh.Margins.Bottom = 1
        self.btnRefresh.TextSettings.HorzAlign = "Center"
        self.btnRefresh.OnClick = self.Refresh_OnClick

        self.btnOutputCopyToClipboard = Button(self)
        self.btnOutputCopyToClipboard.Parent = self.memTitleOutput
        self.btnOutputCopyToClipboard.Text = "Copy to Clipboard"
        self.btnOutputCopyToClipboard.Align = "MostRight"
        self.btnOutputCopyToClipboard.Width = 135
        self.btnOutputCopyToClipboard.Margins.Top = 1
        self.btnOutputCopyToClipboard.Margins.Right = 1
        self.btnOutputCopyToClipboard.Margins.Bottom = 1
        self.btnOutputCopyToClipboard.TextSettings.HorzAlign = "Center"
        self.btnOutputCopyToClipboard.OnClick = self.CopyToClipboard_OnClick

        self.memOutput = Memo(self)
        self.memOutput.Parent = self.layBottom
        self.memOutput.Align = "Client"

        self.layTop = Layout(self)
        self.layTop.Parent = self
        self.layTop.Align = "Top"
        self.layTop.Padding.Top = 20
        self.layTop.Padding.Right = 20
        self.layTop.Padding.Bottom = 20
        self.layTop.Padding.Left = 20
        self.layTop.Height = 369

        self.lblConfiguration = Label(self)
        self.lblConfiguration.Parent = self.layTop
        self.lblConfiguration.Text = "Configuration"
        self.lblConfiguration.Align = "MostTop"
        self.lblConfiguration.Height = 30
        self.lblConfiguration.StyledSettings = ""
        self.lblConfiguration.TextSettings.Font.Size = 20

        self.layAmount = Rectangle(self)
        self.layAmount.Parent = self.layTop
        self.layAmount.Align = "Top"
        self.layAmount.Height = 72
        self.layAmount.Margins.Bottom = 6
        self.layAmount.Padding.Top = 12
        self.layAmount.Padding.Right = 12
        self.layAmount.Padding.Bottom = 12
        self.layAmount.Padding.Left = 12
        self.layAmount.Stroke.Kind = "None"
        self.layAmount.Fill.Color = "x4B000000"
        self.layAmount.XRadius = 8
        self.layAmount.YRadius = 8

        self.layAmountTitleDescription = Layout(self)
        self.layAmountTitleDescription.Parent = self.layAmount
        self.layAmountTitleDescription.Align = "Client"
        
        self.lblAmountTitle = Label(self)
        self.lblAmountTitle.Parent = self.layAmountTitleDescription
        self.lblAmountTitle.Text = "Amount"
        self.lblAmountTitle.Align = "Top"
        self.lblAmountTitle.Height = 24
        self.lblAmountTitle.StyledSettings = ""
        self.lblAmountTitle.TextSettings.Font.Size = 18
        
        self.lblAmountDescription = Label(self)
        self.lblAmountDescription.Parent = self.layAmountTitleDescription
        self.lblAmountDescription.Text = "Select how many passwords you want"
        self.lblAmountDescription.Align = "Client"
        self.lblAmountDescription.StyledSettings = ""
        self.lblAmountDescription.TextSettings.Font.Size = 14

        self.sbAmount = SpinBox(self)
        self.sbAmount.Parent = self.layAmount
        self.sbAmount.Align = "Right"
        self.sbAmount.Width = 140
        self.sbAmount.Value = 20
        self.sbAmount.Min = 1
        self.sbAmount.Max = 1000
        self.sbAmount.OnChange = self.Refresh_OnClick

        self.layPasswordLength = Rectangle(self)
        self.layPasswordLength.Parent = self.layTop
        self.layPasswordLength.Align = "Top"
        self.layPasswordLength.Height = 72
        self.layPasswordLength.Margins.Bottom = 6
        self.layPasswordLength.Padding.Top = 12
        self.layPasswordLength.Padding.Right = 12
        self.layPasswordLength.Padding.Bottom = 12
        self.layPasswordLength.Padding.Left = 12
        self.layPasswordLength.Stroke.Kind = "None"
        self.layPasswordLength.Fill.Color = "x4B000000"
        self.layPasswordLength.XRadius = 8
        self.layPasswordLength.YRadius = 8

        self.layPasswordLengthTitleDescription = Layout(self)
        self.layPasswordLengthTitleDescription.Parent = self.layPasswordLength
        self.layPasswordLengthTitleDescription.Align = "Client"
        
        self.lblPasswordLengthTitle = Label(self)
        self.lblPasswordLengthTitle.Parent = self.layPasswordLengthTitleDescription
        self.lblPasswordLengthTitle.Text = "Password Length"
        self.lblPasswordLengthTitle.Align = "Top"
        self.lblPasswordLengthTitle.Height = 24
        self.lblPasswordLengthTitle.StyledSettings = ""
        self.lblPasswordLengthTitle.TextSettings.Font.Size = 18
        
        self.lblPasswordLengthDescription = Label(self)
        self.lblPasswordLengthDescription.Parent = self.layPasswordLengthTitleDescription
        self.lblPasswordLengthDescription.Text = "Select the length of the password"
        self.lblPasswordLengthDescription.Align = "Client"
        self.lblPasswordLengthDescription.StyledSettings = ""
        self.lblPasswordLengthDescription.TextSettings.Font.Size = 14

        self.sbPasswordLength = SpinBox(self)
        self.sbPasswordLength.Parent = self.layPasswordLength
        self.sbPasswordLength.Align = "Right"
        self.sbPasswordLength.Width = 140
        self.sbPasswordLength.Value = 20
        self.sbPasswordLength.Min = 1
        self.sbPasswordLength.Max = 1000
        self.sbPasswordLength.OnChange = self.Refresh_OnClick

        self.laySpecialCharacters = Rectangle(self)
        self.laySpecialCharacters.Parent = self.layTop
        self.laySpecialCharacters.Align = "Top"
        self.laySpecialCharacters.Height = 72
        self.laySpecialCharacters.Margins.Bottom = 6
        self.laySpecialCharacters.Padding.Top = 12
        self.laySpecialCharacters.Padding.Right = 12
        self.laySpecialCharacters.Padding.Bottom = 12
        self.laySpecialCharacters.Padding.Left = 12
        self.laySpecialCharacters.Stroke.Kind = "None"
        self.laySpecialCharacters.Fill.Color = "x4B000000"
        self.laySpecialCharacters.XRadius = 8
        self.laySpecialCharacters.YRadius = 8

        self.laySpecialCharactersTitleDescription = Layout(self)
        self.laySpecialCharactersTitleDescription.Parent = self.laySpecialCharacters
        self.laySpecialCharactersTitleDescription.Align = "Client"
        
        self.lblSpecialCharactersTitle = Label(self)
        self.lblSpecialCharactersTitle.Parent = self.laySpecialCharactersTitleDescription
        self.lblSpecialCharactersTitle.Text = "Special Characters"
        self.lblSpecialCharactersTitle.Align = "Top"
        self.lblSpecialCharactersTitle.Height = 24
        self.lblSpecialCharactersTitle.StyledSettings = ""
        self.lblSpecialCharactersTitle.TextSettings.Font.Size = 18
        
        self.lblSpecialCharactersDescription = Label(self)
        self.lblSpecialCharactersDescription.Parent = self.laySpecialCharactersTitleDescription
        self.lblSpecialCharactersDescription.Text = "Select whether you want to use special characters or not"
        self.lblSpecialCharactersDescription.Align = "Client"
        self.lblSpecialCharactersDescription.StyledSettings = ""
        self.lblSpecialCharactersDescription.TextSettings.Font.Size = 14
        
        self.lblSwitchSpecialCharacters = Label(self)
        self.lblSwitchSpecialCharacters.Parent = self.laySpecialCharacters
        self.lblSwitchSpecialCharacters.Text = "On"
        self.lblSwitchSpecialCharacters.Align = "Right"
        self.lblSwitchSpecialCharacters.StyledSettings = ""
        self.lblSwitchSpecialCharacters.TextSettings.Font.Size = 18
        self.lblSwitchSpecialCharacters.TextSettings.HorzAlign = "Trailing"
        self.lblSwitchSpecialCharacters.Margins.Right = 8
        self.lblSwitchSpecialCharacters.Width = 72

        self.SpecialCharactersSwitch = Switch(self)
        self.SpecialCharactersSwitch.Parent = self.laySpecialCharacters
        self.SpecialCharactersSwitch.Align = "MostRight"
        self.SpecialCharactersSwitch.isChecked = True
        self.SpecialCharactersSwitch.Width = 72
        self.SpecialCharactersSwitch.OnSwitch = self.SpecialCharactersSwitch_OnSwitch

        self.layLetterCase = Rectangle(self)
        self.layLetterCase.Parent = self.layTop
        self.layLetterCase.Align = "Top"
        self.layLetterCase.Height = 72
        self.layLetterCase.Margins.Bottom = 6
        self.layLetterCase.Padding.Top = 12
        self.layLetterCase.Padding.Right = 12
        self.layLetterCase.Padding.Bottom = 12
        self.layLetterCase.Padding.Left = 12
        self.layLetterCase.Stroke.Kind = "None"
        self.layLetterCase.Fill.Color = "x4B000000"
        self.layLetterCase.XRadius = 8
        self.layLetterCase.YRadius = 8

        self.layLetterCaseTitleDescription = Layout(self)
        self.layLetterCaseTitleDescription.Parent = self.layLetterCase
        self.layLetterCaseTitleDescription.Align = "Client"
        
        self.lblLetterCaseTitle = Label(self)
        self.lblLetterCaseTitle.Parent = self.layLetterCaseTitleDescription
        self.lblLetterCaseTitle.Text = "Letter Case"
        self.lblLetterCaseTitle.Align = "Top"
        self.lblLetterCaseTitle.Height = 24
        self.lblLetterCaseTitle.StyledSettings = ""
        self.lblLetterCaseTitle.TextSettings.Font.Size = 18
        
        self.lblLetterCaseDescription = Label(self)
        self.lblLetterCaseDescription.Parent = self.layLetterCaseTitleDescription
        self.lblLetterCaseDescription.Text = "Select which letter case you want to use"
        self.lblLetterCaseDescription.Align = "Client"
        self.lblLetterCaseDescription.StyledSettings = ""
        self.lblLetterCaseDescription.TextSettings.Font.Size = 14

        self.cbLetterCase = ComboBox(self)
        self.cbLetterCase.Parent = self.layLetterCase
        self.cbLetterCase.Align = "Right"
        self.cbLetterCase.Width = 140
        self.cbLetterCase.Items.Add("Regular")
        self.cbLetterCase.Items.Add("lower")
        self.cbLetterCase.Items.Add("UPPER")
        self.cbLetterCase.ItemIndex = 0
        self.cbLetterCase.OnChange = self.Refresh_OnClick

    def GenerateRandomPassword(self):
        self.memOutput.Lines.Clear()
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if self.SpecialCharactersSwitch.isChecked:
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>/?"

        for i in range(round(self.sbAmount.Value)):
            password = ""
            for j in range(round(self.sbPasswordLength.Value)):
                password += random.choice(characters)
            self.memOutput.Lines.Add(password)


    def SpecialCharactersSwitch_OnSwitch(self, sender):
        if sender.isChecked:
            self.lblSwitchSpecialCharacters.Text = "On"
        else:
            self.lblSwitchSpecialCharacters.Text = "Off"

        self.GenerateRandomPassword()

    def Refresh_OnClick(self, sender):
        self.GenerateRandomPassword()

    def CopyToClipboard_OnClick(self, sender):
        self.memOutput.SelectAll()
        self.memOutput.CopyToClipboard()

    def Form_OnShow(self, sender):
        self.GenerateRandomPassword()

    

def main():
    Application.Initialize()
    Application.Title = 'Password Generator'
    Application.MainForm = frmMain(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
