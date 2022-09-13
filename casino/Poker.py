from random import randint
from asyncore import loop

deck1 = [randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11)]
deck2 = [randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11)]

print(deck1)
x = input('swap or fold? ')

while x == 'swap':
    if x == 'swap':
        y = input('swap which one? ')
        if int(y) in deck1:
            deck1.remove(int(y))
            deck1.append(randint(1, 11))
            print(deck1)
            x = input('swap or fold? ')

loop()

p = sum(deck1)
q = randint(14, 21)

if int(p) > 21:
    print('you lose')
    print('your deck: ' + str(p))
    print('opponent deck: ' + str(q))
    exit()

elif int(q) > 21:
    print('you win')
    print('your deck: ' + str(p))
    print('opponent deck: ' + str(q))
    exit()

elif p > q:
    print('you win')
    print('your deck: ' + str(p))
    print('opponent deck: ' + str(q))
    exit()

elif q > p:
    print('you lose')
    print('your deck: ' + str(p))
    print('opponent deck: ' + str(q))
    exit()

elif p == 21:
    print('you win')
    print('your deck: ' + str(p))
    print('opponent deck: ' + str(q))
    exit()

elif q == 21:
    print('you lose')
    print('your deck: ' + str(p))
    print('opponent deck: ' + str(q))
    exit()
