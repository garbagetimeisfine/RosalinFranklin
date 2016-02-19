"""compute frequency of each allele in the population"""

def freq(population):
    AA = population.count(('A','A'))
    aA = population.count(('a','A'))
    Aa = population.count(('A','a'))
    aa = population.count(('a','a'))

    return ({'AA' : AA,
             'aA' : aA,
             'Aa' : Aa,
             'aa' : aa})
