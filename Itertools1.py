from itertools import product
A = map(int, raw_input().split())
B = map(int, raw_input().split())
sort_list = sorted(product(A,B))
for element in sort_list:
    print element,#there is the comma because we are working on a tuple