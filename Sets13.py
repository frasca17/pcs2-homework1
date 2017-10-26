setA = set(map(int, raw_input().split()))
n = input()
strict_superset = True
for num in range(n):
    setX = set(map(int, raw_input().split()))
    if not setA.issuperset(setX):
        strict_superset = False
        break
print strict_superset 