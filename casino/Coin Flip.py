from asyncore import loop
import random
import time

HOT = ['heads', 'tails']
x = input('heads or tails: ')

if x not in HOT:
    print('what?')
    exit()

print('flipping coin...')
time.sleep(1)
y = random.choice(HOT)

if x == y:
    prob = 0.5
    print('you win')
    print('the probabilty is ' + str(prob))    
    while x == y:
        prob = prob * 0.5
        y = random.choice(HOT)
        x = input('heads or tails: ')
        
        if x not in HOT:
            print('what?')
            exit()

        print('flipping coin...')
        time.sleep(1)

        if x == y:
            print('you win')
            print('the probabilty is ' + str(prob))

        else:
            print('GG, you lost, the probability was ' + str(prob))
            break

    loop()

else:
    print('GG, you lost')
    print('the probability was 0.5')
