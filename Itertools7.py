from itertools import product

k, m = map(int, input().split())
def f(t):# t is the tuple constructed taking one element from each list
    return sum(x**2 for x in t) % m
lists = (list(map(int, input().split()))[1:] for _ in range(k))
smax = max(map(f, product(*lists)))
print(smax)
