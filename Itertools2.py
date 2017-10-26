from itertools import permutations
s, k = raw_input().split(); k = int(k)
permutate = sorted(permutations(s, k))
for element in permutate:
    print "".join(element)
