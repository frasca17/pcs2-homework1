from itertools import combinations
(S, k) = raw_input().split()
S = sorted(S)
k = int(k)
for e in range(1, k+1):
    for i in sorted(combinations(S, e)):
        print "".join(i)