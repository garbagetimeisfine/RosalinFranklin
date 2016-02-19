""" this program is to compare 
title lenght and citation count
for a large data set of published 
papers in major journals"""

import os
import csv
import scipy.stats
import scipy

"""the steps are as follows

1. read in the data file
2. cut the datafile into the subset 
   that were published in 2010
3. Rank from greatest to least for
   both citation number and title length
4. Run Kendall tau on those ranks"""

f = open("C:/Users/Patrick/Documents/Python/AllesinaLab-isc-e278c8656868/Python/data/Letchford_etal_2015_data.csv","r")

csvr = csv.reader(f)

header = next(csvr)
print(header)

my_data = list(csvr)

f.close()

my_data = scipy.array(my_data)

subset = my_data[my_data[:,0] == '2010',]

print(my_data.shape)
print(subset.shape)
print(subset[:5,])

title_rank = scipy.stats.rankdata(subset[:,2])
cites_rank = scipy.stats.rankdata(subset[:,3])

title_abs = subset[:,2]
cites_abs = subset[:,3]

print(title_rank.shape)
print(cites_rank.shape)
print(title_rank[:5])
print(cites_rank[:5])

results = scipy.stats.kendalltau(cites_rank, title_rank)
results2 = scipy.stats.kendalltau(title_abs, cites_abs)
print(results)
print(results2)
