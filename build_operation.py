class BuildOperation:

    def __init__(self, operation=""):
        self.operation=operation
        #self.math_signs=["+","-",chr(215),chr(247)]

    #def __checkBrackets(self):
    #    return True if self.operation.count("(")==self.operation.count(")") else False

    def addChar(self, char):
        self.operation+=str(char)

    def delChar(self):
        self.operation=self.operation[0:-1]

    def clean(self):
        self.operation=""

    def returnEndValue(self):
        return self.operation.replace(chr(247),"/").replace(chr(215),"*").replace(",",".")

