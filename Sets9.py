English = int(raw_input())

roll1 = set(raw_input().split())

French = int(raw_input())

roll2 = set(raw_input().split())

print len(roll1.symmetric_difference(roll2))