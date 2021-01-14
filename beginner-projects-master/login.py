"""
Beginner Python Project using input, print, and conditionals by Gabriel Camejo

 
Twitter @iGabrieLabs : https://twitter.com/iGabrieLabs 
Website: https://www.kylieying.com
Github: https://www.github.com/GabrieLabs


"""

import time

username = 'kylie'
password = 'secretpassword'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access granted')
    print('Please wait')
    time.sleep(5)
    print('Ok... Loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Alright you have security clearance. Pulling up the secret mainframe.')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('You might wanna check both fields...')
