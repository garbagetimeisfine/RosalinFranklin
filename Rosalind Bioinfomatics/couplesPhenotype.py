""" this is to predict the number of offspring with the dominant phenotype
data input is 6 integers each representing the number of couples with the 
genotype pair given each couple has two children"""

AA_AA = 19385
AA_Aa = 17912
AA_aa = 17515
Aa_Aa = 18449
Aa_aa = 16310
aa_aa = 17271

total = 2 * (AA_AA + AA_Aa + AA_aa + (Aa_Aa * 0.75) + (Aa_aa * 0.5))
print total
