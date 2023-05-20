import time

username = '|name|'
password = '123456'

username_input = str(input('Username: '))
password_input = input('Password: ')
username = username.replace('|name|',username_input)

letter = '|name|'
letter = letter.replace('|name|',username_input)

if username_input == username and password_input == password:
    print('Access granted for',letter)
    print('Please wait')
    time.sleep(5)
    print('Ok...')
    time.sleep(1)
    print('Loading...')
    time.sleep(1)
    print ('OK you can come inside')

elif username_input == username and password_input != password:
    print('Password incorrect')
else:
    exit()

