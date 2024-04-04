from tkinter import *
import os
# import filedialog module
from tkinter import filedialog

class FileBrowser :
    def browseFiles():
        currentDirectory = os.getcwd()
        chosenTypes =  (("CSV files","*.csv*"),("all files","*.*"))
        filename = filedialog.askopenfilename(initialdir = currentDirectory, title = "Select the file to be parsed",filetypes = chosenTypes )
        return filename
    
    def setSaveLocation():
        path = filedialog.askdirectory(title="Select Save Location" )
        return path
