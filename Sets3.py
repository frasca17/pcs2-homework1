n, m = map(int, raw_input().split())
seq = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
happiness = 0
for number in seq:
    if number in A:
        happiness += 1
    elif number in B:
        happiness -= 1
print happiness