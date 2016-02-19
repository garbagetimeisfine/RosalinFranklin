""" this program will take a set of DNA strings, construct a profile 
matrix and return the consensus string

I will first read in the FASTA file,

then construct an array of sequences,

build the P matrix,

build the consensus string,

print the string and the p matrix"""

import pyfasta
import scipy

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_cons (2).txt")
my_seqs = list(f.values())
#this is my array of sequences
matrix = scipy.array(my_seqs)

#print(matrix.shape)
P = []
initP = [0,] * matrix.shape[1]
for i in range(4):
    P.append(initP)
P = scipy.array(P)
# this is my array of 0's  in order it will be A, C, G, T 
#print(P.shape)
#print(P[3][11])
# populates P matrix and creates consensus string
consensus = ''
for i in range(matrix.shape[1]):
    for j in range(matrix.shape[0]):
        if matrix[j][i] == "A":
            P[0][i] += 1
        elif matrix[j][i] == "C":
            P[1][i] += 1
        elif matrix[j][i] == "G":
            P[2][i] += 1
        elif matrix[j][i] == "T":
            P[3][i] += 1
    if P[0][i] >= P[1][i] and P[0][i] >= P[2][i] and P[0][i] >= P[3][i]:
        consensus += "A"
    elif P[1][i] >= P[0][i] and P[1][i] >= P[2][i] and P[1][i] >= P[3][i]:
        consensus += "C"
    elif P[2][i] >= P[1][i] and P[2][i] >= P[0][i] and P[2][i] >= P[3][i]:
        consensus += "G"
    elif P[3][i] >= P[1][i] and P[3][i] >= P[2][i] and P[3][i] >= P[0][i]:
        consensus += "T"    
   
#got the right answer now I just need to print it in the right format
Astring = "A:" + "".join(str(P[0][:]))
Astring = Astring.replace("[",' ')     
Astring = Astring.replace("]",' ')
Astring = Astring.replace("\n",' ')         

Cstring = "C:" + "".join(str(P[1][:]))
Cstring = Cstring.replace("[",' ')     
Cstring = Cstring.replace("]",' ')
Cstring = Cstring.replace("\n",' ')   

Gstring = "G:" + "".join(str(P[2][:]))
Gstring = Gstring.replace("[",' ')     
Gstring = Gstring.replace("]",' ')
Gstring = Gstring.replace("\n",' ')   

Tstring = "T:" + "".join(str(P[3][:]))
Tstring = Tstring.replace("[",' ')     
Tstring = Tstring.replace("]",' ')
Tstring = Tstring.replace("\n",' ')   


print(consensus) 
print(Astring)
print(Cstring)
print(Gstring)
print(Tstring)