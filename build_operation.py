class BuildOperation:

    def __init__(self, operation="0"):
        self.operation=operation
        self.special_char=["+","-",chr(215),chr(247), ",",")","("]

    def __len__(self):
        return len(self.operation)

    def __is_integer(self, char):
        try:
            int(char)
        except ValueError:
            return False
        else:
            return True

    def __checkBrackets(self):                                                              # True==Good / False==Bad
        if self.operation.count("(")==self.operation.count(")"):
            return False, "{} razy otowrzyłeś nawias, a zamknołeś {} razy. Ilość otwrać i zamknięc nawiasów musi być taka sama.".format(str(self.operation.count("(")),str(self.operation.count(")")))
        elif "()" in self.operation:
            return False, "Wy działaniu znajduje się pusty nawias."
        else:
            return True

    def __checkChar(self, char):                                                            # True==Good / False==Bad
        if (char in self.special_char and self.operation[-1] in ["+","-",chr(215),chr(247), ","]) or (char in ["+",chr(215),chr(247),","] and self.operation[-1]=="("):
            return False
        else:
            return True

    def addChar(self, char):
        if char=="(" and self.__len__()==1:
            self.operation=self.operation.replace("0","(")
        else:
            if self.__checkChar(char):
                self.operation+=str(char)
            else:
                self.operation=self.operation[0:-1]+str(char)

    def delChar(self):
        self.operation=self.operation[0:-1]

    def clean(self):
        self.operation=""

    def __repr__(self):
        return self.operation.replace(chr(247),"/").replace(chr(215),"*").replace(",",".")

    def __str__(self):
        return self.operation

