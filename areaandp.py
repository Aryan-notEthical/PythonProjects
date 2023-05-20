a = int(input("Enter the lenght"))
b = int(input("Enter the breath"))
c = input("Type 1 to find area and 2 for perimeter")
if(c=="1"):
    area = a*b
    print("The area is",area)
elif(c=="2"):
    perimeter = (a+b) * 2
    print("The  perimeter is", perimeter)
else:
    print("Plz ")
    