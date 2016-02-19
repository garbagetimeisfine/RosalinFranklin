"""exercise in self compatibility"""

import csv

f = open("C:/Users/Patrick/Documents/Python/AllesinaLab-introscicomp2014-97b9c93d5aae/python/Data/GoldbergEtAl/NicSolstatus.csv", "r")

csvr = csv.reader(f)

header = next(csvr)

print("This is the header:",)
print(header)

SelfCount = {"one" : 0, "two" : 0, "three" : 0, "four" : 0, "five": 0, "zero" : 0}


for line in csvr:
    if int(line[1]) == 0:
        SelfCount["zero"] += 1
    elif int(line[1]) == 1:
        SelfCount["one"] += 1
    elif int(line[1]) == 2:
        SelfCount["two"] += 1
    elif int(line[1]) == 3:
        SelfCount["three"] += 1
    elif int(line[1]) == 4:
        SelfCount["four"] += 1
    else:
        SelfCount["five"] += 1
    #print(line)

for thing in SelfCount:
    print("The number of species with " + thing + " Self compatibility is " + str(SelfCount[thing]))
#print(SelfCount)
         
f.close

f = open("C:/Users/Patrick/Documents/Python/AllesinaLab-introscicomp2014-97b9c93d5aae/python/Data/GoldbergEtAl/NicSolstatus.csv", "r")

csvr = csv.reader(f)

header = next(csvr)

print("This is the header:",)
print(header)

GenusDict = {}

for line in csvr:
    species = line[0].split('_')[0]
    if species not in GenusDict:
        count_dict = GenusDict.get(species, {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0})
        count_dict[line[1]] = count_dict[line[1]] + 1
        GenusDict[species] = count_dict
    else:
        count_dict[line[1]] = count_dict[line[1]] + 1
        GenusDict[species] = count_dict

f.close()

for genus in sorted(GenusDict):
    print(genus)
    for status in GenusDict[genus]:
        print("\t", status, ":", GenusDict[genus][status])
