English = int(raw_input())

E_roll_numbers = set(raw_input().split())

French = int(raw_input())

F_roll_numbers = set(raw_input().split())

print len(E_roll_numbers.union(F_roll_numbers))