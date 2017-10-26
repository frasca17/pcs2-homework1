from collections import OrderedDict

n = int(input())
items = [input().rpartition(' ') for _ in range(n)]
products = OrderedDict()

for item in items:
    products[item[0]] = products.get(item[0], 0) + int(item[2])

for item_name, net_price in products.items():
    print(item_name, net_price)