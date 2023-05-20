from time import sleep
def start():
    print("\t\t              i")
    sleep(.25)
    print("\t\t             i  i")
    sleep(.25)
    print("\t\t            i  i  i")
    sleep(.25)
    print("\t\t           i  i  i  i")
    sleep(1)
    print("\t            :---------------------:")
    print("\t            :    Happy    ++++    :")
    sleep(1)
    print("\t            :    ++++     Birthday:")
    sleep(1)
    letter0 = "\t            :    <name>    ++++:   "
    letter0 = letter0.replace("<name>",a1)
    print(letter0)                                   
    print("\t       /__________________________________\ ")
    sleep(1)
    print("\t       :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:")
    sleep(.25) 
    print("\t       :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:")
    sleep(.25)
    print("\t       :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:")
    sleep(.25)
    print("\t  ――――――――――――――――――――――――――――――――――――――――――――――――――")
    sleep(.25)
    print("         :                                                 : ")
    sleep(.25)                                       
    print("         :                                                 : ")
    sleep(.25)
    print("         :                                                 : ")
    sleep(.25)
    print("         :                                                 : ")
    sleep(.25)
    print("         :                                                 : ")
    sleep(.25)
    sleep(.25)
    print("         ____________________________________________________")
    print("Loading......")
    sleep(1)
    print("A message to you.....")
    sleep(4)

    letter = " HAPPY BRITHDAY MAY GOD BLESS YOU <name> !!! :)"
    
    letter = letter.replace("<name>",a1)
    print(letter)
    sleep(9999)
    print("BYE")
    
    
    


a1 = input("What is your name?")
a = input("1.TYPE wish \n2.PRESS 'ENTER' KEY\n(ELSE TYPE 'QUIT' TO QUIT)\n\n:").lower()
    
if (a == "wish"):
    start()

else:
    print("BYE!!")
