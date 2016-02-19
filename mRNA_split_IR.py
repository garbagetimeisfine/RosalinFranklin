import re

RNA = "CTTGACTCAGGCTGTCTCTGATTATCATGGAGTCAGTACCCTTGATAGAAAGGAAATTCCTCCAAGGAGGAAGTTCGAAAAGGGTACATCTACACTGTTCTAcatacaaaacttacaatcagtcctcatgcaggcccctgccatgctggttctgttatattaacaggaacactttCATGCCATCACCTATACATGGCCAAAAAGGACTCAGTTCTCCCCCACACCCCTTTTTCTATCTCTCTGATGTCTAATATCAGAGTACATTCCTGTGCTCCTCTAACACTCAAAACTA".upper()

exon1 = re.search(r'^.*CATACAAAAC', RNA)
print(exon1.group())
intron = re.search(r'CATACAAAAC\w*CATGCCATCA', RNA)
print(intron.group())
exon2 = re.search(r'CATGCCATCACCT\w*CTCAAAACTA', RNA)
print(exon2.group())

print("Exon 1 starts at the first nucleotide and runs to the " + str(intron.start() - 1) + " nucleotide.")
print("Exon 2 goes from nucleotide " + str(exon2.start()) + " to nucleotide " + str(exon2.end()))
print("The intron spans nucleotides " + str(intron.start()) + " to " + str(intron.end() - 11))