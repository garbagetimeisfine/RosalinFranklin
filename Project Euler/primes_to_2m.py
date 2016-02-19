import math

def isprime(x):
    d = 2
    while d <= math.ceil(x / 2):
        if x % d == 0:
            return False
        d += 1
    return True
    
primes = [] 
sumprime = 0
    
for x in range(1,2000001):
    if isprime(x):
        #primes.append(x)
        sumprime += x
            