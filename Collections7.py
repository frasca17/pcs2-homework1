from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    row = deque(map(int, input().split()))
    pile = deque()
    result = "Yes"
    for _ in range(n):
        left = row[0]
        right = row[-1]
        if left <= right and (len(pile) == 0 or right <= pile[-1]):
            pile.append(row.pop())
        elif len(pile) == 0 or left <= pile[-1]:
            pile.append(row.popleft())
        else:
            result = "No"
            break
    print(result)