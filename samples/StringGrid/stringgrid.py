import os
from delphifmx import *

class StringGridSample(Form):

    def __init__(self, owner):
        self.caption = "String Grid Sample"

        self.string_grid = StringGrid(self)
        self.currency_column1 = CurrencyColumn(self.string_grid)
        self.glyph_column1 = GlyphColumn(self.string_grid)
        self.column1 = Column(self.string_grid)
        self.string_column1 = StringColumn(self.string_grid)
        self.progress_column1 = ProgressColumn(self.string_grid)
        self.check_column1 = CheckColumn(self.string_grid)
        self.date_column1 = DateColumn(self.string_grid)
        self.time_column1 = TimeColumn(self.string_grid)
        self.popup_column1 = PopupColumn(self.string_grid)
        self.image_list = ImageList(self)

        self.config()

        self.fill_image_list()
        
        for i in range(0, self.string_grid.RowCount):                                                    
            self.string_grid.Cells[0,i] = i + 1
            self.string_grid.Cells[1,i] = i % self.image_list.Count
            self.string_grid.Cells[2,i] = "Row #" + str(i + 1)

        self.RowIndex = 1

        self.fill_string_grid(4, self.RowIndex, "Progress", "")
        self.fill_string_grid(4, self.RowIndex, "Progress", "0")
        self.fill_string_grid(4, self.RowIndex, "Progress Integer", "100")
        self.fill_string_grid(4, self.RowIndex, 'Progress 50%', '500')
        self.fill_string_grid(4, self.RowIndex, 'Progress 100%', '1000')
        self.fill_string_grid(4, self.RowIndex, 'Progress more than 100%', '10000')
        self.fill_string_grid(4, self.RowIndex, 'Progress less than 0%', '-1')
        self.fill_string_grid(4, self.RowIndex, 'Progress error value', 'Error')
    
        self.fill_string_grid(5, self.RowIndex, 'Check column', "True")
        self.fill_string_grid(5, self.RowIndex, 'Check column', "False")
    
        self.fill_string_grid(6, self.RowIndex, 'Date Format: dd/mm/yyyy', "22/08/2023")
        self.fill_string_grid(6, self.RowIndex, 'Date Format: dd-mm-yyyy', "22-08-2023")
        self.fill_string_grid(6, self.RowIndex, 'Date Format: 22 August 2023', "22 August 2023")
        self.fill_string_grid(6, self.RowIndex, 'Date and Time Format: dd-mm-yyyy hh:mm', "22-08-2023 15:45")
        self.fill_string_grid(6, self.RowIndex, 'Error Date', "Error")

        self.fill_string_grid(7, self.RowIndex, 'Time', "12:45:33")
        self.fill_string_grid(7, self.RowIndex, 'Long Time Format', "18:15:22")
        self.fill_string_grid(7, self.RowIndex, 'Error Time', "Error")

        self.fill_string_grid(8, self.RowIndex, 'Popup by Index', "1")
        self.fill_string_grid(8, self.RowIndex, 'Popup by Text', "interesting text")
        self.fill_string_grid(8, self.RowIndex, 'Popup by Text', "text")        


    def fill_string_grid(self, colIndex, RowIndex, Caption, Value):
        self.string_grid.Cells[2, RowIndex] = Caption
        self.string_grid.Cells[3, RowIndex] = '\'' + Value + '\''
        self.string_grid.Cells[colIndex, RowIndex] = Value
        self.RowIndex += 1


    def config(self):
        self.SetProps(
            Width = 900
        )

        self.string_grid.SetProps(
            Parent = self,
            Align = "Client",
            CanFocus = True,
            RowCount = 100,
            Images = self.image_list,
        )
        self.string_grid.Addobject(self.currency_column1)
        self.string_grid.Addobject(self.glyph_column1)
        self.string_grid.Addobject(self.string_column1)
        self.string_grid.Addobject(self.column1)
        self.string_grid.Addobject(self.progress_column1)
        self.string_grid.Addobject(self.check_column1)
        self.string_grid.Addobject(self.date_column1)
        self.string_grid.Addobject(self.time_column1)
        self.string_grid.Addobject(self.popup_column1)

        self.currency_column1.SetProps(
            Parent = self.string_grid,
            Header = '##',
            ReadOnly = True,
            DecimalDigits = 0,
            Width = 41,
        )

        self.glyph_column1.SetProps(
            Parent = self.string_grid,
            Header = 'Glyph',
            Width = 31
        )

        self.string_column1.SetProps(
            Parent = self.string_grid,
            Header = 'String',
            Width = 215
        )

        self.column1.SetProps(
            Parent = self.string_grid,
            Header = 'Column',
            Width = 135
        )

        self.progress_column1.SetProps(
            Parent = self.string_grid,
            Header = 'Progress',
            Max = 1000
        )

        self.check_column1.SetProps(
            Parent = self.string_grid,
            Header = 'Check'
        )

        self.date_column1.SetProps(
            Parent = self.string_grid,
            Header = 'Date',
            Format = 'dd/mm/yyyy',
            ShowClearButton = True
        )

        self.time_column1.SetProps(
            Parent = self.string_grid,
            Header = 'Time',
            ShowClearButton = True
        )

        self.popup_column1.SetProps(
            Parent = self.string_grid,
            Header = 'Popup'
        )

        self.popup_column1.Items.Add('Some text')
        self.popup_column1.Items.Add('Other text')
        self.popup_column1.Items.Add('Interesting text')


    def add_image_1(self, file_path, img_list):
        '''
        Assign all parameters
        '''
        file_name = os.path.splitext(os.path.basename(file_path))[0]        
        img_list.AddOrSet(file_name, [1.000], [file_path], 536870911, 32, 32)


    def add_image_2(self, file_path, img_list):
        '''
        Skip default parameters
        '''
        file_name = os.path.splitext(os.path.basename(file_path))[0]        
        img_list.AddOrSet(file_name, [1.000], [file_path])


    def fill_image_list(self):
        # 32x32 images
        self.add_image_1(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_RAD.png"), self.image_list)
        self.add_image_1(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_Delphi.png"), self.image_list)
        self.add_image_1(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_EAstudio.png"), self.image_list)
        self.add_image_1(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_ER_portal.png"), self.image_list)
        self.add_image_1(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_ERStudio.png"), self.image_list)
        self.add_image_1(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_Home.png"), self.image_list)
        self.add_image_2(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_instant_demo.png"), self.image_list)
        self.add_image_2(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_StringGrid.png"), self.image_list)
        self.add_image_2(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_DBGrid.png"), self.image_list)
        self.add_image_2(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_CustomGrid.png"), self.image_list)
        self.add_image_2(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_InterBase.png"), self.image_list)
        self.add_image_2(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/Icon_Preferences.png"), self.image_list)


def main():
    Application.Initialize()
    Application.Title = "String Grid Sample"
    Application.MainForm = StringGridSample(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()


if __name__ == "__main__":
    main()
