""" this program takes an alphabet and returns
all the words possible of a given lenght in that alphabet in 'alphabetical' or
lexicagraphical order"""

import itertools
alphabet_size = 6
word_len = 3
x = range(1,alphabet_size + 1)
y = [p for p in itertools.product(x, repeat = word_len)]

alphabet = { "1": "X", "2" : "T", "3" : "C", "4" : "Q", "5" : "I", "6" : "G"}

for tup in y:
    stringy = ""
    for j in range(len(tup)):
        stringy += alphabet[str(tup[j])]
    print stringy