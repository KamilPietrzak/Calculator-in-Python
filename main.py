from build_operation import BuildOperation as Build
from math_core import MathCore as Solution

if __name__=='__main__':
    print(eval("(2+2)*(2+2)"))
    x=Build()
    x.addChar("(")
    x.addChar("2")
    x.addChar("+")
    x.addChar("2")
    x.addChar(")")
    x.addChar("*")
    x.addChar("(")
    x.addChar("2")
    x.addChar("+")
    x.addChar("2")
    x.addChar(")")
    print(x)
    print(Solution(str(x.__repr__()[1])).solution)



