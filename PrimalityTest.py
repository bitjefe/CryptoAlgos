
import random

def isProbablyPrime(p):
    for i in range(0,20):
        a = random.randint(2, p-2)
        if pow(a, p-1, p) != 1:
            return False
    return True

randomNumbersGenerated = 0;

for i in range(0,16):
    loopCountTilPrime = 0;
    randomNumbersGenerated+=1;
    while True:
        rand = random.randint(pow(2,30), pow(2,31))
        isProbablyPrime(rand)
        loopCountTilPrime+=1
        if(isProbablyPrime(rand) == True):
            break
        
    print("The random prime number = ", rand)
    print("Number of loops until prime found = ", loopCountTilPrime)
    print("")

print("Random prime numbers generated = ", randomNumbersGenerated)
