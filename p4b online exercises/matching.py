one_sequence = 'actgatcgattgatcgatcgatcg'
another_sequence   = 'tttagatcgatctttgatc'
 
# here are the five bits of information we described before
def score_match(subject, query, subject_start, query_start, length):
    score = 0
    # for each base in the match
    for i in range(0,length):
        # first figure out the matching base from both sequences
        subject_base = subject[subject_start + i]
        query_base = query[query_start + i]
        # then adjust the score up or down depending on 
        # whether or not they are the same
        if subject_base == query_base:
            score = score + 1
        else:
            score = score - 1
    return score
 
# here is the score for the match we were looking at above
print(score_match(one_sequence, another_sequence, 7, 4, 8))
 
# let's try a few other potential matches
 
# here is the same match but shorter
print(score_match(one_sequence, another_sequence, 7, 4, 4))
 
# how about a longer match
print(score_match(one_sequence, another_sequence, 7, 4, 12))
 
# and a random match
print(score_match(one_sequence, another_sequence, 10, 1, 5))

def pretty_print_match(subject, query, subject_start, query_start, length):
 
    # first print the start/stop positions for the subject sequence
    print(str(subject_start) + (' ' * length) + str(subject_start+length))
 
    # then print the bit of the subject that matches
    print(' ' + subject[subject_start:subject_start+length])
 
    # then print the bit of the query that matches
    print(' ' + query[query_start:query_start+length])
 
    # finally print the start/stop positions for the query
    print(str(query_start) + (' ' * length) + str(query_start+length))
 
    print('n--------------------n')
    
def try_all_matches(subject, query, score_limit):
    for subject_start in range(0,len(subject)):
        for query_start in range(0,len(query)):
            for length in range(0,len(query)):
                if (subject_start + length < len(subject) and query_start + length < len(query)):
                    score = score_match(subject, query, subject_start, query_start, length)
                    # only print a line of output if the score is better than some limie
                    if (score >= score_limit):
                        print('Score : ' + str(score))
                        pretty_print_match(subject, query, subject_start, query_start, length)
 
try_all_matches(one_sequence, another_sequence, 6)

# the arguments are the five bits of information that define a match

 
pretty_print_match(one_sequence, another_sequence, 7, 4, 8)



