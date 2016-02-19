# import function for normal distribution

from numpy.random import normal

# import function for uniform distribution

from numpy.random import uniform 
from math import sqrt

def get_expected_sqrt_x(distribution = "uniform",
                    par1 = 0,
                    par2 = 1,
                    sample_size = 10):
#""" calculate the expectation of sqrt(x) where X is a random variable X can be normal or uniform, with parameters specified by the user"""
    total = 0.0
    for i in range(sample_size):
        if distribution == "uniform":
            z = uniform(par1, par2, 1)
        elif distribution == "normal":
            z = normal(par1, par1,1)
        else:
            print "Unknown distribution. Quitting ..."
            return none
        total = total + sqrt(abs(z))
    return total / sample_size