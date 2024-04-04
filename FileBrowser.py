from tkinter import *
import os
# import filedialog module
from tkinter import filedialog

class FileBrowser :
    def browseFiles():
        currentDirectory = os.getcwd()
        chosenTypes =  (("CSV files","*.csv*"),("all files","*.*"))
        filename = filedialog.askopenfilename(initialdir = currentDirectory, title = "Select a File",filetypes = chosenTypes )
        return filename
