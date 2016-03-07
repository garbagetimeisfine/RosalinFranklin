""" cheating off wikipedia"""
def longest_increasing_subsequence(d):
   # 'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) 
                  + [d[i]])
    return max(l, key=len)
 
def longest_decreasing_subsequence(d):
   # 'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] > d[i]] or [[]], key=len) 
                  + [d[i]])
    return max(l, key=len)
  
 
"""if __name__ == '__main__':
    for d in [[3,2,6,4,5,1], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]]:
        print('a L.I.S. of %s is %s' % (d, longest_increasing_subsequence(d)))"""

f = open("C:/Users/Patrick/Downloads/rosalind_lgis.txt",'r')
N = f.next()
seq = f.next()
seq = seq.split()
for i in range(len(seq)):
    seq[i] = int(seq[i])

print N
print(" ".join(str(x) for x in longest_increasing_subsequence(seq)))
print(" ".join(str(x) for x in longest_decreasing_subsequence(seq)))