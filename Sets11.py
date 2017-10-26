K_family_groups = int(raw_input())
number_rooms = map(int, raw_input().split())
rooms = set(number_rooms)#unique set of room numbers

print (sum(rooms) * K_family_groups - sum(number_rooms)) / (K_family_groups - 1)