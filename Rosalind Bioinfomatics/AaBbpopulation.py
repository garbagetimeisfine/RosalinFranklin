""" an odd little program

we have a patient zero with phenotype AaBb
each generation the population doubles 
all individuals are crossed with a AaBb individual

we need to find the probability that at least 
N individuals with an AaBb genotype belong to generation k"""
import scipy.misc

k = 5
n = 8

population = 2 ** k
p = 0.25

probTrue = 0.0
for i in range(n,population + 1):
   probTrue += (scipy.misc.comb(population,i) * (p**i) * ((1-p) ** (population-i)))
  
print(probTrue)