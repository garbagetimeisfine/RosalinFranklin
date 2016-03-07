""" locate restriction sites. must be homodimers"""

import pyfasta
import mRNAtoAminoAcids as T
import re

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_revp (1).txt")
my_seqs = list(f.values())
for x in my_seqs:
    sequence = str(x)

#this is called bad primer becasue it returns the compliment of the string not
#the reverse compliment...
def badPrimer(primer):
    primer_dimer = ''
    for char in primer:
        if char == "G":
            primer_dimer = "C" + primer_dimer
        elif char == "C":
            primer_dimer = "G" + primer_dimer
        elif char == "A":
            primer_dimer = "T" + primer_dimer
        elif char == "T":
            primer_dimer = "A" + primer_dimer
    return primer_dimer
    
#cut by 4, 6, 8, 10, 12
cuts = [4,6,8,10,12]
for x in cuts:           
    for i in range(len(sequence) - (x-1)):
        if sequence[i:i + x] == badPrimer(sequence[i:i + x]):
            stringyprint = str(i + 1) + " " + str(x)
            print(stringyprint)
    
