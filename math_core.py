class MathCore:

    def __init__(self, operation):
        self.operation=operation
        self.solution=""
        self.__transformation()
        self.__solve()

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
    ######################################################################
    Checking if a number is floating. Returning the appropriate rounding.
    ######################################################################
    '''
    def __decimal_rows(self):
        if float(self.solution) % 1 == 0:
            self.solution=int(self.solution)
        else:
            self.solution=round(self.solution,6)

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
            if i>0 and self.operation[i]=="(":
                if self.operation[i-1]==")" or self.__is_integer(self.operation[i-1]):
                    self.operation=self.operation[0:i] + "*" + self.operation[i:]
            elif self.__is_integer(self.operation[i]):
                if i>0 and self.operation[i-1]==")":
                    self.operation=self.operation[0:i] + "*" + self.operation[i:]

    '''
    ######################################################################################
    The execution of operation, its transformation from string to mathematical operation. 
    Catching the divide-by-zero error.
    ######################################################################################
    '''
    def __solve(self):
        try:
            self.solution=eval(self.operation)
        except ZeroDivisionError:
            self.solution="Division by zero."
        else:
            if self.solution>1000000000:
                self.solution=">1000000000"
            elif self.solution<-1000000000:
                self.solution ="<1000000000"
            else:
                self.__decimal_rows()
                self.solution = str(self.solution)

    '''
    ##################################################################################################
    Return solution. Possible output: Numerical result, >1000000000, <1000000000 or Division by zero.
    ##################################################################################################
    '''
    def __str__(self):
        return self.solution