Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============================================================================================================== RESTART: Shell ==============================================================================================================
>>> import random
TitleString='Number guessing game:5'
print(TitleString)

chances=0
while chances<5:


    InputNumber=int(input('Enter your number(from 1 to 9)'))
    print(InputNumber)

    number=random.randint(1,9)

    if(InputNumber==number):
        print('YOU ARE CORRECT AND HAVE WON THE GAME')
        break

    elif(InputNumber<number):
        print(' YOU HAVE ENTERED A LOWER NUMBER')

    else:
        print('YOU HAVE ENTERED A HIGHER NUMBER')

    chances+=1

if(chances==5):
    print('SORRY YOUR ATTEMPTS ARE OVER YOU LOSE')
