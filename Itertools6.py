from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())
combos = combinations(range(1, n+1), k)# k lenght of combinations
a_indexes = [x[0] + 1 for x in enumerate(letters) if x[1] == 'a']
a_comb = filter(lambda c:set(c) & set(a_indexes) != set(), combinations(range(1,n+1), k))
print (len(list(a_comb)) / len(list(combos)))
