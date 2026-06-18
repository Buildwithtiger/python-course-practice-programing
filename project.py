import random
n=random.randint(1,100)
a=-1
guess =0
while(a!=n):
    guess +=1
    a=int(input("enter the number"))
    if(a>n):
        print("lower number plese")
    else:
        print("higher  number plese")
print(f"you guess the in is {guess} attempts")