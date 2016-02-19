# -*- coding: utf-8 -*-
import re
import pyfasta

f = pyfasta.Fasta("C:/Users/Patrick/Documents/Python/AllesinaLab-isc-e278c8656868/regex/data/Ecoli.fasta")
my_seqs = list(f.keys())

print my_seqs[0]

seq1 = f[my_seqs[0]][:]

print seq1[:40]

match = re.search(r'GATC', seq1)

print match.group()
print match.start()
print match.end()

match2 = re.findall(r'ACC[ATGC]{6}GTGC|GCAC[GATC]{6}GTT', seq1)

if match2:
    print('There are ' + str(len(match2)) + ' matches')
    print('They are: ' + str(match2))

hits = re.finditer(r'ACC[ATGC]{6}GTGC|GCAC[GATC]{6}GTT', seq1)

for matches in hits:
    print(matches.start() + 1, matches.group())
   
EcoKI = re.compile(r'ACC[ATGC]{6}GTGC|GCAC[GATC]{6}GTT')
match3 = EcoKI.findall(seq1)
print(match3)

seq2 = f[my_seqs[1]][:]
print len(seq2)

amp = re.compile(r"(AAC[AC]GGATTAGATACCC[GT]G)([ATCG]+)([CT]T[AG]AAACTCAAATGAATTGACGGGG)")
match4 = amp.findall(seq2)

if match4:
    print('There are ' + str(len(match4)) + ' matches')
    print('They are: ' + str(match4))

#verbose

pattern = r""" 
          ^          #Start of the string
          (\d{5})    #five digit sequence
          ([\s-]{1}  #group of optional parts starts with - or space
          \d{4})?    #followed by four didgets
          $          #end of string
          """
print(re.search(pattern, "60637", re.VERBOSE).group())
print(re.search(pattern, "60637 1503", re.VERBOSE).group())
print(re.search(pattern, "60637-1503", re.VERBOSE).group())
