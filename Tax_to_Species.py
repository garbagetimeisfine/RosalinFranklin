import csv
import re

file = open("C:/Users/Patrick/Documents/Python/AllesinaLab-isc-e278c8656868/regex/data/Pocock2012.csv","r")

csvr = csv.reader(file)

header = next(csvr)
taxon = {}
speclist = []
badlist = []
taxlist = []

for i in csvr:
    taxlist.append(i[3])
    
file.close
print(header)
print(taxlist[:15])

group_word = re.compile(r'-group$')
sp_word = re.compile(r'\ssp(\s|$)')
single_letter = re.compile(r'\s[A-Z](\s|$)')

good_word = re.compile(r'^[A-Za-z\-]+(\s+[A-Za-z\-]+){1,2}$')


for taxon in taxlist:
    if re.search(good_word, taxon) and not re.search(group_word, taxon) and not re.search(sp_word, taxon) and not re.search(single_letter, taxon):
        speclist.append(taxon)
    else:
        badlist.append(taxon)

print("There are " + str(len(set(speclist))) + " taxonomically resolved species in the file " + file.name)
print("These are identified to species: " + "\n" + ', \n'.join(set(speclist)))

#print(len(speclist))

