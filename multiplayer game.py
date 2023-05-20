import random
import time

def gameWin(player1a,player2b):
    if player1a == player2b :
        return None
    elif player1a == 's':
        if player2b =='w':
            return False
        elif player2b == 'g':
            return True
    elif player1a == 'w':
        if player2b == 'g':
            return False
        elif player2b == 's':
            return True
    elif player1a == 'g':
        if player2b == 's':
            return False
        elif player2b == 'w':
            return True      

player1a = input ("player1 turn : snake(s) water(w) or gun(g) ")

player2b = input ("player2 turn : snake(s) water(w) or gun(g) ")
a = gameWin (player1a , player2b)

time.sleep(2)
if a  == None:
    print("tie")
elif a:
    print("player1 won")
else:
    print("player1 lose")


b = gameWin (player2b , player1a)
if b:
    print("player2 won")
else:
    print("player2 lose")
    
