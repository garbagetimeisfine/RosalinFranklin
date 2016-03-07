""" this program is to find the first 'triangle number' with 500 possible divisors """
import math

triangle = sum(range(100))
factors = []
count = 100

def factor(x = 1729):
    d = 2
    myfactors = []
    while x >= d:
        if x % d == 0:
            myfactors.append(d)
            d += 1
        else:
            d = d + 1
    return myfactors

factor500 = False
while not factor500:
    count += 1
    triangle = triangle + count 
    factor500 = len(factor(triangle)) >= 500

print(triangle)
print(len(factor(triangle)))

