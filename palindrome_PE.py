#palindrome
master_list = []
for i in range(800,999):
    for j in range(800,999):
        master_list.append(i * j)

for number in master_list:
    check = str(number)
    if check[0] == check[5] and check[1] == check[4] and check[2] == check[3]:
        palindrom = check
        
print (palindrom)