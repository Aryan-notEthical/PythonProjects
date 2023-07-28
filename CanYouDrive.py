age = int(input("Please enter your age"))
if(age == 18):
    print("Your age is 18 you cannot drive")
elif(age > 6 and age > 18 and age < 100):
    print("You can drive")
elif(age > 100):
    print("how are you even alive!?")
else:
    print("Sit at your home!")