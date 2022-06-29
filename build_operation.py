class BuildOperation:

    def __init__(self, operation="0"):
        self.operation=operation

    def __len__(self):
        return len(self.operation)

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
    ###################################################################################################
    Checking the correctness of operation, before issuing the final version.
    Checking, if all open bracket have been closed. True - Yes, False - No. Additionally send the mes.
    ###################################################################################################
    '''
    def __checkFinale(self):
        if self.operation.count("(")!=self.operation.count(")"):
            return False, "You opened the bracket {} times and I closed it {} time. Close the remaining bracket.".format(str(self.operation.count("(")),str(self.operation.count(")")))
        else:
            return True

    '''
    ########################################################################################################
    Chcecking the correctness of operation, after add new char and return only bool type.
    Argument list:
    #1 - The appearance of two characters from the range side by side: ('-','+','chr(215)','chr(247)',',').
    #2 - Preceding a new character in the range ('+','chr(215)','chr(247)') with the character '('.
    #3 - Proceding a new character in range ('(',')') with the character ','.
    ########################################################################################################
    '''
    def __checkNewCharWithoutMes(self, char):
        if (char in ["-","+",str(chr(215)),str(chr(247)),","] and self.operation[-1] in ["-","+",str(chr(215)),str(chr(247)),","]) or (char in ["+", str(chr(215)),str(chr(247))] and self.operation[-1]=="(") or (char in ["(",")"] and self.operation[-1]==","):
            return False
        else:
            return True

    '''
    ################################################################################################################################################
    Chcecking the correctness of operation, after add new char and return bool type and mes.
    Chcecking if the new character is ',' and the length of the string is 0 or the last character in the string is not a number.
    If the new character is ')', it is checked if the number of openings is not equal to zero and that the last character in the string is not '('.
    ################################################################################################################################################
    '''
    def __checkNewCharwithMes(self, char):
        match char:
            case ",":
                if self.__len__()==1 or not(self.__is_integer(self.operation[-1])):
                    return False, "Przecinek musi być poprzedzony dowolną cyfrą."
                else:
                    return True, ""
            case ")":
                if self.operation.count("(")==0:
                    return False, "Zamknięcie nawiasu musi być poprzedzone otwarciem nawiasu."
                elif self.operation[-1]=="(":
                    return False, "Niemożna wstawiać pustych nawiasów."
                else:
                    return True, ""
            case _:
                return True, ""

    '''
    #################################################################################################################################################
    Adding a new character or replacing it after meeting the conditions of the function __checkNewCharwithMes(char) and __checkNewCharWithoutMes or 
    replacing it after meeting the exception with the first character '(' or '0'.
    #################################################################################################################################################
    '''
    def addChar(self, char):
        if (char=="(" or self.__is_integer(char)) and self.operation=="0":
            self.operation=self.operation.replace("0"," ")
            self.operation+=str(char)
        else:
            if self.__checkNewCharwithMes(char)[0] and self.__checkNewCharWithoutMes(char):
                self.operation+=str(char)
                return True, ""
            elif self.__checkNewCharwithMes(char)[0]==False:
                return False, self.__checkNewCharwithMes(char)[1]
            else:
                self.operation = self.operation[0:-1] + str(char)
                return True, ""

    '''
    #######################################
    Deleting last character in the string.
    #######################################
    '''
    def delChar(self):
        self.operation=self.operation[0:-1]

    '''
    ###################################
    Returning string to default value.
    ###################################
    '''
    def clean(self):
        self.operation="0"

    '''
    ################################################################################################
    Returning the string in its final form if meeting the conditions of the function __checkFinale.
    ################################################################################################
    '''
    def __repr__(self):
        if self.__checkFinale():
            return True, self.operation.replace(chr(247),"/").replace(chr(215),"*").replace(",",".")
        else:
            return False, self.__checkFinale()[1]

    '''
    ########################################
    Returning the string in form for user.
    ########################################
    '''
    def __str__(self):
        return self.operation[1:]

