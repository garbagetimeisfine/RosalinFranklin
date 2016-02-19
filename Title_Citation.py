""" Code to compare the lenght of the titles of papers with their citation counts"""

import csv
import scipy.stats
#import numpy
import scipy

f = open("C:/Users/Patrick/Documents/Python/AllesinaLab-isc-e278c8656868/Python/data/Letchford_etal_2015_data.csv","r")

csvr = csv.reader(f)

header = next(csvr)

print("This is the header: ", header)

"""papers2010 = []

for line in csvr:
    if line[0] == 2010:
        papers2010.append(line)"""

mydata = list(csvr)
f.close()

#print(mydata[0:15])

mydata = scipy.array(mydata)

#print(mydata[0:15])
print(mydata.shape)

subset = mydata[mydata[:,0] == '2010',]
#print(subset[0:15])
print(subset[:,3])
print(subset[:,2])

rank_title = scipy.stats.rankdata(mydata[:,2])
print(rank_title[1:15])
rank_cites = scipy.stats.rankdata(mydata[:,3])
print(rank_cites[1:15])

results = scipy.stats.kendalltau(rank_title, rank_cites)
print(results)
# print the results:
print("Results for all papers published in 2010:")
print("tau", results[0])
print("p-value", results[1])

#print(papers2010)
#lenght = sorted(papers2010, 
        
