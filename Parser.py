import os
from  FileBrowser import FileBrowser


#pareser converts CSV files into insert statements for SQL databases (MSQL RDBMS) (currently only supports csv files)

#opens a file explorer to select the csv file 

filePath =  FileBrowser.browseFiles()

file = open( filePath ,"r")

filename =  os.path.basename(filePath)

tableName , extension = os.path.splitext(filename)



outPut =  open(f"{tableName} insert statement.txt","w")

# Read the CSV file

insertStatement =  f"INSERT INTO {tableName} Values \n"


for input in file :
    input = input.strip('\n')
    insertValue =  f"\t({input})\n"
    insertStatement += insertValue
    
#at the end add a semicolon to finish up the insert statement

insertStatement +=  ";"

outPut.write(insertStatement)
   








