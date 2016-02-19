genome = open("C:/Users/Patrick/Downloads/rosalind_revc.txt", 'r')

primer = genome.read()

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
print(primer_dimer)