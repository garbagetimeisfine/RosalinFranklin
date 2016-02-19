"""exercise in self compatibility"""

import csv

with open("C:Users/Patrick/Documents/Python/AllesinaLab-introscicomp2014-97b9c93d5aae/python/Data/GoldbergEtAl/NicSolstatus.csv", "r") as csvfile:

    csvr = csv.reader(f)

header = next(csvr)

print("This is the header:",)
print(header)
         
