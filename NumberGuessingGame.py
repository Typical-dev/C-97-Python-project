import random
TitleString='Number guessing game:'
print(TitleString)

chances=0
number=random.randint(1,9)

while chances<5:


    InputNumber=int(input('Enter your number(from 1 to 9)'))
    print(InputNumber)


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
