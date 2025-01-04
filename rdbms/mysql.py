from .sql import SQL

class MySQL(SQL):
    __schema = []
    __tableName = ""
    __INSERT_STATEMENT = ""
    data = []
    __dataSnapShot = []
    __occuranceData = {}
    
    def __init__(self,tableName):
        self.__tableName = tableName
        self.__INSERT_STATEMENT = f"INSERT INTO {self.__tableName} Values \n"
        
        
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
    
    def insertIntoSpecificCols(self):
        pass
    
    def analyzeData(self):
        
        for _ in range(len(self.data[0])):
            self.__dataSnapShot.append(set())
            
        print(self.__dataSnapShot)
        
        # analyse each data row and format it for the most likely datatype option
        for column_index, column in enumerate(zip(*self.data)):
            for data in column:
                try:
                    converted_value = int(data.replace("\t", "").replace("\n", ""))
                    self.__dataSnapShot[column_index].add("number")
                except ValueError:
                    formattedData = data.lower().strip()
                    if  formattedData == "true" or formattedData == "false":
                        self.__dataSnapShot[column_index].add("bool")
                    self.__dataSnapShot[column_index].add("string")
                    
                
        print(self.__dataSnapShot)
        
        
        # for column_index, column in enumerate(zip(*self.data)):
            
            
                
        