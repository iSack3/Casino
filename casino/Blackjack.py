from asyncore import loop
from random import randint

z = randint(2, 21)
print('your number is: ' + str(z))
x = input('fold or add? ')


if x == "add":
    y = randint(2, 21)
    s = z + randint(1, 11)
    print(s)
    while s < 21:
        x = input('fold or add? ')
        if x == "add":
            s = s + randint(1, 11)
            print(s)
            if s > 21:
                print('you lose, opposing number was ' + str(y))
                break
            
            if s == 21:
                print('you win, opposing number was ' + str(y))
                break

        if x == "fold":
            y = randint(2, 21)
            if s > y:
                print('you win')
                print('opposing number was: ' + str(y))
                break

            if s < y:
                print('you lose')
                print('opposing number was: ' + str(y))
                break
        loop()
        if s > 21:
            print('you lose, opposing number was ' + str(y))
            break
            
        if s == 21:
            print('you win, opposing number was ' + str(y))
            break


if x == "fold":
    y = randint(2, 21)
    if z > y:
        print('you win')
        print('opposing number was: ' + str(y))

    if z < y:
        print('you lose')
        print('opposing number was: ' + str(y))
