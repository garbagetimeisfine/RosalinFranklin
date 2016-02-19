"""smallest number divisable by 1 - 20 evenly """

indivisable = True
num = 2520
while indivisable:
    if (num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and 
        num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and
        num % 10 == 0 and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and
        num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and
        num % 18 == 0 and num % 19 == 0 and num % 20 == 0):
        indivisable = False
        answer = num
    num += 20
print(answer)