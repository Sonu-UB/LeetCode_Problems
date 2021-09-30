
def romanTointeger(s):
    s=s.replace("IV","IIII").\
                replace("IX","VIIII").\
                replace("XL","XXXX").\
                replace("XC","LXXXX").\
                replace("CD","CCCC").\
                replace("CM","DCCCC")
    result=0
    for i in s:
        if i=="I":
            result +=1
        elif i=="V":
            result +=5
        elif i=="L":
            result +=50
        elif i=="X":
            result +=10 
        elif i=="C":
            result +=100
        elif i=="D":
            result +=500
        elif i=="M":
            result +=1000
        else:
            return "not correct symbol"
    return result