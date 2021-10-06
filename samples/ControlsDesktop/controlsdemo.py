#-------------------------------------------------------------------------------
# Name:        CtrlsDemoFrm
# Purpose:
#
# Author:      lmbelo
#
# Created:     28/09/2021
# Copyright:   1995-2021 Embarcadero Technologies, Inc.
#              All rights reserved
#-------------------------------------------------------------------------------

from delphifmx import *

class CtrlsDemoFrm(Form):

    def __init__(self, owner):
        self.__create_comps()
        self.__config_comps()
        self.__init_comps()

    def __create_comps(self):
        self.mm_menu = MainMenu(self)
        self.mi_file = MenuItem(self.mm_menu)
        self.mi_load_style = MenuItem(self.mm_menu)
        self.mi_exit = MenuItem(self.mm_menu)
        self.od_style = OpenDialog(self)
        self.lo_control = Layout(self)
        self.lo_control_root = Layout(self.lo_control)
        self.tc_tabs = TabControl(self.lo_control_root)
        self.ti_standard = TabItem(self.tc_tabs)
        self.ti_additional = TabItem(self.tc_tabs)
        self.ti_ext_controls = TabItem(self.tc_tabs)
        self.ti_tree_view_list_box = TabItem(self.tc_tabs)
        self.ti_transformation = TabItem(self.tc_tabs)
        self.ti_scroll_box = TabItem(self.tc_tabs)
        self.ti_memo = TabItem(self.tc_tabs)
        self.ti_new = TabItem(self.tc_tabs)
        self.sb_status = StatusBar(self)
        self.lbl_status = Label(self.sb_status)
        self.lbl_scale_label = Label(self.sb_status)
        self.lbl_scale_text = Label(self.sb_status)
        self.tb_scale = TrackBar(self.sb_status)
        #Create tab item components
        self.__create_std_comps(self.ti_standard)

    def __create_std_comps(self, tab):
        self.ai = AniIndicator(tab)
        self.lb_ani_indicator = Label(tab)
        self.btn_glyph = Button(tab)
        self.cp = CalloutPanel(tab)
        self.lbl_cp = Label(self.cp)
        self.callout_bottom = RadioButton(self.cp)
        self.callout_left = RadioButton(self.cp)
        self.callout_right = RadioButton(self.cp)
        self.callout_top = RadioButton(self.cp)
        self.cb = CheckBox(tab)
        self.rb_1 = RadioButton(tab)
        self.rb_2 = RadioButton(tab)
        self.cb_multi_select = CheckBox(tab)
        self.pnl = Panel(tab)
        self.lb_panel = Label(self.pnl)
        self.btn_panel_1 = SpeedButton(self.pnl)
        self.btn_panel_2 = SpeedButton(self.pnl)
        self.pg = ProgressBar(tab)
        self.rb_1 = RadioButton(tab)
        self.rb_2 = RadioButton(tab)
        self.lbl_sb = Label(tab)
        self.sb_1 = ScrollBar(tab)
        self.sb_2 = ScrollBar(tab)
        self.ssb = SmallScrollBar(tab)
        self.cb_string = ComboBox(tab)
        self.lb_string = ListBox(tab)
        self.lbl_lb_string = Label(tab)
        self.lbl_text_box = Label(tab)
        self.edt_text_box = Edit(tab)
        self.tb = TrackBar(tab)
        self.lbl_tb = Label(tab)

    def __config_comps(self):
        self.SetProps(Caption = "FireMonkey Controls - Form", ClientHeight = 539, ClientWidth = 835, Position = "poScreenCenter", DesignerMasterStyle = 0, FormFamily = "TForm")
        self.SetProps(OnClose = self.__on_form_close, OnFocusChanged = self.__on_focus_changed)

        self.mm_menu.SetProps(Parent = self)
        self.mi_file.SetProps(Parent = self.mm_menu, Text = "File")
        self.mi_load_style.SetProps(Parent = self.mi_file, Text = "Load Style...", OnClick = self.__on_load_style_click)
        self.mi_exit.SetProps(Parent = self.mi_file, Text = "Exit", OnClick = (lambda sender: Application.Terminate()))
        self.od_style.SetProps(Filter = "FireMonkey Styles|*.style;*.fsf")

        self.sb_status.SetProps(Parent = self, Padding = Bounds(RectF(2, 5, 30, 5)), Position = Position(PointF(0, 5)), ShowSizeGrip = True)
        self.sb_status.Size.SetProps(Size = SizeF(835, 29), PlatformDefault = False)

        self.lbl_status.SetProps(Parent = self.sb_status, Text = "TStatusBar", Position = Position(PointF(2, 5)))

        self.lbl_scale_text.SetProps(Parent = self.sb_status, Text = "100%", Align = "Right")
        self.lbl_scale_text.Size.SetProps(Size = SizeF(38, 19), PlatformDefault = False)
        self.lbl_scale_text.TextSettings.SetProps(HorzALign = "Center")

        self.tb_scale.SetProps(Parent = self.sb_status, Align = "Right", CanParentFocus = True, Frequency = 0.1, Max = 1.0, Min = 0.5, Orientation = "Horizontal", TabOrder = 2, Value = 1)
        self.tb_scale.Size.SetProps(Size = SizeF(116, 19), PlatformDefault = False)
        self.tb_scale.SetProps(OnChange = self.__on_tb_scale_change)

        self.lbl_scale_label.SetProps(Parent = self.sb_status, Text = "Scale:", Align = "Right")
        self.lbl_scale_label.Size.SetProps(Size = SizeF(57, 19), PlatformDefault = False)
        self.lbl_scale_label.TextSettings.SetProps(HorzALign = "Center")

        self.lo_control.SetProps(Parent = self, Align = "Client", OnResize = self.__on_lo_control_resize)

        self.lo_control_root.SetProps(Parent = self.lo_control, HitTest = True, Padding = Bounds(RectF(5, 5, 5, 5)), Margins = Bounds(RectF(5, 5, 5, 5)), Position = Position(PointF(5, 5)))
        self.lo_control_root.Size.SetProps(Size = SizeF(825, 500), PlatformDefault = False)

        self.tc_tabs.SetProps(Parent = self.lo_control_root, Align = "Client", Margins = Bounds(RectF(4, 4, 4, 4)), TabIndex = 4, TabPosition = "Top")

        self.__config_std_comps()

    def __config_std_comps(self):
        self.ti_standard.SetProps(Parent = self.tc_tabs, IsSelected = False, Text = "Standard")
        self.ti_standard.Size.SetProps(Size = SizeF(68, 26), PlatformDefault = False)

        self.lbl_sb.SetProps(Parent = self.ti_standard, Position = Position(PointF(265, 18)), Text = "ListBox & ListBoxItem", TabOrder = 0)
        self.lbl_sb.Size.SetProps(Size = SizeF(127, 17), PlatformDefault = False)

        self.lbl_text_box.SetProps(Parent = self.ti_standard, Position = Position(PointF(20, 16)), Text = "Edit", TabOrder = 0)
        self.lbl_text_box.Size.SetProps(Size = SizeF(52, 17), PlatformDefault = False)

        self.edt_text_box.SetProps(Parent = self.ti_standard, Position = Position(PointF(15, 32)), Text = "some text", TabOrder = 2, HelpType = "htKeyword")
        self.edt_text_box.Size.SetProps(Size = SizeF(110, 24), PlatformDefault = False)

        self.sb_1.SetProps(Parent = self.ti_standard, Position = Position(PointF(15, 211)), Value = 33, ViewportSize = 20, SmallChange = 0, TabOrder = 3, Orientation = "Horizontal")
        self.sb_1.Size.SetProps(Size = SizeF(179, 18), PlatformDefault = False)
        self.sb_1.SetProps(OnChange = self.__on_change_sb_1)

        self.sb_2.SetProps(Parent = self.ti_standard, Position = Position(PointF(218, 77)), ViewportSize = 0.2, SmallChange = 0, TabOrder = 4, Orientation = "Vertical")
        self.sb_2.Size.SetProps(Size = SizeF(18, 154), PlatformDefault = False)

        self.cb.SetProps(Parent = self.ti_standard, Position = Position(PointF(15, 71)), TabOrder = 5, IsChecked = True, Text = "CheckBox")
        self.cb.Size.SetProps(Size = SizeF(119, 19), PlatformDefault = False)

        self.rb_1.SetProps(Parent = self.ti_standard, Position = Position(PointF(15, 95)), TabOrder = 6, Text = "RadioButton")
        self.rb_1.Size.SetProps(Size = SizeF(94, 19), PlatformDefault = False)

        self.rb_2.SetProps(Parent = self.ti_standard, Position = Position(PointF(113, 95)), TabOrder = 7, IsChecked = True, Text = "RadioButton")
        self.rb_2.Size.SetProps(Size = SizeF(98, 19), PlatformDefault = False)

        self.pg.SetProps(Parent = self.ti_standard, Position = Position(PointF(15, 251)), Value = 33)
        self.pg.Size.SetProps(Size = SizeF(384, 18), PlatformDefault = False)

        self.ai.SetProps(Parent = self.ti_standard, Position = Position(PointF(146, 32)), StyleLookup = 'labelstyle', Enabled = True)
        self.ai.Size.SetProps(Size = SizeF(23, 24), PlatformDefault = False)

        self.lb_ani_indicator.SetProps(Parent = self.ti_standard, Position = Position(PointF(171, 37)), TabOrder = 10, Text = 'Ani indicator')
        self.lb_ani_indicator.Size.SetProps(Size = SizeF(80, 15), PlatformDefault = False)
        self.lb_ani_indicator.TextSettings.HorzAlign = "Center"

        self.lb_string.SetProps(Parent = self.ti_standard, Position = Position(PointF(272, 39)), TabOrder = 11, DisableFocusEffect = True, ItemHeight = 19.00)
        self.lb_string.Size.SetProps(Size = SizeF(127, 166), PlatformDefault = False)
        self.lb_string.DefaultItemStyles.SetProps(ItemStyle = '', GroupHeaderStyle = '', GroupFooterStyle = '')

        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")
        self.lb_string.Items.Add("ListBoxItem")

        self.cb_string.SetProps(Parent = self.ti_standard, Position = Position(PointF(15, 126)), ItemHeight = 19.00, ListBoxResource = 'transparentlistboxstyle', TabOrder = 12)
        self.cb_string.Size.SetProps(Size = SizeF(179, 23), PlatformDefault = False)

        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")
        self.cb_string.Items.Add("ListBoxItem")

        self.btn_glyph.SetProps(Parent = self.ti_standard, Position = Position(PointF(126, 298)), TabOrder = 13, Text = "Glyph")
        self.btn_glyph.Size.SetProps(Size = SizeF(100, 26), PlatformDefault = False)

        self.pnl.SetProps(Parent = self.ti_standard, Position = Position(PointF(412, 16)), TabOrder = 14)
        self.pnl.Size.SetProps(Size = SizeF(138, 145), PlatformDefault = False)

        self.lb_panel.SetProps(Parent = self.pnl, Position = Position(PointF(21, 7)), Text = "Panel")
        self.lb_panel.Size.SetProps(Size = SizeF(94, 22), PlatformDefault = False)
        self.lb_panel.TextSettings.HorzAlign = "Center"

        self.btn_panel_1.SetProps(Parent = self.pnl, Position = Position(PointF(26, 43)), Text = "SpeedButton")
        self.btn_panel_1.Size.SetProps(Size = SizeF(85, 25), PlatformDefault = False)

        self.btn_panel_2.SetProps(Parent = self.pnl, Position = Position(PointF(26, 83)), Text = "SpeedButton")
        self.btn_panel_2.Size.SetProps(Size = SizeF(85, 25), PlatformDefault = False)

        self.ssb.SetProps(Parent = self.ti_standard, Position = Position(PointF(243, 79)), TabOrder = 15, ViewportSize = 33, SmallChange = 0, Orientation = "Vertical")
        self.ssb.Size.SetProps(Size = SizeF(8, 150), PlatformDefault = False)

        self.cb_multi_select.SetProps(Parent = self.ti_standard, Position = Position(PointF(272, 212)), TabOrder = 16, Text = "MultiSelect")
        self.cb_multi_select.Size.SetProps(Size = SizeF(120, 19), PlatformDefault = False)
        self.cb_multi_select.SetProps(OnChange = self.__on_change_cb_multi_select)

        self.cp.SetProps(Parent = self.ti_standard, Position = Position(PointF(412, 185)), TabOrder = 17, CalloutWidth = 23, CalloutLength = 11, CalloutPosition = "Right")
        self.cp.Size.SetProps(Size = SizeF(169, 124), PlatformDefault = False)

        self.lbl_cp.SetProps(Parent = self.cp, Text = "CalloutPanel", Align = "Center")
        self.lbl_cp.Size.SetProps(Size = SizeF(97, 22), PlatformDefault = False)
        self.lbl_cp.TextSettings.SetProps(HorzAlign = "Center")

        self.callout_right.SetProps(Parent = self.cp, Position = Position(PointF(127, 56)), GroupName = "1", IsChecked = True, OnChange = self.__on_co_btn_change)
        self.callout_right.Size.SetProps(Size = SizeF(19, 19), PlatformDefault = False)

        self.callout_top.SetProps(Parent = self.cp, Position = Position(PointF(74, 18)), GroupName = "1", IsChecked = False, OnChange = self.__on_co_btn_change)
        self.callout_top.Size.SetProps(Size = SizeF(19, 19), PlatformDefault = False)

        self.callout_left.SetProps(Parent = self.cp, Position = Position(PointF(15, 58)), GroupName = "1", IsChecked = False, OnChange = self.__on_co_btn_change)
        self.callout_left.Size.SetProps(Size = SizeF(19, 19), PlatformDefault = False)

        self.callout_bottom.SetProps(Parent = self.cp, Position = Position(PointF(74, 86)), GroupName = "1", IsChecked = False, OnChange = self.__on_co_btn_change)
        self.callout_bottom.Size.SetProps(Size = SizeF(19, 19), PlatformDefault = False)

        self.tb.SetProps(Parent = self.ti_standard, Position = Position(PointF(16, 174)), TabOrder = 18, Orientation = "Horizontal", CanParentFocus = True, Value = 33)
        self.tb.Size.SetProps(Size = SizeF(179, 19), PlatformDefault = False)

        self.lbl_tb.SetProps(Parent = self.ti_standard, Position = Position(PointF(16, 232)), TabOrder = 19)
        self.tb.Size.SetProps(Size = SizeF(120, 15), PlatformDefault = False)

    def __init_comps(self):
        self.__on_lo_control_resize(self.lo_control)

    def __on_focus_changed(self, sender):
        #makes the cursor trick
        if not Application.MainForm.Active:
            Application.MainForm.Activate()

    def __on_lo_control_resize(self, sender):
        self.lo_control_root.Width = self.lo_control.Width;
        self.lo_control_root.Height = self.lo_control.Height;

    def __on_form_close(self, sender, action):
        action.Value = "caFree"

    def __on_load_style_click(self, sender):
        if self.od_style.Execute():
            StyleManager().SetStyle(StyleStreaming().LoadFromFile(self.od_style.FileName))

    def __on_change_sb_1(self, sender):
        self.lbl_tb.Text = str(self.sb_1.Value)

    def __on_change_cb_multi_select(self, sender):
        self.lb_string.MultiSelect = self.cb_multi_select.IsChecked

    def __on_co_btn_change(self, sender):
        if self.callout_left.IsChecked:
            self.cp.CalloutPosition = "Left"
        if self.callout_right.IsChecked:
            self.cp.CalloutPosition = "Right"
        if self.callout_top.IsChecked:
            self.cp.CalloutPosition = "Top"
        if self.callout_bottom.IsChecked:
            self.cp.CalloutPosition = "Bottom"

    def __on_tb_scale_change(self, sender):
        self.lo_control_root.Scale.X = self.tb_scale.Value
        self.lo_control_root.Scale.Y = self.tb_scale.Value
        self.lbl_scale_text.Text = str(round(self.tb_scale.Value * 100)) + '%'

def main():
    Application.Initialize()
    Application.Title = "CtrlsDemoFrm"
    Application.MainForm = CtrlsDemoFrm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()


if __name__ == '__main__':
    main()
