import os                                                                                              
from delphifmx import *                                                                                
                                                                                                       
class Form6(Form):                                                                        
    def __init__(self, owner):                                                                         
        self.StyleBook1 = None
        self.CheckBox1 = None
        self.FloatAnimation1 = None
        self.ListBox1 = None
        self.ListBoxItem1 = None
        self.ListBoxItem2 = None
        self.ListBoxItem3 = None
        self.ListBoxItem4 = None
        self.ListBoxItem5 = None
        self.PopupMenu1 = None
        self.MenuItem1 = None
        self.MenuItem2 = None
        self.MenuItem3 = None
        self.MenuItem4 = None
        self.MenuItem5 = None
        self.MenuItem6 = None
        self.MenuItem7 = None
        self.FloatAnimation2 = None
        self.Button1 = None
        self.SpeedButton1 = None
        self.SpeedButton2 = None
        self.RadioButton1 = None
        self.FloatAnimation5 = None
        self.RadioButton2 = None
        self.FloatAnimation6 = None
        self.RadioButton3 = None
        self.FloatAnimation7 = None
        self.CheckBox2 = None
        self.FloatAnimation3 = None
        self.CheckBox3 = None
        self.FloatAnimation4 = None
        self.TrackBar1 = None                                                                                    
        self.LoadProps(os.path.join("%PATH%", "Form6.pydfm"))   

def main():                                                                                                                                                            
    MainForm = Form6(Application)                                                     
    MainForm.Show()                                                                                 
                                                                                                       
if __name__ == '__main__':                                                                           
    main()                                                                                             