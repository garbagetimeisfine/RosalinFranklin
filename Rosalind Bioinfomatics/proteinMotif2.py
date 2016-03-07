""" this fucked up pice of code with throw an error if you run it twice in a row.

between runs shut down python completely and delete the data.txt.flat file.

it also abrevieates protein ID's so they have to be updated by hand"""

import pyfasta
import re

#opens the .txt file as FASTA so I can analyze it. 
f = pyfasta.Fasta("C:/Users/Patrick/Documents/Python/RosalinFranklin/Rosalind Bioinfomatics/data.txt")
my_seqs = list(f.values())
num_seqs = list(f.keys())

Ngly = re.compile(r"(?=(N[^P][ST][^P]))")
namefind = re.compile(r"\|(.*)\|")

for i in range(len(num_seqs)):
    isthere = re.finditer(Ngly,str(my_seqs[i]))
    if isthere != None:
        Title = re.search(namefind, num_seqs[i])
        print(str(Title.group())[1:-1])
        #print(isthere.group())
        loc = ""
        for match in isthere:
            loc += str(match.start() + 1)
            loc += " "
        print(loc)