DelphiFMX4Python - FMX.ControlsDesktop Sample[]()
# DelphiFMX4Python - FMX.ControlsDesktop Sample 


This is a sample that shows the use of multiples FMX controls directly from a Python script.
## Contents



* [1 Location](#Location)
* [2 Description](#Description)
* [3 How to Use the Sample](#How_to_Use_the_Sample)
* [4 Implementation](#Implementation)

* [4.1 CtrlsDemoFrm](#CtrlsDemoFrm)

* [5 Uses](#Uses)
* [6 See Also](#See_Also)


## Location 

You can find the **ControlsDesktop** sample project at:

* **GitHub Repository for DelphiFMX4Python:** [https://github.com/Embarcadero/DelphiFMX4Python/tree/main/samples/ControlsDesktop](https://github.com/Embarcadero/DelphiFMX4Python/tree/main/samples/ControlsDesktop)

## Description 

This application demonstrates the use of multiple FMX controls and shows how to modify its various properties directly from a Python script. The application uses the following controls:

* `MainMenu`: Describes the structure of the form's [main menu](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Menus.TMainMenu).
* `MenuItem`: [Menu item](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Menus.TMenuItem) describes the properties of a menu item.
* `OpenDialog`: [Open dialog](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Dialogs.TOpenDialog)  is a class used to display a file-selection dialog.
* `Layout`: A [layout](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Layouts.TLayout) is a container for other graphical objects.
* `TabControl`: [Tab control](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.TabControl.TTabControl) is a tab set that has the appearance of notebook dividers.
* `TabItem`: [Tab item](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.TabControl.TTabItem) is a tab item in a TTabControl component. A TTabControl contains one or more TTabItem objects.
* `StatusBar`: Represents a [status bar](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TStatusBar) component for use in FireMonkey forms.
* `Label`: A [Label](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TLabel) represents a graphical control used to display text in FireMonkey forms.
* `TrackBar`: Represents a general-purpose [track bar](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TTrackBar) for use in applications where tracking is required.
* `AniIndicator`: Represents an animated [spinning indicator](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TAniIndicator) used for illustrating an indefinite waiting time for application processes.
* `Button`: A [Button](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TButton) is a push button control.
* `CalloutPanel`: A [callout panel](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TCalloutPanel) is container for extra information relevant to another item, with a visual indicator pointing to that item.
* `RadioButton`: Represents a [radio (option) button](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TRadioButton).
* `CheckBox`: Represents a FireMonkey styled [check box](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TCheckBox) that can be either on (selected) or off (cleared).
* `Panel`: Represents a generic general-purpose [panel](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TPanel) used to hold multiple controls for organizing purposes.
* `SpeedButton`: Represents a [push button](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TSpeedButton)  that contains a text caption, for usage in various toolbars that you might employ into your applications.
* `ProgressBar`: Represents an animated [progress bar](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TProgressBar) indicator for general progress indication.
* `ScrollBar`: Represents a standard [scroll bar](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TScrollBar) that is used to scroll the contents of a window, form, or a control.
* `SmallScrollBar`: Represents a variation of a standard [scroll bar (small)](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls.TSmallScrollBar).
* `ComboBox`: A [combo box](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.ListBox.TComboBox) is a button with a list box attached to it.
* `ListBox`: A [list box](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.ListBox.TListBox) displays a set of items in a scrollable list.
* `Edit`: General-purpose FireMonkey [edit box.](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Edit.TEdit).

## How to Use the Sample 


1. We strongly recommend using PyScripter IDE: 

* SourceForge: https://sourceforge.net/projects/pyscripter/
* GitHub: https://github.com/pyscripter/pyscripter

2. Navigate to the location given above and open:

*  PyScripter IDE: **controlsdemo.py**.

3. Under **Tools->Tools** choose **Install Packages with pip**.

4. In the dialog box **Package Name** type **delphifmx**.

5.  Press **Ctrl + F9** or choose **Run > Run**.

6.  Interact with the different controls on the form and test the functionlity of each of them.

## Implementation 


### CtrlsDemoFrm 

On initialization **__init__**, the `__create_comps, __create_std_comps` creates all the visual components and attatch them to the `CtrlsDemoFrm` form. The `__config_comps` set all visual components properties. The `__init_comps` takes the first components actions.  The application defines the following event handlers: 

* `__on_focus_changed`: First activate the form. This is importante to initialize form components.
* `__on_lo_control_resize`: Resizes the control root layout.
* `__on_form_close`: Set the close action to free up the form.
* `__on_load_style_click`: Loads a FMX style and applies to the components layout.
* `__on_change_sb_1`: Displays the track bar value.
* `__on_change_cb_multi_select`: Sets the style for the application.
* `__on_co_btn_change`: Set the callout of callout panel position.
* `__on_tb_scale_change`: Changes the control root layout scale.

## Uses 


* [FMX.Menus](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Menus)
* [FMX.Dialogs](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Dialogs)
* [FMX.Layouts](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Layouts)
* [FMX.TabControl](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.TabControl)
* [FMX.StdCtrls](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.StdCtrls)
* [FMX.ListBox](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.ListBox)
* [FMX.Edit](https://docwiki.embarcadero.com/Libraries/Alexandria/en/FMX.Edit)

## See Also 


* [FireMonkey](https://docwiki.embarcadero.com/RADStudio/Alexandria/en/FireMonkey)
* [FireMonkey Quick Start Guide](https://docwiki.embarcadero.com/RADStudio/Alexandria/en/FireMonkey_Quick_Start_Guide_-_Introduction)

* [FireMonkey Applications Guide](https://docwiki.embarcadero.com/RADStudio/Alexandria/en/FireMonkey_Applications_Guide)
* [FireMonkey Components Guide](https://docwiki.embarcadero.com/RADStudio/Alexandria/en/FireMonkey_Components_Guide)

* [FireMonkey Platform Prerequisites](https://docwiki.embarcadero.com/RADStudio/Alexandria/en/FireMonkey_Platform_Prerequisites)




