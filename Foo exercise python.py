"""exercise file, Stephano U Chicago"""

def foo1(x = 7):
    return x ** 0.5

def foo2(x = 3, y = 5):
    if x > y:
        return x
    return y

def foo3(x = 2, y = 0, z = 9):
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    if x > z:
        tmp = z
        z = x
        x = tmp
    return [x, y, z]

def foo4(x = 6):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo5(x = 1729):
    d = 2
    myfactors = []
    while x > 1:
        if x % d == 0:
            myfactors.append(d)
            x = x / d
        else:
            d = d + 1
    return myfactors

def foo6(x = 25):
    if x == 1:
        return 1
    return x * foo6(x-1)

def foo7(x = 100):
    myp = [2]
    for i in range(3, x + 1):
        success = False
        for j in myp:
            if i % j == 0:
                success == True
                break
        if success == False:
            myp.append(i)
    return myp

def PrimeList(x = 10002):
    primelist = [1]
    count = 1
    i = 1
    while i <= 2000000:
        if len(foo5(i)) == 1:
            primelist.append(i)
            count += 1
            i += 1
        i += 1
    return primelist

primelist10k = PrimeList()

def SumPrimes(x = 1000):
    sumlist = []
    primepair = []
    total = 0
    for i in range(x):
        for prime in primelist10k:
            while prime < (i * 2):
                checker = (i * 2) - prime
                if checker in primelist10k:
                    primepair = [prime, checker]
                    sumlist.append(primepair)
                    total = total + (prime + checker)
    print(total)
    return sumlist
        
        
"""
print(foo1())
print(foo2())
print(foo3())
print(foo4())
print(foo5())
print(foo6())
print(foo7())"""
                
