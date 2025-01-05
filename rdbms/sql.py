from abc import ABC, abstractmethod

class SQL(ABC):
    
    @abstractmethod
    def insertInto():
        pass
    
    @abstractmethod
    def insertIntoSpecificCols():
        pass
    
    @abstractmethod
    def generateInsertStatement():
        pass