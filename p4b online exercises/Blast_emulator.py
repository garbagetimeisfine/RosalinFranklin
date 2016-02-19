""" This is part of the python for beginners onine thing
this is application 1 I'm near the end of it.

left to do:
    extend words left and right
    score and report
    
website http://pythonforbiologists.com/index.php/applied-python-for-biologists/applied-python-1/

for now off to something else"""



import math

one_sequence = 'actgatcgattgatcgatcgatcg'
another_sequence   = 'actgtttagatcgatctttgatc'
 


def word_slice(sequence, word_len):
    blast_dict = {}
    for i in range(int(math.ceil(len(sequence)/word_len))):
        word = sequence[i * word_len: (i + 1) * word_len]
        blast_dict.setdefault(word,[]).append(i)
    return blast_dict
    
#print(word_slice("actgatcgattgatcgatcgatcag",4).items())


def find_matches(subject, query, word_len):
    subject_dict = word_slice(subject, word_len)
    query_dict = word_slice(query, word_len)
    positions = []
    for key in subject_dict:
        if query_dict.has_key(key):
            print("\nThe key " + key + " is in both sequences")
            print("starting at word number(s) " + str(subject_dict[key]) + " in the subject string")
            print("and starting at word number(s) " + str(query_dict[key]) + " in the query string")
            positions.append((subject_dict[key], query_dict[key]))
    return positions

positions = find_matches(one_sequence,another_sequence,3)
print(positions)

def extend_matches(subject, query, positions, word_len):
    #check first
    for i in positions:
        if subject[i * word_len : (i + 1) * word_len] != query[i * word_len : (i + 1) * word_len]:
            print("something is wrong")
        elif subject[i * word_len : (i + 1) * word_len] == query[i * word_len : (i + 1) * word_len]:
            #check right digit