# *******************Holiday homework*******************
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

print("Type 1  for addition")
print("Type 2  for subtraction")
print("Type 3  for multiplication")
print("Type 4  for division")
inp = input("---->")

if (inp == "1"):
    print(a+b)

elif(inp == "2"):
     print(a-b)

elif(inp == "3"):
     print(a*b)

elif(inp == "4"):
     print(a/b)

else:
    print("There is no such number")