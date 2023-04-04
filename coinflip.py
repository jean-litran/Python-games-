import random
print("I will flip a coin 1000 times. Guess how many times it will come up! Heads (Press enter to begin)")
input()
filps = 0
heads = 0
#mecanismo pra jogar a moeda
while flips < 1000:
    if random.randint(0,1) == 1: 
        heads = heads +1
        flips = flips + 1
    if flips == 900:
        print("900 flips an there have been" +str(heads) + 'Heads')
    if flips == 100:
                print('At 100 tosses, heads has come up' +str (heads) +'times so far')
    if flips == 500:
                    print('Halfway Done and heads has come up'+str(heads)+'times.')
                    
print()
print("Out of 1000 coins tosses has came up" +str(heads)+'times')
print('Were you close!')