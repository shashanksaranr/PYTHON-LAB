def r2d(rs):
    roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    romanBack=list(rs)[::-1]
    value=0
    rightVal=roman_dict[romanBack[0]]

    for numeral in romanBack:
        leftVal=roman_dict[numeral]

        if leftVal<rightVal:
            value-=leftVal

        else:
            value+=leftVal
        rightVal=leftVal
    return value
rs=input("Enter a roman number:")
print(r2d(rs))