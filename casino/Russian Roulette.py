from random import randint
import time
from asyncore import loop

print('welcome to RR')
print('this is a random chance game, with the odds of 1/6, and the gamble, your life')

p1 = input('player 1: ')
p2 = input('player 2: ')

x = input(p1 + "'s choice:(1-6)? ")
y = input(p2 + "'s choice:(1-6)? ")

if x == y:
    print('there is already a bullet there')
    exit()

elif int(x) > 6:
    print('there are only 6 bullet holes')
    exit()

elif int(y) > 6:
    print('there are only 6 bullet holes')
    exit()

z = [int(x), int(y)]
count2 = 1
c = 10

while int(x) != c:
    if (count2 % 2) == 0:
        print(p2 + "'s turn")
        print('spinning barrel...')
        time.sleep(2)
        if randint(1, 6) in z:
            print('hit!')
            print(p2 + ' loses!')
            break

        else:
            print('miss!')
            print(' ')
            count2 = count2 + 1
            continue

    else:
        print(p1 + "'s turn")
        print('spinning barrel...')
        time.sleep(2)
        if randint(1, 6) in z:
            print('hit!')
            print(p1 + ' loses!')
            break

        else:
            print('miss!')
            print(' ')
            count2 = count2 + 1
            continue

loop()


