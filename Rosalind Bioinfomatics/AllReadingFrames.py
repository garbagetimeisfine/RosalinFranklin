"""Alright now Ya'll 

this thing is ugly. But it finally worked. It has a few parts

1. import pyfasta, pull the sequence out of the data file we download
2. create the reverse compliment strand. I stole code from a primer
    dimer seq program that I had already written
3. slice both the sense and the RC strand into codon's basicaly split it by 3's 
    three times each at a different starting point. (also stolen code)
4. Translate those strands into amino acid sequences. (also stolen, both this and
    word slice are from an mRNA to amino acid sequence program) 
5. regular expressions are used to search the strings for the following pattern
    A capitol M followed by 0 to many repeats of anything until a space is encountered.
    These correspond to Methanianine followed by other acids, until a stop codon is translated.
    The codon translation program puts in spaces for stop codons. 
6. then you have to go in by hand to remove duplicates... I could have coded this but the only 
    duplicates are short 1 or two letter sequences.
    
    anywho. that's how you get all possible protein sequences out of a DNA sequence.
    
    it's not the most efficent, it translates the whole sequence and then looks for possilble 
    polypeptides. As opposed to checking the DNA and only translating the logical ones.
    
    it's also not written nicely in dynamic progrmaing with smaller programs to pull out and use later.
    which came in handy with the mrna to amino acids example. I should start cutting up my programs like that...
    anywho. here it is done.
    
    On to the next project""" 

import pyfasta
import mRNAtoAminoAcids as T
import re

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_orf (3).txt")
my_seqs = list(f.values())
#ugly.... takes the DNA and makes it RNA because my amino acid program only takes RNA
DNA = str(my_seqs[0]).replace("T", "U")

""" this is code for the reverse compliment of a sequence stolen from a
primer dimer code """
primer = DNA
primer_dimer = ''
for char in primer:
    if char == "G":
        primer_dimer = "C" + primer_dimer
    elif char == "C":
        primer_dimer = "G" + primer_dimer
    elif char == "A":
        primer_dimer = "U" + primer_dimer
    elif char == "U":
        primer_dimer = "A" + primer_dimer
rcDNA = primer_dimer

# now we have our DNA sequence and our reverse compliment DNA sequence

# make 6 word slice lists and translate into amino acids. 

DNA1 = T.word_slice(DNA)
DNA2 = T.word_slice(DNA[1:])
DNA3 = T.word_slice(DNA[2:])
rcDNA1 = T.word_slice(rcDNA)
rcDNA2 = T.word_slice(rcDNA[1:])
rcDNA3 = T.word_slice(rcDNA[2:])

AAlist = []
AAlist.append(T.codon_to_protein(DNA1))
AAlist.append(T.codon_to_protein(DNA2))
AAlist.append(T.codon_to_protein(DNA3))
AAlist.append(T.codon_to_protein(rcDNA1))
AAlist.append(T.codon_to_protein(rcDNA2))
AAlist.append(T.codon_to_protein(rcDNA3))

Mtoend = re.compile(r'(?=(M[^\s]*\s))') 
for string in range(len(AAlist)):
    hits = re.finditer(Mtoend, AAlist[string])
    for matches in hits:
        print matches.group(1)



"""    
match2 = re.findall(Mtoend, AAlist[0])

if match2:
    print('There are ' + str(len(match2)) + ' matches')
    print('They are: ' + str(match2))
            
j = 1
for i in range(len(DNA1)):
    if DNA1[i] == "AUG":
        protein = []
        protein.append(DNA1[i])
        while DNA1[i + j] != "UAA" and DNA1[i + j] != "UGA" and DNA1[i + j] != "UAG":
            protein.append(DNA1[i + j])
            j += 1
        j = 1
        print(T.codon_to_protein(protein))

j = 1
for i in range(len(DNA2)):
    if DNA2[i] == "AUG":
        protein = []
        protein.append(DNA2[i])
        while DNA2[i + j] != "UAA" and DNA2[i + j] != "UGA" and DNA2[i + j] != "UAG":
            protein.append(DNA2[i + j])
            j += 1
        j = 1
        print(T.codon_to_protein(protein))
        
j = 1
for i in range(len(DNA3)):
    if DNA3[i] == "AUG":
        protein = []
        protein.append(DNA3[i])
        while DNA3[i + j] != "UAA" and DNA3[i + j] != "UGA" and DNA3[i + j] != "UAG":
            protein.append(DNA3[i + j])
            j += 1
        j = 1
        print(T.codon_to_protein(protein))
        
j = 1
for i in range(len(rcDNA1)):
    if rcDNA1[i] == "AUG":
        protein = []
        protein.append(rcDNA1[i])
        while rcDNA1[i + j] != "UAA" and rcDNA1[i + j] != "UGA" and rcDNA1[i + j] != "UAG":
            protein.append(rcDNA1[i + j])
            j += 1
        j = 1
        print(T.codon_to_protein(protein))
        
j = 1
for i in range(len(rcDNA2)):
    if rcDNA2[i] == "AUG":
        protein = []
        protein.append(rcDNA2[i])
        while rcDNA2[i + j] != "UAA" and rcDNA2[i + j] != "UGA" and rcDNA2[i + j] != "UAG":
            protein.append(rcDNA2[i + j])
            j += 1
        j = 1
        print(T.codon_to_protein(protein))
        
j = 1
for i in range(len(rcDNA3)):
    if rcDNA3[i] == "AUG":
        protein = []
        protein.append(rcDNA3[i])
        while rcDNA3[i + j] != "UAA" and rcDNA3[i + j] != "UGA" and rcDNA3[i + j] != "UAG":
            protein.append(rcDNA3[i + j])
            j += 1
        j = 1
        print(T.codon_to_protein(protein))"""
