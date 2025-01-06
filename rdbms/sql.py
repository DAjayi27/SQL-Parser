from abc import ABC, abstractmethod
import numpy as np

class SQL(ABC):
    
    __schema = []
    __tableName = ""
    data = []
    __dataSnapShot = []
    __occurrenceData = {}
    
    def __init__(self,tableName):
        self.__tableName = tableName
    
    
    @abstractmethod
    def insertIntoSpecificCols():
        pass
    
    
    def getTableName(self):
        return self.__tableName
    
    def setTableName(self,tableName):
        self.__tableName = tableName
    
    def getSchema(self):
        return self.__schema
    
    def setSchema(self, schema):
        self.__schema = schema
        
    def insertInto(self,inputArray):
        self.data.append(inputArray)
    
    def analyzeData(self):
        
        # initialize set data an occurrence data
        self.intializeOccurrenceData()
            
        
        # analyse each data row and format it for the most likely datatype option
        self.takeDataSnapshot()
                
        # Fomart array to allow for column by column traversal, which is much easier 
        columnFormattedArray = np.array(list(zip(*self.data)),dtype=object)
        
         
        self.formatData(columnFormattedArray)
                
        
        if len(columnFormattedArray) > 1:    
            self.data = list(zip(*columnFormattedArray))
        else:
            self.data = list(*columnFormattedArray)

    def formatData(self, columnFormattedArray):
        for column_index in range(len(columnFormattedArray)):
            column = columnFormattedArray[column_index]
            
            selectedType = ""
            
            
            
            max_value = max(self.__occurrenceData[column_index].values())

            keys_with_max_value = [key for key, value in self.__occurrenceData[column_index].items() if value == max_value]
           
          
            
            # The only situation there there is more than one key with the max value is in the case of 
            # number and boolean (eg the entire col is just 1 and 0, in that case its most likely a bool)
            
            if (len(keys_with_max_value) < 1):
                raise ValueError("invalid values in keys_with_max_value")
            elif (len(keys_with_max_value) == 1):
                selectedType = keys_with_max_value[0]
            elif( len(keys_with_max_value) == 2 and "bool" in keys_with_max_value ):
                selectedType = "bool"
            else:
                # This shouldn't happen keys_with_max_value should only have 2 values when bool is one of them
                raise ValueError("Invalid: bool should be in keys_with_max_value the list.")
            
            for index in range(len(column)):
                data = column[index]
                column[index] = self.__convertData(selectedType,data)

    def takeDataSnapshot(self):
        for column_index, column in enumerate(zip(*self.data)):
            for data in column:
                try:
                    converted_value = int(data.replace("\t", "").replace("\n", ""))
                    
                    if ( converted_value == 1 or converted_value == 0 ):
                        self.__dataSnapShot[column_index].add("bool")
                        self.__occurrenceData[column_index]["bool"]+=1
                    
                    self.__dataSnapShot[column_index].add("number")
                    self.__occurrenceData[column_index]["number"]+=1
                except ValueError:
                    formattedData = data.lower().strip()
                    if  formattedData == "true" or formattedData == "false":
                        self.__dataSnapShot[column_index].add("bool")
                        self.__occurrenceData[column_index]["bool"]+=1
                    else:
                        self.__dataSnapShot[column_index].add("string")
                        self.__occurrenceData[column_index]["string"]+=1

    def intializeOccurrenceData(self):
        for i in range(len(self.data[0])):
            self.__dataSnapShot.append(set())
            self.__occurrenceData.update(
                {
                    i : { "bool" : 0, "number" : 0,"string" : 0}
                }
            )
    
    
    def __convertData(self, convertType,data):
        if convertType == "bool":
            return bool(data)
        elif convertType == "string":
            # remove any problematic characters and return the string
            return str(data).strip().strip('"').lstrip("\t")
        elif convertType == "number":
            return float(data)
        
    def generateInsertStatement(self,formattedOut):
        
        for i,row in enumerate(self.data) :
            
            formatted = []

            for val in row:
                if isinstance(val,str) and val.lower() != "null":
                    formatted.append(f"'{val.replace("'", "\\'")}'")
                else:
                    formatted.append(str(val))

            joined  = ",".join(formatted)
            
            if i < len(self.data) - 1:
                out = f"\t({joined}),\n"
            else:
                out = f"\t({joined})\n"
                    
            formattedOut += out
        
        formattedOut+=";"
        
        return formattedOut
    