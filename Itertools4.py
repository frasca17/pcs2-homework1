from itertools import combinations_with_replacement
(S, k) = raw_input().split()
S = sorted(S)
k = int(k)
combinations = sorted(combinations_with_replacement(S, k))
for element in combinations:
    print "".join(element)