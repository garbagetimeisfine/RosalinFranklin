

def censor(text, word):
    new_list = text.split()
    print(new_list)
    index = 0
    for thing in new_list:
        if word == thing:
            new_list[index] = "*" * len(word)
            print("found it")
        index += 1
    toreturn = " ".join(new_list)
    print(toreturn)
    return toreturn
    
def count(sequence, item):
    counter = 0
    for thing in sequence:
        if thing == item:
            counter += 1
    return counter

def remove_duplicates(toomuch):
    new_list = []
    repeats = []
    for thing in toomuch:
        if count(toomuch, thing) == 1:
            new_list.append(thing)
            
        else:
            repeats.append(thing)
    if repeats:
        new_list.append(repeats[1])
    for i in range(1,len(repeats)):
        if repeats[i] != repeats[i - 1]:
            new_list.append(repeats[i - 1])
            
    return new_list

import math
def median(distribution):
    med = sorted(distribution)
    count = len(distribution)
    mid = count/2
    print(count)
    print(mid)
    if count % 2 == 0:
        a = med[count/2]
        b = med[(count/2) - 1]
        return (a + b) / 2.0
    elif count == 1:
        return med[0]
    else:
         return med[(math.ceil(count/2))]

def print_grades(grades):
    for grade in grades:
        print(grade)
        

print_grades(grades)
