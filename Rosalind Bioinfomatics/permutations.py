"""create permutations"""
import itertools
import math

N = 5
one = itertools.permutations(range(1,N+1))
print math.factorial(N)
for x in one:
    x = str(x)
    x = x.replace(", "," ")
    x = x.replace("(","")
    x = x.replace(")","")
    print x