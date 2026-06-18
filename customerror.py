a=int(input("enther the no"))
b=int(input("enter th no"))

if(b==0):
    raise ZeroDivisionError("u cant divide byb zero")
else:
    print(a/b)