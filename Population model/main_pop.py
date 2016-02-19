

""" Central control program"""


import init_pop
import frequency
import new_pop

"""population = init_pop.with_a_bang(100, 0.52)
new_population = new_pop.generation(population)
print(new_population)
print(frequency.freq(new_population))
print(population)
print(frequency.freq(population))"""

def rosalin(k, m, n):
    population = []
    total = 0
    for i in range(k):
        population.append(  "AA" )
        i += 1
    for j in range(m):
        population.append(  "Aa" )
        j += 1
    for Q in range(n):
        population.append(  "aa" )
        Q += 1
    for i in range(1000000):  
        newpop = new_pop.generation(population)
        distribution = frequency.freq(newpop)
        freqaa = distribution["aa"] / float(len(newpop))
        total += freqaa 
    return total/1000000
    
print(rosalin(2,2,2))
print(1-rosalin(2,2,2))


def simulate_drift(N,p):
    population = init_pop.with_a_bang(N, p)
    fixation = False
    num_generations = 0
    while fixation == False:
        distribution = frequency.freq(population)
        if distribution['AA'] == N or distribution['aa'] == N:
            print "An allele has gone to fixation in ", num_generations
            print "The genotype counts are: ", distribution
            fixation = True
        num_generations += 1
        population = new_pop.generation(population)

#simulate_drift(1000, 0.60)