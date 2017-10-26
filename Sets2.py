M = int(raw_input())
l1 = map(int,raw_input().strip().split(' '))
N = int(raw_input())
l2 = map(int,raw_input().strip().split(' '))
s1 = set(l1).difference(set(l2))
s2 = set(l2).difference(set(l1))
result = sorted(s1.union(s2))
for number in result:
    print number