from asyncore import loop
from random import randint
import time
import random

name1 = input('name1: ')
name2 = input('name2: ')
inj = [name1 + ' coughs out blood', name1 + ': maybe i shouldnt hold back anymore...', name1 + ' spits on ' + name2, name1 + ' is bleeding', name1 + ' pants']
inj2 = [name2 + ': maybe i shouldnt hold back anymore...', name2 + ' coughs out blood', name2 + ' spits on ' + name1, name2 + ' is bleeding', name2 + ' pants']

#middle
print(' ')

#for name1
strenght1 = randint(10, 20)
dur1 = randint(5, 10)
hp1 = randint(50, 100)
print(name1 + ': ')
print('health: ' + str(hp1))
print('strenght: ' + str(strenght1))
print('durability: ' + str(dur1))

#middle
print(' ')

#for name2
strenght2 = randint(10, 20)
dur2 = randint(5, 10)
hp2 = randint(50, 100)
print(name2 + ': ')
print('health: ' + str(hp2))
print('strenght: ' + str(strenght2))
print('durability: ' + str(dur2))

#middle
print(' ')
time.sleep(5)
counter = 1

while hp1 or hp2 > 0:
    counter = counter

    if randint(1, 2) == 2:
        strenght1 * 2

    if randint(1, 2) == 1:
        strenght2 * 2

    x2 = hp2 - strenght1 + dur2
    x1 = hp1 - strenght2 + dur1
    print('turn ' + str(counter))
    print(name1 + ': ' + str(x1))
    hp1 = x1
    print(name2 + ': ' + str(x2))
    hp2 = x2

    if hp1 <= 0:
        print(name2+ " gets to keep " + name1)
        break

    if hp2 <= 0:
        print(name1+ " gets to keep " + name2)
        break

    counter = counter + 1
    print(random.choice(inj))
    print(random.choice(inj2))
    #middle
    print(' ')
    time.sleep(5)
loop
