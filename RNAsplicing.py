import pyfasta
import mRNAtoAminoAcids as T

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_splc (1).txt")
my_seqs = list(f.values())
sequence = []
for x in my_seqs:
    sequence.append(str(x))
my_seq = max(sequence, key=len)
for x in sequence:
    if x != my_seq:
        my_seq = my_seq.replace(x,"")
my_seq = my_seq.replace("T","U")        

print(T.codon_to_protein(T.word_slice(my_seq)))