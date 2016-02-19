"""This program is to initialize a population.
the population will have N individuals, No Gender, and one Gene with 2 alleles 
A and a each individual will be a twople in a list 
p is the probability of getting allele A

Alright... Here we go!"""

import scipy

def with_a_bang(N, p):
    population = []
    for i in range(N):
        if scipy.random.rand() <= p:
            allele1 = 'A'
        else:
            allele1 = 'a'
        if scipy.random.rand() <= p:
            allele2 = 'A'
        else:
            allele2 = 'a'
        population.append((allele1, allele2))
    return population


#print(with_a_bang(10, 0.6))
