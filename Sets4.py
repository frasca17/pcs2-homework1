N = int(raw_input())#total number of country stamps it's a number
country_stamps= set()
for stamp in range(0, N):
    country_stamps.add(raw_input())
print len(country_stamps)