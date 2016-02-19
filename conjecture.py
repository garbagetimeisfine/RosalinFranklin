
def main():    # Find the prime number
##    def isPrime(num):
##        divisor = 2
##        while (divisor <= num / 2):
##            if (num % divisor == 0):
##                return False
##            divisor += 1
##            return True
    # Assign the range and find the sum of prime number
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

    def PrimeList(x = 1000):
        primelist = [1]
        for i in range(x):
            if len(foo5(i)) == 1:
                primelist.append(i)
        return primelist

    primelist10k = PrimeList()
    
    r1, r2 = eval(input("Enter the range of numbers: "))
 
    for even in range(r1, r2 + 1):
        if (even % 2 == 0):
            print(even)
            for a in range(1, even + 1):
                if a in primelist10k and a < even + 1:
                    for b in range(1, even + 1):
                        if b in primelist10k and b < even + 1:
                            if (a + b == even):
                                if (a <= b):
                                    print("  ","=", a, "+", b)

main()
