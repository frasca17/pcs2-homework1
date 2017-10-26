Nsets = int(raw_input())
setA = set(map(int, raw_input().split()))

for number in range(int(raw_input())):
    operations = raw_input().split()
    setB = set(map(int, raw_input().split()))
    if operations[0] == 'update':
        setA.update(setB)
    elif operations[0] == 'intersection_update':
        setA.intersection_update(setB)
    elif operations[0] == 'symmetric_difference_update':
        setA.symmetric_difference_update(setB)
    elif operations[0] == 'difference_update':
        setA.difference_update(setB)
print sum(setA)