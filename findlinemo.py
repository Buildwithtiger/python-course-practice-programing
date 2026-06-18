
with open("log.txt") as f:
    lines= f.readlines()
lineno =1  
for line in lines:    
  if("shweta" in line):
    print(f"yes she is present in linr no {lineno}")
    break
  lineno += 1
else:
 print("she is not present")