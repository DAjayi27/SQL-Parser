

import os
from  FileBrowser import FileBrowser
from rdbms.mysql import MySQL

#parser converts CSV files into insert statements for SQL databases (MSQL RDBMS) (currently only supports csv files)

#opens a file explorer window to select the csv file 

filePath =  FileBrowser.browseFiles()


file = open( filePath ,"r")

filename =  os.path.basename(filePath)

tableName , extension = os.path.splitext(filename)





# Read the CSV file

rbdms = MySQL(tableName)

first_line = file.readline().strip()
first_line = first_line.split(",")

rbdms.insertInto(first_line)

EXPECTED_ROW_SIZE = len(first_line)

for input in file :
    input = input.strip('\n')
    inputArray = input.split(",")
    if len(inputArray) == EXPECTED_ROW_SIZE:
        rbdms.insertInto(inputArray)
    else:
        message = f"The rows in the file appear to not be properly aligned. the row {input} is not aligned"
        raise ValueError(message)
    
rbdms.analyzeData()

insertStatement = rbdms.generateInsertStatement()
    



#get the save path

selectedPath = FileBrowser.setSaveLocation()

savePath = f"{selectedPath}\Insert Statement.txt"

# # create the output file 

outPut =  open(savePath,"w")

outPut.write(insertStatement)


