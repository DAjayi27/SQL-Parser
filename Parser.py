

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




for input in file :
    input = input.strip('\n')
    inputArray = input.split(",")
    rbdms.insertInto(inputArray)
    insertValue =  f"\t({input})\n"
    
rbdms.analyzeData()
    
# #at the end add a semicolon to finish up the insert statement

# insertStatement +=  ";"

# #get the save path

# selectedPath = FileBrowser.setSaveLocation()

# savePath = f"{selectedPath}\{tableName} insert statement.txt"

# # create the output file 

# outPut =  open(savePath,"w")

# outPut.write(insertStatement)


   








