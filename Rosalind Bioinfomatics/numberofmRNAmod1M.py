""" this program takes in an amino acid sequence
and calculates the number of possible mRNA sequences it could have come from
modulo 1,000,000 

note the multiplication by 3 at the end for the three stop codons,

and the -1 in the range call, is to avoid the newline character at the end of the string"""

p = open("C:/Users/Patrick/Downloads/rosalind_mrna (1).txt")
protein = p.read()
p.close
#protein = "MA"
numCodon = {"A" : 4, "C" : 2, "D" : 2, "E" : 2, "F" : 2, 
    "G" : 4, "H" : 2, "I" : 3, "K" : 2, "L" : 6, "M" : 1,
    "N" : 2, "P" : 4, "Q" : 2, "R" : 6, "S" : 6, "T" : 4,
    "V" : 4, "W" : 1, "Y" : 2}
    
    # multiply by 3 for stop codon. 
poss = 1
for i in range(len(protein) - 1):
    poss = (poss * numCodon[protein[i]]) % 1000000
poss = (poss * 3) % 1000000
print(poss)