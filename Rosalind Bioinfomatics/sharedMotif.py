""" this program takes in a FASTA format file 
it checks all the strings against eachother for common motifs
it returns the longest common motif

first string put into check against list.

itterate through the string checking all sub combinations against next string

keep only common strings.

itterate through the list of common strings against next string. 
for each common string itterate through it's sub strings for smaller common motifs.

after done. 

check list of common motifs, print out longest one."""
import re
import pyfasta
import scipy
import sets

#reads in sequences
f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_lcsm (1).txt")
my_seqs = list(f.values())
num_seqs = list(f.items())
#print(len(num_seqs))
#print(my_seqs[1])
motiflist = set([])
#print(matrix.shape)
L = []
initP = [0,] * len(my_seqs[1])
for i in range(len(my_seqs[0])):
    L.append(initP)
L = scipy.array(L)


for i in range(len(my_seqs[0])):
    for j in range(len(my_seqs[1])):
        if my_seqs[0][i] == my_seqs[1][j]:
            if i == 0 or j == 0:
                L[i][j] = 1
            else:
                L[i][j] = L[i - 1][j - 1] + 1
            if L[i][j] >= 2:
                motiflist.add(my_seqs[0][i - L[i][j] + 1 : i+1])
        else:
            L[i][j] = 0
     
for motif in motiflist.copy():
    regex = r"(?=(" + motif + "))"
    for i in range(2,len(num_seqs)):
        if re.search(regex, str(my_seqs[i])) == None:
            motiflist.discard(motif)
            break
    
print(max(motiflist, key = len))
"""





#this function checks a motif. If the motif is in the string it returns the whole value
#if the motif is not completely present it checks substrings and returns a list of matches
def checkVS(motif, sequence):
    regex = r"(?=(" + motif+ "))"
    full = re.search(regex, sequence)
    if full != None:
        return full.group()
    motifs = []
    for i in range(2,len(motif)-1):
        word = motif["""
        
        
        
        