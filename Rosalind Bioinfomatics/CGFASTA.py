import CGcont
import pyfasta

f = pyfasta.Fasta("C:/Users/Patrick/Downloads/rosalind_gc (2).txt")
my_seqs = list(f.keys())

GClist = []

for i in range(len(my_seqs)):
    GC = CGcont.CGcontent(f[my_seqs[i]][:])
    myseq = my_seqs[i]
    GClist.append((myseq,GC))

print(GClist)


#for i in my_seqs:
    
#seq1 = f[my_seqs[0]][:]