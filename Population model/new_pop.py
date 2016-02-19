""" Takes an old generation and makes a new one """

import scipy

def generation(population):
    N = len(population)
    new_generation = []
    for i in range(N):
        mom = scipy.random.randint(N)
        dad = scipy.random.randint(N)
        mom_chr = scipy.random.randint(2)
        dad_chr = 1 - mom_chr
        offspring = (population[mom][mom_chr],population[dad][dad_chr])
        new_generation.append(offspring)
    return new_generation


