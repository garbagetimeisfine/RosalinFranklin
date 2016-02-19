""" this program will take a set of DNA strings, construct a profile 
matrix and return the consensus string

I will first read in the FASTA file,

then construct an array of sequences,

build the P matrix,

build the consensus string,

print the string and the p matrix"""

import pyfasta
import scipy

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_cons.txt")
my_seqs = list(f.values())
#print my_seqs[0]
#print my_seqs[1]

matrix = scipy.array(my_seqs)

print(matrix.shape)


#seq1 = f[my_seqs[0]][:]

#print seq1[:40]