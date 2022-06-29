import math

class MathCore:

    def __init__(self, operation):
        self.operation=operation

    '''
    #####################################################################
    Checking whether the given value can be a variable of the int type.
    True - The given value can be the int type.
    False - The given value can't be the int type.
    #####################################################################
    '''
    def __is_integer(self, char):
        try:
            int(char)
        except ValueError:
            return False
        else:
            return True

    '''
    ###################################################################
    Convert and remove invalid entries for Python, but valid for math. 
    For example:
    2 (2 + 2) -> 2 * 2 (2 + 2)
    (2 + 2) (2 + 2) -> (2 + 2) * (2 + 2)
    ###################################################################
    '''
    def __transformation(self):
        if self.operation[-1]==" ":
            self.operation=self.operation[1:]
        for i in range(len(self.operation)):
            if i !=0 and self.operation[i]=="(":
                if self.operation[i-1]==")" or self.__is_integer(self.operation[i-1]):
                    self.operation=self.operation[0:i-1] + "*" + self.operation[i:]


    def __solution(self):
        pass


    def __str__(self):
        return self.__solution()