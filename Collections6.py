from collections import deque
n = int(input())

seq = deque()
for _ in range(n):
    line = input().split()
    getattr(seq, line[0])(*line[1:])
print(' '.join(map(str, seq)))
    