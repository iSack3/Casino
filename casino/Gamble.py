from random import randint
import random
import time

gm = ['higher', 'lower']
ON = [randint(1, 5), randint(6, 10)]
x = input('choose either ' + str(randint(1, 5)) + ' or ' + str(randint(6, 10)) + ' :')
y = random.choice(gm)
z = random.choice(ON)

if y == 'higher':
    if int(x) < 1:
        print('what')
        exit()

    if int(x) > 10:
        print('what')
        exit()

    if int(x) > int(z):
        print('selecting mode...')
        time.sleep(3)
        print('mode chosen: higher')
        print('opponent selecting number...')
        time.sleep(3)
        print('opponent selected: ' + str(z))
        print('you win')

    if int(x) == int(z):
        print('selecting mode...')
        time.sleep(3)
        print('mode chosen: higher')
        print('opponent selecting number...')
        time.sleep(3)
        print('opponent selected: ' + str(z))
        print('tie')

    if int(x) < int(z):
        print('selecting mode...')
        time.sleep(3)
        print('mode selected: higher')
        print('opponent selecting number...')
        time.sleep(3)
        print('opponent selected: ' + str(z))
        print('you lose')

if y == 'lower':
    if int(x) < 1:
        print('what')
        exit()

    if int(x) > 10:
        print('what')
        exit()

    if int(x) < int(z):
        print('selecting mode...')
        time.sleep(3)
        print('mode selected: lower')
        print('opponent selecting number...')
        time.sleep(3)
        print('opponent selected: ' + str(z))
        print('you win')

    if int(x) == int(z):
        print('selecting mode...')
        time.sleep(3)
        print('mode selected: lower')
        print('opponent selecting number...')
        time.sleep(3)
        print('opponent selected: ' + str(z))
        print('tie')

    if int(x) > int(z):
        print('selecting mode...')
        time.sleep(3)
        print('mode selected: lower')
        print('opponent selecting number...')
        time.sleep(3)
        print('opponent selected: ' + str(z))
        print('you lose')
