"""GRAPH THEORY BITCHES

We're creating a directed graph, out of strings. X connects to Y 
if and only if there is an overlapping sequence that includes the end of 
X and the beginning of Y 

Plan, 
Itterate through the FASTA file 
create a dictionary
Keys = sting name
values = (start 3 letters, end 3 letters)

Itterate through the dictionary, see if the end 3 match with any start 3
if so create a directed edge. 

return these directed edges"""

import pyfasta
import scipy

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_grph (1).txt")
my_seqs = list(f.keys())
seqDict = {}
graphlist = ""
print(my_seqs[1])
for key in range(len(my_seqs)):
    seqDict[my_seqs[key]] = (f[my_seqs[key]][:3], f[my_seqs[key]][-3:])

for string in seqDict:
    for Bstring in seqDict:
        if seqDict[string][1] == seqDict[Bstring][0] and string != Bstring:
            graphlist += string + " " + Bstring + "\n"
print(graphlist)
    

