from build_operation import BuildOperation as Build

if __name__=='__main__':
    x = Build("123+345")
    print(x.operation)
    x.addChar(chr(215))
    x.addChar(6)
    x.addChar(chr(215))
    x.addChar(2)
    print(x.operation)
    #x.delChar()
    #x.delChar()
    #print(x.operation)
    #x.clean()
    #print("To wynik czyszczenia: ", x.operation)
    x.addChar("(")
    x.addChar(")")
    print(x.check())
    print(x.returnEndValue())


