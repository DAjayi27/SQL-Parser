from .sql import SQL
import numpy as np

class MySQL(SQL):


    __INSERT_STATEMENT = ""
    
    
    def __init__(self,tableName):
        super().__init__(tableName)
        self.__INSERT_STATEMENT = f"INSERT INTO {tableName} Values \n"
        
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
    

        

    
    def generateInsertStatement(self):
        
        
        formattedOut = self.__INSERT_STATEMENT
        
        return super().generateInsertStatement(formattedOut)
        
        
        
            
                
            
        
            
        
            
            
            
            
            
        
        
        
            
            
       
            
            
            
            
            
                
        