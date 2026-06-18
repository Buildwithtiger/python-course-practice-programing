n =int(input("enter the no"))
for i in range(1,n+1):
 print(" " * (n-i),end="")
 print(" *" * (1*i-1), end="")
 print("\n")