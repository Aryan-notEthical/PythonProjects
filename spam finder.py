Text = str(input("Enter a text"))
spam = False
if ("play game to win money" in Text):
    spam = True
elif("Go to this wesite to win a car" in Text):
    spam = True
elif("Play music win 2,000,00" in Text):
    spam = True
elif("Congratulations You won a $1,000 walmart gift card"in Text):
    spam = True
if(spam):
    print("It is a spam")
else:
    print("It is not a spam ")
