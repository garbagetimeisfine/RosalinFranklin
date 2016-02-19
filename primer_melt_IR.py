import CGcont

primer = "GGCTATCTATAGATAGCTTCGAGT"

Tm = 81.5 + (0.41 * CGcont.CGcontent(primer) - 500/len(primer))

print(Tm)

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

count = 0 
same = 0
for i in range(len(primer)):
    if primer[i] == primer_dimer[i]:
        same += 1
    count += 1

percent_sticky = same/count * 100
print(percent_sticky)

    