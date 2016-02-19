genome = open("C:/Users/Patrick/Downloads/rosalind_rna.txt", 'r')

DNA = genome.read()
genome.close()
A = DNA.count("A")
C = DNA.count("C")
G = DNA.count("G")
T = DNA.count("T")

RNA = DNA.replace("T", "U")
print RNA
print("%d %d %d %d" % (A, C, G, T)) 