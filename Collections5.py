from collections import OrderedDict

n = int(input())
words = [input() for _ in range(n)]
occurrences = OrderedDict()
for word in words:
    occurrences[word]= occurrences.get(word, 0) + 1
print(len(occurrences))
print(' '.join(map(str, occurrences.values())))