import re

# Read the file
f = open('C:/Users/Patrick/Documents/Python/AllesinaLab-isc-e278c8656868/regex/data/blackbirds.txt', 'r')
text = f.read()
f.close()

# remove \t\n and put a space in
text = text.replace('\t',' ')
text = text.replace('\n',' ')

# note that there are "strange characters" (these are accents
# and non-ascii symbols) that we do not care for, so let's
# transform to ASCII
text = text.decode('ascii', 'ignore')

## Now write a regular expression that captures 
## the Kingdom, Philum and Species name for each species.

my_reg = r"""
         \s*Kingdom\s* #find Kingdom
         (\w*\s)       #Take whatever word follows it
         [\s\w\,\-]*   #inbewteen crap
         Phylum\s*     #find Phylum
         (\w*\s)       #Extract phylum
         [\s\w\,\-]*   #inbetween crap
         Species\s*    #Find species
         (\w*\s\w*)    #Extract Species
         """
match = re.findall(my_reg, text, re.VERBOSE)

for line in match:
    print(str(line))

# such that re.findall(my_reg, text) should  return
#[(u'Animalia', u'Chordata', u'Euphagus carolinus'),
# (u'Animalia', u'Chordata', u'Euphagus cyanocephalus'),
# (u'Animalia', u'Chordata', u'Turdus boulboul'),
# (u'Animalia', u'Chordata', u'Agelaius assimilis')]
my_reg2 = my_reg = r'\s*Kingdom\s+(\w*)Phylum\s+(\w*)[\s\w\,\-]*Species\s+(\w*\s\w*)\s'

match2 = re.findall(my_reg2, text)

for line2 in match2:
    print(str(line2))