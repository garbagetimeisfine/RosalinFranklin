""" this program is intended to take K, M, N as populations 
of homozygus dominant, heterozygus, and homozygus recessive
respectively, given k,m,n the program will return the 
probablity that the offspring will have at least 1 dominant 
allele"""

k = 21 #dominant
m = 17 #heterozygus
n = 22 #recessive
total = float(k + m + n)
""" we're going to work by summing the probabilities of no dominant, then subtracting 1"""
#probability of picking an organism from each group
probK = k / total
probM = m / total
probN = n / total

#probability of two n's since both are homozygus recessive the offsping will be recessive
probNN = probN * ((n - 1)/(total -1))


#probability of two m's 
probMM = probM * ((m - 1)/(total -1))
recessiveProbMM = 0.25 * probMM

#probability m then n
probMN = probM * (n / (total - 1))
recessiveProbMN = probMN * 0.5

#probability n then m
probNM = probN * (m / (total - 1))
recessiveProbNM = probNM * 0.5

recessiveProb = recessiveProbNM + recessiveProbMM + recessiveProbMN + probNN
dominantProb = 1 - recessiveProb

print(dominantProb)

