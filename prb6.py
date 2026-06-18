mark = int(input("enter ur marks"))
if(mark<=100 and mark >= 90):
    grade ="ex"
elif(mark < 90 and mark >= 80):
    grade ="A"
elif(mark < 80 and mark >= 70):
    grade ="A"
elif(mark <70 and mark >= 60):
    grade ="B"
elif(mark <60 and mark >= 50):
    grade ="C"
elif(mark <50 ):
    grade ="fail"
print("your grade is",grade)