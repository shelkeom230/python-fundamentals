# OOP 

class student:
    __id=0
    __name=None
    __branch=None

    def __init__(self,id,name,branch):
        self.__id=id
        self.__name=name
        self.__branch=branch
    
    def setid(self,id):
        self.__id=id
    
    def getid(self):
        return self.__id
    
    def setname(self,name):
        self.__name=name
    
    def getname(self):
        return self.__name
    
    def setbranch(self,branch):
        self.__branch=branch

    def getbranch(self):
        return self.__branch

obj=student(50,"omkar","cse")
obj.setid(51)
print(obj.getbranch())
print(obj.getid())