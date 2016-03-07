""" this program takes a list of protein identifyers, 

goes to uniprot and pulls their amino acid sequences in FASTA format

it then searches each file for the N-Glycosilation motif using regular expressions

and then it returns the title of each sequence along with 

the locations of each motif occurance."""

import urllib2  # the lib that handles the url stuff



#get's list of IDS from assignment file

A = open("C:/Users/Patrick/Downloads/rosalind_mprt (4).txt", 'r')
proteinID = A.read()
A.close()
proteinIDs = proteinID.split()



#creates data file that we will write our files to
#os.makedirs("C:\Users\Patrick\Documents\Python\RosalinFranklin\Rosalind Bioinfomatics\data")
data = open("C:\Users\Patrick\Documents\Python\RosalinFranklin\Rosalind Bioinfomatics\data.txt", "w")
#pulls the data for each gene and writes it to the .txt file
for i in range(len(proteinIDs)):
    URL = "http://www.uniprot.org/uniprot/" + proteinIDs[i] + ".fasta"
    tempData = urllib2.urlopen(URL) # it's a file like object and works just like a file
    data.writelines(tempData)
data.close()





