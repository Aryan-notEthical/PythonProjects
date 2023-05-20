
letter = ''' Dear  <|NAME|>
Good morning this is to be inform you that you are selected for the job
in Google. Date for joining 31/6/2021 click on this link for a meeting https://www.youtube.com/watch?v=dQw4w9WgXcQ.

'''

name = input("Enter your name")
letter = letter.replace("<|NAME|>",name)
print(letter)