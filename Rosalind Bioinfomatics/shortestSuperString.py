""" 
NOT CURRENTLY WORKING   
a program to assemble a genome, more or less

a set of up to 50 strings are given, we know they are all from the 
same DNA strand. That they match another string by at least half their length.

plan. 

read all strings into python.
split all strings into tuples. one half in each tuple. 
.... wait, but it's at least half not exactly half. 

how do we align... 

check all of them against eachother? A vs all check all alignments. 

regular expressions can be used to match the end of a sequence against another 
sequence? 

check the last 20 character's of a string against all other strings
when you find a hit, align the sequences and create a larger string

then take the last 20 character of that string and repeat.

then repeat using the beginning of the sequence."""

import pyfasta
import re

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_long.txt")
my_seqs = list(f.keys())

seqDict = {}
for key in range(len(my_seqs)):
    seqDict[my_seqs[key]] = (f[my_seqs[key]][:20], f[my_seqs[key]][-20:])
    
for i in range(len(my_seqs)):
    front = re.compile(r'' + seqDict[my_seqs[i]][1])
    if re.search(front, f[my_seqs[i]][:]):
        print "hi there"