from collections import Counter

number_shoes = int(input())
shoes = Counter(map(int, input().split()))
number_customers = int(input())
money = []
for customer in range(number_customers):
    size, price = map(int, input().split())
    if shoes[size] > 0: 
        money.append(price)
        shoes.subtract(Counter([size]))
print(sum(money))
