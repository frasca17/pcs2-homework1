from collections import defaultdict
n, m = map(int, input().split())
a = list(input() for _ in range(n))
b = list(input() for _ in range(m))
d = defaultdict(list)

for i, j in enumerate(a):
    if j in b:
        d[j].append(i+1)
        
for k in b:
    if k in d:
        print(' '.join(map(str, d[k])))
    else:
        print(-1)

