from random import randint

x = randint(1, 5)
y = input('guess the number from 1 to 5: ')

if int(y) == x:
    print('you win')

else:
    print('you lose, number was: ' + str(x))