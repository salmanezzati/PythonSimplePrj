


class Robot:
    def __init__(self):
        self.a = 12
        self.__b = 33

    def getVersion(self):
        return self.__getNum()
    
    def setVersion(self, version):
        self.__b = version

    def __getNum(self):
        return self.__b


myObj = Robot()
myObj.setVersion(60)
print(myObj.getVersion())
