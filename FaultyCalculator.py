num1 = int(input("first number: "))
num2 = int(input("second number: "))
print("Select your operation")
print("Type 1 for Addition")
print("Type 2 for Subtraction")
print("Type 3 for Multiplication")
print("Type 4 for Divition")
opr = int(input("Operation: "))
if(num1 == 56):
    if(num2 == 6):
        if(opr == 4):
            print("Answer: 4")
            exit()

if(num1 == 56):
    if(num2 == 9):
        if(opr == 1):
            print("Answer: 77")
            exit()

if(num1 == 45):
    if(num2 == 3):
        if(opr == 3):
            print("Answer: 555")
            exit()
            

if(opr == 1):
    print(num1+num2)
elif(opr == 2):
    print(num1-num2)
elif(opr == 3):
    print(num1*num2)
elif(opr == 4):
    print(num1/num2)
